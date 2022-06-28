from datetime import date
from random import random
from urllib import request
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View, generic
# from .utils import DataMixin
from .models import *
from django.views.generic import ListView
from .forms import *
from .urls import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import  login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.defaults import page_not_found
from django.views.decorators.cache import cache_page
from django.core.cache import cache


def page_not_found_view(request, exception):
    return redirect('/')

# Main page
# save cache
@cache_page(60*5)
def homepage(request):
    users_feedbacks = Feedbacks.objects.order_by('-date_time')
    context = {
        'title' : 'Название',
        'user_feedbacks' : users_feedbacks,
        'cat_select' : 1,
    }

    return render(request, 'catalog/index.html', context=context)

# Callbacks
def create_feedback(request):
    form = FeedbacksForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # claer cache
            cache.clear()
    return redirect('/#redirect-cb')

# Profile
class viewProfile(LoginRequiredMixin, ListView):
    model = User
    template_name = 'catalog/profile.html'
    queryset = Category.objects.all()

    def get_queryset(self):
        user_autheticate = User.objects.get(username=self.request.user)
        order_list = Orders.objects.filter(owner=user_autheticate)
        return order_list

    def get_context_data(self, **kwargs):
        content = User
        context = super().get_context_data(**kwargs)
        c_def = {
            'settings' : 'Настройки',
            'awaitings' : 'Ожидание',
            'personal_promo' : 'Промокоды',
            'orders' : 'Мои заказы',
            'sales' : 'Акции',
            'cat_select' : 4,
            'username' : content.username,
            'email' : content.email,
            'first_name' : content.first_name,
            'order_list' : self.get_queryset,
        }
        context['title'] = 'Профиль'
        # context['cat_select'] = 4
        context = dict(list(context.items()) + list(c_def.items()))
        return context

# Catalog
class AllGoods(ListView):
    categories = Category.objects.all()
    queryset = Goods.objects.filter()
    template_name = 'catalog/catalog.html'
    context_object_name = 'goods'
    extra_context = {'title' : 'Каталог', 'cat_select' : 2, 'queryset' : queryset, 'cats' : categories}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context = dict(list(context.items()))
        return context

# Catalog category filter
# save cache
@cache_page(60*5)
def filter_goods_category(request, slug):
    categories = Category.objects.filter(slug=slug)
    queryset = Goods.objects.filter(cat__in=categories)
    context = {'title' : slug.title(), 'cats' : categories, 'queryset' : queryset, 'back' : True}
    return render(request, 'catalog/catalog.html', context=context)

# Auth
def login(request):
    #redirect на главную страницу, если пользователь авторизован
    if auth.get_user(request).is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                request.session['errors'] = ''
                # clear cache
                cache.clear()
                return redirect('profile')
            else:
                request.session['errors'] = 'Неверный логин или пароль'
                return redirect('login')

    context = {
        'title' : 'Логин',
    }
    return render(request, 'catalog/login.html', context=context)

# Register
def register(request):
    if auth.get_user(request).is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first_name']
            email = request.POST['email']
            User.objects.create_user(username=username, password=password, first_name=first_name, email=email)
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            # clear cache
            cache.clear()

            # Присвоение пользователю id в доп. информации о пользователях для
            # последующего добавления ему заказов по id, Many-to-one связь(Model Orders)
            username_id_orders = request.user.id
            profile = Profile.objects.filter(id=username_id_orders).update(username=f'{username_id_orders}')

            return redirect('homePage')

    context = {
        'title' : 'Регистрация',
    }

    return render(request, 'catalog/register.html')

# Logout
def logout_view(request):
    logout(request)
    # clear cache
    cache.clear()
    return redirect('/')

# Cart functions
def add_to_cart(request, id):
    if request.method == 'POST':
        if not request.session.get('cart'):
            request.session['cart'] = list()
        else:
            request.session['cart'] = list(request.session['cart'])

    item_exist = next((item for item in request.session["cart"] if item["type"] == request.POST.get("type") and item["id"] == id), False)

    add_data = {
        'type' : request.POST.get('type'),
        'id' : id,
    }

    if not item_exist:
        request.session['cart'].append(add_data)
        request.session.modified = True
    print(request.session['cart'])
    return redirect(request.POST.get('url_from'))

def remove_from_cart(request, id):
    goods = Goods.objects.all()
    list = []
    if request.session.get('cart'):
        for item in request.session['cart']:
            list.append(int(item['id']))

    if request.method == 'POST':
        for item in request.session['cart']:
            if item['id'] == id:
                item.clear()

        while {} in request.session['cart']:
            request.session['cart'].remove({})

        if not request.session['cart']:
            del request.session['cart']

        request.session.modified = True

    return redirect(request.POST.get('url_from'))

# Delte all id from cart
def delete_cart(request):
    if request.session.get('cart'):
        del request.session['cart']
        request.session.modified = True
    return redirect(request.POST.get('url_from'))

# Cart view
def cart_page(request, get_summ=False):
    goods = Goods.objects.all()
    # Adding items from cart session to template
    cart_list = []
    if request.session.get('cart'):
        for item in request.session['cart']:
            cart_list.append(int(item['id']))

    total_price = 0
    # result cost
    for g in goods:
        if g.id in cart_list:
            price = int(g.price)
            #it's for using total_price in func below-make_New_Order for adding summ in model
            #Look at mark (!)
            total_price += price
    if get_summ:
        return total_price

    context = {
        'title' : 'Корзина',
        'cart_list' : cart_list,
        'goods' : goods,
        'cat_select' : 3,
        'total_price' : total_price,
    }

    return render(request, 'catalog/cart.html', context=context)

# creating new order
def make_New_Order(request):
    form = OrdersForm(request.POST)
    if request.method == 'POST':
#  (!)  here we user cart_page
        total_price = cart_page(request, get_summ=True)
        # filter by username(id)
        profile = Profile.objects.filter(username=request.user.id)
        # random order number
        order_number = random() * 1000000
        # getting good's id's
        summ = request.session['cart']
        cart_list = []
        for item in request.session['cart']:
            cart_list.append(int(item['id']))
        # delete session cart
        del request.session['cart']
        #creating new order
        Orders.objects.create(order_number=order_number, total_price=total_price, items_ordered=cart_list, owner=request.user, order_owner=profile[0])
        return redirect('profile')
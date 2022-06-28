import imp
from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    # main page
    path('', homepage, name='homePage'),
    # create feedback
    path('feedback/', create_feedback, name='create_feedback'),
    # profile link
    path('profile/', viewProfile.as_view(), name='profile'),
    # catalog
    path('catalog/', include([
        path('', cache_page(60*10)(AllGoods.as_view()), name='catalog'),
        path('<slug:slug>', filter_goods_category, name='category')
        ])),
    path('logout/', logout_view, name='logout'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    # cart
    path('cart/', include([
        path('', cart_page, name='cart'),
        path('<id>/add/', add_to_cart, name='add'),
        path('<id>/remove', remove_from_cart, name='remove'),
        path('delete/', delete_cart, name='delete'),
    ])),
    # ordering
    path('ordering/', make_New_Order, name='ordering')
]
import imp
from django.contrib import admin
from .models import *

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'price')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ratingcomment', 'feedback_text')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'total_price', 'order_number', 'order_owner', 'items_ordered')
    list_display_links = ('id',)
    search_fields = ('name',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'username')
    list_display_links = ('id',)
    search_fields = ('name',)

admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feedbacks, FeedbacksAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Profile, ProfileAdmin)
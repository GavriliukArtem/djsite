from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_goods/', AddGoods.as_view(), name='add_goods'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('search/', Search.as_view(), name='search'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('update/<slug:prd_slug>/', UpdateGoods.as_view(), name='update'),
    path('delete/<slug:prd_slug>/', DeleteGoods.as_view(), name='delete'),
    path('pruduct/<slug:prd_slug>/', ShowProduct.as_view(), name='ditail'),
    path('category/<slug:cat_slug>/', ShopCategory.as_view(), name='category')

]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),

    #admin
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_cake_master_add', views.admin_cake_master_add, name='admin_cake_master_add'),
    path('admin_cake_master_view', views.admin_cake_master_view, name='admin_cake_master_view'),
    path('admin_cake_master_delete', views.admin_cake_master_delete, name='admin_cake_master_delete'),
    path('admin_cake_master_search', views.admin_cake_master_search, name='admin_cake_master_search'),
    path('admin_cake_master_update', views.admin_cake_master_update, name='admin_cake_master_update'),


    path('admin_cake_payment_view', views.admin_cake_payment_view, name='admin_cake_payment_view'),

    path('admin_cake_orders_view', views.admin_cake_orders_view, name='admin_cake_orders_view'),
    path('admin_cake_orders_view2', views.admin_cake_orders_view2, name='admin_cake_orders_view2'),

    #user
    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),
    path('user_cake_master_ view', views.user_cake_master_view, name='user_cake_master_view'),

    path('user_cake_master_search', views.user_cake_master_search, name='user_cake_master_search'),


    path('user_cake_payment_add', views.user_cake_payment_add, name='user_cake_payment_add'),
    path('user_cake_payment_view', views.user_cake_payment_view, name='user_cake_payment_view'),

    path('user_cake_orders_view', views.user_cake_orders_view, name='user_cake_orders_view'),

]
from django.contrib import admin

#user_login,user_details,cake_master,cake_order,cake_payment
# Register your models here.
from .models import user_login,user_details,cake_master,cake_order,cake_payment


admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(cake_master)
admin.site.register(cake_order)
admin.site.register(cake_payment)

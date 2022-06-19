from django.contrib import admin
from quotes.models import *

# Register your models here.

admin.site.register(Quote)


from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    model = User
admin.site.register(User, CustomUserAdmin)
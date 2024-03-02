# from django.contrib import admin
# from django.contrib.auth import admin as auth_admin
#
# from .forms import UserChangeForm, UserCreationForm
# from .models import *
#
#
# @admin.register(CustomUser)
# class UserAdmin(auth_admin.UserAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#     model = CustomUser
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('cpf', 'password1', 'password2'),
#         }),
#     )
#
#     fieldsets = auth_admin.UserAdmin.fieldsets + (
#         ("Informações Pessoais", {"fields": ("cpf",)}),
#     )
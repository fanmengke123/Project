from django.contrib import admin
from .models import User, ConfirmString
import hashlib


# Register your models here.

def mymd5(data):
    return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()


class UserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.password = mymd5(request.POST.get('password'))
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)


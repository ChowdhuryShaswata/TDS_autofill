from django.contrib import admin
from .models import NameGenerator, TDSUser
# Register your models here.
admin.site.register(NameGenerator)
admin.site.register(TDSUser)

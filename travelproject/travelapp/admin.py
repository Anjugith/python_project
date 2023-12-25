from django.contrib import admin
from . models import Place
from . models import Workers
# Register your models here.
admin.site.register(Place),
admin.site.register(Workers)
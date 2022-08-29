from django.contrib import admin

from familiares_app.views import home
from .models import *

# Register your models here.

admin.site.register(Familiar)
from django.contrib import admin
from .models import TodosModel
from .models import Profile

# Register your models here.
admin.site.register(TodosModel)
admin.site.register(Profile)
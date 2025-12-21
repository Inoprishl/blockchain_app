from django.contrib import admin
from .models import StepModel, LessonModel

# Register your models here.
admin.site.register(StepModel)
admin.site.register(LessonModel)
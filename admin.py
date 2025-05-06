from django.contrib import admin
from .models import Profile,GarbageReport,WorkerLocation



# Register your models here.
admin.site.register(Profile)
admin.site.register(GarbageReport)
admin.site.register(WorkerLocation)
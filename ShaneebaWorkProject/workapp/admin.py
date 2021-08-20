from django.contrib import admin

from .models import *
admin.site.register(Project)
admin.site.register(WorkType)
admin.site.register(WorkStatus)
admin.site.register(Works)


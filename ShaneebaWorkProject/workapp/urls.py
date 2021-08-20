
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("works/",WorksGetPost.as_view()),
    path("works/<int:id>",WorkUpdateDelete.as_view()),
    path("project/",ProjectView.as_view()),
    path("worktype/",WorkTypeView.as_view()),
    path("workstatus/",WorkStatusView.as_view()),
    path("datefilter/",DateFilter.as_view()),
    path("delete/<int:id>",DeleteWork2.as_view())

]

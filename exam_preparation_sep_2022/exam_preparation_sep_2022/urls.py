from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',  include('exam_preparation_sep_2022.web.urls')),
]

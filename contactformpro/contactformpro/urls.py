
from django.contrib import admin
from django.urls import path
from contactformapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.contact_view)
]

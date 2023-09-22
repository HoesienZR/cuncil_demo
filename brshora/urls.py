from django.urls import path
from . import views

app_name = 'brshora'
urlpatterns = [
    path('br/',views.brstatueview,name='brstatueview'),
                  ]
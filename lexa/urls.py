from django.urls import path

from . import views

urlpatterns = [
    path('leshka/', views.leshka, name='leshka'),
    path('klyatov/', views.klyatov, name='klyatov')
]

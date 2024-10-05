from django.urls import path
from . import views

urlpatterns = [
    path('article/<slug:slug>', views.article, name='article'),
    path('vote/', views.vote, name='vote'),
    path('poll/<int:poll_id>/results/', views.get_poll_results, name='poll_results'),
    path('', views.home, name='home'),
]
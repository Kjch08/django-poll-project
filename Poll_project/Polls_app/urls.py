from django.urls import path
from .import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
    path('<int:question_id>/results/',views.question_results, name='question_results'),
]

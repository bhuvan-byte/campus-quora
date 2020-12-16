from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('list/',views.QuestionView.as_view(),name='list'),
    path('<int:pk>',views.QuestionDetailView.as_view(),name='detail'),
    path('askquestion/',views.add_question,name='add_question'),
]
from django.urls import path
from .views import sign_up_view
urlpatterns=[
    path('register/', sign_up_view.as_view(),name='register'),
]
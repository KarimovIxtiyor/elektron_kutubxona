from django.urls import  path
from .views import SignUPView

urlpatterns=[
    path('signup/',SignUPView.as_view(),name='signup'),
]
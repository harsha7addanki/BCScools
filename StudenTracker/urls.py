from django.urls import path
from .views import index, classinfo, studentinfo

urlpatterns = [
    path('', index, name='index'),
    path('class/', classinfo, name='class'),
    path('student/', studentinfo, name='student')
]

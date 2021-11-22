from django.urls import path
from app import views

#template URLs
app_name= 'app'

urlpatterns=[
    path('registrations/',views.register,name='register'),
    path('user_login',views.user_login,name='user_login')
]

from django.conf.urls import url
from loginsys import views


app_name = 'loginsys'

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^login_vk/', views.show_auth, name='login_vk'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
]


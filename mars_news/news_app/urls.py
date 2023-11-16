from django.urls import path
from .views import login_view, main_page, register_view, logout_view

urlpatterns = [
    path('', view=main_page, name='home'),
    path('login/', view=login_view, name='login'),
    path('logout/', view=logout_view, name='logout'),
    path('register/', view=register_view, name='register'),

]



















# from django.urls import path
# from . import views

# urlpatterns = [
#  
#     path('register/', views.register_view, name='register'),
#    
# ]

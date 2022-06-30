from django.urls import path

from petstagram.main.views import show_home, show_dash_board, show_profile, show_photo

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dash_board, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>/', show_photo, name='pet photo details')
)

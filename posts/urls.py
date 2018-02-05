from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.DetailFormView.as_view(), name='detail'),
    path('<int:pk>/edit', views.EditView.as_view(), name='edit'),
    # path('<int:pk>/reply/', views.ReplyView.as_view(), name='reply'),
]

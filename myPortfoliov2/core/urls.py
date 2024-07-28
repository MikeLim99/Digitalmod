from django.urls import path
from . import views
from .views import blogs, detailedBlog

urlpatterns = [
    path('', views.home, name='home'),
    path('posts&updates/', blogs.as_view(), name='blogs'),
    path('article/<int:pk>', detailedBlog.as_view(), name='detailed-Blog'),
    path('contact/', views.contacts, name='contacts'),
    path('MyPortfolio/', views.portfolio, name='portfolio'),
    path('<int:id>/', views.detailedPortfolio, name='detailedPortfolio'),
]
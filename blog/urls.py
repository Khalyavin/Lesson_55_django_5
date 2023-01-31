
from django.urls import path

from blog.apps import BlogConfig
from blog.views import contacts, BlogActiveListView, BlogAllListView, BlogCreateView, BlogUpdateView, \
    BlogDeleteView, BlogDetailView, change_status

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogActiveListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),

    path('list/', BlogAllListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('detail/<slug:pk>/', BlogDetailView.as_view(), name='detail'),

    path('status/<int:pk>/', change_status, name='status'),
]

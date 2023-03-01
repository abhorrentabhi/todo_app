from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('update/<int:task_id>', views.update, name='update'),
    path('cbvlist/', views.TaskListView.as_view(), name='cbvlist'),
    path('cbvdetail/<int:pk>', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='cbvdelete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
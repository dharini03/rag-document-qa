# from django.urls import path
# from .views import UploadView, AskView

# urlpatterns = [
#     path('upload/', UploadView.as_view(), name='upload'),
#     path('ask/', AskView.as_view(), name='ask'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("upload/", views.upload_view, name="upload_page"),
    path("chat/", views.chat_view, name="chat_view"),
]

from django.urls import path

from .views import UserAPIView, UserDetailAPIView

user_api = UserAPIView.as_view()
user_detail_api = UserDetailAPIView.as_view()

urlpatterns = [
    path("users", user_api, name="users"),
    path("users/<int:user_id>", user_detail_api, name="user-detail")
]

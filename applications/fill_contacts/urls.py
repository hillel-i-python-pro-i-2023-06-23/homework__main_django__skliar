from django.urls import path
from . import views, views_for_HW_13

apps_name = "fill_contacts"

urlpatterns = [
    path("test/", views.UserList.as_view(), name="test"),
    path("view", views.phoneuser_list, name="view"),
    path("all/", views_for_HW_13.all, name="all"),
    path("one/", views_for_HW_13.one_user, name="one"),
    path("add/", views_for_HW_13.add_user, name="add"),
    path("delete/", views_for_HW_13.delete, name="delete"),
    path("update/", views_for_HW_13.update, name="update"),
]

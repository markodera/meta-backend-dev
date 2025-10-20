from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
app_name = "LiitlelemoneAPI"

urlpatterns = [
    path("menu-item/", views.MenuItemView.as_view(), name="menu_item"),
    path("menu-item/<int:pk>/", views.SingleMenuItemView.as_view(), name="single_item"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("category/<int:pk>/", views.SingleCategoryView.as_view(), name="single_category"),
    path("secret/", views.secret),
    path("api-token-auth/", obtain_auth_token, name="token_generator"),
    path("manager-view/", views.manager_view, name="manager_view"),
    # path("menu-item/", views.menu_items, name='menu_item'),
    path("throttle-check/", views.throttle_check, name="throttle_check"),
    path("throttle-check-auth/", views.throttle_check_auth, name="throttle_check_auth"),
    path("manager/", views.managers, name="managers")
    # path("menu-item/<int:pk>/", views.single_item, name='single_item'),
    # path("category/", views.category_view, name='category'),
    # path("category/<int:pk>/", views.single_category, name='single_category')
]
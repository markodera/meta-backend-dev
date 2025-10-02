from django.urls import path
from . import views

app_name = "LiitlelemoneAPI"

urlpatterns = [
    path("menu-item/", views.MenuItemView.as_view(), name="menu_item"),
    path("menu-item/<int:pk>/", views.SingleMenuItemView.as_view(), name="single_item"),
    path("category/", views.CategoryView.as_view(), name="category"),
    path("category/<int:pk>/", views.SingleCategoryView.as_view(), name="single_category")
    # path("menu-item/", views.menu_items, name='menu_item'),
    # path("menu-item/<int:pk>/", views.single_item, name='single_item'),
    # path("category/", views.category_view, name='category'),
    # path("category/<int:pk>/", views.single_category, name='single_category')
]
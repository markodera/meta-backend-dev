from rest_framework import generics
from .models import MenuItem, Category
from . serializers import MenuItemSerilaizer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
# class based view

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerilaizer
    ordering_fields=['price', 'inventory']
    search_fields = ['title','category__title']
    def get_queryset(self):

        queryset = MenuItem.objects.select_related('category').all()
        category_name = self.request.query_params.get('category')
        to_price = self.request.query_params.get('to_price')
        search = self.request.query_params.get('search')
        # ordering = self.request.query_params.get('ordering')
        if category_name:
            queryset = queryset.filter(category__title=category_name)
        if to_price:
            queryset = queryset.filter(price__lte=to_price)
        if search :
            queryset = queryset.filter(title__startswith=search)       
        # if ordering:
        #     ordering_fields = ordering.split(",")
        #     queryset = queryset.order_by(*ordering_fields)
        return queryset

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerilaizer

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
# Function Based View
# @api_view(['GET','POST'])
# def category_view(request):
#     if request.method == 'GET':
#         items = Category.objects.select_related().all()
#         serializer_item = CategorySerializer(items, many=True)
#         return Response(serializer_item.data)
#     elif request.method == 'POST':
#         serializer_item = CategorySerializer(data=request.data)
#         serializer_item.is_valid(raise_exception=True)
#         serializer_item.save()
#         return Response(serializer_item.data, status.HTTP_201_CREATED)
    


# @api_view(['GET','POST'])
# def single_category(request, id):
#     item = get_object_or_404(Category, pk=id)
#     serializer_item = CategorySerializer(item)
#     return Response(serializer_item.data)

# @api_view(['GET', 'POST'])
# def menu_items(request):
#     if request.method =='GET':       
#         items = MenuItem.objects.select_related('category').all()
#         category_name = request.query_params.get('category')
#         to_price = request.query_params.get('to_price')
#         search = request.query_params.get('search')
#         ordering = request.query_params.get('ordering')
#         perpage = request.query_params.get('perpage', default=2)
#         page = request.query_params.get('page', default=1)
#         if category_name:
#             items = items.filter(category__title=category_name)
#         if to_price:
#             items = items.filter(price__lte=to_price)
#         if search:
#             items = items.filter(title__startswith=search)
#         if ordering:
#             ordering_fields = ordering.split(",")
#             items = items.order_by(*ordering_fields)
#         paginator = Paginator(items, per_page=perpage)
#         try:
#             items = paginator.page(number=page)
#         except EmptyPage:
#             items = []
#         serializer_item = MenuItemSerilaizer(items, many=True)
#         return Response(serializer_item.data)
#     elif request.method == 'POST':
#         serializer_item =MenuItemSerilaizer(data=request.data)
#         serializer_item.is_valid(raise_exception=True)
#         # serializer_item.validated_data
#         serializer_item.save()
#         return Response(serializer_item.data, status.HTTP_201_CREATED)
    
# @api_view(['GET','POST'])
# def single_item(request, id):
#     item = get_object_or_404(MenuItem, pk=id)
#     serializer_item = MenuItemSerilaizer(item)
#     return Response(serializer_item.data)
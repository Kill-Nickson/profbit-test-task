from django.shortcuts import render
from django.views.generic import ListView

from .models import Product


class ProductsView(ListView):
    template_name = 'product_list.html'
    paginate_by = 50
    context_object_name = 'product_list'

    def get_queryset(self):
        queryset = Product.objects.all().values('name')
        return queryset

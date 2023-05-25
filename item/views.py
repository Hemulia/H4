from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import Item, Brand

class ItemListView(ListView):
	model = Item

class ItemCreateView(CreateView):
	model = Item
	fields = ["name", "quantity", "brand"]
	success_url = "/"

class ItemUpdateView(UpdateView):
	model = Item
	fields = ["name", "quantity", "brand"]
	success_url = "/"

class ItemDeleteView(DeleteView):
	model = Item
	success_url = "/"

class BrandListView(ListView):
	model = Brand

class BrandUpdateView(UpdateView):
	model = Brand
	fields = ["name"]
	success_url = "/"
	
class BrandCreateView(CreateView):
	model = Brand
	fields = ["name"]
	success_url = "/"

class BrandDeleteView(DeleteView):
	model = Brand
	success_url = "/"


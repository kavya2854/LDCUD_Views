from django.shortcuts import render
from app.models import *
from django.views.generic import ListView
# Create your views here.
class school_list(ListView):
    model = School
    context_object_name = 'schools'
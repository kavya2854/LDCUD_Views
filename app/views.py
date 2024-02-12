from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView
# Create your views here.
class school_list(ListView):
    model = School
    context_object_name = 'schools'
    # ordering=['sname']
    # queryset=School.objects.filter(id=1)
    # template_name = 'app/school_list.html'

class SchoolDetail(DetailView):
    model = School
    context_object_name = 'sclobject'

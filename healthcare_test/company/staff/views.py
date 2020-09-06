from django.views.generic import ListView, DetailView
from .models import Employee, Department
from .forms import EmployeeForm 
from django.shortcuts import render,redirect

class EmployeeList(ListView):
    model = Employee

class EmployeeDetail(DetailView):
    queryset = Employee.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DepartmentList(ListView):
    model = Department

class DepartmentDetail(DetailView):
    queryset = Department.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def home_view(request): 
    context ={} 
    form = EmployeeForm(request.POST or None, request.FILES or None) 
      
    if form.is_valid(): 
        form.save() 
        return redirect('/employee/')
    context['form']= form 
    print(context)
    return render(request, "index.html", context)
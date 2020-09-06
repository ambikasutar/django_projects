from django.urls import path
from .views import EmployeeList, EmployeeDetail, DepartmentList, DepartmentDetail,home_view

urlpatterns = [
    path('employee/', EmployeeList.as_view(), name='index'),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='details'),
    path('department/', DepartmentList.as_view(), name='depart'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='ddetails'),
    path('employee/create/', home_view, name="create_emp"),

]


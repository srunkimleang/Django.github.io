from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)
def employee_form(request, id=0):
    if request.method == "GET":# if the method is GET it will show the form
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form':form})
    else: # if the method is POST it will record in to database
        if id ==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance = employee)
        if form.is_valid(): # to check if it is valid form or not
            form.save() # save to database
        return redirect('/employee/list') # urls /employee/list
def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')

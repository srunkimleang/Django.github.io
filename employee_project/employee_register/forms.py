from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'#this is bring all the properties inside models from Employee class
        fields = ('fullname', 'mobile', 'emp_code', 'position') #it maintain order of this list fullname moblie emp_code position
        labels = {
            'fullname':'Full Name',
            'emp_code':'Emp.Code'
        }
    def __init__(self, *args, **kwargs): #__init__ to change "select" in Position from ------
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = 'select'
        self.fields['emp_code'].required = False
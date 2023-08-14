from django.shortcuts import render, get_object_or_404, redirect

from models2.web.models import Employee, Department


def index(request):
    # долния ред се нария QuerySet
    employees = Employee.objects.filter(department_id=1)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')


def department_details(request, pk):
    context = {
        'department': get_object_or_404(Department, pk=pk)
    }
    return render(request, 'department-details.html', context)
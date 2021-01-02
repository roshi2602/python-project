from django.contrib import admin
from employee.models import Employee




class EmployeeAdmin(admin.ModelAdmin):
	list_display=['id_number','first_name','last_name']
		
admin.site.register(Employee,EmployeeAdmin)



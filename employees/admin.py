from django.contrib import admin
from .models import Organization, Section, JobTitle, SalaryGrade, Employee

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    pass

@admin.register(SalaryGrade)
class SalaryGradeAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employeeName', 'get_organization_name', 'get_section_name', 'get_job_title', 'joiningDate', 'employmentStatus')
    list_filter = ('organizationID', 'sectionID', 'jobTitleID', 'employmentStatus')
    search_fields = ('employeeName', 'nationalID', 'employeeNo')

    def get_organization_name(self, obj):
        return obj.organizationID.organizationName
    get_organization_name.short_description = 'সংগঠন'

    def get_section_name(self, obj):
        return obj.sectionID.sectionName
    get_section_name.short_description = 'বিভাগ'

    def get_job_title(self, obj):
        return obj.jobTitleID.jobTitle
    get_job_title.short_description = 'পদবীর নাম'

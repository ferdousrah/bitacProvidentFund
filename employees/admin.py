from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Organization, Section, JobTitle, SalaryGrade, Employee
from django.contrib.admin.sites import AdminSite
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter


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
    list_display = ('get_photo', 'employeeNo', 'employeeName', 'get_organization_name', 'get_section_name', 'get_job_title', 'joiningDate', 'employmentStatus')
    search_fields = ('employeeName', 'nationalID', 'employeeNo')
    list_filter = (
        ('sectionID__sectionName', DropdownFilter),
        ('jobTitleID__jobTitle', DropdownFilter),
        ('employmentStatus', ChoiceDropdownFilter),
    )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe('<img src="{}" style="max-width: 40px; max-height: 40px; border-radius: 50%;" />'.format(obj.photo.url))
        else:
            return 'No Photo'
    get_photo.allow_tags = True
    get_photo.short_description = 'Photo'

    def get_organization_name(self, obj):
        return obj.organizationID.organizationName
    get_organization_name.short_description = 'সংগঠন'

    def get_section_name(self, obj):
        return obj.sectionID.sectionName
    get_section_name.short_description = 'বিভাগ'

    def get_job_title(self, obj):
        return obj.jobTitleID.jobTitle
    get_job_title.short_description = 'পদবীর নাম'

    class Media:
        css = {
            'all': ('admin_custom.css',),  # Path to your custom CSS file
        }

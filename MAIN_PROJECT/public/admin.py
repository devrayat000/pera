from django.contrib import admin
from .models import announcements, assignments, class_tests

admin.site.site_header = 'Mechanical 20 Dashboard'


admin.site.register(announcements)
admin.site.register(assignments)
admin.site.register(class_tests)



# Register your models here.

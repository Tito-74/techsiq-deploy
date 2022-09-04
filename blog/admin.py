from django.contrib import admin

from blog.models import Blog, Category, CohortApplication, TechsiqTeam
# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(TechsiqTeam)
admin.site.register(CohortApplication)

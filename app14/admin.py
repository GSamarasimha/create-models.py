from django.contrib import admin

from app14.models import Access_records, Topic, Webpage

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Access_records)
from django.contrib import admin

# Register your models here.
from .models import Story, Paragraph

admin.site.register((Story, Paragraph, ))

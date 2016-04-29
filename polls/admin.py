from django.contrib import admin

# Register your models here.

from .models import mcsv
from .models import Survey
from .models import Response

admin.site.register(Survey)
admin.site.register(Response)
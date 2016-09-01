from django.contrib import admin
from .models import NHSBTFile, NHSBTRecord, NHSBTLog

# Register your models here.
admin.register(NHSBTFile)
admin.register(NHSBTRecord)
admin.register(NHSBTLog)
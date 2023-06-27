from django.contrib import admin

from apps.core.models import APIEndpoint, Authorization, Parameter


admin.site.register(APIEndpoint)
admin.site.register(Parameter)
admin.site.register(Authorization)

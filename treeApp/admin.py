from django.contrib import admin
from .models import clients
from .models import Users
from .models import orders
from .models import requirements

# Register your models here.
admin.site.register(clients)
admin.site.register(Users)
admin.site.register(orders)
admin.site.register(requirements)



from django.contrib import admin

from .models.requestStatus import RequestStatus
from .models.review import Review
from .models.request import Request
from .models.user import User
from .models.roles import Roles
from .models.service import Service

admin.site.register(Request)
admin.site.register(RequestStatus)
admin.site.register(User)
admin.site.register(Roles)
admin.site.register(Service)
admin.site.register(Review)

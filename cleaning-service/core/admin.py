from django.contrib import admin
from core.models.requestStatus import RequestStatus
from core.models.review import Review
from core.models.order import Order
from core.models.user import User
from core.models.roles import Roles
from core.models.service import Service

admin.site.register(Order)
admin.site.register(RequestStatus)
admin.site.register(User)
admin.site.register(Roles)
admin.site.register(Service)
admin.site.register(Review)

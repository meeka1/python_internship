import factory
from faker import Faker
fake = Faker()

from core.models import roles, user, service, order, requestStatus, review


class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = roles.Roles
    roles = 'client'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = user.User
    fullname = fake.name()
    role = factory.SubFactory(RoleFactory)


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = service.Service
    name = fake.name()
    cost = 12


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = requestStatus.RequestStatus
    status = "pending"


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = order.Order
    user_id = factory.SubFactory(UserFactory)
    status_id = factory.SubFactory(StatusFactory)
    address = fake.address()
    total_area = 15
    total_cost = factory.SubFactory(ServiceFactory)
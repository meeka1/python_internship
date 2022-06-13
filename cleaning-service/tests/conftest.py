import pytest

from  rest_framework.test import APIClient 
from pytest_factoryboy import register
from tests.factory import RoleFactory, UserFactory, ServiceFactory, StatusFactory, OrderFactory

register(RoleFactory)
register(UserFactory)
register(ServiceFactory)
register(OrderFactory)
register(StatusFactory)

@pytest.fixture
def client():
   return APIClient()


@pytest.fixture
def new_user(user_factory):
    user = user_factory.create()
    return user


@pytest.fixture
def new_role(role_factory):
    role = role_factory.create()
    return role


@pytest.fixture
def new_service(service_factory):
    service = service_factory.create()
    return service


@pytest.fixture
def new_order(order_factory):
    order = order_factory.create()
    return order
    

@pytest.fixture
def new_status(status_factory):
    status = status_factory.create()
    return status
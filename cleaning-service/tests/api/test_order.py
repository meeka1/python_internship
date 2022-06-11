import json
import pytest
from mixer.backend.django import mixer
from core.models import order

@pytest.mark.django_db
def test_order_list(client):
   mixer.blend(order.Order)
   response = client.get(f'http://127.0.0.1:8000/api/order/')
   assert response.json()!=None
   assert len(response.json())==1
   assert response.status_code==200

@pytest.mark.django_db
def test_order_create(client, new_user, new_status, new_service):
    data = {
        'total_area':196.89,
        'total_cost':new_service.id,
        'user_id':new_user.id,
        'address':'Dobra',
        'created_at':'02-02-2002',
        'status_id':new_status.id,
    }
    url = f'http://127.0.0.1:8000/api/order/create/'
    response = client.post(url, data)

    assert response.json() != None
    assert response.status_code == 201
    assert  json.loads(response.content)["address"]==data["address"]

@pytest.mark.django_db
def test_order_detail(client):
    ord = mixer.blend(order.Order)
    url = (f'http://127.0.0.1:8000/api/order/{ord.id}/')
    response = client.get(url)
    res = response.content
    my_json = res.decode('utf-8').replace("'", '"')
    data = json.loads(my_json)
    url = (f'http://127.0.0.1:8000/api/order/update/{ord.id}/')
    response = client.put(url, data)

    assert response.json() != None
    assert response.status_code == 200

@pytest.mark.django_db
def test_order_delete(client):
    ord = mixer.blend(order.Order)
    url = (f'http://127.0.0.1:8000/api/order/delete/{ord.id}/')
    response = client.delete(url)

    assert response.status_code == 204
    assert order.Order.objects.filter(pk=ord.id).exists()==False
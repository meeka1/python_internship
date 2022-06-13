import pytest, json
from mixer.backend.django import mixer
from django.urls import reverse
from core.models import service


@pytest.mark.django_db
def test_service_list(client, new_user):
   mixer.blend(service.Service, user_id = new_user)
   url = reverse('service_list')
   response = client.get(url)
   assert response.json()!=None
   assert len(response.json())==1
   assert response.status_code==200


@pytest.mark.django_db
def test_service_create(client, new_user):
    data = {
        'name':'Meeeka',
        'cost':12.99,
        'company':'Exadel',
        'user_id':new_user.id,
    }
    url = reverse('service_create')
    response = client.post(url, data)

    assert response.json() != None
    assert response.status_code == 201
    assert service.Service.objects.filter(name=data['name']).exists()


@pytest.mark.django_db
def test_service_detail(client, new_user):
    serv = mixer.blend(service.Service, user_id=new_user)
    url = reverse('service_detail', kwargs={"pk":serv.id})
    response = client.get(url)
    res = response.content
    my_json = res.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    url = reverse('service_update', kwargs={"pk":serv.id})
    response = client.put(url, data)

    assert response.json() != None
    assert response.status_code == 200


@pytest.mark.django_db
def test_service_delete(client):
    serv = mixer.blend(service.Service)
    url = reverse('service_delete', kwargs={"pk":serv.id})
    response = client.delete(url)

    assert response.status_code==204
    assert not service.Service.objects.filter(pk=serv.id).exists()
    
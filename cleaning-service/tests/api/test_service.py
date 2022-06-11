import pytest, json
from mixer.backend.django import mixer
from core.models import service

@pytest.mark.django_db
def test_service_list(client, new_user):
   mixer.blend(service.Service, user_id = new_user)
   response = client.get(f'http://127.0.0.1:8000/api/service/')
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
    url = f'http://127.0.0.1:8000/api/service/create/'
    response = client.post(url, data)

    assert response.json() != None
    assert response.status_code == 201
    assert  json.loads(response.content)["company"]==data["company"]

@pytest.mark.django_db
def test_service_detail(client, new_user):
    serv = mixer.blend(service.Service, user_id=new_user)
    url = f'http://127.0.0.1:8000/api/service/{serv.id}/'
    response = client.get(url)
    res = response.content
    my_json = res.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    url = f'http://127.0.0.1:8000/api/service/update/{serv.id}/'
    response = client.put(url, data)

    assert response.json() != None
    assert response.status_code == 200

@pytest.mark.django_db
def test_service_delete(client):
    serv = mixer.blend(service.Service)
    url = f'http://127.0.0.1:8000/api/service/delete/{serv.id}/'
    response = client.delete(url)

    assert response.status_code==204
    assert service.Service.objects.filter(pk=serv.id).exists()==False
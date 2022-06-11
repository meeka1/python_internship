import pytest
import json
from mixer.backend.django import mixer
from core.models import user


@pytest.mark.django_db
def test_user_list(client):
   mixer.blend(user.User)
   response = client.get(f'http://127.0.0.1:8000/api/user/')
   assert response.json() != None
   assert len(response.json()) == 1
   assert response.status_code == 200

@pytest.mark.django_db
def test_user_create(client):
   data = {
      'fullname':'Ha Nyugan',
      'email':'hyugan@gmail.com',
      'phone':'99987797',
      'role':'client'
   }
   url = 'http://127.0.0.1:8000/api/user/create/'
   response = client.post(url, data)

   assert response.json() != None
   assert response.status_code == 201
   assert json.loads(response.content)["fullname"]==data["fullname"]

@pytest.mark.django_db
def test_user_detail(client):
   userr = mixer.blend(user.User, fullname='Ha Nyugan')
   url = (f'http://127.0.0.1:8000/api/user/{userr.id}/')
   response = client.get(url)
   res = response.content
   my_json = res.decode('utf-8').replace("'", '"')
   data = json.loads(my_json)
   url = (f'http://127.0.0.1:8000/api/user/update/{userr.id}/')
   response = client.put(url, data)

   assert response.json()!=None
   assert response.status_code==200

@pytest.mark.django_db
def test_user_delete(client):
   userr = mixer.blend(user.User)
   url = (f'http://127.0.0.1:8000/api/user/delete/{userr.id}/')
   response = client.delete(url)

   assert response.status_code==204
   assert user.User.objects.filter(pk=userr.id).exists()==False

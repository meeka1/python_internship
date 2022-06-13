import pytest
import json
from mixer.backend.django import mixer
from django.urls import reverse
from core.models import user


@pytest.mark.django_db
def test_user_list(client):
   mixer.blend(user.User)
   url = reverse('user_list')
   response = client.get(url)
   
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
   url = reverse('user_create')
   response = client.post(url, data)

   assert response.json() != None
   assert response.status_code == 201
   assert user.User.objects.filter(fullname=data['fullname']).exists()


@pytest.mark.django_db
def test_user_detail(client):
   userr = mixer.blend(user.User, fullname='Ha Nyugan')
   url = reverse('user_detail', kwargs={"pk":userr.id})
   response = client.get(url)
   res = response.content
   my_json = res.decode('utf-8').replace("'", '"')
   data = json.loads(my_json)
   url = reverse('user_update', kwargs={"pk":userr.id})
   response = client.put(url, data)

   assert response.json()!=None
   assert response.status_code==200


@pytest.mark.django_db
def test_user_delete(client):
   userr = mixer.blend(user.User)
   url = reverse('user_delete', kwargs={"pk":userr.id})
   response = client.delete(url)

   assert response.status_code==204
   assert user.User.objects.filter(pk=userr.id).exists()==False

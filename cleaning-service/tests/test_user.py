import  pytest 
from  rest_framework.test import APIClient
from  core.models.user  import User
import  json


@pytest.fixture
def client():
   return APIClient()

@pytest.mark.django_db
def test_user_post(client):
    payload=dict(
       #id = 1,
       fullname = "Mashkhura Eshmatova",
       email = "harry@hogwarts.com",
       phone = "998999999999",
       role = "client"
    )
    response=client.post('http://127.0.0.1:8000/api/user/create/',data=payload,format='json')
    assert  response.status_code==201

@pytest.mark.django_db
def  test_user_list(client):
   User.objects.create(
       #id = 5,
       fullname = "Shahruza Eshmatova",
       email = "harry@hogwarts.com",
       phone = "998999999999",
       role = "client"
   )
   User.objects.create(
       #id = 1,
       fullname = "Saida Eshmatova",
       email = "harry@hogwarts.com",
       phone = "998999999999",
       role = "client"
   )
   response=client.get('http://127.0.0.1:8000/api/user/')
   assert response.status_code==200
   assert len(response.content)

@pytest.mark.django_db
def test_user_detail_404(client):
    response=client.get('http://127.0.0.1:8000/api/user/2/')
    assert  response.status_code==405    

@pytest.mark.django_db
def  test_user_update(client):
   user = User.objects.create(
       #id = 1,
       fullname = "Shahruza Eshmatova",
       email = "harry@hogwarts.com",
       phone = "998999999999",
       role = "client"
   )
   payload=dict(
      fullname = "Shahruza Eshmatova", 
      email = "harry@hogwarts.com",
      phone = "998999999999",
      role = "client"
      )
   response=client.put(f'http://127.0.0.1:8000/api/user/{user.id}/', payload,  format='json')
   user.refresh_from_db()
   assert  json.loads(response.content)["fullname"]==payload["fullname"]


@pytest.mark.django_db
def  test_service_delete(client):
   user= User.objects.create(
       #id = 1,
       fullname = "Shahruza Eshmatova",
       email = "harry@hogwarts.com",
       phone = "998999999999",
       role = "client"
    )
   response=client.delete(f'http://127.0.0.1:8000/api/user/delete/{user.id}/')
   assert  response.status_code==204
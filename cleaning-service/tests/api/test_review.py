import json
import pytest
from mixer.backend.django import mixer
from rest_framework.reverse import reverse
from core.models import review


@pytest.mark.django_db
def test_review_list(client, new_service, new_user, new_order):
    mixer.blend(review.Review, service_id=new_service, order_id=new_order, user_id=new_user)
    url = reverse('review_list')
    response=client.get(url)
    assert response.json() != None
    assert len(response.json()) == 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_review_create(client, new_service, new_user, new_order):
    data = {
        "order_id": new_order.id,
        "rating": 3,
        "feedback": "dsadas",
        "created_at": "2022-05-22",
        "service_id": new_service.id,
        "user_id": new_user.id,
    }
    url = reverse('review_create')
    response = client.post(url, data=data)

    assert response.json() != None
    assert response.status_code == 201
    assert review.Review.objects.filter(order_id=data["order_id"]).exists()


@pytest.mark.django_db
def test_review_detail(client, new_service, new_order):
    rev = mixer.blend(review.Review, service_id=new_service, order_id=new_order)
    url = reverse('review_detail', kwargs={"pk":rev.id})
    response = client.get(url)
    res = response.content
    my_json = res.decode('utf-8').replace("'", '"')
    data = json.loads(my_json)
    url = reverse('review_update', kwargs={"pk":rev.id})
    response = client.put(url, data)

    assert response.json() != None
    assert response.status_code == 200


@pytest.mark.django_db
def test_review_delete(client, new_service, new_order):
    rev = mixer.blend(review.Review, service_id=new_service, order_id=new_order)
    url = reverse('review_delete', kwargs={"pk":rev.id})
    response = client.delete(url)

    assert response.status_code == 204
    assert not review.Review.objects.filter(pk=rev.id).exists()

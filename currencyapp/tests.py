import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_setup(request):
    return User.objects.create_user(username='temporary', email='jlennon@beatles.com', password='temporary')


def test_not_logined(client):
    response = client.get('/currency/')
    assert response.status_code == 302


@pytest.mark.django_db
def test_logined(client, user_setup):
    user = user_setup
    client.force_login(user)
    response = client.get('/currency/')
    assert response.status_code == 200
    assert b'Company' in response.content

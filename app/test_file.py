from django.urls import reverse
from .views import register_user
import pytest
from django.test.client import RequestFactory


@pytest.mark.django_db #
def register_view():
    path = reverse("register")
    request = RequestFactory().get(path)
    response = register_user(request)
    assert response.status_code == 200
import pytest
pytestmark = pytest.mark.django_db
from mixer.backend.django import mixer

from django.contrib.admin.sites import AdminSite

from .. import models
from .. import admin

class TestPostAdmin:
    def test_excrept(self):
        site=AdminSite()
        post_admin = admin.PostAdmin(models.Post,site)

        obj=mixer.blend('sampleApp.Post',body='Hello World')
        result = post_admin.excerpt(obj)
        assert result == 'Hello', 'Should return first few characters'

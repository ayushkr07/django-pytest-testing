import pytest
pytestmark = pytest.mark.django_db
from mixer.backend.django import mixer
class TestPost:
    def test_model(self):
        obj=mixer.blend('sampleApp.Post')
        assert obj.pk == 1, 'Should create a Post instance'

    def test_get_excerpt(self):
        obj = mixer.blend('sampleApp.Post',body='Hello World')
        result=obj.get_excerpt(5)
        assert result == 'Hello', 'Should return first few characters'
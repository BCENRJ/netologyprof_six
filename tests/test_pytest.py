import pytest
from project.instruments import create_new_folder_ya_disk


class TestClass:
    token = 'PASTE YOUR YANDEX TOKEN'

    # Two passed tests
    @pytest.mark.parametrize('a, b, r', [(token, 't_folder', 201), (token, 't_folder_1', 201)])
    def test_create_new_folder_ya_disk_param(self, a, b, r):
        result = create_new_folder_ya_disk(a, b)
        assert result == r

    # Third passed
    def test_create_new_folder_ya_disk(self):
        result = create_new_folder_ya_disk(self.token, 't_folder')
        assert result != 201

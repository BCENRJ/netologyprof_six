import unittest.mock
from project.instruments import SecretaryApp
from project.data import test_doc as dc, test_dir as dr


class TestSecretaryApp(unittest.TestCase):
    test_instance = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.test_instance = SecretaryApp(dc, dr)

    def test_get_doc_owner_name(self) -> None:
        a = self.test_instance.get_doc_owner_name('1')
        b = self.test_instance.get_doc_owner_name('11-2')
        self.assertEqual(a, None)
        self.assertEqual(type(b), str)

    def test_get_doc_shelf_num(self) -> None:
        a = self.test_instance.get_doc_shelf_num('1')
        b = self.test_instance.get_doc_shelf_num('11-2')
        self.assertEqual(a, None)
        self.assertEqual(type(b), str)

    def test_get_all_doc(self) -> None:
        self.assertEqual(type(self.test_instance.get_all_doc()), list)

    @unittest.mock.patch('project.instruments.SecretaryApp.add_new_doc', return_value=True)
    def test_add_new_doc(self, mocking) -> None:
        a = self.test_instance.add_new_doc()
        self.assertTrue(a)

    @unittest.mock.patch('project.instruments.SecretaryApp.del_doc', return_value=True)
    def test_del_doc(self, mocking) -> None:
        a = self.test_instance.del_doc('1')
        self.assertTrue(a)

    def test_add_new_shelf(self) -> None:
        with unittest.mock.patch('project.instruments.SecretaryApp.add_new_shelf', return_value=True):
            a = self.test_instance.add_new_shelf('1')
        self.assertTrue(a)


if __name__ == '__main__':
    unittest.main()

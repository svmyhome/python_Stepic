import unittest

from stepic.testing.city_function import city_transform


class nameTestClass(unittest.TestCase):

    def test_city_country(self):
        formatted_city = city_transform('cbdc', 'cjdncjd')
        self.assertEqual(formatted_city, 'Cbdc, Cjdncjd')

    def test_city_country_count(self):
        formatted_city = city_transform('cbdc', 'cjdncjd', '5000')
        self.assertEqual(formatted_city, 'Cbdc, Cjdncjd, 5000')


if __name__ == '__main':
    unittest.main()

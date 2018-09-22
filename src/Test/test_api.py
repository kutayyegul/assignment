import unittest
import requests


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://jsonplaceholder.typicode.com/"

    def test_should_return_200_code(self):
        r = requests.get(self.base_url + "users")
        assert r.status_code, 200

    def test_should_be_less_than_200ms(self):
        r = requests.get(self.base_url + "users")
        print r.elapsed.total_seconds()
        assert r.elapsed.total_seconds() <= 0.200

    def test_should_return_group_companies(self):
        r = requests.get(self.base_url + "users")

        output = r.json()


        for value in output:

            companyName = value["company"]["name"]

            if "Group" in companyName:
                print(companyName)


if __name__ == "__main__":
    unittest.main()
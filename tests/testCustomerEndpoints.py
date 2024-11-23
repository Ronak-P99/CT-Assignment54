import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from services.customerService import find_customers_gmail
from app import create_app, init_customers_info_data
from database import db



class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.app = create_app("TestingConfig")
        with self.app.app_context():
            db.drop_all()
            db.create_all()
        self.client = self.app.test_client()

    def test_create_customer(self):
        customer_payload = {"name": "customer1", "email": "customer1@gmail.com", "phone": "1234567890"}

        response = self.client.post("/customers/", json = customer_payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["name"], "customer1")

    def test_find_gmail(self):
        customer_payload = [(u'Customer Two', u'customer2@gmail.com', u'092319283')]
        response = self.client.get("/customers/gmail/", json = customer_payload)
        self.assertEqual(response.json["name"], "Customer Two" )












if __name__ == '__main__':
    unittest.main()
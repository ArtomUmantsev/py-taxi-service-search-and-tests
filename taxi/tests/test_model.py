from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Driver, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="test", country="testcountry"
        )
        self.assertEqual(
            str(manufacturer), f"{manufacturer.name} {manufacturer.country}"
        )

    def test_driver_str(self):
        driver = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="testfirst",
            last_name="testlast",
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})",
        )

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(
            name="test", country="testcountry"
        )
        driver = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="testfirst",
            last_name="testlast",
        )
        car = Car.objects.create(
            model="test",
            manufacturer=manufacturer,
        )
        car.drivers.set([driver])
        self.assertEqual(str(car), f"{car.model}")

    def test_create_driver_with_license_number(self):
        username = "test"
        password = "test123"
        license_number = "TES12345"
        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number,
        )
        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)

"""Test."""
import datetime
import logging
from django.test import TestCase
# from django.utils import timezone
from .data_container import BME280dc
from .models import BME280
from .store_tph import StoreTph
import tph.settings as ts

logger = logging.getLogger(__name__)


class BME280ModelTests(TestCase):
    """Test BME280Model."""

    def test_save_BM280(self):
        """Save data."""
        w_bme280 = BME280(
            temperature=0.0,
            pressure=0.0,
            humidity=0.0,
        )
        w_bme280.save()
        id = w_bme280.id
        r_bme280s = BME280.objects.filter(id=id).values()
        self.assertEqual(r_bme280s[0]['temperature'], 0.0)


class BME280dcTests(TestCase):
    """Teest data container BME280dc."""

    def test_get_BME280dc_t(self):
        """Get datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        self.assertEqual(temperature, w_bme280dc.t)

    def test_get_BME280dc_p(self):
        """Get datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        self.assertEqual(pressure, w_bme280dc.p)

    def test_get_BME280dc_h(self):
        """Get datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        self.assertEqual(humidity, w_bme280dc.h)

    def test_get_BME280dc_mdt(self):
        """Get datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        self.assertIsInstance(w_bme280dc.mdt, datetime.datetime)

    def test_set_BME280dc_t(self):
        """Set datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        w_bme280dc.t = 5.8
        self.assertEqual(5.8, w_bme280dc.t)

    def test_set_BME280dc_p(self):
        """Set datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        w_bme280dc.p = 987
        self.assertEqual(987, w_bme280dc.p)

    def test_set_BME280dc_h(self):
        """Set datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        w_bme280dc.h = 24
        self.assertEqual(24, w_bme280dc.h)


class StoreTphTests(TestCase):
    """Test StoreTPH."""

    def test_save_StoreTph(self):
        """Save data."""
        storeTph = StoreTph(ts.BME280CH1_ADDR)
        id = storeTph.save()
        mbe280 = BME280().objects.get(id=id)
        self.assertEqual(id, mbe280['id'])

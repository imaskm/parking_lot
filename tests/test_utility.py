import unittest
from src import utility
from src.classes import parkingLot

class TestUtility(unittest.TestCase):

    def test_check_if_parking_lot_already_exists(self):
        try:
            parking_object = utility.create_parking_lot(1)
            self.assertEqual(True, utility.check_if_parking_lot_already_exists())
            # import pdb
            # pdb.set_trace()
            del parking_object.__class__.instance
            self.assertEqual(False, utility.check_if_parking_lot_already_exists())
        finally:
            try:
                if parking_object:
                    del parking_object
            except UnboundLocalError:
                pass

    def test_create_parking_lot(self):
        try:
            parking_object = utility.create_parking_lot(1)
            self.assertIsInstance(parking_object, parkingLot.ParkingLot)
        finally:
            del parking_object

    def test_get_parking_lot(self):
        try:
            parking_object = parkingLot.ParkingLot(1)
            self.assertIsInstance(utility.get_parking_lot(), parkingLot.ParkingLot)
        finally:
            del parking_object






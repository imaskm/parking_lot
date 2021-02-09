import unittest
from src.classes import parkingLot


class TestParkingLot(unittest.TestCase):
    def setUp(self) -> None:
        self.max_slot = 5
        self.slots_filled = 0
        self.parking_lot = parkingLot.ParkingLot(self.max_slot)

    def tearDown(self) -> None:
        del self.parking_lot

    def test_get_max_slots(self):
        self.assertEqual(self.max_slot, self.parking_lot.get_max_slots())

    def test_get_slots_filled(self):
        self.assertEqual(self.slots_filled, self.parking_lot.get_slots_filled())

    def test_get_available_slot(self):
        self.assertEqual(self.max_slot-self.slots_filled, self.parking_lot.get_available_slot())


if __name__ == '__main__':
    unittest.main()

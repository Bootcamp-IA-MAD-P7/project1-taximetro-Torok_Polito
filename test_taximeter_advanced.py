import unittest
import os
from datetime import datetime
from taximetro_advanced import DigitalTaximeter, save_trip_history


class TestDigitalTaximeterFare(unittest.TestCase):
    def test_calculate_fare_normal_values(self):
        taximeter = DigitalTaximeter()
        taximeter.stopped_time = 10
        taximeter.moving_time = 20

        result = taximeter.calculate_fare()

        self.assertAlmostEqual(result, 1.2)

    def test_calculate_fare_zero_values(self):
        taximeter = DigitalTaximeter()
        taximeter.stopped_time = 0
        taximeter.moving_time = 0

        result = taximeter.calculate_fare()

        self.assertEqual(result, 0)

    def test_calculate_fare_only_stopped(self):
        taximeter = DigitalTaximeter()
        taximeter.stopped_time = 30
        taximeter.moving_time = 0

        result = taximeter.calculate_fare()

        self.assertAlmostEqual(result, 0.6)

    def test_calculate_fare_only_moving(self):
        taximeter = DigitalTaximeter()
        taximeter.stopped_time = 0
        taximeter.moving_time = 30

        result = taximeter.calculate_fare()

        self.assertAlmostEqual(result, 1.5)


class TestSaveTripHistoryAdvanced(unittest.TestCase):
    def test_save_trip_history_creates_file(self):
        filename = "test_trip_history.txt"

        trip_data = {
            "start": datetime(2026, 5, 12, 14, 30, 0),
            "end": datetime(2026, 5, 12, 14, 30, 0),
            "stopped_time": 20,
            "moving_time": 100,
            "total_fare": 5.02
        }

        save_trip_history(trip_data, filename)

        self.assertTrue(os.path.exists(filename))

        expected_content = "START: 2026-05-12 14:30:00 | END: 2026-05-12 14:30:00 | STOPPED: 20.0s | MOVING: 100.0s | FARE: €5.02\n"

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        self.assertEqual(content, expected_content)

        os.remove(filename)


if __name__ == "__main__":
    unittest.main()
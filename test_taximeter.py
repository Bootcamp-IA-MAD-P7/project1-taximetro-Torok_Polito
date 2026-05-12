import unittest #librería necesaria de python para poder hacer los testeos
import os #para interactuar con el sistema operativo
from taximetro_intermediate import calculate_fare, save_trip_history #importo las funciones que voy a testear
from datetime import datetime

class TestCalculateFare(unittest.TestCase): #voy a agrupar todos los test de la función CalculateFare en esta clase
    def test_calculate_fare_normal_values(self):
        result = calculate_fare(10, 20) #testeo con valores normales - 10 parado y 20 en movimiento
        self.assertAlmostEqual(result, 1.2) #le paso el resultado real y el esperado 1.2 self.assertAlmostEqual(valor_real, valor_esperado)
    
    def test_calculate_fare_zero_values(self):
        result = calculate_fare(0, 0) #testeo con valores cero, el resultado esperado es 0
        self.assertEqual(result, 0)

    def test_calculate_fare_only_stopped(self):
        result = calculate_fare(30, 0) #testeo con 30 segundos parado y 0 en movimiento, el resultado esperado es 0.6
        self.assertAlmostEqual(result, 0.6)

    def test_calculate_fare_only_moving(self):
        result = calculate_fare(0, 30) #testeo con 0 segundos parado y 30 en movimiento, el resultado esperado es 1.5
        self.assertAlmostEqual(result, 1.5)
    
class TestSaveTripHistory(unittest.TestCase): #voy a agrupar todos los test de la función SaveTripHistory en esta clase
    def test_save_trip_history_creates_file(self):
        trip_data = {
        "start": datetime(2026, 5, 12, 14, 30, 0),
        "end": datetime(2026, 5, 12, 14, 30, 0),
        "stopped_time": 20,
        "moving_time": 100,
        "total_fare": 5.02
        }
        save_trip_history(trip_data, "test_trip_history.txt") #archivo específico de testeo
        self.assertTrue(os.path.exists("test_trip_history.txt")) #verifico que el archivo se haya creado
        
        expected_content = "START: 2026-05-12 14:30:00 | END: 2026-05-12 14:30:00 | STOPPED: 20.0s | MOVING: 100.0s | FARE: €5.02\n"

        with open("test_trip_history.txt", "r", encoding="utf-8") as file:
            content = file.read()
        self.assertEqual(content, expected_content)
        os.remove("test_trip_history.txt") #elimino el archivo después de testear para que no de error si se crea dos veces

if __name__ == "__main__":
    unittest.main()
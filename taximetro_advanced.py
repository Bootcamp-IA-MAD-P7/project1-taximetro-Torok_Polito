import time
import logging
from datetime import datetime 

logging.basicConfig(
    filename='taximeter.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
    ) 

"""
creo una clase para encapsular toda la lógica del taxímetro y evitar tener variables globales. 
Esto también me permite crear múltiples instancias del taxímetro si quisiera.
"""
class DigitalTaximeter: 
    def __init__(self): #en el constructor inicializo todas las variables necesarias para el funcionamiento del taxímetro, tanto las de estado como las tarifas.
        self.trip_active = False
        self.stopped_time = 0
        self.moving_time = 0
        self.state = None
        self.state_start_time = 0
        self.trip_start_datetime = None

        self.stopped_rate = 0.02 #las tarifas las defino como atributos del objeto en lugar de variables locales.
        self.moving_rate = 0.05

    def calculate_fare(self): #Calcula la tarifa usando los tiempos y tarifas guardados en el objeto.
        fare = self.stopped_time * self.stopped_rate + self.moving_time * self.moving_rate
        return fare

    def start_trip(self): #inicializa un nuevo viaje y resetea los estados del taxímetro
        self.trip_active = True
        self.trip_start_datetime = datetime.now()
        self.stopped_time = 0
        self.moving_time = 0
        self.state = 'stopped' #el viaje empieza detenido
        self.state_start_time = time.time()
        
    def change_state(self, new_state): #Actualiza el tiempo acumulado del estado anterior y cambia al nuevo estado.
        duration = time.time() - self.state_start_time

        if self.state == 'stopped':
            self.stopped_time += duration
        else:
            self.moving_time += duration

        self.state = new_state
        self.state_start_time = time.time()
    
    def finish_trip(self): #finaliza el viaje, calcula la tarifa total y devuelve un resumen del viaje.
        duration = time.time() - self.state_start_time

        if self.state == 'stopped':
            self.stopped_time += duration
        else:
            self.moving_time += duration

        total_fare = self.calculate_fare()
        trip_end_datetime = datetime.now()

        trip_data = {
            "start": self.trip_start_datetime,
            "end": trip_end_datetime,
            "stopped_time": self.stopped_time,
            "moving_time": self.moving_time,
            "total_fare": total_fare
        }

        save_trip_history(trip_data)

        self.trip_active = False
        self.state = None

        return trip_data

def run_taximeter():
    print("welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")
        
    taximeter = DigitalTaximeter()
        
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == 'start':
            
            if taximeter.trip_active:
                print("Error: A trip is already in progress.")
                continue

            taximeter.start_trip()
            print("Trip started. Initial state: 'stopped'.")
            
        elif command in ("stop", "move"):

            if not taximeter.trip_active:
                print("Error: No active trip. Please start first.")
                continue

            new_state = 'stopped' if command == "stop" else "moving"

            taximeter.change_state(new_state)

            print(f"State changed to '{new_state}'.")
            
        elif command == "finish":
            
            if not taximeter.trip_active:
                print("ERROR: No active trip to finish")
                continue
            
            trip_data = taximeter.finish_trip()
            
            print(f"\n-- Trip summary --")
            print(f"Stopped time: {trip_data['stopped_time']:.1f} seconds")
            print(f"Moving time: {trip_data['moving_time']:.1f} seconds")
            print(f"Total fare: €{trip_data['total_fare']:.2f}\n")
            print("-------------------------------\n")
            
        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Unknown command. Please use 'start', 'stop', 'move', 'finish', or 'exit'.")
                
def save_trip_history(trip_data, filename="trip_history.txt"):
    formatted_start = trip_data["start"].strftime("%Y-%m-%d %H:%M:%S")
    formatted_end = trip_data["end"].strftime("%Y-%m-%d %H:%M:%S")

    trip_record = f"START: {formatted_start} | END: {formatted_end} | STOPPED: {trip_data['stopped_time']:.1f}s | MOVING: {trip_data['moving_time']:.1f}s | FARE: €{trip_data['total_fare']:.2f}\n"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(trip_record)

if __name__ == "__main__":
    run_taximeter()
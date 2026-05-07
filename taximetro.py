import time

def calculate_fare(seconds_stopped, seconds_moving):
    """
    Calcular la tarifa total en euros.
    - Stopped: 0.02 €/s
    - Moving: 0.05 €/s
    """
    fare= seconds_stopped * 0.02 + seconds_moving * 0.05
    return fare

def taximeter():
    """
    Funci{on para manejar y mostar las opciones del taxímetro.
    """
    print("welcome to the F% Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_active = False
    start_time = 0
    stopped_time = 0
    moving_time = 0
    state = None # 'stopped' or 'moving'
    state_start_time = 0

    while True:
        command = input("> ").strip().lower()

        if command == 'start':
            if trip_active:
                print("Error: A trip is already in progress.")
                continue
            trip_active = True
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped' #Iniciamos un estado 'stoped'
            state_start_time = time.time()
            print("Trip started. Initial state: 'stopped'.")
            
        elif command in ("stop", "move"):
            if not trip_active:
                print("Error: No active trip. Please start first.")
                continue
            #Calcula el tiempo del estado anterior
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else: 
                moving_time += duration

            #cambia el estado
            state = 'stopped' if command == "stop" else "moving"
            state_start_time = time.time()
            print(f"State changed to '{state}'.")

        elif command == "finish":
            if not trip_active:
                print("Error: No active trip to finish.")
                continue
            #Agregar el tiempo del último estado
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration
            #Calcula la tarifa total y muestra el resumen del viaje
            total_fare = calculate_fare(stopped_time, moving_time)
            print(f"\n-- Trip Summary --")
            print(f"Stopped time: {stopped_time:.1f} seconds")
            print(f"Moving time: {moving_time:.1f} seconds")
            print(f"Total fare: €{total_fare:.2f}\n")
            print("---------------------\n")

            #Reset las variables para el próximo viaje
            trip_active = False
            state = None

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Unknown command. Please use 'start', 'stop', 'move', 'finish', or 'exit'.")


if __name__ == "__main__":
    taximeter()
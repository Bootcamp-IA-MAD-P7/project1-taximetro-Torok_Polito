import time  #importa la librería time que permite medir el tiempo real

def calculate_fare(seconds_stopped, seconds_moving): #recibe como datos cuanto estuvo  el taxi parado y cuanto en movimiento
    """
    En el nivel intermedio vamos a crear una variable para los precios porque por si un día cambian sea más fácil de modificar.
    """
    stopped_rate = 0.02
    moving_rate = 0.05
    fare= seconds_stopped * stopped_rate + seconds_moving * moving_rate #calcula el precio llamando a las variables
    return fare

def taximeter(): #esta es la función más importante del programa. muestra mensajes, recibe comandos y calcula los tiempos.
    """
    Funcion para manejar y mostar las opciones del taxímetro.
    """
    print("welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n") #son los primeros comandos que se imprimen para que el usuario sepa que opciones tiene

    trip_active = False #no hay viajes activos
    start_time = 0
    stopped_time = 0 #acá se van a guardar el tiempo parado y el tiempo en movimiento
    moving_time = 0
    state = None # 'stopped' or 'moving'
    state_start_time = 0 #guarda el momento en que empezó el estado actual para el cálculo

    while True:
        command = input("> ").strip().lower() #espera a que escribas algo en ese paréntesis, quita los espacios al inicio y final y lo vuelve minúscula

        if command == 'start': #revisa si hay un viaje comenzado y si volvés a iniciarlo da error
            if trip_active:
                print("Error: A trip is already in progress.")
                continue
            trip_active = True #si no había un viaje activo, lo inicia
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
            if state == 'stopped': #si el estado era parado suma ese tiempo a stopped_time, si era en movimiento suma a moving_time
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
            print(f"Moving time: {moving_time:.1f} seconds") #muestra un número con un decimal
            print(f"Total fare: €{total_fare:.2f}\n") #muestra un número con dos decimales
            print("---------------------\n")

            #Reset las variables para el próximo viaje
            trip_active = False
            state = None

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break #sale del programa si el comando es exit

        else:
            print("Unknown command. Please use 'start', 'stop', 'move', 'finish', or 'exit'.")


if __name__ == "__main__": #solo ejecuta esto si el archivo fue lanzado directamente, no si fue importado como módulo
    taximeter()
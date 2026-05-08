import time  #importa la librería time que permite medir el tiempo real
from datetime import datetime #esta libreria la quiero porque decidí guardar los registros con fecha y hora humana.

def calculate_fare(seconds_stopped, seconds_moving): #recibe como datos cuanto estuvo  el taxi parado y cuanto en movimiento
    """
    En el nivel intermedio vamos a crear una variable para los precios porque por si un día cambian sea más fácil de modificar.
    """
    stopped_rate = 0.02
    moving_rate = 0.05
    fare= seconds_stopped * stopped_rate + seconds_moving * moving_rate #calcula el precio llamando a las variables
    return fare

def save_trip_history(trip_data):
    """ 
    Hice esta función auxiliar para que el código no me quede tan extenso en la función taximeter. Lo que hace es definir el formato del registro delviaje y
    guardarlo en un archivo de texto. El registro incluye la fecha y hora de inicio y fin del viaje, el tiempo parado, el tiempo en movimiento y la tarifa total.
    Llamaré a esta función al finalizar el viaje para mantener el dato siempre en crudo y recién luego convertirlo a string.
    """
    formatted_start = trip_data["start"].strftime("%Y-%m-%d %H:%M:%S")
    formatted_end = trip_data["end"].strftime("%Y-%m-%d %H:%M:%S")

    trip_record = f"START: {formatted_start} | END: {formatted_end} | STOPPED: {trip_data['stopped_time']:.1f}s | MOVING: {trip_data['moving_time']:.1f}s | FARE: €{trip_data['total_fare']:.2f}\n"

    with open("trip_history.txt", "a") as file:
        file.write(trip_record) #primero le doy formato y después recién lo guardo por si se produce un error, que no afecte al archivo y para facilitar el debugueo.

def taximeter(): #esta es la función más importante del programa. muestra mensajes, recibe comandos y calcula los tiempos.
    print("welcome to the F5 Taximeter!")
    print("Available commands: 'start', 'stop', 'move', 'finish', 'exit'\n") #son los primeros comandos que se imprimen para que el usuario sepa que opciones tiene

    trip_active = False #no hay viajes activos
    stopped_time = 0 #acá se van a guardar el tiempo parado y el tiempo en movimiento
    moving_time = 0
    state = None # 'stopped' or 'moving'
    state_start_time = 0 #guarda el momento en que empezó el estado actual para el cálculo
    trip_start_datetime = None #guarda la fecha y hora del inicio del viaje, para mostrarlo en el resumen al finalizar el viaje

    while True:
        command = input("> ").strip().lower() 

        if command == 'start': #en esta version del proyecto en este tramo inicio el contador para el registro del viaje.
            if trip_active:
                print("Error: A trip is already in progress.")
                continue
            trip_active = True
            trip_start_datetime = datetime.now() #guarda la fecha y hora del inicio del viaje
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
            trip_end_datetime = datetime.now() #guardo el momento de finalización

            trip_data = { #creo un diccionario con toda la información del viaje para luego guardarlo en el archivo de texto
                "start": trip_start_datetime,
                "end": trip_end_datetime,
                "stopped_time": stopped_time,
                "moving_time": moving_time,
                "total_fare": total_fare
                }

            save_trip_history(trip_data) #guardo el viaje en el archivo de txt


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
import pytube
import colorama
from colorama import Fore, Style
from tqdm import tqdm
import time
def titulo():
    titulo_= Fore.GREEN + """
         .-----------------------------------:.          
       .:-----------===------------------------:         
      .-----------*%%%%%*+=---------------------:.       
     .------------#%%%%%%%%%#*+=------------------.      
    .-------------#%++#%%%%%%%%%*------------------.     
   .--------------+=---*%%%%%%%%%*------------------.    
   :--------------------+%%%%%%%%%*-----------------:    
  .----------------------+%%%%%%%%%*-----------------.   
  :-----------------------*%%%%%%%%%*----------------:   
  :------------------------+*#%%%%%%%*----------------   
  -----------------------------%%%%%%%*---------------.  
  -----------------------------#%%%%%%%*--------------.  
  :----------------------------#%%%%%%%%*-------------.  
  :----------------------------*%%%%%*=#%*------------   
  .----------------------------*%%%%%*--=#*----------:   
   :---------------------------+%%%%%+----=----------.   
   .---------------------------=%%#%%+--------------:    
    .---------------------------%%=*%+--------------.    
     .--------------------------%%--#=-------------.     
      .-------------------------##---------------:.      
       .:-----------------------**--------------:.       
         .----------------------+=-------------.          
    """
    print(titulo_)
titulo()
def barra_de_conexion(total_iteraciones):
    barra_progreso = tqdm(total=total_iteraciones, desc="Conectando a YouTube", unit="iter")
    for _ in range(total_iteraciones):
        time.sleep(0.02)
        barra_progreso.update(1)
    barra_progreso.close()
def barra_de_carga(total_iteraciones):
    barra_progreso = tqdm(total=total_iteraciones, desc="Descargando", unit="iter")
    for _ in range(total_iteraciones):
        time.sleep(0.015)
        barra_progreso.update(1)
    barra_progreso.close()
#opciones
print(Fore.GREEN + "1. Descargar videos"),
print(Fore.GREEN + "2. Salir")

opcion= int(input(Fore.BLUE + "Ingresa una opción: "))

while True: #bucle que finaliza con la opción 2
    if opcion==1:
        url = input(Fore.BLUE + "Ingresa el url de descarga: ")
        print(f"Preparando descarga")
        barra_de_conexion(total_iteraciones=100)
        destino = "Descarga_video" #directorio donde se guardarán los videos
        app = pytube.YouTube(url)
        video = app.streams.get_highest_resolution() #Busca descargar la mayor resolución que tenga el video
        #Descarga
        video.download(destino)
        barra_de_carga(total_iteraciones=100)
        print(Fore.GREEN + "El video está descargado")
    elif opcion==2:
        print(Fore.RED + "Saliendo del programa...")
        break #finaliza el bucle.
        
        
        
        


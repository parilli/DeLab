import requests
import json
import utils
import csv
import time


while(True):                                   # Una vez empezadoel algoritmo este siempre se estrá ejecutando
    print("******Empezando consulta*****")
    organizations = utils.getOrganizations()  # primero obtenemos todas las organizaciones disponibles
    # Listar organizaciones
    #utils.listOrganizations(organizations)
    # Hacer inventario 
    print("Creando inventario...")
    utils.makeInventory(organizations,"DeLab")
    print("¡Inventario creado exitosamente!")
    print("\nLa próxima consulta se realizará a la(s): "+ str(time.strftime("%H:%M:%S",time.localtime(time.time()+5*60))))
    time.sleep(5*60) # Esta función retrasa la ejecución del programa por tantos segundos se pasen como input. En este caso 5 minutos = 5*60 seg


            

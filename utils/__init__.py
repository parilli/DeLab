import requests
import json
import csv
import os

def getOrganizations():

    # Primero hacemos la operación de getOrganizations 

    url = "https://api.meraki.com/api/v1/organizations"    # dirección para hacer el request
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }
    payload = None
    response = requests.get( url, headers=headers, data = payload)
    response.raise_for_status() # para verificar que el request se hizo bien
    
    # Luego pasamos la repuesta del request a json, para poder manejarla más fácil
    organizationsInfo = json.loads(response.text)  # este objeto es de tipo lista


    return organizationsInfo

def listOrganizations(organizationsInfo):

    n = len(organizationsInfo)                     # el largo de esta lista es igual al número de organizaciones (en este caso 29)
    print("Lista de organizaciones:")

    # tenemos una lista que tiene por elementos objetos de tipo diccionario, cada diccionario contiene información
    # específica de cada una de las organizaciones como el nombre, id, etc.
    # Así que necesitamos acceder a cada uno de estos diccionarios uno a uno
    
    for i in range (n):
        organizationName = organizationsInfo[i]['name']  # en el elemento i de la lista, accedemos a la categoría de 'name'
        print(str(i)+"."+str(organizationName))



def getOrganizationId(organizationsInfo,organizationName):
    organizationId = None
    for i in range (len(organizationsInfo)):
        if (organizationsInfo[i]['name']==organizationName):
            organizationId = organizationsInfo[i]['id']
            
    if (organizationId == None):
        raise NameError("Introduzca un nombre de organización válido")
        
    else:
        return organizationId
    
def getDevices(organizationId): # esta funcion tiene como input el id correspondiente a la oganización de la cual se quieren obtener los equipos
    
    url = "https://api.meraki.com/api/v1/organizations/"+str(organizationId)+"/devices" # direccion en donde estan los devices 

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }

    response = requests.request('GET', url, headers=headers, data = payload)  # se hace el request al url especificado
    devicesInfo = response.json()       # respuesta en formato json (lista)
    
    return devicesInfo   # se regresa la lista con todos los equipos de dicha organizacion

def makeInventory(organizationInfo,organizationName):
    os.chdir(str(os.getcwd())+'/inventario')
    with open('devices_file.csv', mode='w') as devices_file:
        device_writer = csv.writer(devices_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        device_writer.writerow(['Modelo del equipo', 'Nombre', 'dirección MAC','dirección IP','Número serial','Status'])
        id = getOrganizationId(organizationInfo,organizationName)
        devices = getDevices(int(id))
        for j in range(len(devices)):
            # print(str(j)+"."+str(devices[j]['name']))
            if(devices[j]['productType']== "wireless" or devices[j]['productType']== "appliance"):
                device_writer.writerow([devices[j]['model'], devices[j]['name'], devices[j]['mac'], devices[j]['lanIp'],devices[j]['serial'],devices[j]['configurationUpdatedAt']])

   

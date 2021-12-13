import requests
import json



def listOrganizations():

    # Primero hacemos la operación de getOrganizations 

    url = "https://api.meraki.com/api/v1/organizations"    # dirección para hacer el request
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    }
    payload = None
    response = requests.get( url, headers=headers, data = payload)

    # Luego pasamos la repuesta del request a json, para poder manejarla más fácil
    response.raise_for_status()
    organizationsInfo = json.loads(response.text)  # este objeto es de tipo lista
    n = len(organizationsInfo)                     # el largo de esta lista es igual al número de organizaciones (en este caso 29)
    print("Lista de organizaciones:")

    # tenemos una lista que tiene por elementos objetos de tipo diccionario, cada diccionario contiene información
    # específica de cada una de las organizaciones como el nombre, id, etc.
    # Así que necesitamos acceder a cada uno de estos diccionarios uno a uno
    
    for i in range (n):
        organizationName = organizationsInfo[i]['name']  # en el elemento i de la lista, accedemos a la categoría de 'name'
        print(str(i)+"."+str(organizationName))

   
    


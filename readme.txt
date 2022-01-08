****************** Automatización de procesos en DeLab ******************

En este repositorio se desarrollaron ciertas funciones para automatizar algunos procesos dentro de la compañia,
y de esta manera mejorar la experiencia de nuestros empleados.

Pasos a seguir:


1. Deberá clonar el repositorio localmente, para poder disponer de las nuevas funciones.
2. Una vez clonado el repositorio en su máquina local, para poder acceder a las funciones deberá importar el directorio utils
Con el comando "import utils", podrá usar las funciones definidas en el archivo __init__.py. (como se muestra en el archivo example.py)
3. Cada vez que se use una de estas funciones deberá colocarse el prefijo utils. Ejm: "utils.listOrganizations"

Las funciones implementadas hasta ahora son:

    1. getOrganizations()------>  hace un request al servidor de meraki, usando la API key correspondiente. 
        inputs: void
        outputs:  [organizationsInfo]->informacion de todas las organizaciones en formato json

    2. listOrganizations(organizationsInfo)------>  sirve para listar todas las organizaciones que se tiene acceso. Toma como entrada la respuesta de la primera función.
        inputs: [organizationsInfo]
        outputs: void
    
    3. getOrganizationId(organizationsInfo,organizationName) ---> nos regresa el ID de la organizacion especificada
        inputs: [organizationsInfo]; [organizationName]->nombre de la organizacion de la cual se desea conocer el ID
        outputs: [organizationId]-> ID de la organizacion
    
    4. getDevices(organizationId)------>  hace un request al servidor de meraki, usando la API key correspondiente. 
        inputs: [organizationId]
        outputs:  [devicesInfo]->informacion de todas los equipos correspondientes a la organizacion especificada en formato json

    5. makeInventory(organizationsInfo,organizationName) ---> genera el inventario de los equipos de la organizacion especificada en un archivo de formato .csv
        inputs: [organizationsInfo]: [organizationName]
        outputs: void

**************** ACTUALIZACIÓN ****************
**************** (08/01/2022) *****************

En esta nueva actualización el inventario que se genera automáticamente ahora siempre estará actualizado. El nuevo script (appDeLab.py) se ejecutará en la plataforma Docker de la compañia en producción.

Este script ya mencionado cuenta con un temporizador que nos permite realizar una consulta y generar un inventario cada 5 minutos.
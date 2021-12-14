import requests
import json
import utils
import csv

# Archivo demostrativo del procedimiento que se debe realizar para listar las organizaciones desponibles con la API key
# y además de cómo se puede hacer un inventario con las funciones implementadas recientemente.

organizations = utils.getOrganizations()  # primero obtenemos todas las organizaciones disponibles

# Listar organizaciones
utils.listOrganizations(organizations)

# Hacer inventario 
utils.makeInventory(organizations,"DeLab")


            

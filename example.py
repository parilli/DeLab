import requests
import json
import utils
import csv

# Listar organizaciones
organizations = utils.getOrganizations()
utils.listOrganizations(organizations)

# Hacer inventario 
utils.makeInventory(organizations,"DeLab")


            

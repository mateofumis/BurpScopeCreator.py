#!/usr/bin/python3

import json
import signal
import sys
import re

# Función para manejar la interrupción de Ctrl + C
def handle_interrupt(signum, frame):
    print("\n[-] Se ha presionado Ctrl + C. El proceso se ha interrumpido.")
    sys.exit(1)

# Manejar la interrupción de Ctrl + C
signal.signal(signal.SIGINT, handle_interrupt)

# Crear una estructura de datos vacía para el scope
burp_scope = {
    "target": {
        "scope": {
            "advanced_mode": True,
            "exclude": [],
            "include": [],
        }
    }
}

# Imprimir banner
print('''
 ______                    ______                        _______
(____  \                  / _____)                      (_______)                    _
 ____)  )_   _  ____ ____( (____   ____ ___  ____  _____ _        ____ _____ _____ _| |_ ___   ____
|  __  (| | | |/ ___)  _ \____ \ / ___) _ \|  _ \| ___ | |      / ___) ___ (____ (_   _) _ \ / ___)
| |__)  ) |_| | |   | |_| |____) | (__| |_| | |_| | ____| |_____| |   | ____/ ___ | | || |_| | |
|______/|____/|_|   |  __(______/ \____)___/|  __/|_____)\______)_|   |_____)_____|  \__)___/|_|
                    |_|                     |_|
by hackermater (Mateo Fumis)
      ''')

# Solicitar al usuario que ingrese el archivo de subdominios y dominios dentro del scope
subdomains_file = input("[+] Ingrese el nombre del archivo de subdominios dentro del scope: ")
domains_file = input("[+] Ingrese el nombre del archivo de dominios dentro del scope: ")

# Leer el archivo de subdominios dentro del scope
try:
    with open(subdomains_file, 'r') as subdomains:
        subdomain_list = subdomains.read().splitlines()
except:
    subdomain_list = ""

# Leer el archivo de dominios dentro del scope
try:
    with open(domains_file, 'r') as domains:
        domain_list = domains.read().splitlines()
except:
    domain_list = ""

# Solicitar al usuario que ingrese el archivo de subdominios y dominios fuera del alcance (out of scope)
subdomains_out_of_scope_file = input("[+] Ingrese el nombre del archivo de subdominios fuera del scope: ")
domains_out_of_scope_file = input("[+] Ingrese el nombre del archivo de dominios fuera del scope: ")

# Leer el archivo de subdominios fuera del scope
try:
    with open(subdomains_out_of_scope_file, 'r') as subdomains_out_of_scope:
        subdomain_out_of_scope_list = subdomains_out_of_scope.read().splitlines()
except:
    subdomain_out_of_scope_list = ""

# Leer el archivo de dominios fuera del scope
try:
    with open(domains_out_of_scope_file, 'r') as domains_out_of_scope:
        domain_out_of_scope_list = domains_out_of_scope.read().splitlines()
except:
    domain_out_of_scope_list = ""

# Función para crear el scope en el formato de BurpSuite
def create_scope_object(host, port, protocol, is_subdomain=False):
    if is_subdomain:
        host_pattern = f"^.*\." + re.escape(host).replace(r'\-', '-') + "$"
    else:
        host_pattern = f"^" + re.escape(host).replace(r'\-', '-') + "$"

    return {
        "enabled": True,
        "file": "^/.*",
        "host": host_pattern,
        "port": f"^{port}$",
        "protocol": protocol
    }

for domain in domain_list:
    burp_scope["target"]["scope"]["include"].append(create_scope_object(domain, "80", "http", False))
    burp_scope["target"]["scope"]["include"].append(create_scope_object(domain, "443", "https", False))

for subdomain in subdomain_list:
    burp_scope["target"]["scope"]["include"].append(create_scope_object(subdomain, "80", "http", True))
    burp_scope["target"]["scope"]["include"].append(create_scope_object(subdomain, "443", "https", True))

# Función para crear el out-of-scope en el formato de BurpSuite
def create_out_of_scope_object(host, port, protocol, is_subdomain=False):
    if is_subdomain:
        host_pattern = f"^.*\." + re.escape(host).replace(r'\-', '-') + "$"
    else:
        host_pattern = f"^" + re.escape(host).replace(r'\-', '-') + "$"

    return {
        "enabled": True,
        "file": "^/.*",
        "host": host_pattern,
        "port": f"^{port}$",
        "protocol": protocol
    }

for domain in domain_out_of_scope_list:
    burp_scope["target"]["scope"]["exclude"].append(create_out_of_scope_object(domain, "80", "http", False))
    burp_scope["target"]["scope"]["exclude"].append(create_out_of_scope_object(domain, "443", "https", False))

for subdomain in subdomain_out_of_scope_list:
    burp_scope["target"]["scope"]["exclude"].append(create_out_of_scope_object(subdomain, "80", "http", True))
    burp_scope["target"]["scope"]["exclude"].append(create_out_of_scope_object(subdomain, "443", "https", True))

# Nombre del archivo JSON de salida
output_file = input("[+] Ingrese el nombre del archivo JSON de salida: ")

# Guardar el scope en un archivo JSON
with open(output_file, 'w') as json_file:
    json.dump(burp_scope, json_file, indent=4)

print(f"El archivo '{output_file}' se ha creado con el formato para Burp Suite.")

# Imprimir mensaje de despedida
print("Happy Hacking!!")

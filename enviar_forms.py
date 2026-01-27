import json
import requests
import time
from datetime import datetime

FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScj5ojYNzPVZ2NX0Cq2vp5A4AEciLG_ijfG4O_IY165fMaVRQ/formResponse"

FORM_IDS = {
    "quien_reporta": "677790829",
    "correo": "1000518918",
    "prioridad": "1918714904",
    "novedad": "83265125",
    "negocio": "158791591",
    "tipo": "1743756408",
    "area": "2041407819",
    "equipo": "990038080"
}

# Cargar archivos
with open("tiendas.json") as f:
    TIENDAS = json.load(f)

with open("servicios.json") as f:
    SERVICIOS = json.load(f)

with open("estado.txt") as f:
    indice = int(f.read().strip())

# Seleccionar 2 tiendas por día
bloque = TIENDAS[indice:indice + 2]

print("📤 Envío iniciado:", datetime.now())

for tienda in bloque:
    for servicio in SERVICIOS:
        data = {
            f"entry.{FORM_IDS['quien_reporta']}": tienda["correo"],
            f"entry.{FORM_IDS['correo']}": tienda["correo"],
            f"entry.{FORM_IDS['negocio']}": tienda["tienda"],
            f"entry.{FORM_IDS['novedad']}": servicio["descripcion"],
            f"entry.{FORM_IDS['area']}": servicio["area"],
            f"entry.{FORM_IDS['equipo']}": servicio["equipo"],
            f"entry.{FORM_IDS['prioridad']}": servicio["prioridad"],
            f"entry.{FORM_IDS['tipo']}": servicio["tipo"]
        }

        r = requests.post(FORM_URL, data=data)
        print(f"✅ {tienda['tienda']} | {servicio['descripcion']} | {r.status_code}")
        time.sleep(20)

# Actualizar estado
nuevo_indice = indice + 2 if indice + 2 < len(TIENDAS) else 0
with open("estado.txt", "w") as f:
    f.write(str(nuevo_indice))

print("✅ Proceso finalizado")

import json
import requests
import time
from datetime import datetime

# ===============================
# URL DEL FORMULARIO
# ===============================
FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScj5ojYNzPVZ2NX0Cq2vp5A4AEciLG_ijfG4O_IY165fMaVRQ/formResponse"

# ===============================
# IDS DEL FORMULARIO (FIJOS)
# ===============================
FORM_IDS = {
    "quien_reporta": "677790829",
    "correo": "1000518918",
    "negocio": "158791591",
    "novedad": "83265125",
    "area": "2041407819",
    "equipo": "990038080",
    "prioridad": "1918714904",
    "tipo": "1743756408"
}

# ===============================
# CARGAR CONFIGURACIÓN
# ===============================
with open("tiendas.json", "r", encoding="utf-8") as f:
    TIENDAS = json.load(f)

with open("servicios.json", "r", encoding="utf-8") as f:
    SERVICIOS = json.load(f)

with open("estado.txt", "r") as f:
    indice = int(f.read().strip())

# ===============================
# SELECCIONAR 2 TIENDAS
# ===============================
tiendas_hoy = TIENDAS[indice:indice + 2]

print("📤 Iniciando envío:", datetime.now())

# ===============================
# ENVÍO DE FORMULARIOS
# ===============================
for tienda in tiendas_hoy:
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
        print(f"✅ Tienda {tienda['tienda']} | {servicio['descripcion']} | {r.status_code}")
        time.sleep(20)

# ===============================
# ACTUALIZAR ESTADO
# ===============================
nuevo_indice = indice + 2 if indice + 2 < len(TIENDAS) else 0
with open("estado.txt", "w") as f:
    f.write(str(nuevo_indice))

print("✅ Proceso finalizado")

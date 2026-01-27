import requests
import time

URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScj5ojYNzPVZ2NX0Cq2vp5A4AEciLG_ijfG4O_IY165fMaVRQ/formResponse"

# ====== TIENDAS ======
tiendas = [
    ("asto254@olimpica.com.co", "1254"),
]

# ====== ACTIVIDADES ======
# Cada actividad contiene TODO lo necesario para el formulario
actividades = [
    {
        "descripcion": "Ahorro energetico: ajustes nevera de lacteos",
        "tipo_servicio": "Refrigeración",
        "area": "LACTEOS",
        "equipo": "RACK",
        "prioridad": "3",
    }
]

# ====== IDS DEL FORMULARIO ======
FIELDS = {
    "quien_reporta": "entry.677790829",
    "correo": "entry.1000518918",
    "negocio": "entry.158791591",
    "novedad": "entry.83265125",
    "tipo_servicio": "entry.1743756408",
    "area": "entry.2041407819",
    "equipo": "entry.990038080",
    "prioridad": "entry.1918714904",
}

# ====== CONTROL DE ESTADO ======
with open("estado.txt", "r") as f:
    inicio = int(f.read().strip())

fin = inicio + 1

for correo, tienda in tiendas[inicio:fin]:
    for act in actividades:
        data = {
            FIELDS["quien_reporta"]: correo,
            FIELDS["correo"]: correo,
            FIELDS["negocio"]: tienda,
            FIELDS["novedad"]: act["descripcion"],
            FIELDS["tipo_servicio"]: act["tipo_servicio"],
            FIELDS["area"]: act["area"],
            FIELDS["equipo"]: act["equipo"],
            FIELDS["prioridad"]: act["prioridad"],
        }

        r = requests.post(URL, data=data)
        print(f"Enviado → Tienda {tienda} | {act['descripcion']} | HTTP {r.status_code}")
        time.sleep(20)

nuevo_inicio = fin if fin < len(tiendas) else 0

with open("estado.txt", "w") as f:
    f.write(str(nuevo_inicio))

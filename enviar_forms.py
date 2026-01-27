import requests
from datetime import datetime

FORM_URL = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScj5ojYNzPVZ2NX0Cq2vp5A4AEciLG_ijfG4O_IY165fMaVRQ/formResponse"

FORM_IDS = {
    "quien_reporta": "677790829",
    "correo": "1000518918",
    "prioridad": "1918714904",
    "novedad": "83265125",
    "negocio": "158791591",
    "tipo_solicitud": "1743756408",
    "area": "2041407819",
    "equipo": "990038080"
}

SERVICIOS = [
    {
        "tienda": "1254",
        "correo": "asto254@olimpica.com.co",
        "descripcion": "Ahorro energetico: ajustes nevera de lacteos",
        "area": "LACTEOS",
        "equipo": "RACK",
        "tipo": "Refrigeración"
    },
    {
        "tienda": "1254",
        "correo": "asto254@olimpica.com.co",
        "descripcion": "Ahorro energetico: ajustes nevera de fruver",
        "area": "FRUVER",
        "equipo": "RACK",
        "tipo": "Refrigeración"
    },
    {
        "tienda": "1254",
        "correo": "asto254@olimpica.com.co",
        "descripcion": "Ahorro energetico: ajustes nevera de carnes",
        "area": "PROCESO DE CARNES",
        "equipo": "RACK",
        "tipo": "Refrigeración"
    }
]

def enviar_reporte(servicio):
    data = {
        f"entry.{FORM_IDS['quien_reporta']}": servicio["correo"],
        f"entry.{FORM_IDS['correo']}": servicio["correo"],
        f"entry.{FORM_IDS['prioridad']}": "3",
        f"entry.{FORM_IDS['novedad']}": servicio["descripcion"],
        f"entry.{FORM_IDS['negocio']}": servicio["tienda"],
        f"entry.{FORM_IDS['tipo_solicitud']}": servicio["tipo"],
        f"entry.{FORM_IDS['area']}": servicio["area"],
        f"entry.{FORM_IDS['equipo']}": servicio["equipo"],
    }

    r = requests.post(FORM_URL, data=data)
    print(f"HTTP {r.status_code} → {servicio['descripcion']}")

if __name__ == "__main__":
    print("📤 Iniciando envío de formularios...")
    for servicio in SERVICIOS:
        enviar_reporte(servicio)
    print("✅ Proceso finalizado:", datetime.now())

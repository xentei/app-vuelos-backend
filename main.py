# app-vuelos-backendfrom fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
from datetime import datetime

app = FastAPI()

@app.get("/vuelos")
def obtener_vuelos():
    url = "http://www.tams.com.ar/organismos/vuelos.aspx"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.content, "html.parser")
        # Aquí debes ajustar la extracción según la estructura HTML específica del sitio.
        # Este es un ejemplo simple.
        vuelos = []
        tabla_vuelos = soup.find_all("tr")  # Esto podría cambiar dependiendo del HTML
        for fila in tabla_vuelos:
            columnas = fila.find_all("td")
            if columnas:
                vuelo = {
                    "codigo": columnas[0].text.strip(),
                    "destino": columnas[1].text.strip(),
                    "estado": columnas[2].text.strip(),
                    "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Solo como ejemplo
                }
                vuelos.append(vuelo)
        return {"vuelos": vuelos}
    else:
        return {"error": "No se pudo acceder a la información"}


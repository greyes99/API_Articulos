from fastapi import FastAPI

import json
import urllib.request

import ssl

app = FastAPI()

apikey = "87dd2fd2967a8e8228edcf5a585512fc"
ssl._create_default_https_context = ssl._create_unverified_context    

@app.get("/listado_pais/{country}")
def obtenerArticulos(country: str = "us"):
    url = f"https://gnews.io/api/v4/search?q=example&lang=en&country={country}&max=10&apikey={apikey}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if data["totalArticles"] == 0:
                return { "message": "No se encontraron artículos" }
            else:
                return data
    except Exception as e:
        return {"error": "Ocurrió un error al obtener las noticias.", "details": str(e)}
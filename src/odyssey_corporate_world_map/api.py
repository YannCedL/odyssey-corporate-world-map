# API FastAPI pour le moteur Odyssey Corporate World Map
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .mapper import map_corporate_sites

app = FastAPI(
    title="Odyssey Corporate World Map API",
    description="Moteur de Cartographie Mondiale des Implantations d'Entreprises",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil avec carte mondiale
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Odyssey API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Odyssey", "version": "1.0.0"}

@app.get("/api/v1/map", response_model=ResultContract)
def get_map(siren: str = Query("383474814")):
    return map_corporate_sites(siren)

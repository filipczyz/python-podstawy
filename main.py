from fastapi import FastAPI
import requests
import shutil
from mózg_ai import policz_ludzi_na_zdjeciu

app = FastAPI()


@app.get("/analizuj-z-linku")
def analiza_zdjecia(link: str):
    nazwa_pliku = "pobrane_z_neta.jpg"
    try:
        odpowiedz = requests.get(link, stream=True)
        with open(nazwa_pliku, 'wb') as plik:
            shutil.copyfileobj(odpowiedz.raw, plik)
    except Exception:
        return {"Blad": "Nie udalo sie pobrac zdjecia. Sprawdz link."}


    liczba = policz_ludzi_na_zdjeciu(nazwa_pliku)
    return {
        "Status": "Zrobione",
        "Ile_osob": liczba,
        "Info": "Otwórz plik wynik.jpg w projekcie, żeby zobaczyć ramki."
    }




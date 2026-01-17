import cv2
from ultralytics import YOLO
model = YOLO('yolov8n.pt')


def policz_ludzi_na_zdjeciu(sciezka_pliku):
    wyniki = model(sciezka_pliku)

    ile_osob = 0
    for wynik in wyniki:
        for box in wynik.boxes:
            if int(box.cls) == 0:
                ile_osob += 1

        wynik.save(filename="wynik.jpg")
    return ile_osob

if __name__ == "__main__":
    try:
        liczba = policz_ludzi_na_zdjeciu("man.jpg")
        print(f"\n--- SUKCES! ---")
        print(f"Wykryto osób: {liczba}")
        print(f"Zapisano plik: wynik.jpg")
    except Exception as e:
        print(f"Błąd: {e}")
        print("Sprawdź, czy plik 'test.jpg' na pewno jest w folderze projektu!")
import os

def berechne_platzbedarf(wurzel):
    platz = 0
    anzahl = 0
    for v, uv, d in os.walk(wurzel):
        anzahl += 1
        for datei in d:
            pfad = os.path.join(v,datei)
            platz += os.path.getsize(pfad)
    return anzahl, platz

# os.walk(wurzel) liefert nicht alle Dateien auf einmal,
# sondern iteriert rekursiv durch alle Verzeichnisse
# – inklusive Unterverzeichnissen – und gibt für jedes
# einzelne Verzeichnis ein eigenes Tupel zurück : (v, uv, d)
#
# Beispiel Baum:
# /projekt
#   ├── readme.txt
#   ├── daten
#   │   ├── a.txt
#   │   └── b.txt
#   └── src
#       └── main.py
#
# os.walk('/projekt') liefert nacheinander:
#
# ('/projekt', ['daten', 'src'], ['readme.txt'])
#
# ('/projekt/daten', [], ['a.txt', 'b.txt'])
#
# ('/projekt/src', [], ['main.py'])
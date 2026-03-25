import chardet

def detect_encoding(filepath):
    """Versucht das Encoding einer Datei zu erkennen."""
    with open(filepath, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
    return result['encoding'], result['confidence']


def read_text_file(filepath, expected_encoding='utf-8'):
    """Liest eine Textdatei im gegebenen Encoding."""
    try:
        with open(filepath, encoding=expected_encoding) as f:
            content = f.read()
        print(f"\nDatei erfolgreich gelesen mit Encoding '{expected_encoding}'.\n")
        print("🔹 Inhalt:\n", content)
    except UnicodeDecodeError as e:
        print(f"\nUnicodeDecodeError: {e}")
        print("Möglicherweise ist das Encoding falsch.")
        print("Tipp: Verwende detect_encoding(), um Encoding zu prüfen.")


def hex_debug(text):
    """Zeigt Text als Hexbytes zur Analyse von fehlerhaften Zeichen."""
    print("\n🔍 Hex-Darstellung des Textes:")
    print(' '.join(f"{ord(c):04x}" for c in text))


# ==== Beispielverwendung ====

if __name__ == "__main__":
    filepath = "output.txt"  # Beispiel-Datei

    print(f"Überprüfe Datei: {filepath}")

    encoding, confidence = detect_encoding(filepath)
    print(f"Erkanntes Encoding: {encoding} (Konfidenz: {confidence:.2f})")

    read_text_file(filepath, expected_encoding=encoding)

    # Optional: Hex-Analyse eines bekannten Textes
    known_text = "Hello, 世界! 🌍🚀 — Привет мир! — مرحبا بالعالم! — שלום עולם! — हैलो वर्ल्ड!"
    hex_debug(known_text)

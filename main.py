# main.py
from scripts.descargar import descargar_desde_csv

if __name__ == "__main__":
    print("=" * 60)
    print("🎶 DESCARGADOR AUTOMÁTICO DE CANTOS DE AVES")
    print("=" * 60)
    
    descargar_desde_csv("urls.csv")

    print("=" * 60)
    print("✅ Descargas completadas correctamente")
    print("=" * 60)

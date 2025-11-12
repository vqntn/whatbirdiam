# scripts/descargar.py
import os
import yt_dlp
import pandas as pd

# Carpeta donde se guardarán los audios
CARPETA_AUDIOS = "audios"
os.makedirs(CARPETA_AUDIOS, exist_ok=True)

# Ruta a FFmpeg (asegúrate de que esté en la raíz del proyecto)
FFMPEG_PATH = os.path.join(os.getcwd(), "ffmpeg.exe")

def descargar_audio(url, nombre_archivo, especie):
    """Descarga el audio de YouTube y lo guarda en formato WAV"""
    carpeta_destino = os.path.join(CARPETA_AUDIOS, especie)
    os.makedirs(carpeta_destino, exist_ok=True)

    outtmpl = os.path.join(carpeta_destino, f"{nombre_archivo}.%(ext)s")

    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'ffmpeg_location': FFMPEG_PATH,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
        'postprocessor_args': ['-ar', '44100', '-ac', '1'],
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        print(f"✅ Descargado: {nombre_archivo}.wav ({especie})")
    except Exception as e:
        print(f"❌ Error con {url}: {e}")

def descargar_desde_csv(csv_path="urls.csv"):
    """Lee un archivo CSV con columnas: url;nombre;especie"""
    if not os.path.exists(csv_path):
        print(f"❌ No se encontró el archivo '{csv_path}'. Asegúrate de que esté en la carpeta del proyecto.")
        return

    # Leer usando punto y coma como separador
    data = pd.read_csv(csv_path, sep=';')

    for _, row in data.iterrows():
        descargar_audio(row["url"], row["nombre"], row["especie"])

if __name__ == "__main__":
    descargar_desde_csv("urls.csv")


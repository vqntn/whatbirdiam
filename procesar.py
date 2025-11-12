# scripts/procesar.py
import os
import librosa
import soundfile as sf
from tqdm import tqdm

CARPETA_AUDIOS = "audios"
CARPETA_PROCESADOS = "procesados"
os.makedirs(CARPETA_PROCESADOS, exist_ok=True)

def procesar_audio(path_entrada, path_salida):
    y, sr = librosa.load(path_entrada, sr=44100, mono=True)
    y, _ = librosa.effects.trim(y, top_db=20)  # Quita silencios
    sf.write(path_salida, y, sr)

def procesar_todos():
    for especie in os.listdir(CARPETA_AUDIOS):
        carpeta_in = os.path.join(CARPETA_AUDIOS, especie)
        carpeta_out = os.path.join(CARPETA_PROCESADOS, especie)
        os.makedirs(carpeta_out, exist_ok=True)

        for archivo in tqdm(os.listdir(carpeta_in), desc=f"Procesando {especie}"):
            if archivo.endswith(".wav"):
                in_path = os.path.join(carpeta_in, archivo)
                out_path = os.path.join(carpeta_out, archivo)
                procesar_audio(in_path, out_path)

if __name__ == "__main__":
    procesar_todos()


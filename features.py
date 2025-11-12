# scripts/features.py
import os
import numpy as np
import librosa
import pandas as pd
from tqdm import tqdm

CARPETA_PROCESADOS = "procesados"
CARPETA_FEATURES = "features"
os.makedirs(CARPETA_FEATURES, exist_ok=True)

def extraer_features(path_audio):
    y, sr = librosa.load(path_audio, sr=44100)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

def generar_dataset():
    data, labels = [], []
    for especie in os.listdir(CARPETA_PROCESADOS):
        carpeta = os.path.join(CARPETA_PROCESADOS, especie)
        for archivo in tqdm(os.listdir(carpeta), desc=f"Extrayendo {especie}"):
            if archivo.endswith(".wav"):
                path = os.path.join(carpeta, archivo)
                feat = extraer_features(path)
                data.append(feat)
                labels.append(especie)

    df = pd.DataFrame(data)
    df["label"] = labels
    df.to_csv(os.path.join(CARPETA_FEATURES, "dataset.csv"), index=False)
    print("✅ Dataset generado en /features/dataset.csv")

if __name__ == "__main__":
    generar_dataset()


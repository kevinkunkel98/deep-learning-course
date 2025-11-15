# Deep Learning Course - Hausaufgabe W1

## Setup

### Automatische Installation

Führe das Setup-Skript aus:
```bash
chmod +x setup.sh
./setup.sh
```

### Manuelle Installation

Falls das automatische Setup nicht funktioniert:

1. **Virtual Environment erstellen:**
   ```bash
   python3 -m venv venv
   ```

2. **Virtual Environment aktivieren:**
   ```bash
   source venv/bin/activate
   ```

3. **Pakete installieren:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Verwendung

### Virtual Environment aktivieren
```bash
source venv/bin/activate
```

### JupyterLab starten
```bash
jupyter-lab
```

### Python-Skripte ausführen
```bash
python3 dein_skript.py
```

### Virtual Environment deaktivieren
```bash
deactivate
```

## Installierte Pakete
- matplotlib
- scikit-image
- numpy
- jupyterlab
- torch (PyTorch)
- torchvision
- torchaudio

## Ordnerstruktur
- `course/` - Kursunterlagen und Hausaufgaben
- `slides/` - Präsentationsfolien
- `venv/` - Python Virtual Environment


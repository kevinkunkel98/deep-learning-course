# Deep Learning Course

Dieses Repository enthält Materialien, Hausaufgaben und Projekte für den Deep Learning Kurs.

## 🚀 Schnellstart

### 1. Erstmalige Installation

```bash
./setup.sh
```

Dieses Skript erstellt automatisch ein virtuelles Python-Environment und installiert alle Abhängigkeiten.

### 2. Environment aktivieren

```bash
source venv/bin/activate
```

Oder verwende das Aktivierungsskript:
```bash
source activate_env.sh
```

### 3. Environment deaktivieren

```bash
deactivate
```

## 📦 Installierte Pakete

- **PyTorch**: 2.9.1
- **TorchVision**: 0.24.1
- **TorchAudio**: 2.9.1
- **NumPy**: 2.3.4
- **Matplotlib**: 3.10.7
- **Scikit-image**: 0.25.2
- **JupyterLab**: 4.4.9

## 📁 Projektstruktur

```
.
├── week 1 hw/          # Hausaufgaben Woche 1
├── week 2 hw/          # Hausaufgaben Woche 2
├── course/             # Kursmaterialien und Aufgabenstellungen
├── slides/             # Vorlesungsfolien
├── venv/               # Virtuelles Python-Environment (nicht in Git)
├── requirements.txt    # Python-Abhängigkeiten
├── setup.sh           # Installations-Skript
└── activate_env.sh    # Aktivierungs-Skript
```

## 💻 Verwendung

### FMNIST Training ausführen

```bash
source venv/bin/activate
python "FMNIST PyTorch LogReg Class.py"
```

### JupyterLab starten

```bash
source venv/bin/activate
jupyter-lab
```

## 💡 Tipps

- Das `venv/` Verzeichnis ist in `.gitignore` eingetragen und wird nicht versioniert
- Bei jedem neuen Terminal-Fenster muss das Environment neu aktiviert werden
- Alle Python-Skripte sollten im aktivierten Environment ausgeführt werden
- numpy
- jupyterlab
- torch (PyTorch)
- torchvision
- torchaudio

## Ordnerstruktur
- `course/` - Kursunterlagen und Hausaufgaben
- `slides/` - Präsentationsfolien
- `venv/` - Python Virtual Environment


# Cross-Camera Player Mapping

This project detects and maps football players across two camera views using YOLOv8 and the Hungarian algorithm.

## 🔧 Setup

Run on **Google Colab** or locally (Python 3.11+).

### 📦 Dependencies

- ultralytics
- opencv-python-headless
- numpy
- scipy

Install via pip:
```bash
pip install ultralytics opencv-python-headless numpy scipy
```

## ▶️ How to Run

1. Upload `broadcast.mp4` and `tacticam.mp4` in Colab.
2. Run all notebook cells.
3. Output saved as `player_id_mapping.json`.

## 📂 Files

- `notebook.ipynb` — Colab notebook
- `player_id_mapping.json` — output
- `broadcast.mp4`, `tacticam.mp4` — input clips

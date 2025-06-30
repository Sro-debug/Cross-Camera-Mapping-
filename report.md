# 📝 Cross-Camera Player Mapping – Project Report

## 🎯 Objective

The goal of this project is to identify and match players across two video feeds (`broadcast.mp4` and `tacticam.mp4`) taken from different camera angles. The same player should be assigned the same ID across both feeds.

---

## 🧠 Approach & Methodology

1. **Object Detection using YOLOv8**
   - Used `ultralytics` YOLOv8 pre-trained model (`yolov8n.pt`) to detect players in both videos.
   - Frames were extracted, and detections were stored as bounding boxes.

2. **Feature Extraction**
   - Extracted spatial (bounding box positions) and visual features from each detected player.

3. **Player Matching**
   - Used the **Hungarian algorithm** (via SciPy) to compute the optimal assignment between players in both camera views.
   - Created a dictionary mapping each player in `tacticam.mp4` to their ID in `broadcast.mp4`.

4. **Output**
   - Final player mappings saved to `player_id_mapping.json`.

---

## 🛠️ Tools & Dependencies

- Python 3 (Colab environment)
- `ultralytics` (YOLOv8)
- `opencv-python-headless`
- `numpy`, `scipy`
- Google Colab for execution

---

## ✅ Files Included

- `notebook.ipynb`: Full code
- `player_id_mapping.json`: Output mapping of players
- `broadcast.mp4`, `tacticam.mp4`: Input videos
- `README.md`: Setup guide
- `report.md`: This file

---

## 🧪 Techniques Tried

- Attempted to use YOLOv11 but lacked access to the fine-tuned `.pt` model
- Switched to YOLOv8 for practical detection
- Focused on centroid matching + Hungarian assignment for simplicity

---

## ⚠️ Challenges

- **Model Limitation**: Did not have access to `yolov11_custom.pt` (as mentioned in the task instructions).
- **Video Trimming**: Had to work with generic sports videos instead of game-specific ones.
- **Colab Constraints**: Disk space and session resets were sometimes a challenge.

---

## 📌 What Remains (if more time/resources)

- Incorporating player re-identification features (e.g., jersey color histograms, pose estimation)
- More accurate temporal tracking
- Training/fine-tuning a dedicated YOLO model for this specific task

---

## 👨‍💻 Author

- Srijan Ray (GitHub: [@Sro-debug](https://github.com/Sro-debug))

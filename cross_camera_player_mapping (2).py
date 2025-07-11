# -*- coding: utf-8 -*-
"""Cross_Camera_Player_Mapping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nE7cGbjQL-Gm1aD_ZMv-tSlZ7zbSqUEo

# 🎯 Cross-Camera Player Mapping
This notebook detects and matches players across two camera views using YOLOv11 and the Hungarian algorithm.
"""

from google.colab import files

# Upload your model and videos
uploaded = files.upload()

# Commented out IPython magic to ensure Python compatibility.
# ✅ Install required libraries (run this once)
# %pip install ultralytics opencv-python-headless scipy numpy

from ultralytics import YOLO

# Load the fine-tuned YOLOv11 model (adjust filename if needed)
model = YOLO('yolov8n.pt')

import cv2

def detect_players(video_path, model):
    cap = cv2.VideoCapture(video_path)
    detections = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        detections.append(results[0])
    cap.release()
    return detections

def extract_features(detections):
    features = []
    for det in detections:
        frame_features = []
        if det.boxes is not None:
            for box in det.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                center = ((x1 + x2) / 2, (y1 + y2) / 2)
                frame_features.append({'bbox': (x1, y1, x2, y2), 'center': center})
        features.append(frame_features)
    return features

import numpy as np

def average_frame_features(features):
    avg_positions = {}
    counts = {}
    for frame in features:
        for i, player in enumerate(frame):
            if i not in avg_positions:
                avg_positions[i] = np.array(player['center'])
                counts[i] = 1
            else:
                avg_positions[i] += np.array(player['center'])
                counts[i] += 1
    for i in avg_positions:
        avg_positions[i] /= counts[i]
    return avg_positions

from scipy.optimize import linear_sum_assignment

def match_players(broadcast_avg, tacticam_avg):
    b_ids = list(broadcast_avg.keys())
    t_ids = list(tacticam_avg.keys())
    cost_matrix = np.zeros((len(b_ids), len(t_ids)))
    for i, b in enumerate(b_ids):
        for j, t in enumerate(t_ids):
            cost_matrix[i, j] = np.linalg.norm(broadcast_avg[b] - tacticam_avg[t])
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return {t_ids[col]: b_ids[row] for row, col in zip(row_ind, col_ind)}

# 🔁 Run the full pipeline
broadcast_detections = detect_players('broadcast.mp4', model)
tacticam_detections = detect_players('tacticam.mp4', model)

broadcast_features = extract_features(broadcast_detections)
tacticam_features = extract_features(tacticam_detections)

broadcast_avg = average_frame_features(broadcast_features)
tacticam_avg = average_frame_features(tacticam_features)

player_mapping = match_players(broadcast_avg, tacticam_avg)
print("✅ Player Mapping:", player_mapping)

import json

with open('player_id_mapping.json', 'w') as f:
    json.dump(player_mapping, f, indent=4)

print("📝 Saved player mapping to 'player_id_mapping.json'")
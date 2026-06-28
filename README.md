# 🎭 Audience Reaction Sync

An AI-powered real-time audience analytics system that detects people, tracks facial landmarks, estimates attention, predicts engagement, and provides live analytics through a FastAPI backend and React dashboard.

---

## 📌 Overview

Audience Reaction Sync is designed to analyze audience behavior in real time using computer vision and machine learning. The system detects multiple people, tracks facial features, estimates attention levels, predicts engagement scores, logs session data, and visualizes analytics through an interactive dashboard.

---

## ✨ Features

* 👥 Multi-person detection and tracking
* 😊 Face Mesh landmark detection
* 👁️ Eye Aspect Ratio (EAR) calculation
* 👄 Mouth Aspect Ratio (MAR) calculation
* 👀 Blink detection
* 🧭 Head pose estimation (Yaw, Pitch, Roll)
* 🎯 Real-time attention scoring
* 🤖 Machine Learning based engagement prediction
* 📊 React dashboard with live analytics
* ⚡ FastAPI REST API
* 📈 Engagement and attention timeline charts
* 📝 CSV session logging
* 📄 Automatic PDF report generation

---

## 🏗️ System Architecture

```text
Webcam
   │
   ▼
YOLO Person Detection
   │
   ▼
MediaPipe Face Mesh
   │
   ▼
Feature Extraction
(EAR, MAR, Blink, Head Pose)
   │
   ▼
Attention Engine
   │
   ▼
Engagement Prediction Model
   │
   ▼
CSV Logger
   │
   ├── FastAPI REST API
   │
   └── React Dashboard
```

---

## 🛠️ Tech Stack

### Programming Languages

* Python
* JavaScript

### Backend

* FastAPI
* Uvicorn

### Frontend

* React
* Vite
* Axios
* Chart.js

### Computer Vision

* OpenCV
* MediaPipe
* YOLO

### Machine Learning

* PyTorch
* NumPy
* Pandas

### Visualization

* Chart.js
* React Chart.js

### Reporting

* ReportLab

---

## 📂 Project Structure

```text
audience-reaction-sync/

├── api/
├── frontend/
├── models/
├── modules/
├── outputs/
│   ├── logs/
│   ├── reports/
│   ├── graphs/
│   └── videos/
├── scripts/
├── tests/
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/trivikram-06/audience-reaction-sync.git
```

Go to the project

```bash
cd audience-reaction-sync
```

Create a virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the AI Application

```bash
python app.py
```

---

## ▶️ Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run React Dashboard

```bash
cd frontend
npm install
npm run dev
```

Open

```text
http://localhost:5173
```

---

## 📊 REST API

| Endpoint     | Description              |
| ------------ | ------------------------ |
| `/`          | Project information      |
| `/health`    | Health check             |
| `/analytics` | Session analytics        |
| `/latest`    | Latest audience status   |
| `/history`   | Complete session history |

---

## 📄 Reports

The system automatically generates:

* CSV session logs
* PDF audience reports
* Analytics dashboard
* Engagement timeline
* Attention timeline

---

## 🎯 Applications

* Smart classrooms
* Online learning analytics
* Conferences
* Corporate meetings
* Audience engagement monitoring
* Presentation analysis
* Research studies

---

## 🔮 Future Enhancements

* Live webcam streaming in dashboard
* Emotion recognition
* Speaker engagement analysis
* Cloud deployment
* Database integration
* Mobile dashboard
* Real-time notifications

---

## 👨‍💻 Author

**Trivikram Anbanandan**

VIT Chennai

---

## 📜 License

This project is licensed under the MIT License.

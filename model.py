import cv2
import numpy as np
import joblib
from ultralytics import YOLO

# Load your trained temperature prediction model
temp_model = joblib.load("animal_temp_model.pkl")

# Load YOLOv8 model (uses pretrained YOLOv8n for speed)
yolo_model = YOLO("yolov8n.pt")

# Supported labels and their encoded values (used during model training)
supported_animals = {
    "dog": 0,
    "cat": 1,
    "horse": 2,
    "cow": 3,
    "sheep": 5,
    "person": 6  # Human
}

# Default vitals per entity (HeartRate, RespRate, AmbientTemp)
default_vitals = {
    "dog": [90, 20, 25],
    "cat": [110, 25, 25],
    "horse": [45, 12, 25],
    "cow": [60, 30, 25],
    "sheep": [75, 20, 25],
    "person": [72, 16, 25]  # Human vitals
}

print("📸 Starting webcam for detection and temperature prediction...")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = yolo_model.predict(source=frame, imgsz=640, conf=0.5, verbose=False)[0]
    detected_entities = set()

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        label = yolo_model.model.names[int(class_id)].lower()

        if label in supported_animals:
            detected_entities.add(label)

            # Draw bounding box and label
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label.upper(), (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Predict temp for first detected entity
    if detected_entities:
        entity = list(detected_entities)[0]
        print(f"🧠 Detected: {entity}")

        vitals = default_vitals[entity]
        features = np.array([[supported_animals[entity]] + vitals])
        predicted_temp_c = temp_model.predict(features)[0]
        predicted_temp_f = (predicted_temp_c * 9/5) + 32  # Convert to Fahrenheit

        print(f"🌡️ Estimated Body Temp for {entity.title()}: {predicted_temp_c:.2f} °C / {predicted_temp_f:.2f} °F\n")

    # Show webcam feed
    cv2.imshow("YOLO Animal & Human Temp Predictor", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

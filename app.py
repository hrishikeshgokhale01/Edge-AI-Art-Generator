import cv2
import numpy as np
from utils import preprocess_for_model, postprocess, load_hailo_model

# Initialize video capture and load the default model
cap = cv2.VideoCapture(0)  # USB Camera
model = load_hailo_model("models/mosaic_style.onnx")

print("Press '1' for Mosaic Style, '2' for Rain Princess Style, 'q' to Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess and run inference
    input_frame = preprocess_for_model(frame)
    stylized_frame = model.predict(input_frame)  # Hailo model inference
    output_frame = postprocess(stylized_frame)

    # Display the stylized frame
    cv2.imshow("Stylized Video", output_frame)

    # Handle user input for style switching
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        model = load_hailo_model("models/mosaic_style.onnx")
    elif key == ord('2'):
        model = load_hailo_model("models/rain_princess_style.onnx")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
from utils import preprocess_for_model, postprocess
from hailo_platform import HEF, VDevice  # Import Hailo SDK components

# Load Hailo model
def load_hailo_model(hef_path):
    device = VDevice()  # Initialize the Hailo device
    network_groups = device.configure(HEF(hef_path))  # Load HEF (Hailo Executable File)
    return network_groups[0]  # Return the primary network group

# Initialize video capture and load the default model
cap = cv2.VideoCapture(0)  # USB Camera
model = load_hailo_model("models/mosaic_style.hef")  # Load a Hailo-optimized HEF file

print("Press '1' for Mosaic Style, '2' for Rain Princess Style, 'q' to Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess and run inference
    input_frame = preprocess_for_model(frame)
    results = model.run(input_frame)  # Run inference using the Hailo model
    output_frame = postprocess(results)

    # Display the stylized frame
    cv2.imshow("Stylized Video", output_frame)

    # Handle user input for style switching
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'):
        model = load_hailo_model("models/mosaic_style.hef")
    elif key == ord('2'):
        model = load_hailo_model("models/rain_princess_style.hef")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

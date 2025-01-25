import cv2
import numpy as np

def preprocess_for_model(frame):
    # Resize and normalize the input frame
    input_frame = cv2.resize(frame, (224, 224))
    input_frame = input_frame.astype(np.float32) / 255.0
    input_frame = np.transpose(input_frame, (2, 0, 1))  # Channels first
    input_frame = np.expand_dims(input_frame, axis=0)  # Add batch dimension
    return input_frame

def postprocess(output):
    # Convert the model output back to displayable format
    output = np.squeeze(output)  # Remove batch dimension
    output = np.transpose(output, (1, 2, 0))  # Channels last
    output = (output * 255).astype(np.uint8)  # Denormalize
    return cv2.cvtColor(output, cv2.COLOR_RGB2BGR)

def load_hailo_model(model_path):
    # Placeholder for loading Hailo-optimized ONNX models
    from hailo_sdk import Net
    return Net.load(model_path)

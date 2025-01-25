# Edge-AI-Art-Generator
This repository demonstrates how to deploy an Edge AI Art Generator on a Raspberry Pi 5 using a Hailo AI accelerator and a USB-controlled camera. The system captures live video, applies real-time style transfer, and displays the stylized feed.


## Features
- Real-time style transfer using optimized models.
- Switch styles dynamically via keyboard inputs.
- Display live video feed with applied artistic effects.

---

## Requirements

### Hardware
- Raspberry Pi 5
- Hailo AI acceleration module
- USB-controlled camera
- Monitor (for output)

### Software
- Python 3.9+
- Hailo TAPPAS SDK
- OpenCV
- ONNX Runtime

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/edge-ai-art-generator.git
   cd edge-ai-art-generator
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Hailo SDK:**
   Follow the [Hailo SDK setup guide](https://hailo.ai/sdk/) to configure the environment.

4. **Download Models:**
   Download pre-trained style transfer models and place them in the `models/` directory.

---

## Usage

1. **Run the Script:**
   ```bash
   python app.py
   ```

2. **Keyboard Controls:**
   - `1`: Apply Mosaic Style
   - `2`: Apply Rain Princess Style
   - `q`: Quit the application

---

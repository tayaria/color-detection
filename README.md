# Color Detection System

A real-time color detection application that identifies and tracks red, green, blue, and yellow colors using computer vision with OpenCV.

## 🎨 Features

- **Multi-Color Detection**: Automatically detects red, green, blue, and yellow colors
- **Real-Time Processing**: Live video feed with instant color recognition
- **Debug Information**: Displays pixel count for each detected color
- **Simple Interface**: Minimalist design with keyboard controls
- **Lightweight**: Efficient processing for smooth performance

## 📋 Prerequisites

- Python 3.7+
- Webcam or camera device
- pip package manager

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/tayaria/color-detection.git
cd color-detection
```

2. **Install dependencies**
```bash
pip install opencv-python numpy
```

## 📦 Dependencies
```txt
opencv-python>=4.5.0
numpy>=1.19.0
```

## 💻 Usage

1. **Run the application**
```bash
python python detect_color.py
```

2. **Point your camera** at colored objects (red, green, blue, or yellow)

3. **View real-time detection** with color names and pixel counts displayed on screen

4. **Press 'q'** to quit the application

## 🎮 Controls

| Key | Action |
|-----|--------|
| `q` | Quit application |

## 🛠️ How It Works

The system uses HSV (Hue, Saturation, Value) color space for accurate detection:

1. Captures video frames from webcam
2. Converts RGB to HSV color space
3. Applies color range masks for target colors
4. Counts pixels matching each color
5. Displays results with visual feedback

## 📁 Project Structure
```
color-detection-system/
│
├── color_detector.py      # Main application
├── README.md             # Documentation
├── .gitignore           # Git ignore rules
```

## ⚙️ Configuration

Adjust HSV ranges in `color_detector.py` to fine-tune detection:
```python
# Example: Red color range
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
```

## 🐛 Troubleshooting

**Camera not detected?**
- Check webcam connection and permissions
- Try different camera index: `cv2.VideoCapture(1)`

**Inaccurate color detection?**
- Improve lighting conditions
- Calibrate HSV ranges for your environment
- Ensure colored objects are clearly visible

**Performance issues?**
- Lower camera resolution
- Close resource-intensive applications
- Update graphics drivers

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 🔮 Future Enhancements

- [ ] Additional color detection (orange, purple, etc.)
- [ ] Bounding boxes around detected colors
- [ ] Configuration file for custom HSV ranges
- [ ] Video file input support
- [ ] CSV export of detection results
- [ ] Interactive HSV calibration tool
- [ ] Multi-language support

## 👤 Author

**Aymen Tayari**
- GitHub: [tayaria](https://github.com/tayaria/color-detection)
- Email: aymentayari191@gmail.com

## 🙏 Acknowledgments

- OpenCV community
- NumPy developers
- All contributors and testers

## 📸 Screenshots

<img width="805" height="638" alt="image" src="https://github.com/user-attachments/assets/a97c1d84-1c83-437b-93e9-254e6adcd6a1" />

<img width="797" height="637" alt="image" src="https://github.com/user-attachments/assets/ab640256-9b07-4225-bc30-02309d0acf09" />




---

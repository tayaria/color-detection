# Color Detection System
A real-time color detection application that identifies and tracks red, green, blue, and yellow colors using computer vision.
Features

Multi-Color Detection: Detects four primary colors (red, green, blue, and yellow)
Real-Time Display: Live video feed with visual indicators showing detected colors
Debug Information: Displays pixel count for each detected color
Simple Interface: Easy-to-use keyboard controls
Performance Optimized: Efficient processing for smooth real-time operation

Prerequisites
Before running this project, ensure you have the following installed:

Python 3.7 or higher
pip (Python package installer)
A working webcam or camera device

Installation

Clone the repository:

bashgit clone https://github.com/yourusername/color-detection-system.git
cd color-detection-system

Install required dependencies:

bashpip install -r requirements.txt
```

## Required Dependencies

Create a `requirements.txt` file with the following packages:
```
opencv-python>=4.5.0
numpy>=1.19.0
Usage

Run the main script:

bashpython color_detector.py
```

2. The application will open a window showing the live camera feed

3. Point the camera at colored objects to detect:
   - Red objects
   - Green objects
   - Blue objects
   - Yellow objects

4. Debug information will be displayed on screen showing:
   - Detected color name
   - Pixel count for each color

5. Press `q` to quit the application

## How It Works

The application uses OpenCV's HSV (Hue, Saturation, Value) color space for accurate color detection:

1. **Capture**: Reads frames from the webcam
2. **Convert**: Transforms RGB to HSV color space
3. **Threshold**: Applies color range masks for each target color
4. **Count**: Calculates the number of pixels for each color
5. **Display**: Shows results with visual feedback

## Project Structure
```
color-detection-system/
│
├── color_detector.py      # Main application script
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore file
Configuration
You can adjust color detection sensitivity by modifying the HSV range values in the code:
python# Example HSV ranges (Hue, Saturation, Value)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
Keyboard Controls
KeyActionqQuit the application
Troubleshooting
Camera not detected

Ensure your webcam is properly connected
Check camera permissions in your system settings
Try changing the camera index in the code: cv2.VideoCapture(0) to cv2.VideoCapture(1)

Colors not detected accurately

Adjust lighting conditions (avoid direct sunlight or very dim environments)
Calibrate HSV ranges for your specific lighting setup
Ensure the colored object occupies sufficient area in the frame

Performance issues

Lower the camera resolution
Reduce frame processing rate
Close other resource-intensive applications

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

OpenCV community for the powerful computer vision library
Contributors and testers who helped improve the application

Contact
Your Name - @yourtwitter
Project Link: https://github.com/yourusername/color-detection-system
Future Enhancements

 Add more color detection options
 Implement color tracking with bounding boxes
 Add configuration file for custom HSV ranges
 Support for video file input
 Export detection results to CSV
 GUI for real-time HSV range adjustment

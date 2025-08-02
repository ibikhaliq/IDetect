# IDetect
A real-time facial recognition system built with Python and OpenCV that detects, encodes, and identifies faces using live camera feed. The system compares faces with known encodings to mark attendance or verify identity, making it useful for security and automation applications.
Features:
🔍 Detects and recognizes faces in real time using webcam

🧠 Uses facial encodings to compare with known faces

✅ Automatically logs recognized faces with timestamps

📂 Easily expandable to new identities

🛡️ Useful for attendance systems, security verification, and automation


🛠️ Tech Stack
Python 3.8+

OpenCV

face_recognition (based on dlib)

NumPy

🧪 How It Works
Loads known face images and encodes them

Captures live video using webcam

Detects faces in each frame and encodes them

Compares live encodings with known ones

Displays names and marks attendance in Attendance.csv

📌 To Add New People:
Add a clear image to the Images/ folder

Name the file as the person’s name (e.g., ElonMusk.jpg)

Restart the program — that’s it!



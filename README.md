# 🎭 Face Recognition Attendance System  

📌 **A Python-based attendance system that utilizes face recognition to automate attendance marking.**  

---

## 🚀 Introduction  

The **Face Recognition Attendance System** is a powerful and efficient Python application that captures video from a webcam, detects faces, matches them against known individuals, and logs attendance automatically. This system eliminates the need for manual attendance marking, making it ideal for schools, workplaces, and events.  

---

## 📜 Features  

✔️ **Real-time Face Recognition** – Detects and identifies faces instantly.  
✔️ **Automated Attendance Logging** – Records recognized individuals in a CSV file with timestamps.  
✔️ **Easy Face Registration** – Simply place images in the `faces` folder to add new users.  
✔️ **User-Friendly Interface** – Displays names on the video feed for recognized faces.  
✔️ **CSV-Based Attendance Records** – Generates attendance files automatically each day.  
✔️ **Efficient and Fast Processing** – Uses OpenCV and face_recognition libraries for optimized performance.  

---

## 🛠 Installation  

Before running the program, install the required dependencies using pip:  

```bash
pip install face_recognition cmake opencv-python numpy
```

---

## 🎯 Usage  

### 1️⃣ Prepare the Known Faces  
📂 Place clear and recognizable images of known individuals in the `faces` directory.  
🔖 Ensure each file name matches the individual's name (e.g., `John_Doe.jpg`).  

### 2️⃣ Run the Program  
Execute the script to start face recognition:  

```bash
python main.py
```

🎥 The program will access the default webcam and start scanning faces.  

### 3️⃣ Attendance Recording  
📌 Recognized individuals will have their names displayed on the screen.  
📄 A CSV file (`YYYY-MM-DD.csv`) will be generated to log attendance records.  

### 4️⃣ Exit the Program  
Press **'q'** on your keyboard to stop the video capture and exit.  

---

## 📦 Requirements  

Ensure you have **Python 3.10** installed along with the following dependencies:  

- `face_recognition`  
- `cmake`  
- `opencv-python`  
- `numpy`  

---

## ⚡ Demo  
 
![Screenshot 2025-01-30 180055](https://github.com/user-attachments/assets/553b06f9-6d6a-43a2-b8c0-7f8d67db3099)

---

## 🛠 Troubleshooting  

💡 **Face Not Recognized?**  
✔️ Ensure the `faces` directory contains clear images.  
✔️ Check that face images are well-lit and high resolution.  

💡 **Application Not Running?**  
✔️ Verify that all dependencies are installed correctly.  
✔️ Try running the script with administrator privileges.  

---

## 👨‍💻 Developer  

💡 **Shubham Jaiswal**  

🔗 [GitHub Profile](https://github.com/shubhujais15)  

---

🎯 **Make attendance hassle-free with facial recognition!** 🚀  

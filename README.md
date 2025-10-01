# Nerf Turret Controller (PyQt5 + Arduino)

A Python + PyQt5 GUI application to control a Nerf turret built with an Arduino, servos, and a motor.  
Move your mouse over the GUI pad to control the turret’s pan/tilt servos, toggle the flywheel motor, and fire darts.

---

## 🚀 Features
- **GUI built with PyQt5**  
- Mouse-controlled **pan/tilt servos** (0–180° range)  
- **Motor toggle button** to power the flywheels  
- **Shoot action** triggered by mouse click  
- Communication via **serial protocol** over USB  

---

## 🖥️ Software Requirements
- Python 3.7+  
- [PyQt5](https://pypi.org/project/PyQt5/)  
- Arduino IDE (for uploading the sketch)  

Install Python dependencies:
```bash
pip install pyqt5 pyserial

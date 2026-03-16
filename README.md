# 🔐 Secure Coding Review - CodeAlpha Internship

## 📌 Overview
This project demonstrates a secure coding review by identifying vulnerabilities in a Flask web application and applying fixes.

---

## ⚠️ Vulnerable Version
File: `app_vulnerable.py`

Issues:
- Plain text password storage
- No input validation
- Debug mode enabled

---

## ✅ Secure Version
File: `app_secure.py`

Fixes:
- Password hashing using werkzeug
- Input validation implemented
- Debug mode disabled

---

## 🛠️ Technologies Used
- Python
- Flask
- Werkzeug Security

---

## 🎯 Learning Outcome
This project helped understand:
- Common web vulnerabilities
- Secure coding practices
- Importance of protecting user data

---

## 🚀 How to Run

```bash
pip install flask
python app_secure.py

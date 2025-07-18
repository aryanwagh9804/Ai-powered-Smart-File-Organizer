# 📁 AI-Powered Smart File Organizer

An intelligent desktop automation tool that automatically classifies and organizes your files into structured folders using Machine Learning (ML). It works in real-time to declutter your system and improve productivity — all powered by a custom-trained AI model.

---

## 🔍 Overview

This project detects and classifies files (based on their names or content) and moves them into appropriate category-based folders such as **Documents**, **Images**, **Code**, **Presentations**, and more.

It includes:
- 🧠 A trained ML model (Naive Bayes or similar)
- 📂 A real-time file sorting system using `watchdog`
- 🌐 Optional Streamlit UI + REST API (Flask) for web/mobile extension

---

## 🧠 Features

- ✅ AI-based file type classification (by name or content)
- ✅ Auto-folder creation and file sorting
- ✅ Real-time folder monitoring
- ✅ Streamlit UI for manual testing
- ✅ Flask REST API for integration with mobile/web
- ✅ Option to run silently on startup (background automation)

---

## 📸 Project Output

Here’s a screenshot showing automatically sorted folders by file type:

![Project Output Screenshot]([https://github.com/aryanwagh9804/Ai-powered-Smart-File-Organizer/blob/main/Screenshot%202025-07-18%20095736.png])

---

## 💻 Technology Stack

| Layer         | Tools / Libraries                  |
|---------------|------------------------------------|
| ML Model      | scikit-learn, Naive Bayes, TF-IDF  |
| Backend       | Python, Flask, Watchdog            |
| Frontend (UI) | Streamlit                          |
| File System   | OS, shutil                         |
| Deployment    | Run as background script or REST API|



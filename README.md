# ⚡ ECE Terminal-Based Task Manager (CLI)

<p align="center">
  <b>Krishnakant Gupta</b><br>
  B.Tech in Electronics and Communication Engineering (2025–2029)<br>
  <b>VIT Bhopal University</b><br>
  <i>Registration No: 25BEC10094</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Interface-CLI-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Embedded_Systems-orange?style=for-the-badge" />
</p>

---

## 🌟 Project Overview
The **CLI To-Do List Manager** is a high-efficiency, lightweight Python utility designed for engineers who work primarily in terminal environments. While heavy GUI apps consume valuable RAM needed for EDA tools and circuit simulations, this tool provides a zero-latency way to track technical tasks, hardware debugging steps, and project milestones directly from the command line.

---

## 📋 Key Features

* **⚡ Lightweight Execution:** Optimized for low-resource environments, including SSH terminals and embedded Linux boards (e.g., Raspberry Pi).
* **💾 Non-Volatile Persistence:** Automatically saves data to a local `todo.txt` file, simulating the "Save-to-Flash" logic used in electronic systems.
* **🔍 Numbered Task View:** Simplifies task tracking with an indexed list for rapid removal and updates.
* **🛡️ Robust Error Handling:** Implementation of `try-except` blocks to prevent system crashes during invalid data entry.
* **🌐 Offline Functionality:** 100% functional without internet access, ensuring privacy for proprietary engineering data.

---

## 📂 Project Structure

| File | Function |
| :--- | :--- |
| 📄 `todo_list.py` | Main application logic and File I/O operations. |
| 📝 `todo.txt` | Data storage file (Automatically generated). |
| 📘 `README.md` | Project documentation and technical overview. |

---

## 🛠️ Technical Specifications

* **Language:** Python 3.x
* **Paradigm:** Procedural Programming
* **Core Modules:** `os` (File system verification and path handling)
* **Data Structure:** Python Lists with persistent File I/O synchronization

---

## 🚀 Installation & Usage

1. **Prerequisites:** Ensure you have Python installed.
   ```bash
   python --version

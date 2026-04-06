# 🐷 Digital Piggy Bank Pro & CLI

A versatile suite of tools to track your personal savings goals. Whether you prefer a sleek **Web Dashboard**, a fast **C++ Executable**, or a flexible **Python Script**, this project ensures you hit your targets with style and precision.

---

## ✨ Features Across All Versions

* **🎯 Goal Centric:** Always define *what* you are saving for (e.g., "New Camera" or "Emergency Fund").
* **📊 Smart Analytics:** Instant calculation of the **Remaining Amount** and **Completion Percentage**.
* **💾 Data Persistence:**
    * **Web:** Uses `localStorage` (Browser).
    * **C++ & Python:** Uses local files (`data.txt` / `piggy_data.json`).
* **🌍 Multi-Language:** Full support for **IT, EN, FR, DE, ES**.
* **💱 Multi-Currency:** Toggle between **€, $, and £**.

---

## 🚀 How to Use

### 1. Web Version (HTML/JS)
*Best for: A premium visual experience with animated charts.*
* **Setup:** Open `index.html` in any modern web browser.
* **Features:** Includes **Chart.js** integration for a dynamic doughnut chart and a fully responsive dark theme.
* **Persistence:** Data is saved automatically in your browser's cache.

### 2. C++ Version
*Best for: High performance and minimal resource usage.*
* **Compilation:** Use a C++ compiler (like `g++`):
    ```bash
    g++ main.cpp -o piggybank
    ./piggybank
    ```
* **Usage:** Follow the CLI prompts to enter your data.
* **Persistence:** Saves your progress in a `data.txt` file in the same folder.

### 3. Python Version
*Best for: Flexibility and ease of modification.*
* **Requirements:** Requires Python 3.x installed.
* **Execution:**
    ```bash
    python piggy_bank.py
    ```
* **Features:** Includes an ASCII progress bar (`[████---]`) and robust JSON data handling.
* **Persistence:** Saves state in `piggy_data.json` with UTF-8 encoding.

---

## 🛠️ Technical Comparison

| Feature | Web (HTML/CSS/JS) | C++ (CLI) | Python (CLI) |
| :--- | :--- | :--- | :--- |
| **Interface** | Modern Dark UI | Terminal | Terminal |
| **Visuals** | Animated Charts | Text-based | ASCII Progress Bar |
| **Storage** | LocalStorage | .txt File | .json File |
| **Dependencies** | Chart.js (CDN) | Standard Library | Standard Library |

---

## 💡 Privacy & Security
Regardless of the version you choose, **all data stays on your machine**. No financial information is ever transmitted to a server or third-party service.
---

# Example


*Created with ❤️ for smart savers worldwide.*

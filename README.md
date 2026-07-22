# 🔗 Flask URL Shortener with Custom Alias

A lightweight, modern, and user-friendly URL Shortener web application built using **Python Flask** and **Vanilla CSS**. Features instant link shortening, optional custom alias creation, one-click copy to clipboard, and a custom 404 page for missing links.

---

## ✨ Features

- **⚡ Instant Shortening**: Converts long URLs into compact 6-character short codes (letters & numbers).
- **🏷️ Custom Alias Support**: Enter a personalized alias (e.g., `my-custom-link`) or leave it blank to auto-generate a code.
- **🛡️ Input Validation**:
  - Automatically prepends `https://` if missing.
  - Validates custom alias characters (`A-Z`, `a-z`, `0-9`, `-`, `_`).
  - Checks for alias uniqueness and displays clear error messages for invalid/duplicate inputs.
- **📋 One-Click Copy**: Built-in clipboard helper with interactive confirmation ("Copied!").
- **🎨 Modern Mint & Teal UI**: Clean dashboard-inspired design with responsive layouts, rounded cards, subtle shadows, and CSS animations.
- **🚫 Custom 404 Page**: Displays a friendly error page when visiting a non-existent short URL.
- **🚀 Zero Database Setup**: Uses an in-memory Python dictionary data structure for fast execution without database dependencies.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask 3.0.3
- **Frontend**: HTML5, Vanilla CSS3 (Custom Variables, Flexbox, Keyframe Animations)
- **Typography**: Plus Jakarta Sans & Inter (Google Fonts)

---

## 📁 Project Structure

```
url_shortener/
├── app.py               # Main Flask application (routes, generator, validation, dictionary store)
├── requirements.txt     # Python dependencies (Flask)
├── README.md            # Project documentation
├── static/
│   └── style.css        # Full CSS design system & responsive styling
└── templates/
    ├── index.html       # Home page (form, alias input, result box)
    └── error.html       # Custom 404 page
```

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener/url_shortener
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

4. **Open in Browser:**
   Navigate to `http://127.0.0.1:5000` in your web browser.


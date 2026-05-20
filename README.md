# CloudOps Dashboard 🚀

A lightweight, self-service automation portal that allows teams to easily Start and Stop AWS EC2 sandbox environments to eliminate unnecessary cloud spend.

---

## 📸 Interface Preview
<img src=""C:\Users\srahimun\Pictures\Screenshots\dashboard.png"" alt="Dashboard UI" width="450"/>

---

## 🛠️ Features & Architecture
* **Frontend:** Clean HTML5/CSS3 dashboard using vanilla JavaScript (`Fetch API`) to send asynchronous control requests without reloading the page.
* **Backend:** Python `Flask` API handling structured state transitions securely.
* **Cloud Integration:** Managed programmatically using the `Boto3 SDK` for AWS.
* **Security First:** Zero hardcoded credentials. Credentials are loaded dynamically via terminal environment variables to enforce best practices.

---

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install flask flask-cors boto3
2.**Set your AWS credentials in your terminal**
   ```bash
   pip install flask flask-cors boto3
3. **Run the backend API:**
   ```bash
   python app.py

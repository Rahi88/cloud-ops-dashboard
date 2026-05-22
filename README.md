# CloudOps Dashboard 🚀

A lightweight, self-service automation portal that allows teams to easily Start and Stop AWS EC2 sandbox environments to eliminate unnecessary cloud spend.

## 📸 Interface Preview
<img width="1727" height="1130" alt="Screenshot 2026-05-22 112835" src="https://github.com/user-attachments/assets/8ae46f20-0790-4e0a-a090-f9bd6723b905" />

## 🛠️ Features & Architecture
* **Frontend:** Clean HTML5/CSS3 dashboard using vanilla JavaScript (`Fetch API`) to send asynchronous control requests without reloading the page.
* **Backend:** Python `Flask` API handling structured state transitions securely.
* **Cloud Integration:** Managed programmatically using the `Boto3 SDK` for AWS.
* **Security First:** Zero hardcoded credentials. Credentials are loaded dynamically via terminal environment variables to enforce best practices.



## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install flask flask-cors boto3
2. **Set your AWS credentials in your terminal**
   ```bash
   pip install flask flask-cors boto3
   
3.  **Run the backend API:**
   ```bash
    python app.py

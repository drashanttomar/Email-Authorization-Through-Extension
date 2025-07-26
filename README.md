Email Authorization Browser Extension

A real-time browser extension that scans emails directly from your email platform and instantly classifies them as Authorized, Suspicious, or Unauthorized using a trained machine learning model.

🌐 Frontend (Browser Extension)
popup.html – UI for the popup displaying the scan result
manifest.json – Extension configuration (permissions, scripts, icons)
icon.png – Extension icon for browser toolbar
content.js – Script that extracts email data from webmail pages (Gmail, Outlook, etc.)
🧠 Backend (Authorization Engine)
App.py – Backend API that receives extracted email data and returns the authorization result
train.py – Script to train the ML model using labeled email data
email_auth_model.pkl – Trained classification model
vectorizer.pkl – Text vectorizer used to preprocess input email content
email.csv – Sample training dataset containing labeled email records
⚙️ How It Works
The extension monitors email content in the browser.
Extracted details (domain, subject, body) are sent to the backend.
The backend uses the ML model to classify the email.
A popup (popup.html) shows whether the email is:
✅ Authorized
⚠️ Suspicious
❌ Unauthorized
📦 Technologies Used
Frontend: HTML, CSS, JavaScript (Chrome Extension APIs)
Backend: Python, Flask/FastAPI (for API), scikit-learn (for model training)
ML Techniques: Text classification using domain, subject, and body features

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer once at startup
model = joblib.load("email_auth_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/check_email', methods=['POST'])
def check_email():
    data = request.json
    email_content = data.get("content", "")
    
    if not email_content.strip():
        return jsonify({"error": "No content provided"}), 400

    vectorized = vectorizer.transform([email_content])
    prediction = model.predict(vectorized)

    status = "Authorized" if prediction[0] == 1 else "Unauthorized"
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(debug=True)

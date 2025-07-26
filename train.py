import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load dataset
df = pd.read_csv("data/emails.csv")  # Ensure this file exists

# Combine fields into one
df["text"] = df["domain"] + " " + df["subject"] + " " + df["body"]

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Split & train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Save model and vectorizer
os.makedirs("models", exist_ok=True)
joblib.dump(clf, "models/email_auth_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model and vectorizer saved to 'models/'")
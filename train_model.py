import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


file_path = "data.xsv"  
df = pd.read_csv(file_path, delimiter=",")


if "filename" not in df.columns or "category" not in df.columns:
    raise ValueError("Dataset must contain 'filename' and 'category' columns")


vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5))  
X = vectorizer.fit_transform(df["filename"])
y = df["category"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix")
plt.show()
print("Classification Report:")
print(classification_report(y_test, y_pred))
plt.figure(figsize=(8, 5))
sns.histplot(y_pred, label="Predicted Categories", color="blue", kde=True , bins=len(set(y)))
sns.histplot(y_test, label="Actual Categories", color="red", kde=True, bins=len(set(y)), alpha=0.5)
plt.legend()
plt.title("Predicted vs. Actual Categories Histogram")
plt.xlabel("Category")
plt.ylabel("Frequency")
plt.show()
with open("file_classifier.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)
print("Training complete. Model saved as 'file_classifier.pkl'.")

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load dataset and train model
iris = load_iris()
X, y = iris.data, iris.target
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(X, y)

# Save the model
joblib.dump(clf, "model.joblib")
print("Model trained and saved successfully.")

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

vulnerable_path = r'C:\Users\***\***\Dataset CWE-787.csv'
secure_path = r'C:\Users\***\***\Dataset códigos corretos.csv'

vulnerable_code = pd.read_csv(vulnerable_path, header=None, names=['code'])
secure_code = pd.read_csv(secure_path, header=None, names=['code'])

vulnerable_code['label'] = 1
secure_code['label'] = 0

data = pd.concat([vulnerable_code, secure_code], ignore_index=True)

X = data['code']
y = data['label']

vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Secure', 'Vulnerable'],
            yticklabels=['Secure', 'Vulnerable'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
sns.heatmap(cm_normalized, annot=True, fmt='.2f', cmap='Blues', xticklabels=['Secure', 'Vulnerable'],
            yticklabels=['Secure', 'Vulnerable'])
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Normalized Confusion Matrix')
plt.show()

fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
plt.show()

sns.histplot(y_pred, bins=2, kde=False, color='blue', label='Predicted')
sns.histplot(y_test, bins=2, kde=False, color='red', label='Actual', alpha=0.5)
plt.legend()
plt.title('Distribution of Predictions vs Actual')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.show()

sns.histplot(y_prob, bins=10, kde=True)
plt.title('Distribution of Predicted Probabilities')
plt.xlabel('Predicted Probability')
plt.ylabel('Frequency')
plt.show()


def analyze_code(new_code):
    new_code_vectorized = vectorizer.transform([new_code])
    prediction = model.predict(new_code_vectorized)
    return "Vulnerable to CWE-787!" if prediction[0] == 1 else "Secure code!"


if __name__ == "__main__":
    user_code = input("Please enter the code to analyze:\n")
    result = analyze_code(user_code)
    print(result)

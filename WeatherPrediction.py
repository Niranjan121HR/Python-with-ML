from sklearn.linear_model import LogisticRegression
import numpy as np
X = np.array([[15], [18], [21], [30], [35]])
y = np.array([0, 0, 1, 1, 1])

# Training ML model by using Logistic regression
model = LogisticRegression()
model.fit(X, y)
# model.predict([[19]]) 
print(model.predict([[19]]))
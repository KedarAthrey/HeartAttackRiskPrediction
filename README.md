
# HeartAttackRisk
## Explanation
This code uses a variety of models( RandomForest, SVC, Logistic Regression, Perceptrons, etc.) to predict the risk of a heart attack.
It uses 11 basic metrics:
- Age
- Gender
- Type of Chest Pain
- Resting Blood Pressure
- Cholesterol Levels 
- Fasting Blood sugar 
- Resting ECG measure 
- Maximum Heart rate 
- Presence of Exercise Angina( heart pain during exercise)
- Oldpeak measure( a dip in the ST limb of an ECG during exercise compared to rest)
- ST limb slope 

The models tested were:
- SVC
- LinearSVC
- RandomForest
- KNN
- Gaussian NB
- Perceptron
- SGDClassifier
- DecisionTreeClassifier

The model with the highest accuracy was the SVC (using the 'rbf' kernel)

## Workflow
The major steps followed were:

- Assigning ranges to numerical data, to convert them into categorical data
-  One hot encoding numerical data to ensure that the model only receives Boolean inputs
- Passing the inputs to the various classifiers, and assessing accuracy based on their precision, recall, success rate, and F-1 score

## Demo

1) Run the Jupyter Notebook
2) Download the dataset from https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

3) Edit the file paths in the Jupyter Notebook accordingly

4) After saving the trained SVC model as a  .joblib file, run the second .py file "HeartRiskBack.py"
5) Input your details accordingly,
[ I'm not the best at frontend right now, so it's not very pretty :) ] 









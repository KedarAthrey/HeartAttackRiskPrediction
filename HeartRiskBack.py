import joblib
import numpy as np

def get_binary_input(prompt):
    while True:
        response = input(prompt + " (y/n): ").lower()
        if response in ['y', 'n']:
            return 1 if response == 'y' else 0
        print("Invalid input. Please enter 'y' or 'n'.")

def get_mutually_exclusive_input(prompt, options):
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return [1 if i == choice-1 else 0 for i in range(len(options))]
            print("Invalid choice. Please enter a number within the given range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_age_group(age):
    age_groups = ['child', 'Young_Adult', 'Older_Adult', 'Middle_Aged', 'Y_Senior_Citizen', 'O_Senior_Citizen', 'Elderly']
    if age <= 25:
        index = 0
    elif age <= 35:
        index = 1
    elif age <= 45:
        index = 2
    elif age <= 55:
        index = 3
    elif age <= 65:
        index = 4
    elif age <= 75:
        index = 5
    else:
        index = 6
    return [1 if i == index else 0 for i in range(len(age_groups))]

def get_numerical_input(prompt, categories):
    while True:
        try:
            value = float(input(prompt + f" ({categories[0]}-{categories[-1]}): "))
            result = [0] * (len(categories) - 1)
            for i, threshold in enumerate(categories[1:]):
                if value <= threshold:
                    result[i] = 1
                    return result
            return result  # If value is greater than all thresholds, return all zeros
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    inputs = []
    
    # Binary inputs (3 features)
    inputs.append(get_binary_input("Is FastingBS high? (>120 mg/dl)"))
    inputs.append(get_binary_input("Is ExerciseAngina present?"))
    inputs.append(get_binary_input("Is Sex Female?"))
    
    # Chest Pain Type (4 features)
    inputs.extend(get_mutually_exclusive_input("Select Chest Pain Type:", ["ASY", "ATA", "NAP", "TA"]))
    
    # Resting ECG (3 features)
    inputs.extend(get_mutually_exclusive_input("Select Resting ECG Type:", ["LVH", "Normal", "ST"]))
    
    # ST Slope (3 features)
    inputs.extend(get_mutually_exclusive_input("Select ST Slope Type:", ["Down", "Flat", "Up"]))
    
    # Age group (7 features)
    while True:
        try:
            age = int(input("Enter age: "))
            if 0 <= age <= 100:
                inputs.extend(get_age_group(age))
                break
            else:
                print("Age must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
    # Cholesterol (6 features)
    inputs.extend(get_numerical_input("Enter Cholesterol level", [0, 100, 175, 250, 325, 400, 600]))
    
    # Resting BP (5 features)
    inputs.extend(get_numerical_input("Enter Resting Blood Pressure", [0, 100, 125, 150, 175, float('inf')]))
    
    # Max HR (7 features)
    inputs.extend(get_numerical_input("Enter Max Heart Rate", [0, 70, 90, 110, 130, 150, 170, float('inf')]))
    
    # Oldpeak (8 features)
    inputs.extend(get_numerical_input("Enter Oldpeak value", [-float('inf'), -0.75, 0, 0.75, 1.5, 2.25, 3, 4, float('inf')]))

    # Load the SVM model
    try:
        model = joblib.load('svm_heartrisk.joblib')
        print("Model loaded successfully.")
    except FileNotFoundError:
        print("Error: Model file not found. Please ensure 'svm_heartrisk.joblib' is in the current directory.")
        return
    except Exception as e:
        print(f"Error loading the model: {e}")
        return
    
    # Prepare the input for prediction
    X = np.array(inputs).reshape(1, -1)
    
    # Make prediction
    try:
        prediction = model.predict(X)
        probability = model.predict_proba(X)[0][1]  # Probability of the positive class

        print(f"Prediction: {'High risk' if prediction[0] == 1 else 'Low risk'}")
        print(f"Probability of high risk: {probability:.2f}")
    except Exception as e:
        print(f"Error making prediction: {e}")
    
    print(f"Number of features in input: {X.shape[1]}")

if __name__ == "__main__":
    main()
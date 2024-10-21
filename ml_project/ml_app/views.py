import pickle
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy as np
c = pd.Index(['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history',
       'bmi', 'HbA1c_level', 'blood_glucose_level'],
      dtype='object')
# Load the model when the application starts
with open(r'ml_app\static\model\logistic_regression_model_2.pkl', 'rb') as file:
    model = pickle.load(file)

def index(request):
    print(type(model))
    return render(request, 'ml_app/index.html', {"answer":-1})
def predict(request):
    if request.method == 'POST':
        # Get data from the request (adjust based on your input)
        cols = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history',
       'bmi', 'HbA1c_level', 'blood_glucose_level']
        values = []
        for col in cols:
            values.append(request.POST.get(col))
        
        input_data = pd.DataFrame(np.array(values).reshape(1, -1), columns=c)

        # Make the prediction
        prediction = model.predict(input_data)
        
        
        answer = prediction[0]
        print(answer)
        return render(request, 'ml_app/index.html', {"answer":answer})

    

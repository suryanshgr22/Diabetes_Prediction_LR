# Diabetes Risk Prediction Web Application

A machine learning web application that predicts diabetes risk based on user-input health metrics. Built with Django and scikit-learn, this application provides real-time predictions using a trained logistic regression model.

## Features
- User-friendly web interface for inputting health metrics
- Real-time diabetes risk prediction
- Supports various health indicators including:
  - Age
  - Gender
  - Hypertension status
  - Heart disease history
  - Smoking history
  - BMI
  - HbA1c level
  - Blood glucose level

## Technologies Used
- Python 3.x
- Django
- scikit-learn
- pandas
- numpy
- HTML/CSS

## Installation and Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/diabetes-prediction.git
cd diabetes-prediction
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start the development server
```bash
python manage.py runserver
```

6. Visit `http://127.0.0.1:8000/` in your web browser

## Usage
1. Navigate to the home page
2. Fill in all required health metrics in the form
3. Click the "Predict" button
4. View your prediction result

## Model Information
The prediction model is a logistic regression classifier trained on diabetes-related health metrics. The model takes into account various factors such as BMI, age, blood glucose levels, and other health indicators to predict diabetes risk.

## Project Structure
```
diabetes-prediction/
│
├── ml_app/                  # Main application directory
│   ├── static/             # Static files (CSS, models)
│   │   └── model/         # Trained model files
│   ├── templates/         # HTML templates
│   ├── views.py           # View functions
│   └── models.py          # Django models
│
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Development
To contribute to this project:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Requirements
See `requirements.txt` for a list of all dependencies.

## Future Improvements
- Add data visualizations for prediction insights
- Implement user authentication
- Add ability to save prediction history
- Include more detailed health metrics



## Acknowledgments
- Dataset source: [(https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)]

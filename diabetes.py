from pathlib import Path
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / 'model_rf.pkl'
SCALER_PATH = ROOT / 'scaler.pkl'

app = Flask(__name__, static_folder='static', template_folder='templates')

with MODEL_PATH.open('rb') as model_file:
    model = pickle.load(model_file)

with SCALER_PATH.open('rb') as scaler_file:
    scaler = pickle.load(scaler_file)

FEATURES = [
    ('Pregnancies', 'Pregnancy count', 'times'),
    ('Glucose', 'Sugar reading', 'mg/dL'),
    ('BloodPressure', 'Blood pressure', 'mmHg'),
    ('BMI', 'Weight index', 'kg/m²'),
    ('Age', 'Age', 'years'),
    ('DiabetesPedigreeFunction', 'Family risk score', '0 - 1'),
]

RANGE_HINTS = {
    'Pregnancies': '0 - 12',
    'Glucose': '70 - 200',
    'BloodPressure': '40 - 120',
    'BMI': '15 - 45',
    'Age': '15 - 90',
    'DiabetesPedigreeFunction': '0.0 - 1.0',
}

INSIGHT_TEXT = {
    'Pregnancies': 'How many times the person has been pregnant.',
    'Glucose': 'Blood sugar level after fasting.',
    'BloodPressure': 'Resting blood pressure in mmHg.',
    'BMI': 'Body mass index from height and weight.',
    'Age': 'How old the person is in years.',
    'DiabetesPedigreeFunction': 'A family history score for diabetes risk.',
}

DEFAULT_INPUTS = {
    'SkinThickness': 20.536458,
    'Insulin': 79.799479,
}

SCALER_ORDER = [
    'Pregnancies',
    'Glucose',
    'BloodPressure',
    'SkinThickness',
    'Insulin',
    'BMI',
    'DiabetesPedigreeFunction',
    'Age',
]


def compute_bmi_flags(bmi_value):
    bmi_value = float(bmi_value)
    normal = 1 if 18.5 <= bmi_value < 25 else 0
    overweight = 1 if 25 <= bmi_value < 30 else 0
    obese = 1 if bmi_value >= 30 else 0
    return normal, overweight, obese


def build_model_input(inputs):
    base = [
        inputs['Pregnancies'],
        inputs['Glucose'],
        inputs['BloodPressure'],
        DEFAULT_INPUTS['SkinThickness'],
        DEFAULT_INPUTS['Insulin'],
        inputs['BMI'],
        inputs['DiabetesPedigreeFunction'],
        inputs['Age'],
    ]
    bmi_normal, bmi_overweight, bmi_obese = compute_bmi_flags(inputs['BMI'])
    full_vector = np.array(base + [bmi_normal, bmi_overweight, bmi_obese], dtype=float).reshape(1, -1)
    return scaler.transform(full_vector)


@app.route('/')
def home():
    return render_template('index.html', features=FEATURES, hints=RANGE_HINTS, info=INSIGHT_TEXT)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json or request.form
    inputs = {}

    for key, label, unit in FEATURES:
        raw_value = data.get(key, '')
        try:
            value = float(raw_value)
        except (TypeError, ValueError):
            value = 0.0
        inputs[key] = value

    X = build_model_input(inputs)
    prediction = int(model.predict(X)[0])
    probability = float(model.predict_proba(X)[0][prediction]) if hasattr(model, 'predict_proba') else 0.0
    confidence = round(probability * 100, 1)

    if prediction == 1:
        status = 'High diabetes risk'
        badge = 'high-risk'
        advice = 'This profile indicates a higher chance of diabetes. Please consult a doctor and check your diet and exercise plan.'
    else:
        status = 'Lower diabetes risk'
        badge = 'low-risk'
        advice = 'The result is lower risk, but keep monitoring your diet and stay active for long-term health.'

    return jsonify({
        'prediction': status,
        'confidence': confidence,
        'badge': badge,
        'advice': advice,
        'values': inputs,
    })


if __name__ == '__main__':
    app.run(debug=True)

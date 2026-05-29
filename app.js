const form = document.getElementById('predict-form');
const predictionText = document.getElementById('prediction-text');
const confidenceValue = document.getElementById('confidence-value');
const adviceText = document.getElementById('advice-text');
const resultPill = document.getElementById('result-pill');
const meterFill = document.getElementById('meter-fill');
const valueList = document.getElementById('value-list');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    const payload = {};

    for (const [key, value] of formData.entries()) {
        payload[key] = value;
    }

    setBusy(true);
    clearPreview();

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            throw new Error('Prediction request failed');
        }

        const data = await response.json();
        renderResult(data);
    } catch (error) {
        renderError();
        console.error(error);
    } finally {
        setBusy(false);
    }
});

function renderResult(data) {
    const { prediction, confidence, advice, values, badge } = data;
    predictionText.textContent = prediction;
    confidenceValue.textContent = `${confidence}%`;
    adviceText.textContent = advice;
    resultPill.textContent = prediction;

    const isHighRisk = badge === 'high-risk';
    resultPill.style.background = isHighRisk ? 'rgba(255, 82, 82, 0.18)' : 'rgba(103, 222, 197, 0.16)';
    predictionText.style.color = isHighRisk ? '#ffb3b3' : '#bdf5dc';

    meterFill.style.width = `${Math.min(100, Math.max(0, confidence))}%`;
    meterFill.style.background = isHighRisk
        ? 'linear-gradient(90deg, #ff7b87 0%, #ffb08f 100%)'
        : 'linear-gradient(90deg, #65e9ff 0%, #8cffb5 100%)';

    valueList.innerHTML = Object.entries(values)
        .map(([key, value]) => {
            const label = key
                .replace('DiabetesPedigreeFunction', 'Family risk score')
                .replace('BloodPressure', 'Blood pressure')
                .replace('Glucose', 'Sugar reading')
                .replace('Pregnancies', 'Pregnancy count')
                .replace('BMI', 'BMI')
                .replace('Age', 'Age');
            return `<li><span>${label}</span><strong>${Number(value).toFixed(2)}</strong></li>`;
        })
        .join('');
}

function renderError() {
    predictionText.textContent = 'Unable to predict';
    confidenceValue.textContent = '--%';
    adviceText.textContent = 'Please enter valid numbers in every field and try again.';
    resultPill.textContent = 'Error';
    resultPill.style.background = 'rgba(255, 90, 90, 0.18)';
    meterFill.style.width = '0%';
    meterFill.style.background = 'linear-gradient(90deg, #ff7b87 0%, #ffb08f 100%)';
    valueList.innerHTML = '';
}

function clearPreview() {
    valueList.innerHTML = '';
}

function setBusy(isBusy) {
    const button = form.querySelector('button[type=submit]');
    if (isBusy) {
        button.textContent = 'Scanning values...';
        button.disabled = true;
        button.style.opacity = '0.8';
    } else {
        button.textContent = 'Check Risk';
        button.disabled = false;
        button.style.opacity = '1';
    }
}

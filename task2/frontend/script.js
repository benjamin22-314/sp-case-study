document.getElementById('imageInput').addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '<p style="text-align:center;">Analysing image...</p>';

    const formData = new FormData();
    formData.append('image', file);

    try {
        const response = await fetch('http://localhost:5000/analyse', {
            method: 'POST',
            body: formData
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();

        resultDiv.innerHTML = '';

        const predictionsContainer = document.createElement('div');

        for (const [key, value] of Object.entries(data)) {
            const predictionItem = document.createElement('div');
            predictionItem.classList.add('prediction-item');

            const label = document.createElement('span');
            label.classList.add('prediction-label');
            label.textContent = key.replace(/_/g, ' ').toUpperCase();

            const valueSpan = document.createElement('span');
            valueSpan.classList.add('prediction-value');
            valueSpan.textContent = value;

            predictionItem.appendChild(label);
            predictionItem.appendChild(valueSpan);

            predictionsContainer.appendChild(predictionItem);
        }

        resultDiv.appendChild(predictionsContainer);
    } catch (error) {
        resultDiv.innerHTML = `<p class="error-message">Error: ${error.message}</p>`;
    }
});
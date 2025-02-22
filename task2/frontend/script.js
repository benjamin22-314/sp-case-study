document.getElementById('imageInput').addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (!file) return;
 
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = 'Analysing image...';
 
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
        resultDiv.innerHTML = `
            Image predictions:
            aze_passport: ${data.aze_passport}
            est_id: ${data.est_id}
            esp_id: ${data.esp_id}
            grc_passport: ${data.grc_passport}
            rus_internalpassport: ${data.rus_internalpassport}
            srb_passport: ${data.srb_passport}
            svk_id: ${data.svk_id}
            lva_passport: ${data.lva_passport}
            fin_id: ${data.fin_id}
            alb_id: ${data.alb_id}
            `;
    } catch (error) {
        resultDiv.innerHTML = `Error: ${error.message}`;
    }
});

document.getElementById('submitBtn').addEventListener('click', async () => {
    const jsonFile = document.getElementById('jsonFile').files[0];
    const jsonText = document.getElementById('jsonText').value;
    const outputElement = document.getElementById('output');
    outputElement.textContent = '';

    let jsonData;

    if (jsonFile) {
        const fileContent = await jsonFile.text();
        try {
            jsonData = JSON.parse(fileContent);
        } catch (error) {
            outputElement.textContent = 'Error parsing JSON file: ' + error.message;
            return;
        }
    } else if (jsonText) {
        try {
            jsonData = JSON.parse(jsonText);
        } catch (error) {
            outputElement.textContent = 'Error parsing JSON text: ' + error.message;
            return;
        }
    } else {
        outputElement.textContent = 'Please provide a JSON file or text.';
        return;
    }

    try {
        const response = await fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(jsonData),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const processedJson = await response.json();
        outputElement.textContent = JSON.stringify(processedJson, null, 2);
    } catch (error) {
        outputElement.textContent = 'Error processing JSON: ' + error.message;
    }
});

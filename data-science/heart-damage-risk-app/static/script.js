document.getElementById('uploadForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Предотвращаем стандартную отправку формы

    const fileInput = this.querySelector('input[type="file"]');
    const file = fileInput.files[0];

    const data = new FormData();
    data.append('file', file); // Добавляем файл в объект FormData

    try {
        const response = await fetch('/predict/', {
            method: 'POST',
            body: data,
        });

        const result = await response.json();
        const errorValue = result['error'];

        if (errorValue !== undefined && errorValue.trim().length > 0) {
            document.getElementById('errorMessage').innerText = errorValue;
        } else {
            const resultDiv = document.getElementById('resultBox');
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '<code">' + result + '</code>';
            // resultDiv.innerHTML = '<pre>' + result + '</pre>';
            // resultDiv.innerHTML = '<pre>' + JSON.stringify(result, null, 2) + '</pre>';
            document.getElementById('errorMessage').innerText = ''; // очищаем ошибку
        }
    } catch (err) {
        document.getElementById('errorMessage').innerText = err.message || 'Возникла неизвестная ошибка.';
    }
});
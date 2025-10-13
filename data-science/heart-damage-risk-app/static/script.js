document.getElementById('uploadForm').addEventListener('submit', async function(event) {
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

        // Отображаем результат на странице
        const resultDiv = document.getElementById('resultBox');
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = '<pre>' + JSON.stringify(result, null, 2) + '</pre>';
    } catch (err) {
        console.error(err.message);
        alert('Возникла ошибка при обработке файла.');
    }
});
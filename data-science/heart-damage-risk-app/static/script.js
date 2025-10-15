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
            const jsonTable = document.getElementById('jsonTable');
            jsonTable.style.display = 'table';

            // Получаем ссылку на tbody
            const tableBody = document.getElementById('tableBody');

            // Найдем все строки в таблице и удалим их одну за другой
            while (tableBody.firstChild) {
                tableBody.removeChild(tableBody.firstChild);
            }

            // Перебираем ключи и значения из JSON
            for (const [key, value] of Object.entries(JSON.parse(result))) {
                // Формируем новую строку таблицы
                const row = `
                    <tr>
                        <td>${key}</td>
                        <td>${value}</td>
                    </tr>
                `;
                // Добавляем строку в таблицу
                tableBody.insertAdjacentHTML('beforeend', row);
            }
            document.getElementById('errorMessage').innerText = ''; // очищаем ошибку
        }
    } catch (err) {
        document.getElementById('errorMessage').innerText = err.message || 'Возникла неизвестная ошибка.';
    }
});
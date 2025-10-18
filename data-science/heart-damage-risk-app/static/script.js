document.getElementById('uploadForm').addEventListener('submit', async function (event) {
    event.preventDefault(); // Предотвращаем стандартную отправку формы

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    const showFull = document.getElementById('show_full').checked;
    const showPercent = document.getElementById('show_percent').checked;

    const data = new FormData();
    data.append('file', file);

    const params = {
        show_full: showFull,
        show_percent: showPercent
    };

    const queryString = Object.keys(params)
        .map(key => encodeURIComponent(key) + '=' + encodeURIComponent(params[key]))
        .join('&');

    const url = `/predict?${queryString}`;


    try {
        const response = await fetch(url, {
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
            const percentCharacter = '%';
            for (const [key, originalValue] of Object.entries(JSON.parse(result))) {
                let result = originalValue;
                if (showPercent) {
                    // Если showPercent=true, добавляем знак "%" к исходному значению
                    result = result + '%';
                } else {
                    // Если showPercent=false, преобразуем "1" в "Да", а "0" в "Нет"
                    result = result === 1 ? "Да" : "Нет";
                }

                // Формируем новую строку таблицы
                const row = `
                    <tr>
                        <td>${key}</td>
                        <td>${result}</td>
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
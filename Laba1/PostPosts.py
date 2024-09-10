import requests
import json

# URL для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для нового поста
new_post = {
    "title": "Тестовый пост",
    "body": "Это тестовое тело поста",
    "userId": 1
}

# Отправляем POST-запрос
response = requests.post(url, json=new_post)

# Проверяем успешность запроса
if response.status_code == 201:  # Код 201 означает, что ресурс был создан
    # Выводим сформированный JSON
    created_post = response.json()
    print("Сформированный JSON для нового поста:")
    print(json.dumps(created_post, indent=4, ensure_ascii=False))
else:
    print("Не удалось создать пост. Код ошибки:", response.status_code)



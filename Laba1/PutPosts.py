import requests
import json

# URL для отправки PUT-запроса (замени {id} на идентификатор поста, который нужно обновить)
post_id = 1  # Идентификатор поста, который был создан ранее
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

# Данные для обновления поста
updated_post = {
    "title": "Обновлённый пост",
    "body": "Это обновлённое тело поста",
    "userId": 1,
    "id": post_id  # Указываем ID поста
}

# Отправляем PUT-запрос
response = requests.put(url, json=updated_post)

# Проверяем успешность запроса
if response.status_code == 200:
    # Выводим обновлённый JSON
    updated_post_response = response.json()
    print("Обновлённый JSON для поста:")
    print(json.dumps(updated_post_response, indent=4, ensure_ascii=False))
else:
    print("Не удалось обновить пост. Код ошибки:", response.status_code)

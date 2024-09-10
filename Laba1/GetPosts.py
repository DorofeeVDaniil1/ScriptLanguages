import requests

# URL для запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Выполняем GET-запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Парсим JSON-ответ
    posts = response.json()

    # Фильтруем посты, где id пользователя (userId) четный
    even_user_posts = [post for post in posts if post['userId'] % 2 == 0]

    # Выводим посты в консоль
    for post in even_user_posts:
        print(f"ID пользователя: {post['userId']}")
        print(f"ID поста: {post['id']}")
        print(f"Заголовок: {post['title']}")
        print(f"Тело: {post['body']}")
        print("-" * 50)
else:
    print("Не удалось получить данные. Код ошибки:", response.status_code)

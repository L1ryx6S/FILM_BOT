import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('show.db')
cursor = conn.cursor()

# Создание таблицы, если ещё не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS shows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    release_dates TEXT,
    episode_count TEXT,
    status TEXT,
    your_status TEXT
)
''')

# Полный список всех данных
full_data = [
    # Ваши предыдущие записи
    {"title": "Последний министр", "release_dates": "26 марта 2020 — настоящее время", "episode_count": "30+1 (специальный эпизод)", "status": "закончен показ 14 серий второго сезона"},
    {"title": "Проект «Анна Николаевна»", "release_dates": "26 марта 2020 — настоящее время", "episode_count": "16+1 (специальный эпизод)", "status": "закончен показ второго сезона"},
    {"title": "Беезумие", "release_dates": "22 апреля — 17 июня 2020", "episode_count": "8", "status": "закончен"},
    {"title": "Фея", "release_dates": "30 апреля 2020", "episode_count": "фильм", "status": "-"},
    {"title": "Водоворот", "release_dates": "27 июня — 7 августа 2020", "episode_count": "8", "status": "закончен"},
    {"title": "Просто представь, что мы знаем", "release_dates": "24 сентября 2020 — настоящее время", "episode_count": "4", "status": "закончен"},
    {"title": "Беспринципные", "release_dates": "15 октября 2020 — настоящее время", "episode_count": "32", "status": "закончен показ четвёртого сезона"},
    {"title": "Мажор. Фильм", "release_dates": "2 января 2021", "episode_count": "фильм", "status": "-"},
    {"title": "Настя, соберись!", "release_dates": "3 — 10 января 2021", "episode_count": "10", "status": "закончен"},
    {"title": "Авантюристы", "release_dates": "14 января — 18 февраля 2021", "episode_count": "7", "status": "закончен"},
    {"title": "Топи", "release_dates": "28 января — 25 февраля 2021", "episode_count": "7", "status": "закончен"},
    {"title": "Я не шучу", "release_dates": "4 марта — 24 марта 2021", "episode_count": "8", "status": "закончен"},
    {"title": "Майор Гром: Чумной доктор", "release_dates": "5 мая 2021", "episode_count": "фильм", "status": "-"},
    {"title": "Пищеблок", "release_dates": "19 мая 2021 — настоящее время", "episode_count": "16", "status": "закончен показ второго сезона"},
    {"title": "Хочу всё знать", "release_dates": "1 июня 2021 — 16 февраля 2023", "episode_count": "110", "status": "закончен"},
    {"title": "Зелёный мэр", "release_dates": "20 августа — 10 сентября 2021", "episode_count": "8", "status": "закончен"},
    {"title": "Пропавшая", "release_dates": "9 — 11 сентября 2021", "episode_count": "4", "status": "закончен"},
    {"title": "Старые шишки", "release_dates": "31 декабря 2021", "episode_count": "фильм", "status": "-"},
    {"title": "Этерна: Часть первая", "release_dates": "20 января 2022", "episode_count": "фильм", "status": "-"},
    {"title": "Орёл и решка. Кино", "release_dates": "14 февраля 2022", "episode_count": "фильм", "status": "-"},
    {"title": "Нулевой пациент", "release_dates": "19 мая — 23 июня 2022", "episode_count": "7+1 (специальный эпизод)", "status": "закончен"},
    {"title": "Конец света", "release_dates": "27 октября — 8 декабря 2022", "episode_count": "8", "status": "закончен"},
    {"title": "Монастырь", "release_dates": "19 ноября 2022 — настоящее время", "episode_count": "6", "status": "закончен показ первого сезона"},
    {"title": "Мажор в Сочи", "release_dates": "22 декабря 2022", "episode_count": "фильм", "status": "-"},
    {"title": "Гром: Трудное детство", "release_dates": "1 января 2023", "episode_count": "фильм", "status": "-"},
    {"title": "Фандорин. Азазель", "release_dates": "19 января — 23 февраля 2023", "episode_count": "6", "status": "закончен"},
    {"title": "Король и Шут", "release_dates": "2 марта — 13 апреля 2023; 7 августа 2023", "episode_count": "8+1 (специальный эпизод)", "status": "закончен"},
    {"title": "Кибердеревня", "release_dates": "23 сентября 2023 — настоящее время; 23 декабря 2023", "episode_count": "10 + 1 (новогодний эпизод)", "status": "закончен показ первого сезона"},
    {"title": "Объяснялкины", "release_dates": "19 октября 2023 — 12 декабря 2024", "episode_count": "9", "status": "закончен"},
    {"title": "Цикады", "release_dates": "26 октября — 14 декабря 2023", "episode_count": "8", "status": "закончен"},
    {"title": "Триггер. Фильм", "release_dates": "21 декабря 2023", "episode_count": "фильм", "status": "-"},
    {"title": "Как друзья Захара женили", "release_dates": "1 января — 6 февраля 2024", "episode_count": "17", "status": "закончен"},
    {"title": "Иные", "release_dates": "25 января — 22 февраля 2024", "episode_count": "6", "status": "закончен"},
    {"title": "Внутри убийцы", "release_dates": "22 февраля — 21 марта 2024", "episode_count": "5", "status": "закончен"},
    {"title": "На автомате", "release_dates": "5 июня — 17 июля 2024", "episode_count": "8", "status": "закончен"},
    {"title": "Майор Гром: Игра", "release_dates": "15 августа 2024", "episode_count": "фильм", "status": "-"},
    {"title": "Игры", "release_dates": "3 августа — 14 сентября 2024", "episode_count": "8", "status": "закончен"},
    {"title": "Преступление и наказание", "release_dates": "2 — 30 ноября 2024", "episode_count": "10", "status": "закончен"},
    {"title": "Красная поляна", "release_dates": "28 декабря 2024 — 25 января 2025", "episode_count": "10", "status": "закончен"},
    {"title": "Киберслав", "release_dates": "31 декабря 2024 — настоящее время", "episode_count": "8", "status": "закончен"},
    {"title": "Этерна", "release_dates": "5 июля 2025 — настоящее время", "episode_count": "6", "status": "готовится показ первого сезона"},
    {"title": "Король и Шут. Навсегда", "release_dates": "19 февраля 2026", "episode_count": "фильм", "status": "-"},
    {"title": "Фурия", "release_dates": "2026", "episode_count": "8", "status": "в производстве"},
    {"title": "Спойлер", "release_dates": "2026", "episode_count": "10", "status": "в производстве"}
]

# Вставляем все записи
for show in full_data:
    cursor.execute('''
    INSERT INTO shows (title, release_dates, episode_count, status)
    VALUES (?, ?, ?, ?)''',
    (show['title'], show['release_dates'], show['episode_count'], show['status'])
    )

# Сохраняем и закрываем соединение
conn.commit()
conn.close()

print("База данных успешно обновлена всеми записями.")
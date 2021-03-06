# Final BestHack2022 Web-development
## Команда: AXIOM
### Направление: Web Development

### Состав команды:
- Зворыгин Владимир Андреевич,
- Есис Александр Иванович,
- Дановский Илья Валентинович

### Реализованный функционал:
1. Информация по новостям
- Реализовано real-time общение клиента и сервера с помощью websockets и передача данных об актуальных новостях из базы данных.


2. Курсы валют
- На платформе реализован просмотр котировок пяти валют, вся информация передаётся в real-time. Графики котировок строятся с помощью Chart.js

3. Администрирование 
-В веб-приложении существуют пользователи двух ролей: обычный клиент и администратор. У администратора есть возможность заходить в панель админа и создавать/изменять/удалять любые данные.

4. Пользователи
- Авторизация всех пользователей происходит по логину и паролю. Все данные проходят валидацию, и не допускается регистрация пользователей с простым паролем.

5. Операции в веб-приложении
- На платформе пользователь может пополнять баланс и покупать валюту по текущему курсу

6. Сохранение истории операций
- Созданы модели операций купли-продажи валют и пополнения/снятия баланса

7. Дополнительное
- Наличие unit-тестов в Django
- Дизайн. 2 темы: светлая и тёмная


## Инструкция по запуску (Linux)

Чтобы запустить проект локально на компьютере:
1. Создайте виртуальное окружение и запустите его:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Перейдите в репозиторий с проектом:
   ```
   cd application/
   ```
3. Выполните следующие команды:
   ```
   pip3 install -r ../requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate --run-syncdb
   python3 manage.py runserver
   ```
4. Перейдите на `http://127.0.0.1:8000/`, чтобы увидеть основную страницу

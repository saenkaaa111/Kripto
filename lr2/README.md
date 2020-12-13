# Kripto
Методы аутентификации

Задание: Реализовать аутентификацию по одноразовому паролю с хешированием MD5 (можно использовать функцию из библиотеки). В таблице идентификаторов должны храниться: логин, email, хеш пароля (md5), срок действия пароля. Таблица идентификаторов должна представлять собой таблицу в реляционной БД, данные должны передаваться через SQL-запросы. При истечении срока действия пароля аутентификация не должна проходить. При аутентификации на сервере генерируется пароль для отправки на почту и в таблицу идентификаторов сохраняется его хэш. Сравниваются не пароли, а результаты MD5. 
 
Выполнение:
1. Необходимо открыть консоль и перейти в папку проекта
2. Установить зависимости командой: pip install requirements.txt
3. запустить проект и фласк 
4. Переход на главную страницу и ввод логина. Если логин введен тот, который присутсвует в базе данных, то произойтет отправка письма с паролем на указанную почту в базе данных.
5. Ввод пароля в графу и переход на страницу с приветсвтием в случае правильно введенного пароля.
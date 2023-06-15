## Тест Войт-Кампфа
#### Проверьте человек Вы или андройд
1. Чтобы запустить тест, введите в терминале:

        python3 main.py
2. Вопросы и ответы на них выводятся автоматически.
3. После это необходимо ввести следующие параметры через пробел:
    - дыхание (12-16 вдох/мин)
    - частота сердечных сокращений (60-100 удар/мин)
    - уровень покраснения (6 уровней)
    - расширение зрачка (2-8) мм
4. Если введенные данные не проходят проверку на валидность, необходимо повторить ввод данных.

5. Если сумма очков теста больше среднего значения, то Вы человек. Если меньше, то андройд.
6. Для запуска тестов pytest необходимо ввести в терминале, находясь в корневом каталоге проекта:

        pytest
7. Для создания документации нужно установить программу Sphinx и тему sphinx-rtd-theme для проекта Sphinx:
        
        pip install sphinx
        pip install sphinx-rtd-theme
8. Затем находясь в папке dosc, необходимо запустить файл make.bat:
        
        make html
9. После переходим в build/html 
    python3 http.server
10. И переходим по ссылке)
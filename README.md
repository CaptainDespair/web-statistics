# web-statistics
//Проект обретает логический конец (доразработка)//

1. Веб-приложение FullStack, на фреймворке Django. Основано на оф.документации, но полностью переработано под цели автора.
2. Приложение представляет собой:

    Опрос1:
    
        вопрос1
        
        вопрос2
        
        вопрос3
        
    Опрос2:
    
        вопрос1
        
        вопрос2
        
        вопрос3
        
    ... 
    
Ответив на вопросы, выводится статистика.

3. Функциональность приложения соответствует требованиям. Необходимо добавить кнопки "вернуться", выводить статистику в более 
надлежащем виде, а также добавить CSS. (сделано)

4. Необходимо добавить тесты, отредактировать API admin (сделано)

5. Приложение работает и будет работать только локально. 

*Регистрация, переработка синтаксиса зависит от дальнейших требований автора.

Запуск проекта: 
>python manage.py runserver

Или же используя Docker:
>docker-compose build

>docker-compose up

Вы можете скачать образ <b>captaindespair/webstatistics</b> прямо с https://hub.docker.com/ и одновременно запустить проект командой (при наличии докера на вашей ОС):
>docker run -it -p 8000:8000  captaindespair/webstatistics python3 /webstatistics/manage.py runserver 0.0.0.0:8000

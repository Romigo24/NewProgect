# Программа для игры в слова

### Начало игры
Для начала программа берет случайное слово из текстового файла и оно становится загаданным игроку.Обязательно указываем сам файл и путь к нему.
На основе именно этого файла будет строиться вся игра.


### Отображение игры
Пользовательский интерфейс минималистичен, только загаданное слво которое скрыто от глаз и сопровождается лишь подчеркиванием, буквы будут показаны в случае отгадки.
![гифка1](https://github.com/user-attachments/assets/cb2dff54-e2ce-4b9d-81a6-dadf0b7c672c)

### Пользовательский ввод
Программа просит пользователя ввести букву, при этом показывая оставшееся число попыток.Если программа не распознает введенный символ, 
она выведет сообщение с этим символом и попросит ввести снова.


### Функция для подсчёта букв
Функция определяет символы в случайном слове, и определяет результаты игры.
Игроку даётся 6 попыток.

Функция сравнивает символы загаданного слова и введенных пользователем букв.Если все символы в загаданном слове совпадают,
тогда игра завершается и выводит на экран сообщение `'You win'!`

Если пользователь угадывает букву, которая встречается несколько раз, она отображается во всех местах.
Если введенной пользователем буквы нет в слове, тогда буква добавляется в разряд неудачных догадок, и отнимается одна попытка.
Показывает пользователю угаданные буквы, сообщение о проигрыше и загаданное слово.



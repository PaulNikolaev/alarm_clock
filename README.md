# Будильник

Простое приложение на Python с графическим интерфейсом (Tkinter) для установки напоминаний и проигрывания звука в указанное время.

## Описание
Программа позволяет:
- Установить напоминание на определенное время.
- Ввести текст напоминания.
- Получить уведомление с текстом при наступлении времени.
- Остановить воспроизведение звукового сигнала.

## Установка
1. Убедитесь, что у вас установлен Python (рекомендуемая версия 3.8+).
2. Установите зависимости:
   ```sh
   pip install pygame
   ```
3. Загрузите или скопируйте файлы программы.
4. Подготовьте аудиофайл `reminder.mp3` и поместите его в папку с программой.

## Использование
1. Запустите программу:
   ```sh
   python script.py
   ```
2. Нажмите кнопку **"Установить напоминание"**.
3. Введите время в формате `чч:мм` (24-часовой формат).
4. Введите текст напоминания.
5. Когда наступит заданное время, появится уведомление и заиграет музыка.
6. Чтобы остановить звук, нажмите **"Остановить музыку"**.
7. Для выхода из программы нажмите **"Выход"**.

## Зависимости
- `tkinter` (встроен в стандартную библиотеку Python)
- `pygame` (устанавливается через pip)
- `datetime` и `time` (встроены в стандартную библиотеку Python)



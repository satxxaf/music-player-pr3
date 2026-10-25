# music-player-pr3

ПР3 по ТиВПО

Вариант 18 - «Музыкальный плеер».

## Описание
Консольная модель музыкального плеера на Python без графического интерфейса.
Функции: воспроизведение (play), пауза (pause), переключение треков (next / previous).
Переключение зациклено. Если плейлист пуст, play / next / previous выбрасывают
ValueError («Плейлист пуст»).

Тесты написаны на pytest по четырём подходам: TDD, ATDD, BDD, SDD.

## Структура
- `music_player.py` - класс MusicPlayer (логика плеера)
- `main.py` - демонстрационный запуск
- `test_player.py` - тесты (TDD, ATDD, BDD, SDD)
- `requirements.txt` - зависимости (pytest)

## Требования
- Python 3.10 или новее

## Установка и запуск
    pip install pytest
    python main.py
    python -m pytest -v

Запуск тестов отдельного подхода:

    Для TDD:
    python -m pytest -v -k "test_tdd_"

    Для ATDD:
    python -m pytest -v -k "test_atdd_"

    Для BDD:
    python -m pytest -v -k "test_bdd_"

    Для SDD:
    python -m pytest -v -k "test_sdd_"
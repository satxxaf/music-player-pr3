"""Музыкальный плеер (вариант 18).

Плеер хранит список треков, номер текущего трека и признак воспроизведения.
Переключение треков зациклено: после последнего идёт первый, перед первым - последний.
"""


class MusicPlayer:
    """Простой музыкальный плеер без графического интерфейса."""

    def __init__(self, tracks):
        """Создаёт плеер.

        tracks - список названий треков (может быть пустым).
        После создания выбран первый трек, воспроизведение выключено.
        """
        self.tracks = list(tracks)
        self.current_index = 0
        self.is_playing = False

    def _check_not_empty(self):
        """Выбрасывает ValueError, если плейлист пуст."""
        if len(self.tracks) == 0:
            raise ValueError("Плейлист пуст")

    def current_track(self):
        """Возвращает название текущего трека."""
        self._check_not_empty()
        return self.tracks[self.current_index]

    def play(self):
        """Запускает воспроизведение. Повторный вызов ничего не меняет."""
        self._check_not_empty()
        self.is_playing = True

    def pause(self):
        """Ставит воспроизведение на паузу. Если трек не играет, ничего не меняется."""
        self.is_playing = False

    def next_track(self):
        """Переключает на следующий трек (после последнего - первый).

        Состояние воспроизведения (играет / не играет) сохраняется.
        """
        self._check_not_empty()
        self.current_index = (self.current_index + 1) % len(self.tracks)

    def previous_track(self):
        """Переключает на предыдущий трек (перед первым - последний).

        Состояние воспроизведения (играет / не играет) сохраняется.
        """
        self._check_not_empty()
        self.current_index = (self.current_index - 1) % len(self.tracks)

    def status(self):
        """Возвращает строку состояния для вывода пользователю."""
        if len(self.tracks) == 0:
            return "Плейлист пуст"
        if self.is_playing:
            return "Играет: " + self.tracks[self.current_index]
        return "Остановлено: " + self.tracks[self.current_index]

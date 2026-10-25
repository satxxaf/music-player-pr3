"""Демонстрационный запуск музыкального плеера."""

from music_player import MusicPlayer


def main():
    player = MusicPlayer(["Трек1", "Трек2", "Трек3"])

    print(player.status())

    player.play()
    print("play     -> " + player.status())

    player.next_track()
    print("next     -> " + player.status())

    player.pause()
    print("pause    -> " + player.status())

    player.previous_track()
    print("previous -> " + player.status())

    empty_player = MusicPlayer([])
    try:
        empty_player.play()
    except ValueError as error:
        print("Пустой плейлист -> ошибка: " + str(error))


if __name__ == "__main__":
    main()

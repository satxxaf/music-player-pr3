"""Тесты музыкального плеера: TDD, ATDD, BDD и SDD (pytest)."""

import pytest

from music_player import MusicPlayer


def make_player():
    """Плеер с тремя треками."""
    return MusicPlayer(["Трек1", "Трек2", "Трек3"])


# TDD: юнит-тесты отдельных методов

def test_tdd_play_starts_playback():
    player = make_player()
    assert player.is_playing is False  # сразу после создания плеер не играет

    player.play()

    assert player.is_playing is True


def test_tdd_pause_stops_playback():
    player = make_player()
    player.play()

    player.pause()

    assert player.is_playing is False


def test_tdd_next_moves_to_next_track_and_wraps():
    player = make_player()

    player.next_track()
    assert player.current_track() == "Трек2"

    player.next_track()
    player.next_track()  # после последнего трека снова первый
    assert player.current_track() == "Трек1"


def test_tdd_previous_from_first_goes_to_last():
    player = make_player()

    player.previous_track()

    assert player.current_track() == "Трек3"


def test_tdd_empty_playlist_raises_value_error():
    player = MusicPlayer([])

    with pytest.raises(ValueError):
        player.play()


# ATDD: приёмочные тесты (действия пользователя, проверяем статус на экране)

def test_atdd_user_presses_play_and_first_track_starts():
    player = make_player()

    player.play()

    assert player.status() == "Играет: Трек1"


def test_atdd_user_switches_track_while_playing():
    player = make_player()

    player.play()
    player.next_track()

    assert player.status() == "Играет: Трек2"


def test_atdd_user_pauses_and_resumes_same_track():
    player = make_player()

    player.play()
    player.pause()
    assert player.status() == "Остановлено: Трек1"

    player.play()
    assert player.status() == "Играет: Трек1"


def test_atdd_user_presses_play_on_empty_playlist():
    player = MusicPlayer([])

    with pytest.raises(ValueError):
        player.play()

    assert player.status() == "Плейлист пуст"


# BDD: сценарии в формате Given-When-Then (в комментариях)

def test_bdd_scenario_play_starts_playback():
    # Given треки загружены
    player = make_player()

    # When я нажимаю "play"
    player.play()

    # Then начинается воспроизведение
    assert player.is_playing is True
    # And играет первый трек
    assert player.current_track() == "Трек1"


def test_bdd_scenario_pause_stops_playback():
    # Given трек воспроизводится
    player = make_player()
    player.play()

    # When я нажимаю "pause"
    player.pause()

    # Then воспроизведение остановлено
    assert player.is_playing is False
    # And текущий трек не меняется
    assert player.current_track() == "Трек1"


def test_bdd_scenario_next_switches_to_second_track():
    # Given воспроизводится первый трек
    player = make_player()
    player.play()

    # When я нажимаю "next"
    player.next_track()

    # Then играет второй трек
    assert player.status() == "Играет: Трек2"


def test_bdd_scenario_empty_playlist_shows_error():
    # Given плейлист пуст
    player = MusicPlayer([])

    # When я нажимаю "play"
    with pytest.raises(ValueError) as error:
        player.play()

    # Then плеер сообщает об ошибке
    assert str(error.value) == "Плейлист пуст"


# SDD: примеры из таблицы спецификаций (pytest.mark.parametrize)

def do_action(player, action):
    """Выполняет одно нажатие кнопки по её названию."""
    if action == "play":
        player.play()
    elif action == "pause":
        player.pause()
    elif action == "next":
        player.next_track()
    elif action == "previous":
        player.previous_track()


@pytest.mark.parametrize(
    "tracks, actions, expected_track, expected_playing",
    [
        (["Трек1", "Трек2", "Трек3"], [], "Трек1", False),
        (["Трек1", "Трек2", "Трек3"], ["play"], "Трек1", True),
        (["Трек1", "Трек2", "Трек3"], ["play", "pause"], "Трек1", False),
        (["Трек1", "Трек2", "Трек3"], ["play", "next"], "Трек2", True),
        (["Трек1", "Трек2", "Трек3"], ["next", "next", "next"], "Трек1", False),
    ],
)
def test_sdd_player_state_matches_specification(
    tracks, actions, expected_track, expected_playing
):
    player = MusicPlayer(tracks)

    for action in actions:
        do_action(player, action)

    assert player.current_track() == expected_track
    assert player.is_playing == expected_playing

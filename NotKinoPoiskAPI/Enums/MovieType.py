from enum import Enum


class MovieType(Enum):
    """
    Класс Enum, представляющий различные типы фильмов.

    Attributes:
        FILM (str): Represents a film.
        VIDEO (str): Represents a video.
        TV_SERIES (str): Represents a TV series.
        MINI_SERIES (str): Represents a mini-series.
        TV_SHOW (str): Represents a TV show.
    """
    FILM = "Фильм"
    VIDEO = "Видео"
    TV_SERIES = "ТВ-сериал"
    MINI_SERIES = "Мини-сериал"
    TV_SHOW = "ТВ-шоу"

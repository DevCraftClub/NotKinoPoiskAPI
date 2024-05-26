from enum import Enum


class ProductionStatus(Enum):
	FILMING = "Фильм в процессе съемок"
	PRE_PRODUCTION = "Предварительное производство"
	COMPLETED = "Завершено"
	ANNOUNCED = "Объявлено / Анонсировано"
	UNKNOWN = "Неизвестно"
	POST_PRODUCTION = "Пост-производство"

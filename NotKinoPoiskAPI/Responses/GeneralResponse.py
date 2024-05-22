from dataclasses import dataclass, field


@dataclass
class GeneralResponse:
	"""
	Объект ответа
	:param total: Количество найденных объектов
	:param items: Список найденных объектов
	"""
	total: int
	items: list = field(default_factory=list, init=False)

	def __post_init__(self):
		if self.items is None:
			self.items = list()

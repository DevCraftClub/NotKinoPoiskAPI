from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.Episode import Episode


@dataclass
class Season:
	"""
	Класс для хранения информации о сезоне.
	"""
	number: int
	"""Номер сезона"""
	episodes: List[Episode] = field(default_factory=list)
	"""Список серий"""

	def __post_init__(self):
		self.episodes = ObjectController.list_to_object(self.episodes, Episode)

	def add_episode(self, episode: Union[Episode, list[Episode]]):
		"""
		Добавление серии

		:param Union[Episode, list[Episode]] episode: Серия или список серий
		"""
		if isinstance(episode, list):
			self.episodes.extend(episode)
		else:
			self.episodes.append(episode)

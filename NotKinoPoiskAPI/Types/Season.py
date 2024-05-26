from dataclasses import dataclass, field
from typing import List, Union

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Types.Episode import Episode


@dataclass
class Season:
	number: int
	episodes: List[Episode] = field(default_factory=list)

	def __post_init__(self):
		self.episodes = ObjectController.list_to_object(self.episodes, Episode)

	def add_episode(self, episode: Union[Episode, list[Episode]]):
		if isinstance(episode, list):
			self.episodes.extend(episode)
		else:
			self.episodes.append(episode)

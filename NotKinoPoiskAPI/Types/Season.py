from dataclasses import dataclass, field
from typing import Union

from NotKinoPoiskAPI.Types.Episode import Episode


@dataclass
class Season:
	number: int
	episodes: list[Episode] = field(default_factory=list)

	def add_episode(self, episode: Union[Episode, list[Episode]]):
		if isinstance(episode, list):
			self.episodes.extend(episode)
		else:
			self.episodes.append(episode)

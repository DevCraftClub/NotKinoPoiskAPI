from typing import Union

from paprika import data, NonNull

from NotKinoPoiskAPI.Types.Episode import Episode


@data
class Season:
	number: NonNull[int]
	episodes: list[Episode] = []

	def add_episode(self, episode: Union[Episode, list[Episode]]):
		if isinstance(episode, list):
			self.episodes.extend(episode)
		else:
			self.episodes.append(episode)

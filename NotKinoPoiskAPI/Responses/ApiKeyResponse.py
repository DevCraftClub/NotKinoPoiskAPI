from dataclasses import dataclass

from NotKinoPoiskAPI.Controller.ObjectController import ObjectController
from NotKinoPoiskAPI.Enums.ApiAccountType import ApiAccountType
from NotKinoPoiskAPI.Types.ApiKeyResponseDailyQuota import ApiKeyResponseDailyQuota
from NotKinoPoiskAPI.Types.ApiKeyResponseTotalQuota import ApiKeyResponseTotalQuota


@dataclass
class ApiKeyResponse:
	"""
	Класс для хранения информации о ключе API.
	:param totalQuota: Ключ API.
	"""
	totalQuota: ApiKeyResponseTotalQuota
	dailyQuota: ApiKeyResponseDailyQuota
	accountType: ApiAccountType

	def __post_init__(self):
		if isinstance(self.totalQuota, dict):
			self.totalQuota = ObjectController.json_to_object(self.totalQuota, ApiKeyResponseTotalQuota)
		if isinstance(self.dailyQuota, dict):
			self.dailyQuota = ObjectController.json_to_object(self.dailyQuota, ApiKeyResponseDailyQuota)
		if isinstance(self.accountType, str):
			self.accountType = ObjectController.find_enum(self.accountType, ApiAccountType)

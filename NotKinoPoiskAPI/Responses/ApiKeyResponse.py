from dataclasses import dataclass

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

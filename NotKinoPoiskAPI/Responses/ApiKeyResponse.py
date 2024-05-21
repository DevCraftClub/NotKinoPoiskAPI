from paprika import NonNull, data

from NotKinoPoiskAPI.Enums.ApiAccountType import ApiAccountType
from NotKinoPoiskAPI.Types.ApiKeyResponseDailyQuota import ApiKeyResponseDailyQuota
from NotKinoPoiskAPI.Types.ApiKeyResponseTotalQuota import ApiKeyResponseTotalQuota


@data
class ApiKeyResponse:
	"""
	Класс для хранения информации о ключе API.
	:param totalQuota: Ключ API.
	"""
	totalQuota: NonNull[ApiKeyResponseTotalQuota]
	dailyQuota: NonNull[ApiKeyResponseDailyQuota]
	accountType: NonNull[ApiAccountType]

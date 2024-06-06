"""laundrify API errors"""

class LaundrifyApiException(Exception):
	"""Base exception for laundrify_aio"""

class InvalidFormat(LaundrifyApiException):
	"""AuthCode has an invalid format."""

class UnknownAuthCode(LaundrifyApiException):
	"""AuthCode could not be found."""

class ApiConnectionException(LaundrifyApiException):
	"""Could not connect the the API."""

class UnauthorizedException(LaundrifyApiException):
	"""Request is not authorized."""

class LaundrifyDeviceException(Exception):
	"""Base exception for laundrify devices."""

class DeviceConnectionException(LaundrifyDeviceException):
	"""Could not connect to the device (locally)."""

class UnsupportedFunctionException(LaundrifyDeviceException):
	"""The function is not supported by this device."""

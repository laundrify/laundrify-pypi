"""Base class for a laundrify WiFi plug."""

from asyncio import TimeoutError
from aiohttp.client_exceptions import ClientError
from .exceptions import DeviceConnectionException, UnsupportedFunctionException

class LaundrifyDevice:
    def __init__(self, machine_data: dict, laundrify_api):
        self.laundrify_api = laundrify_api

        # assign all machine_data properties to the object
        # and remove leading underscores to avoid linting errors with semi-private properties
        for key, value in machine_data.items():
            setattr(self, key.lstrip('_'), value)
    
    async def is_pingable(self):
        return False

    async def get_power(self):
        """Read current power consumption for a machine"""
        try:
            res = await self.laundrify_api.client_session.request('get', f"http://{self.internalIP}/status", timeout=3)
            res = await res.json()
            
            if self.model == "M01":
                return res["sensor"]["power"]
            elif self.model == "SU02":
                if self.firmwareVersion >= "2.0.0":
                    return res["power"]["watts"]
                else:
                    # v1.x firmware doesn't report power, so we raise an exception
                    raise UnsupportedFunctionException("Querying power measurements is not supported by this device.")
        except (TimeoutError, ClientError) as err:
            raise DeviceConnectionException(f"{type(err).__name__} while requesting http://{self.internalIP}/status") from err
        
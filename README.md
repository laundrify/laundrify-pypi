# laundrify_aio

`laundrify_aio` is a python package to communicate with the [laundrify](https://laundrify.de) API.

It has primarily been developed for the Home Assistant integration.

## Usage Example

```python
import asyncio
from laundrify_aio import LaundrifyAPI

async def main():
	# Generate a new AuthCode in the laundrify App (`Smart-Home Integration -> Home Assistant -> Integration aktivieren`)
	auth_code = '123-456'

	# exchange your auth code for a long-lived access token
	access_token = await LaundrifyAPI.exchange_auth_code(auth_code)

	# initialize a new client with the previously obtained access token
	laundrify_client = LaundrifyAPI(access_token)

	# get all machines
	machines = await laundrify_client.get_machines()

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
```

## Development/Build

To build and publish the package, run the following:

```bash
# Make a source distribution and a wheel
python3 setup.py sdist bdist_wheel

# Make sure the long description will render correctly
twine check dist/*

# (optional) upload to TestPyPI
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# upload to PyPI
twine upload dist/*
```


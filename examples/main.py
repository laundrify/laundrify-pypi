"""Example script to show how to use laundrify_aio."""

import asyncio
import json
from laundrify_aio import LaundrifyAPI

async def main():
	# Generate a new AuthCode in the laundrify App (`Smart-Home Integration -> Home Assistant -> Integration aktivieren`)
	auth_code = '999-001'

	# exchange your auth code for a long-lived access token
	access_token = await LaundrifyAPI.exchange_auth_code(auth_code)

	# initialize a new client with the previously obtained access token
	laundrify_client = LaundrifyAPI(access_token)

	# get all machines
	machines = await laundrify_client.get_machines()

	print( json.dumps(machines, indent=4) )

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
# Changelog

## v1.2.0 (2024-06-08)
 - **(!) BREAKING CHANGE:** `get_machines()` now returns a dict of `LaundrifyDevice` objects indexed by their ID
 - feat: query devices locally for latest power measurements
 - refactor: raise an error by default if response code is 400 or higher
 - refactor: replace InvalidTokenException by a general UnauthorizedException

## v1.1.2 (2022-05-27)

 - fix: use correct API endpoint

## v1.1.1 (2022-03-02)

 - feat: pass external ClientSession

## v1.1.0 (2022-03-01)

 - refactor: streamline exception naming
 - fix: raise UnauthorizedException
 - feat: implement token validation and account ID retrieval

## v1.0.0 (2022-01-26)

Initial release
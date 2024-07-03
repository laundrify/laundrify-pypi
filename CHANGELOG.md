# Changelog

## v1.2.2 (2024-07-03)
 - **⚠️ BREAKING CHANGES:** 
   - `get_machines()` now returns a list of `LaundrifyDevice` objects
   - leading underscores are removed in property names (i.e. `_id` becomes `id`)
 - feat: query devices locally for latest power measurements
 - feat: add `dist_wheel` command to build the package
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
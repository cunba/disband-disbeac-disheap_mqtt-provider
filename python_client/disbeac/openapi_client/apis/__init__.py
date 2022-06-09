
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from python_client.disbeac.openapi_client.api.disbeacs_api import DisbeacsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from api.service.disbeacs_api import DisbeacsApi
from api.service.locations_api import LocationsApi


# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from openapi_client.api.alarms_api import AlarmsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from python_client.openapi_client.api.alarms_api import AlarmsApi
from python_client.openapi_client.api.ambient_noises_api import AmbientNoisesApi
from python_client.openapi_client.api.disbands_api import DisbandsApi
from python_client.openapi_client.api.disbeacs_api import DisbeacsApi
from python_client.openapi_client.api.heart_rate_api import HeartRateApi
from python_client.openapi_client.api.humidity_api import HumidityApi
from python_client.openapi_client.api.lightnings_api import LightningsApi
from python_client.openapi_client.api.locations_disbeacs_api import LocationsDisbeacsApi
from python_client.openapi_client.api.login_api import LoginApi
from python_client.openapi_client.api.oxygen_api import OxygenApi
from python_client.openapi_client.api.pressure_api import PressureApi
from python_client.openapi_client.api.temperatures_api import TemperaturesApi
from python_client.openapi_client.api.users_api import UsersApi

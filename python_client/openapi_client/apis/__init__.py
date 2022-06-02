
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
from api.service.alarms_api import AlarmsApi
from api.service.ambient_noises_api import AmbientNoisesApi
from api.service.disbands_api import DisbandsApi
from api.service.disbeacs_api import DisbeacsApi
from api.service.heart_rate_api import HeartRateApi
from api.service.humidity_api import HumidityApi
from api.service.lightnings_api import LightningsApi
from api.service.locations_disbeacs_api import LocationsDisbeacsApi
from api.service.login_api import LoginApi
from api.service.oxygen_api import OxygenApi
from api.service.pressure_api import PressureApi
from api.service.temperatures_api import TemperaturesApi
from api.service.users_api import UsersApi

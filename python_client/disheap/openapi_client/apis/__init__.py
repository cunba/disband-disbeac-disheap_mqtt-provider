
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from python_client.disheap.openapi_client.api.disorders_api import DisordersApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from api.service.disorders_api import DisordersApi
from api.service.events_api import EventsApi
from api.service.homeworks_api import HomeworksApi
from api.service.login_api import LoginApi
from api.service.school_years_api import SchoolYearsApi
from api.service.subjects_api import SubjectsApi
from api.service.timetables_api import TimetablesApi
from api.service.users_api import UsersApi

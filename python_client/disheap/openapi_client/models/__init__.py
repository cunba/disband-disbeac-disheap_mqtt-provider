# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from python_client.disheap.openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from python_client.disheap.openapi_client.model.disorder import Disorder
from python_client.disheap.openapi_client.model.disorder_dto import DisorderDTO
from python_client.disheap.openapi_client.model.error_response import ErrorResponse
from python_client.disheap.openapi_client.model.event import Event
from python_client.disheap.openapi_client.model.event_dto import EventDTO
from python_client.disheap.openapi_client.model.handled_response import HandledResponse
from python_client.disheap.openapi_client.model.homework import Homework
from python_client.disheap.openapi_client.model.homework_dto import HomeworkDTO
from python_client.disheap.openapi_client.model.jwt_request import JwtRequest
from python_client.disheap.openapi_client.model.jwt_response import JwtResponse
from python_client.disheap.openapi_client.model.password_change_dto import PasswordChangeDTO
from python_client.disheap.openapi_client.model.school_year import SchoolYear
from python_client.disheap.openapi_client.model.school_year_dto import SchoolYearDTO
from python_client.disheap.openapi_client.model.subject import Subject
from python_client.disheap.openapi_client.model.subject_dto import SubjectDTO
from python_client.disheap.openapi_client.model.timetable import Timetable
from python_client.disheap.openapi_client.model.timetable_dto import TimetableDTO
from python_client.disheap.openapi_client.model.update_user_dto import UpdateUserDTO
from python_client.disheap.openapi_client.model.user_dto import UserDTO
from python_client.disheap.openapi_client.model.user_model import UserModel

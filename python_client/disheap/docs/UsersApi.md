# openapi_client.UsersApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{id} | Delete user
[**get_user_by_email**](UsersApi.md#get_user_by_email) | **GET** /users/emails/{email} | Get user by email
[**get_user_by_id**](UsersApi.md#get_user_by_id) | **GET** /users/{id} | Get user by ID
[**save_user**](UsersApi.md#save_user) | **POST** /users | Save user
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{id} | Update user
[**update_user_email**](UsersApi.md#update_user_email) | **PATCH** /users/{id}/email | Update user&#39;s email
[**update_user_password**](UsersApi.md#update_user_password) | **PATCH** /users/{id}/password | Update user&#39;s password


# **delete_user**
> UserModel delete_user(id)

Delete user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import users_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.user_model import UserModel
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_response = api_instance.delete_user(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |

### Return type

[**UserModel**](UserModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_email**
> UserModel get_user_by_email(email)

Get user by email

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import users_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.user_model import UserModel
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    email = "email_example" # str | User email

    # example passing only required values which don't have defaults set
    try:
        # Get user by email
        api_response = api_instance.get_user_by_email(email)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User email |

### Return type

[**UserModel**](UserModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> UserModel get_user_by_id(id)

Get user by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import users_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.user_model import UserModel
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get user by ID
        api_response = api_instance.get_user_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID |

### Return type

[**UserModel**](UserModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_user**
> UserModel save_user(user_dto)

Save user

### Example


```python
import time
import openapi_client
from api.service import users_api
from openapi_client.model.user_dto import UserDTO
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.user_model import UserModel
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    user_dto = UserDTO(
        name="name_example",
        surname="surname_example",
        birthday="birthday_example",
        is_disorder=True,
        email="email_example",
        password="password_example",
        role="role_example",
        disorder_id="disorder_id_example",
        school_year_id="school_year_id_example",
    ) # UserDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save user
        api_response = api_instance.save_user(user_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->save_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_dto** | [**UserDTO**](UserDTO.md)|  |

### Return type

[**UserModel**](UserModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> HandledResponse update_user(id, update_user_dto)

Update user

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import users_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.handled_response import HandledResponse
from openapi_client.model.update_user_dto import UpdateUserDTO
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | User id
    update_user_dto = UpdateUserDTO(
        name="name_example",
        surname="surname_example",
        birthday="birthday_example",
        email="email_example",
    ) # UpdateUserDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update user
        api_response = api_instance.update_user(id, update_user_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |
 **update_user_dto** | [**UpdateUserDTO**](UpdateUserDTO.md)|  |

### Return type

[**HandledResponse**](HandledResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_email**
> HandledResponse update_user_email(id, email)

Update user's email

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import users_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.handled_response import HandledResponse
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | User id
    email = "email_example" # str | User email

    # example passing only required values which don't have defaults set
    try:
        # Update user's email
        api_response = api_instance.update_user_email(id, email)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_user_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |
 **email** | **str**| User email |

### Return type

[**HandledResponse**](HandledResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password**
> HandledResponse update_user_password(id, password_change_dto)

Update user's password

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import users_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.password_change_dto import PasswordChangeDTO
from openapi_client.model.handled_response import HandledResponse
from pprint import pprint
# Defining the host is optional and defaults to http://63.33.86.240:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://63.33.86.240:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = "id_example" # str | User id
    password_change_dto = PasswordChangeDTO(
        password="password_example",
    ) # PasswordChangeDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update user's password
        api_response = api_instance.update_user_password(id, password_change_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->update_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |
 **password_change_dto** | [**PasswordChangeDTO**](PasswordChangeDTO.md)|  |

### Return type

[**HandledResponse**](HandledResponse.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


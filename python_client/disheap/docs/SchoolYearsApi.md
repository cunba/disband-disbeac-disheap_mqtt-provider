# openapi_client.SchoolYearsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_school_years**](SchoolYearsApi.md#delete_all_school_years) | **DELETE** /school-years | Delete all school years
[**delete_school_year**](SchoolYearsApi.md#delete_school_year) | **DELETE** /school-years/{id} | Delete school year
[**get_all_school_years**](SchoolYearsApi.md#get_all_school_years) | **GET** /school-years | Get all school years
[**get_school_year_by_id**](SchoolYearsApi.md#get_school_year_by_id) | **GET** /school-years/{id} | Get school year by ID
[**save_school_year**](SchoolYearsApi.md#save_school_year) | **POST** /school-years | Save school year
[**update_school_year**](SchoolYearsApi.md#update_school_year) | **PUT** /school-years/{id} | Update school year


# **delete_all_school_years**
> [SchoolYear] delete_all_school_years()

Delete all school years

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import school_years_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.school_year import SchoolYear
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
    api_instance = school_years_api.SchoolYearsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Delete all school years
        api_response = api_instance.delete_all_school_years()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchoolYearsApi->delete_all_school_years: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SchoolYear]**](SchoolYear.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_school_year**
> SchoolYear delete_school_year(id)

Delete school year

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import school_years_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.school_year import SchoolYear
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
    api_instance = school_years_api.SchoolYearsApi(api_client)
    id = "id_example" # str | School year ID

    # example passing only required values which don't have defaults set
    try:
        # Delete school year
        api_response = api_instance.delete_school_year(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchoolYearsApi->delete_school_year: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| School year ID |

### Return type

[**SchoolYear**](SchoolYear.md)

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
**404** | School year not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_school_years**
> [SchoolYear] get_all_school_years()

Get all school years

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import school_years_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.school_year import SchoolYear
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
    api_instance = school_years_api.SchoolYearsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all school years
        api_response = api_instance.get_all_school_years()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchoolYearsApi->get_all_school_years: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SchoolYear]**](SchoolYear.md)

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
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_year_by_id**
> SchoolYear get_school_year_by_id(id)

Get school year by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import school_years_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.school_year import SchoolYear
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
    api_instance = school_years_api.SchoolYearsApi(api_client)
    id = "id_example" # str | School year ID

    # example passing only required values which don't have defaults set
    try:
        # Get school year by ID
        api_response = api_instance.get_school_year_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchoolYearsApi->get_school_year_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| School year ID |

### Return type

[**SchoolYear**](SchoolYear.md)

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
**404** | Timetable not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_school_year**
> SchoolYear save_school_year(school_year_dto)

Save school year

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import school_years_api
from openapi_client.model.school_year_dto import SchoolYearDTO
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.school_year import SchoolYear
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
    api_instance = school_years_api.SchoolYearsApi(api_client)
    school_year_dto = SchoolYearDTO(
        name="name_example",
        study="study_example",
    ) # SchoolYearDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save school year
        api_response = api_instance.save_school_year(school_year_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchoolYearsApi->save_school_year: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_year_dto** | [**SchoolYearDTO**](SchoolYearDTO.md)|  |

### Return type

[**SchoolYear**](SchoolYear.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**400** | Bad request |  -  |
**404** | User not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_school_year**
> str update_school_year(id, school_year_dto)

Update school year

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import school_years_api
from openapi_client.model.school_year_dto import SchoolYearDTO
from openapi_client.model.error_response import ErrorResponse
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
    api_instance = school_years_api.SchoolYearsApi(api_client)
    id = "id_example" # str | School year id
    school_year_dto = SchoolYearDTO(
        name="name_example",
        study="study_example",
    ) # SchoolYearDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update school year
        api_response = api_instance.update_school_year(id, school_year_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SchoolYearsApi->update_school_year: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| School year id |
 **school_year_dto** | [**SchoolYearDTO**](SchoolYearDTO.md)|  |

### Return type

**str**

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
**404** | School year not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


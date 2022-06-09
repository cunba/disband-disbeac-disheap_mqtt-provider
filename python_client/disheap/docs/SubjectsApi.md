# openapi_client.SubjectsApi

All URIs are relative to *http://63.33.86.240:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_subject**](SubjectsApi.md#delete_subject) | **DELETE** /subjects/{id} | Delete subject
[**delete_subjects_by_school_year_id**](SubjectsApi.md#delete_subjects_by_school_year_id) | **DELETE** /subjects/school-years/{schoolYearId} | Delete subjects by school year ID
[**get_subjctes_by_school_year_id**](SubjectsApi.md#get_subjctes_by_school_year_id) | **GET** /subjects/school-years/{schoolYearId} | Get subjects by school year ID
[**get_subject_by_id**](SubjectsApi.md#get_subject_by_id) | **GET** /subjects/{id} | Get subject by ID
[**save_subject**](SubjectsApi.md#save_subject) | **POST** /subjects | Save subject
[**update_subject**](SubjectsApi.md#update_subject) | **PUT** /subjects/{id} | Update subject


# **delete_subject**
> Subject delete_subject(id)

Delete subject

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import subjects_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.subject import Subject
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
    api_instance = subjects_api.SubjectsApi(api_client)
    id = "id_example" # str | Subject ID

    # example passing only required values which don't have defaults set
    try:
        # Delete subject
        api_response = api_instance.delete_subject(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubjectsApi->delete_subject: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subject ID |

### Return type

[**Subject**](Subject.md)

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
**404** | Subject not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subjects_by_school_year_id**
> [Subject] delete_subjects_by_school_year_id(school_year_id)

Delete subjects by school year ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import subjects_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.subject import Subject
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
    api_instance = subjects_api.SubjectsApi(api_client)
    school_year_id = "schoolYearId_example" # str | School year ID

    # example passing only required values which don't have defaults set
    try:
        # Delete subjects by school year ID
        api_response = api_instance.delete_subjects_by_school_year_id(school_year_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubjectsApi->delete_subjects_by_school_year_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_year_id** | **str**| School year ID |

### Return type

[**[Subject]**](Subject.md)

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

# **get_subjctes_by_school_year_id**
> [Subject] get_subjctes_by_school_year_id(school_year_id)

Get subjects by school year ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import subjects_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.subject import Subject
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
    api_instance = subjects_api.SubjectsApi(api_client)
    school_year_id = "schoolYearId_example" # str | School year ID

    # example passing only required values which don't have defaults set
    try:
        # Get subjects by school year ID
        api_response = api_instance.get_subjctes_by_school_year_id(school_year_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubjectsApi->get_subjctes_by_school_year_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_year_id** | **str**| School year ID |

### Return type

[**[Subject]**](Subject.md)

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

# **get_subject_by_id**
> Subject get_subject_by_id(id)

Get subject by ID

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import subjects_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.subject import Subject
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
    api_instance = subjects_api.SubjectsApi(api_client)
    id = "id_example" # str | Subject ID

    # example passing only required values which don't have defaults set
    try:
        # Get subject by ID
        api_response = api_instance.get_subject_by_id(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubjectsApi->get_subject_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subject ID |

### Return type

[**Subject**](Subject.md)

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
**404** | Subject not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_subject**
> Subject save_subject(subject_dto)

Save subject

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import subjects_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.subject_dto import SubjectDTO
from openapi_client.model.subject import Subject
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
    api_instance = subjects_api.SubjectsApi(api_client)
    subject_dto = SubjectDTO(
        name="name_example",
        school_year_id="school_year_id_example",
    ) # SubjectDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Save subject
        api_response = api_instance.save_subject(subject_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubjectsApi->save_subject: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_dto** | [**SubjectDTO**](SubjectDTO.md)|  |

### Return type

[**Subject**](Subject.md)

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
**404** | School year not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subject**
> str update_subject(id, subject_dto)

Update subject

### Example

* Bearer (JWT) Authentication (bearer):

```python
import time
import openapi_client
from api.service import subjects_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.subject_dto import SubjectDTO
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
    api_instance = subjects_api.SubjectsApi(api_client)
    id = "id_example" # str | Subject id
    subject_dto = SubjectDTO(
        name="name_example",
        school_year_id="school_year_id_example",
    ) # SubjectDTO | 

    # example passing only required values which don't have defaults set
    try:
        # Update subject
        api_response = api_instance.update_subject(id, subject_dto)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SubjectsApi->update_subject: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Subject id |
 **subject_dto** | [**SubjectDTO**](SubjectDTO.md)|  |

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
**404** | Subject not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


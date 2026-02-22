# ibex_client.PlanningApplicationsApi

All URIs are relative to *https://ibex.seractech.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_post**](PlanningApplicationsApi.md#applications_post) | **POST** /applications | Search planning applications by date range and council
[**search_post**](PlanningApplicationsApi.md#search_post) | **POST** /search | Search for planning applications by location


# **applications_post**
> List[ApplicationsResponseSchema] applications_post(applications_request_schema)

Search planning applications by date range and council

Retrieve planning applications filtered by council ID, date ranges, and various application attributes. Supports keyword filtering and extensive data extensions.

### Example


```python
import ibex_client
from ibex_client.models.applications_request_schema import ApplicationsRequestSchema
from ibex_client.models.applications_response_schema import ApplicationsResponseSchema
from ibex_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ibex.seractech.co.uk
# See configuration.py for a list of all supported configuration parameters.
configuration = ibex_client.Configuration(
    host = "https://ibex.seractech.co.uk"
)


# Enter a context with an instance of the API client
with ibex_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibex_client.PlanningApplicationsApi(api_client)
    applications_request_schema = ibex_client.ApplicationsRequestSchema() # ApplicationsRequestSchema | 

    try:
        # Search planning applications by date range and council
        api_response = api_instance.applications_post(applications_request_schema)
        print("The response of PlanningApplicationsApi->applications_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanningApplicationsApi->applications_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applications_request_schema** | [**ApplicationsRequestSchema**](ApplicationsRequestSchema.md)|  | 

### Return type

[**List[ApplicationsResponseSchema]**](ApplicationsResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response, returning applications data |  -  |
**400** | Bad Request - Invalid input parameters |  -  |
**403** | Forbidden - JWT could not be authorised |  -  |
**413** | Payload Too Large - Response data exceeds size limits |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_post**
> List[SearchResponseSchema] search_post(search_request_schema)

Search for planning applications by location

Find all planning applications within a specified radius from coordinates or within a custom polygon boundary. Returns detailed application data including decisions, appeals, and project classifications.

### Example


```python
import ibex_client
from ibex_client.models.search_request_schema import SearchRequestSchema
from ibex_client.models.search_response_schema import SearchResponseSchema
from ibex_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ibex.seractech.co.uk
# See configuration.py for a list of all supported configuration parameters.
configuration = ibex_client.Configuration(
    host = "https://ibex.seractech.co.uk"
)


# Enter a context with an instance of the API client
with ibex_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ibex_client.PlanningApplicationsApi(api_client)
    search_request_schema = ibex_client.SearchRequestSchema() # SearchRequestSchema | 

    try:
        # Search for planning applications by location
        api_response = api_instance.search_post(search_request_schema)
        print("The response of PlanningApplicationsApi->search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanningApplicationsApi->search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request_schema** | [**SearchRequestSchema**](SearchRequestSchema.md)|  | 

### Return type

[**List[SearchResponseSchema]**](SearchResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response, returning search data |  -  |
**400** | Bad Request - Invalid input parameters |  -  |
**403** | Forbidden - JWT could not be authorised |  -  |
**413** | Payload Too Large - Response data exceeds size limits |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# ibex_client.PlanningStatisticsApi

All URIs are relative to *https://ibex.seractech.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats_post**](PlanningStatisticsApi.md#stats_post) | **POST** /stats | Get council planning statistics


# **stats_post**
> StatsResponseSchema stats_post(stats_request_schema)

Get council planning statistics

Retrieve council-level planning statistics and performance metrics including application counts, decision times, and approval rates.

### Example


```python
import ibex_client
from ibex_client.models.stats_request_schema import StatsRequestSchema
from ibex_client.models.stats_response_schema import StatsResponseSchema
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
    api_instance = ibex_client.PlanningStatisticsApi(api_client)
    stats_request_schema = ibex_client.StatsRequestSchema() # StatsRequestSchema | 

    try:
        # Get council planning statistics
        api_response = api_instance.stats_post(stats_request_schema)
        print("The response of PlanningStatisticsApi->stats_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlanningStatisticsApi->stats_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stats_request_schema** | [**StatsRequestSchema**](StatsRequestSchema.md)|  | 

### Return type

[**StatsResponseSchema**](StatsResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response, returning statistics data |  -  |
**400** | Bad Request - Invalid input parameters |  -  |
**403** | Forbidden - JWT could not be authorised |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# StatsRequestSchemaInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**council_id** | **int** | Council ID to get statistics for | 
**date_from** | **date** | Start date for statistics period | 
**date_to** | **date** | End date for statistics period | 

## Example

```python
from ibex_client.models.stats_request_schema_input import StatsRequestSchemaInput

# TODO update the JSON string below
json = "{}"
# create an instance of StatsRequestSchemaInput from a JSON string
stats_request_schema_input_instance = StatsRequestSchemaInput.from_json(json)
# print the JSON string representation of the object
print(StatsRequestSchemaInput.to_json())

# convert the object into a dict
stats_request_schema_input_dict = stats_request_schema_input_instance.to_dict()
# create an instance of StatsRequestSchemaInput from a dict
stats_request_schema_input_from_dict = StatsRequestSchemaInput.from_dict(stats_request_schema_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



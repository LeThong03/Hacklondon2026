# StatsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**StatsRequestSchemaInput**](StatsRequestSchemaInput.md) |  | 

## Example

```python
from ibex_client.models.stats_request_schema import StatsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StatsRequestSchema from a JSON string
stats_request_schema_instance = StatsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(StatsRequestSchema.to_json())

# convert the object into a dict
stats_request_schema_dict = stats_request_schema_instance.to_dict()
# create an instance of StatsRequestSchema from a dict
stats_request_schema_from_dict = StatsRequestSchema.from_dict(stats_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApplicationsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**ApplicationsInputSchema**](ApplicationsInputSchema.md) |  | 
**extensions** | [**ApplicationsExtensionsSchema**](ApplicationsExtensionsSchema.md) |  | [optional] 
**filters** | [**ApplicationsFiltersSchema**](ApplicationsFiltersSchema.md) |  | [optional] 

## Example

```python
from ibex_client.models.applications_request_schema import ApplicationsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsRequestSchema from a JSON string
applications_request_schema_instance = ApplicationsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ApplicationsRequestSchema.to_json())

# convert the object into a dict
applications_request_schema_dict = applications_request_schema_instance.to_dict()
# create an instance of ApplicationsRequestSchema from a dict
applications_request_schema_from_dict = ApplicationsRequestSchema.from_dict(applications_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ApplicationsInputSchema

Input parameters for searching planning applications by date range and council

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_range_type** | **str** | Type of date used for filtering. If empty, assumes any | [optional] 
**date_to** | **date** | End date of applications | 
**date_from** | **date** | Start date of applications | 
**council_id** | **List[float]** | List of council ids to search within | [optional] 
**page** | **float** | Page number - default is 1 | [optional] 
**page_size** | **float** | Number of applications per page - maximum and default is 1000 | [optional] 

## Example

```python
from ibex_client.models.applications_input_schema import ApplicationsInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsInputSchema from a JSON string
applications_input_schema_instance = ApplicationsInputSchema.from_json(json)
# print the JSON string representation of the object
print(ApplicationsInputSchema.to_json())

# convert the object into a dict
applications_input_schema_dict = applications_input_schema_instance.to_dict()
# create an instance of ApplicationsInputSchema from a dict
applications_input_schema_from_dict = ApplicationsInputSchema.from_dict(applications_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



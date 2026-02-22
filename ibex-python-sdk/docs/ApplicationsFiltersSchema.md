# ApplicationsFiltersSchema

Optional filters to narrow down application search results by type and keywords

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**normalised_application_type** | **List[str]** | filters applications on the project type - multiple types can be a comma separated list | [optional] 
**keywords** | **List[str]** | Filters applications on keywords present in the proposal | [optional] 
**normalised_decision** | **List[str]** | filters applications on the normalised decision - multiple types can be a comma separated list | [optional] 
**num_new_houses** | [**NumNewHousesFilterSchema**](NumNewHousesFilterSchema.md) |  | [optional] 

## Example

```python
from ibex_client.models.applications_filters_schema import ApplicationsFiltersSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsFiltersSchema from a JSON string
applications_filters_schema_instance = ApplicationsFiltersSchema.from_json(json)
# print the JSON string representation of the object
print(ApplicationsFiltersSchema.to_json())

# convert the object into a dict
applications_filters_schema_dict = applications_filters_schema_instance.to_dict()
# create an instance of ApplicationsFiltersSchema from a dict
applications_filters_schema_from_dict = ApplicationsFiltersSchema.from_dict(applications_filters_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



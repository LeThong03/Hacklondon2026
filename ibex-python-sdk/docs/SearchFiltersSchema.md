# SearchFiltersSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**normalised_application_type** | **List[str]** | filters applications on the project type - multiple types can be a comma separated list | [optional] 
**project_type** | **List[str]** | filters applications on the project type - multiple types can be a comma separated list | [optional] 
**normalised_decision** | **List[str]** | filters applications on the normalised decision - multiple types can be a comma separated list | [optional] 
**num_new_houses** | [**NumNewHousesFilterSchema**](NumNewHousesFilterSchema.md) |  | [optional] 

## Example

```python
from ibex_client.models.search_filters_schema import SearchFiltersSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFiltersSchema from a JSON string
search_filters_schema_instance = SearchFiltersSchema.from_json(json)
# print the JSON string representation of the object
print(SearchFiltersSchema.to_json())

# convert the object into a dict
search_filters_schema_dict = search_filters_schema_instance.to_dict()
# create an instance of SearchFiltersSchema from a dict
search_filters_schema_from_dict = SearchFiltersSchema.from_dict(search_filters_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



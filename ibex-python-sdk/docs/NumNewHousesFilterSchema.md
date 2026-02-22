# NumNewHousesFilterSchema

Filter applications by number of new houses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | Minimum number of new houses | [optional] 
**max** | **int** | Maximum number of new houses | [optional] 

## Example

```python
from ibex_client.models.num_new_houses_filter_schema import NumNewHousesFilterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NumNewHousesFilterSchema from a JSON string
num_new_houses_filter_schema_instance = NumNewHousesFilterSchema.from_json(json)
# print the JSON string representation of the object
print(NumNewHousesFilterSchema.to_json())

# convert the object into a dict
num_new_houses_filter_schema_dict = num_new_houses_filter_schema_instance.to_dict()
# create an instance of NumNewHousesFilterSchema from a dict
num_new_houses_filter_schema_from_dict = NumNewHousesFilterSchema.from_dict(num_new_houses_filter_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



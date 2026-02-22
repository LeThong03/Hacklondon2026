# DateInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_range_type** | **str** | Type of date used for filtering. Must be defined if either date_to and date_from are provided | [optional] 
**date_to** | **date** | End date of applications | [optional] 
**date_from** | **date** | Start date of applications | [optional] 

## Example

```python
from ibex_client.models.date_input_schema import DateInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DateInputSchema from a JSON string
date_input_schema_instance = DateInputSchema.from_json(json)
# print the JSON string representation of the object
print(DateInputSchema.to_json())

# convert the object into a dict
date_input_schema_dict = date_input_schema_instance.to_dict()
# create an instance of DateInputSchema from a dict
date_input_schema_from_dict = DateInputSchema.from_dict(date_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



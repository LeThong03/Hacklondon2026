# AppealsSchema

Details about planning appeals associated with applications, including outcomes and timelines

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appeal_ref** | **str** |  | [optional] 
**appeal_url** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**decision_date** | **date** |  | [optional] 
**decision** | **str** |  | [optional] 
**case_type** | **str** |  | [optional] 

## Example

```python
from ibex_client.models.appeals_schema import AppealsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsSchema from a JSON string
appeals_schema_instance = AppealsSchema.from_json(json)
# print the JSON string representation of the object
print(AppealsSchema.to_json())

# convert the object into a dict
appeals_schema_dict = appeals_schema_instance.to_dict()
# create an instance of AppealsSchema from a dict
appeals_schema_from_dict = AppealsSchema.from_dict(appeals_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



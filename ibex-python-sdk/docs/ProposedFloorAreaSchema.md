# ProposedFloorAreaSchema

Floor area data from extracted application forms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gross_internal_area_to_add_sqm** | **float** |  | [optional] 
**existing_gross_floor_area_sqm** | **float** |  | [optional] 
**proposed_gross_floor_area_sqm** | **float** |  | [optional] 
**floor_area_to_be_lost_sqm** | **float** |  | [optional] 
**floor_area_to_be_gained_sqm** | **float** |  | [optional] 

## Example

```python
from ibex_client.models.proposed_floor_area_schema import ProposedFloorAreaSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ProposedFloorAreaSchema from a JSON string
proposed_floor_area_schema_instance = ProposedFloorAreaSchema.from_json(json)
# print the JSON string representation of the object
print(ProposedFloorAreaSchema.to_json())

# convert the object into a dict
proposed_floor_area_schema_dict = proposed_floor_area_schema_instance.to_dict()
# create an instance of ProposedFloorAreaSchema from a dict
proposed_floor_area_schema_from_dict = ProposedFloorAreaSchema.from_dict(proposed_floor_area_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



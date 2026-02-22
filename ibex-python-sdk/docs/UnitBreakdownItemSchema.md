# UnitBreakdownItemSchema

Individual unit type/tenure/bedroom combination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**residential_unit_type** | **str** | Type of dwelling (e.g. House, Flat, Bungalow, Semi-Detached) | [optional] 
**tenure** | **str** | Tenure type (e.g. Market Housing, Social Rent, Shared Ownership) | [optional] 
**development_type** | **str** | Type of development (e.g. New Build, Conversion) | [optional] 
**number_of_units** | **int** | Number of units in this category | [optional] 
**bedrooms_per_unit** | **int** | Number of bedrooms per unit | [optional] 
**provider** | **str** | Housing provider (e.g. Private, Housing Association) | [optional] 
**gia_per_unit** | **float** | Gross internal area per unit in sqm | [optional] 

## Example

```python
from ibex_client.models.unit_breakdown_item_schema import UnitBreakdownItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UnitBreakdownItemSchema from a JSON string
unit_breakdown_item_schema_instance = UnitBreakdownItemSchema.from_json(json)
# print the JSON string representation of the object
print(UnitBreakdownItemSchema.to_json())

# convert the object into a dict
unit_breakdown_item_schema_dict = unit_breakdown_item_schema_instance.to_dict()
# create an instance of UnitBreakdownItemSchema from a dict
unit_breakdown_item_schema_from_dict = UnitBreakdownItemSchema.from_dict(unit_breakdown_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



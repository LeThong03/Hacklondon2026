# ProposedUnitMixSchema

Residential unit breakdown from extracted application forms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_existing_residential_units** | **int** |  | [optional] 
**total_proposed_residential_units** | **int** |  | [optional] 
**proposed_1_bed_units** | **int** |  | [optional] 
**proposed_2_bed_units** | **int** |  | [optional] 
**proposed_3_bed_units** | **int** |  | [optional] 
**proposed_4_plus_bed_units** | **int** |  | [optional] 
**affordable_housing_units** | **int** |  | [optional] 
**proposed_terraced_count** | **int** | Number of proposed terraced homes | [optional] 
**proposed_semi_count** | **int** | Number of proposed semi-detached homes | [optional] 
**proposed_detached_count** | **int** | Number of proposed detached homes | [optional] 
**proposed_flat_count** | **int** | Number of proposed flats/apartments | [optional] 
**proposed_market_units** | **int** | Number of market rate units | [optional] 
**proposed_affordable_units** | **int** | Number of affordable housing units (all types) | [optional] 
**proposed_shared_ownership_units** | **int** | Number of shared ownership units | [optional] 
**proposed_social_rent_units** | **int** | Number of social rent units | [optional] 
**units_to_be_added** | [**List[UnitBreakdownItemSchema]**](UnitBreakdownItemSchema.md) | Detailed breakdown of units to be added | [optional] 
**units_to_be_lost** | [**List[UnitBreakdownItemSchema]**](UnitBreakdownItemSchema.md) | Detailed breakdown of units to be lost/demolished | [optional] 

## Example

```python
from ibex_client.models.proposed_unit_mix_schema import ProposedUnitMixSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ProposedUnitMixSchema from a JSON string
proposed_unit_mix_schema_instance = ProposedUnitMixSchema.from_json(json)
# print the JSON string representation of the object
print(ProposedUnitMixSchema.to_json())

# convert the object into a dict
proposed_unit_mix_schema_dict = proposed_unit_mix_schema_instance.to_dict()
# create an instance of ProposedUnitMixSchema from a dict
proposed_unit_mix_schema_from_dict = ProposedUnitMixSchema.from_dict(proposed_unit_mix_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# NumberOfApplicationsSchema

Count of applications for each normalised application type within the specified period

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_material_amendment** | **int** | Number of non-material amendment applications | [optional] 
**discharge_of_conditions** | **int** | Number of discharge of conditions applications | [optional] 
**listed_building_consent** | **int** | Number of listed building consent applications | [optional] 
**advertisement_consent** | **int** | Number of advertisement consent applications | [optional] 
**householder_planning_application** | **int** | Number of householder planning applications | [optional] 
**tree_preservation_order** | **int** | Number of tree preservation order applications | [optional] 
**lawful_development** | **int** | Number of lawful development applications | [optional] 
**change_of_use** | **int** | Number of change of use applications | [optional] 
**full_planning_application** | **int** | Number of full planning applications | [optional] 
**conservation_area** | **int** | Number of conservation area applications | [optional] 
**utilities** | **int** | Number of utilities applications | [optional] 
**unknown** | **int** | Number of applications with unknown type | [optional] 
**environmental_impact** | **int** | Number of environmental impact applications | [optional] 
**section_106** | **int** | Number of section 106 applications | [optional] 
**pre_application** | **int** | Number of pre-application enquiries | [optional] 
**other** | **int** | Number of other application types | [optional] 

## Example

```python
from ibex_client.models.number_of_applications_schema import NumberOfApplicationsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NumberOfApplicationsSchema from a JSON string
number_of_applications_schema_instance = NumberOfApplicationsSchema.from_json(json)
# print the JSON string representation of the object
print(NumberOfApplicationsSchema.to_json())

# convert the object into a dict
number_of_applications_schema_dict = number_of_applications_schema_instance.to_dict()
# create an instance of NumberOfApplicationsSchema from a dict
number_of_applications_schema_from_dict = NumberOfApplicationsSchema.from_dict(number_of_applications_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# BaseApplicationsSchema

Base planning application information shared across all application response types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**council_id** | **int** |  | 
**council_name** | **str** |  | 
**planning_reference** | **str** |  | 
**url** | **str** |  | 
**proposal** | **str** |  | 
**raw_address** | **str** |  | 
**raw_application_type** | **str** |  | 
**normalised_application_type** | [**NormalisedApplicationTypeEnum**](NormalisedApplicationTypeEnum.md) |  | 
**application_date** | **date** |  | 
**decided_date** | **date** |  | 
**raw_decision** | **str** |  | 
**normalised_decision** | [**NormalisedDecisionEnum**](NormalisedDecisionEnum.md) |  | 
**geometry** | **str** |  | 

## Example

```python
from ibex_client.models.base_applications_schema import BaseApplicationsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BaseApplicationsSchema from a JSON string
base_applications_schema_instance = BaseApplicationsSchema.from_json(json)
# print the JSON string representation of the object
print(BaseApplicationsSchema.to_json())

# convert the object into a dict
base_applications_schema_dict = base_applications_schema_instance.to_dict()
# create an instance of BaseApplicationsSchema from a dict
base_applications_schema_from_dict = BaseApplicationsSchema.from_dict(base_applications_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



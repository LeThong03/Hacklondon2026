# ApplicationsExtensionsSchema

Optional data extensions to include additional information like appeals and project details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_type** | **bool** |  | [optional] 
**heading** | **bool** |  | [optional] 
**appeals** | **bool** |  | [optional] 
**num_new_houses** | **bool** | Include number of new houses from extraction classifier | [optional] 
**document_metadata** | **bool** | Include document metadata (date published, document type, description, link) | [optional] 
**proposed_unit_mix** | **bool** | Include residential unit breakdown from extracted application forms | [optional] 
**proposed_floor_area** | **bool** | Include floor area data from extracted application forms | [optional] 
**num_comments_received** | **bool** | Include number of public comments received | [optional] 

## Example

```python
from ibex_client.models.applications_extensions_schema import ApplicationsExtensionsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsExtensionsSchema from a JSON string
applications_extensions_schema_instance = ApplicationsExtensionsSchema.from_json(json)
# print the JSON string representation of the object
print(ApplicationsExtensionsSchema.to_json())

# convert the object into a dict
applications_extensions_schema_dict = applications_extensions_schema_instance.to_dict()
# create an instance of ApplicationsExtensionsSchema from a dict
applications_extensions_schema_from_dict = ApplicationsExtensionsSchema.from_dict(applications_extensions_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



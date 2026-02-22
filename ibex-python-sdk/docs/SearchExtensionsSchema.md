# SearchExtensionsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appeals** | **bool** |  | [optional] 
**centre_point** | **bool** |  | [optional] 
**heading** | **bool** |  | [optional] 
**unlimited_radius** | **bool** | toggle this as true to receive results outside of the 500m radius limit | [optional] 
**project_type** | **bool** |  | [optional] 
**num_new_houses** | **bool** | Include number of new houses from extraction classifier | [optional] 
**document_metadata** | **bool** | Include document metadata (date published, document type, description, link) | [optional] 
**proposed_unit_mix** | **bool** | Include residential unit breakdown from extracted application forms | [optional] 
**proposed_floor_area** | **bool** | Include floor area data from extracted application forms | [optional] 
**num_comments_received** | **bool** | Include number of public comments received | [optional] 

## Example

```python
from ibex_client.models.search_extensions_schema import SearchExtensionsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SearchExtensionsSchema from a JSON string
search_extensions_schema_instance = SearchExtensionsSchema.from_json(json)
# print the JSON string representation of the object
print(SearchExtensionsSchema.to_json())

# convert the object into a dict
search_extensions_schema_dict = search_extensions_schema_instance.to_dict()
# create an instance of SearchExtensionsSchema from a dict
search_extensions_schema_from_dict = SearchExtensionsSchema.from_dict(search_extensions_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



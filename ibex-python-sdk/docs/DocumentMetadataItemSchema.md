# DocumentMetadataItemSchema

Metadata about a document associated with the application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_published** | **date** |  | [optional] 
**document_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**document_link** | **str** |  | [optional] 

## Example

```python
from ibex_client.models.document_metadata_item_schema import DocumentMetadataItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentMetadataItemSchema from a JSON string
document_metadata_item_schema_instance = DocumentMetadataItemSchema.from_json(json)
# print the JSON string representation of the object
print(DocumentMetadataItemSchema.to_json())

# convert the object into a dict
document_metadata_item_schema_dict = document_metadata_item_schema_instance.to_dict()
# create an instance of DocumentMetadataItemSchema from a dict
document_metadata_item_schema_from_dict = DocumentMetadataItemSchema.from_dict(document_metadata_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SearchResponseSchema


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
**appeals** | [**List[AppealsSchema]**](AppealsSchema.md) | Appeals associated with this application (only present if appeals extension requested) | [optional] 
**project_type** | [**ProjectTypeEnum**](ProjectTypeEnum.md) |  | [optional] 
**centre_point** | **str** | Center point of the geometry (only present if centre_point extension requested) | [optional] 
**heading** | **str** |  | [optional] 
**num_new_houses** | **int** | Number of new houses from extraction classifier (only present if num_new_houses extension requested) | [optional] 
**document_metadata** | [**List[DocumentMetadataItemSchema]**](DocumentMetadataItemSchema.md) | Document metadata (only present if document_metadata extension requested) | [optional] 
**proposed_unit_mix** | [**ProposedUnitMixSchema**](ProposedUnitMixSchema.md) | Residential unit breakdown (only present if proposed_unit_mix extension requested) | [optional] 
**proposed_floor_area** | [**ProposedFloorAreaSchema**](ProposedFloorAreaSchema.md) | Floor area data (only present if proposed_floor_area extension requested) | [optional] 
**num_comments_received** | **int** | Number of public comments received (only present if num_comments_received extension requested) | [optional] 

## Example

```python
from ibex_client.models.search_response_schema import SearchResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseSchema from a JSON string
search_response_schema_instance = SearchResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SearchResponseSchema.to_json())

# convert the object into a dict
search_response_schema_dict = search_response_schema_instance.to_dict()
# create an instance of SearchResponseSchema from a dict
search_response_schema_from_dict = SearchResponseSchema.from_dict(search_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



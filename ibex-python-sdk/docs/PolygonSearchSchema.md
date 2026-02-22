# PolygonSearchSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**polygon** | [**PolygonRequestSchema**](PolygonRequestSchema.md) |  | 

## Example

```python
from ibex_client.models.polygon_search_schema import PolygonSearchSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonSearchSchema from a JSON string
polygon_search_schema_instance = PolygonSearchSchema.from_json(json)
# print the JSON string representation of the object
print(PolygonSearchSchema.to_json())

# convert the object into a dict
polygon_search_schema_dict = polygon_search_schema_instance.to_dict()
# create an instance of PolygonSearchSchema from a dict
polygon_search_schema_from_dict = PolygonSearchSchema.from_dict(polygon_search_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



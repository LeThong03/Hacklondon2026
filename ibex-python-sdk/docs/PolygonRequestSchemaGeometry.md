# PolygonRequestSchemaGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | **List[List[List[float]]]** |  | [optional] 

## Example

```python
from ibex_client.models.polygon_request_schema_geometry import PolygonRequestSchemaGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonRequestSchemaGeometry from a JSON string
polygon_request_schema_geometry_instance = PolygonRequestSchemaGeometry.from_json(json)
# print the JSON string representation of the object
print(PolygonRequestSchemaGeometry.to_json())

# convert the object into a dict
polygon_request_schema_geometry_dict = polygon_request_schema_geometry_instance.to_dict()
# create an instance of PolygonRequestSchemaGeometry from a dict
polygon_request_schema_geometry_from_dict = PolygonRequestSchemaGeometry.from_dict(polygon_request_schema_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# PolygonRequestSchema

Polygon defining the search area - in [long,lat] or [easting,northing]. Either this or 'radius' and 'coordinates' should be provided, but not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**PolygonRequestSchemaGeometry**](PolygonRequestSchemaGeometry.md) |  | [optional] 

## Example

```python
from ibex_client.models.polygon_request_schema import PolygonRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolygonRequestSchema from a JSON string
polygon_request_schema_instance = PolygonRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PolygonRequestSchema.to_json())

# convert the object into a dict
polygon_request_schema_dict = polygon_request_schema_instance.to_dict()
# create an instance of PolygonRequestSchema from a dict
polygon_request_schema_from_dict = PolygonRequestSchema.from_dict(polygon_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GeometryInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**srid** | **float** | Valid SRID of input- currently we support 4326 (lat/long) or 27700 (easting/northing) | 
**radius** | **float** | Radius of the search area in metres | 
**coordinates** | **List[float]** | Coordinates of the center of the search area - either [long,lat] or [easting,northing] | 
**polygon** | [**PolygonRequestSchema**](PolygonRequestSchema.md) |  | 

## Example

```python
from ibex_client.models.geometry_input_schema import GeometryInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GeometryInputSchema from a JSON string
geometry_input_schema_instance = GeometryInputSchema.from_json(json)
# print the JSON string representation of the object
print(GeometryInputSchema.to_json())

# convert the object into a dict
geometry_input_schema_dict = geometry_input_schema_instance.to_dict()
# create an instance of GeometryInputSchema from a dict
geometry_input_schema_from_dict = GeometryInputSchema.from_dict(geometry_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



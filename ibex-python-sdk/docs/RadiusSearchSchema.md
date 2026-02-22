# RadiusSearchSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | **float** | Radius of the search area in metres | 
**coordinates** | **List[float]** | Coordinates of the center of the search area - either [long,lat] or [easting,northing] | 

## Example

```python
from ibex_client.models.radius_search_schema import RadiusSearchSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusSearchSchema from a JSON string
radius_search_schema_instance = RadiusSearchSchema.from_json(json)
# print the JSON string representation of the object
print(RadiusSearchSchema.to_json())

# convert the object into a dict
radius_search_schema_dict = radius_search_schema_instance.to_dict()
# create an instance of RadiusSearchSchema from a dict
radius_search_schema_from_dict = RadiusSearchSchema.from_dict(radius_search_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



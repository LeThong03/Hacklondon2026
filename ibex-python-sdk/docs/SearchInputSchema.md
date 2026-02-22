# SearchInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_range_type** | **str** | Type of date used for filtering. Must be defined if either date_to and date_from are provided | [optional] 
**date_to** | **date** | End date of applications | [optional] 
**date_from** | **date** | Start date of applications | [optional] 
**srid** | **float** | Valid SRID of input- currently we support 4326 (lat/long) or 27700 (easting/northing) | 
**radius** | **float** | Radius of the search area in metres | 
**coordinates** | **List[float]** | Coordinates of the center of the search area - either [long,lat] or [easting,northing] | 
**polygon** | [**PolygonRequestSchema**](PolygonRequestSchema.md) |  | 
**page** | **float** | Page number - default is 1 | [optional] 
**page_size** | **float** | Number of applications per page - maximum and default is 5000 | [optional] 

## Example

```python
from ibex_client.models.search_input_schema import SearchInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SearchInputSchema from a JSON string
search_input_schema_instance = SearchInputSchema.from_json(json)
# print the JSON string representation of the object
print(SearchInputSchema.to_json())

# convert the object into a dict
search_input_schema_dict = search_input_schema_instance.to_dict()
# create an instance of SearchInputSchema from a dict
search_input_schema_from_dict = SearchInputSchema.from_dict(search_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



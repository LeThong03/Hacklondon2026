# AverageDecisionTimeSchema

Average decision time in days for each project type. Null values indicate insufficient data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**small_residential** | **float** | Average days to decision for small residential projects | [optional] 
**tree** | **float** | Average days to decision for tree-related applications | [optional] 
**large_residential** | **float** | Average days to decision for large residential projects | [optional] 
**home_improvement** | **float** | Average days to decision for home improvement projects | [optional] 
**mixed** | **float** | Average days to decision for mixed-use projects | [optional] 
**medium_residential** | **float** | Average days to decision for medium residential projects | [optional] 

## Example

```python
from ibex_client.models.average_decision_time_schema import AverageDecisionTimeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AverageDecisionTimeSchema from a JSON string
average_decision_time_schema_instance = AverageDecisionTimeSchema.from_json(json)
# print the JSON string representation of the object
print(AverageDecisionTimeSchema.to_json())

# convert the object into a dict
average_decision_time_schema_dict = average_decision_time_schema_instance.to_dict()
# create an instance of AverageDecisionTimeSchema from a dict
average_decision_time_schema_from_dict = AverageDecisionTimeSchema.from_dict(average_decision_time_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



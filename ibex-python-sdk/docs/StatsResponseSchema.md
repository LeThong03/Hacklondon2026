# StatsResponseSchema

Council-level planning statistics and performance metrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**council_development_activity_level** | [**CouncilDevelopmentActivityLevelEnum**](CouncilDevelopmentActivityLevelEnum.md) |  | 
**approval_rate** | **float** | Percentage of applications approved within the specified period | 
**refusal_rate** | **float** | Percentage of applications refused within the specified period | 
**average_decision_time** | [**AverageDecisionTimeSchema**](AverageDecisionTimeSchema.md) |  | 
**number_of_applications** | [**NumberOfApplicationsSchema**](NumberOfApplicationsSchema.md) |  | 
**number_of_new_homes_approved** | **int** | Total number of new homes approved within the specified period | 

## Example

```python
from ibex_client.models.stats_response_schema import StatsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of StatsResponseSchema from a JSON string
stats_response_schema_instance = StatsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(StatsResponseSchema.to_json())

# convert the object into a dict
stats_response_schema_dict = stats_response_schema_instance.to_dict()
# create an instance of StatsResponseSchema from a dict
stats_response_schema_from_dict = StatsResponseSchema.from_dict(stats_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



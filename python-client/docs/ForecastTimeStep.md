# ForecastTimeStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ForecastTimeStepData**](ForecastTimeStepData.md) |  | 
**time** | **str** | The time these forecast values are valid for. Timestamp in format YYYY-MM-DDThh:mm:ssZ (ISO 8601) | 

## Example

```python
from openapi_client.models.forecast_time_step import ForecastTimeStep

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastTimeStep from a JSON string
forecast_time_step_instance = ForecastTimeStep.from_json(json)
# print the JSON string representation of the object
print ForecastTimeStep.to_json()

# convert the object into a dict
forecast_time_step_dict = forecast_time_step_instance.to_dict()
# create an instance of ForecastTimeStep from a dict
forecast_time_step_form_dict = forecast_time_step.from_dict(forecast_time_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ForecastTimeStepDataNext6Hours

Parameters with validity times over six hours. Will not exist for all time steps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**ForecastTimePeriod**](ForecastTimePeriod.md) |  | 
**summary** | [**ForecastSummary**](ForecastSummary.md) |  | 

## Example

```python
from openapi_client.models.forecast_time_step_data_next6_hours import ForecastTimeStepDataNext6Hours

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastTimeStepDataNext6Hours from a JSON string
forecast_time_step_data_next6_hours_instance = ForecastTimeStepDataNext6Hours.from_json(json)
# print the JSON string representation of the object
print ForecastTimeStepDataNext6Hours.to_json()

# convert the object into a dict
forecast_time_step_data_next6_hours_dict = forecast_time_step_data_next6_hours_instance.to_dict()
# create an instance of ForecastTimeStepDataNext6Hours from a dict
forecast_time_step_data_next6_hours_form_dict = forecast_time_step_data_next6_hours.from_dict(forecast_time_step_data_next6_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



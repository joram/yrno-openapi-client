# ForecastTimeStepDataNext12Hours

Parameters with validity times over twelve hours. Will not exist for all time steps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**ForecastTimePeriod**](ForecastTimePeriod.md) |  | 
**summary** | [**ForecastSummary**](ForecastSummary.md) |  | 

## Example

```python
from openapi_client.models.forecast_time_step_data_next12_hours import ForecastTimeStepDataNext12Hours

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastTimeStepDataNext12Hours from a JSON string
forecast_time_step_data_next12_hours_instance = ForecastTimeStepDataNext12Hours.from_json(json)
# print the JSON string representation of the object
print ForecastTimeStepDataNext12Hours.to_json()

# convert the object into a dict
forecast_time_step_data_next12_hours_dict = forecast_time_step_data_next12_hours_instance.to_dict()
# create an instance of ForecastTimeStepDataNext12Hours from a dict
forecast_time_step_data_next12_hours_form_dict = forecast_time_step_data_next12_hours.from_dict(forecast_time_step_data_next12_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



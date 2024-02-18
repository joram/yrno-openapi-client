# ForecastTimeStepDataNext1Hours

Parameters with validity times over one hour. Will not exist for all time steps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**ForecastTimePeriod**](ForecastTimePeriod.md) |  | 
**summary** | [**ForecastSummary**](ForecastSummary.md) |  | 

## Example

```python
from openapi_client.models.forecast_time_step_data_next1_hours import ForecastTimeStepDataNext1Hours

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastTimeStepDataNext1Hours from a JSON string
forecast_time_step_data_next1_hours_instance = ForecastTimeStepDataNext1Hours.from_json(json)
# print the JSON string representation of the object
print ForecastTimeStepDataNext1Hours.to_json()

# convert the object into a dict
forecast_time_step_data_next1_hours_dict = forecast_time_step_data_next1_hours_instance.to_dict()
# create an instance of ForecastTimeStepDataNext1Hours from a dict
forecast_time_step_data_next1_hours_form_dict = forecast_time_step_data_next1_hours.from_dict(forecast_time_step_data_next1_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



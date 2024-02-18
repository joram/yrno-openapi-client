# ForecastTimeStepData

Forecast for a specific time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instant** | [**ForecastTimeStepDataInstant**](ForecastTimeStepDataInstant.md) |  | 
**next_12_hours** | [**ForecastTimeStepDataNext12Hours**](ForecastTimeStepDataNext12Hours.md) |  | [optional] 
**next_1_hours** | [**ForecastTimeStepDataNext1Hours**](ForecastTimeStepDataNext1Hours.md) |  | [optional] 
**next_6_hours** | [**ForecastTimeStepDataNext6Hours**](ForecastTimeStepDataNext6Hours.md) |  | [optional] 

## Example

```python
from openapi_client.models.forecast_time_step_data import ForecastTimeStepData

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastTimeStepData from a JSON string
forecast_time_step_data_instance = ForecastTimeStepData.from_json(json)
# print the JSON string representation of the object
print ForecastTimeStepData.to_json()

# convert the object into a dict
forecast_time_step_data_dict = forecast_time_step_data_instance.to_dict()
# create an instance of ForecastTimeStepData from a dict
forecast_time_step_data_form_dict = forecast_time_step_data.from_dict(forecast_time_step_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



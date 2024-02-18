# ForecastTimeStepDataInstant

Parameters which applies to this exact point in time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**ForecastTimeInstant**](ForecastTimeInstant.md) |  | [optional] 

## Example

```python
from openapi_client.models.forecast_time_step_data_instant import ForecastTimeStepDataInstant

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastTimeStepDataInstant from a JSON string
forecast_time_step_data_instant_instance = ForecastTimeStepDataInstant.from_json(json)
# print the JSON string representation of the object
print ForecastTimeStepDataInstant.to_json()

# convert the object into a dict
forecast_time_step_data_instant_dict = forecast_time_step_data_instant_instance.to_dict()
# create an instance of ForecastTimeStepDataInstant from a dict
forecast_time_step_data_instant_form_dict = forecast_time_step_data_instant.from_dict(forecast_time_step_data_instant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



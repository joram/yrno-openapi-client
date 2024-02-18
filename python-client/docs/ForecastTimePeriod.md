# ForecastTimePeriod

Weather parameters valid for a specified time period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_temperature_max** | **float** | Maximum air temperature in period | [optional] 
**air_temperature_min** | **float** | Minimum air temperature in period | [optional] 
**precipitation_amount** | **float** | Best estimate for amount of precipitation for this period | [optional] 
**precipitation_amount_max** | **float** | Maximum amount of precipitation for this period | [optional] 
**precipitation_amount_min** | **float** | Minimum amount of precipitation for this period | [optional] 
**probability_of_precipitation** | **float** | Probability of any precipitation coming for this period | [optional] 
**probability_of_thunder** | **float** | Probability of any thunder coming for this period | [optional] 
**ultraviolet_index_clear_sky_max** | **float** | Maximum ultraviolet index if sky is clear | [optional] 

## Example

```python
from openapi_client.models.forecast_time_period import ForecastTimePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastTimePeriod from a JSON string
forecast_time_period_instance = ForecastTimePeriod.from_json(json)
# print the JSON string representation of the object
print ForecastTimePeriod.to_json()

# convert the object into a dict
forecast_time_period_dict = forecast_time_period_instance.to_dict()
# create an instance of ForecastTimePeriod from a dict
forecast_time_period_form_dict = forecast_time_period.from_dict(forecast_time_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



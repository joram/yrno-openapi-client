# ForecastSummary

Summary of weather conditions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol_code** | [**WeatherSymbol**](WeatherSymbol.md) |  | 

## Example

```python
from openapi_client.models.forecast_summary import ForecastSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastSummary from a JSON string
forecast_summary_instance = ForecastSummary.from_json(json)
# print the JSON string representation of the object
print ForecastSummary.to_json()

# convert the object into a dict
forecast_summary_dict = forecast_summary_instance.to_dict()
# create an instance of ForecastSummary from a dict
forecast_summary_form_dict = forecast_summary.from_dict(forecast_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



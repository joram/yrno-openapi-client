# METJSONForecast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**PointGeometry**](PointGeometry.md) |  | 
**properties** | [**Forecast**](Forecast.md) |  | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.metjson_forecast import METJSONForecast

# TODO update the JSON string below
json = "{}"
# create an instance of METJSONForecast from a JSON string
metjson_forecast_instance = METJSONForecast.from_json(json)
# print the JSON string representation of the object
print METJSONForecast.to_json()

# convert the object into a dict
metjson_forecast_dict = metjson_forecast_instance.to_dict()
# create an instance of METJSONForecast from a dict
metjson_forecast_form_dict = metjson_forecast.from_dict(metjson_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



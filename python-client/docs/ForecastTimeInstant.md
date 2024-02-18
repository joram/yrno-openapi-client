# ForecastTimeInstant

Weather parameters valid for a specific point in time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_pressure_at_sea_level** | **float** | Air pressure at sea level | [optional] 
**air_temperature** | **float** | Air temperature | [optional] 
**cloud_area_fraction** | **float** | Amount of sky covered by clouds. | [optional] 
**cloud_area_fraction_high** | **float** | Amount of sky covered by clouds at high elevation. | [optional] 
**cloud_area_fraction_low** | **float** | Amount of sky covered by clouds at low elevation. | [optional] 
**cloud_area_fraction_medium** | **float** | Amount of sky covered by clouds at medium elevation. | [optional] 
**dew_point_temperature** | **float** | Dew point temperature at sea level | [optional] 
**fog_area_fraction** | **float** | Amount of area covered by fog. | [optional] 
**relative_humidity** | **float** | Amount of humidity in the air. | [optional] 
**wind_from_direction** | **float** | The direction wind is coming from, in degrees clockwise from North | [optional] 
**wind_speed** | **float** | Speed of wind | [optional] 
**wind_speed_of_gust** | **float** | Speed of wind gust | [optional] 

## Example

```python
from openapi_client.models.forecast_time_instant import ForecastTimeInstant

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastTimeInstant from a JSON string
forecast_time_instant_instance = ForecastTimeInstant.from_json(json)
# print the JSON string representation of the object
print ForecastTimeInstant.to_json()

# convert the object into a dict
forecast_time_instant_dict = forecast_time_instant_instance.to_dict()
# create an instance of ForecastTimeInstant from a dict
forecast_time_instant_form_dict = forecast_time_instant.from_dict(forecast_time_instant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



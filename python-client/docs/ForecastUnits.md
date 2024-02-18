# ForecastUnits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_pressure_at_sea_level** | **str** |  | [optional] 
**air_temperature** | **str** |  | [optional] 
**air_temperature_max** | **str** |  | [optional] 
**air_temperature_min** | **str** |  | [optional] 
**cloud_area_fraction** | **str** |  | [optional] 
**cloud_area_fraction_high** | **str** |  | [optional] 
**cloud_area_fraction_low** | **str** |  | [optional] 
**cloud_area_fraction_medium** | **str** |  | [optional] 
**dew_point_temperature** | **str** |  | [optional] 
**fog_area_fraction** | **str** |  | [optional] 
**precipitation_amount** | **str** |  | [optional] 
**precipitation_amount_max** | **str** |  | [optional] 
**precipitation_amount_min** | **str** |  | [optional] 
**probability_of_precipitation** | **str** |  | [optional] 
**probability_of_thunder** | **str** |  | [optional] 
**relative_humidity** | **str** |  | [optional] 
**ultraviolet_index_clear_sky_max** | **str** |  | [optional] 
**wind_from_direction** | **str** |  | [optional] 
**wind_speed** | **str** |  | [optional] 
**wind_speed_of_gust** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.forecast_units import ForecastUnits

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastUnits from a JSON string
forecast_units_instance = ForecastUnits.from_json(json)
# print the JSON string representation of the object
print ForecastUnits.to_json()

# convert the object into a dict
forecast_units_dict = forecast_units_instance.to_dict()
# create an instance of ForecastUnits from a dict
forecast_units_form_dict = forecast_units.from_dict(forecast_units_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



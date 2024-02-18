# ForecastMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**ForecastUnits**](ForecastUnits.md) |  | 
**updated_at** | **str** | Update time for this forecast | 

## Example

```python
from openapi_client.models.forecast_meta import ForecastMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastMeta from a JSON string
forecast_meta_instance = ForecastMeta.from_json(json)
# print the JSON string representation of the object
print ForecastMeta.to_json()

# convert the object into a dict
forecast_meta_dict = forecast_meta_instance.to_dict()
# create an instance of ForecastMeta from a dict
forecast_meta_form_dict = forecast_meta.from_dict(forecast_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



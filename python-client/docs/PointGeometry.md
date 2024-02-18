# PointGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **List[float]** | [longitude, latitude, altitude]. All numbers in decimal. | 
**type** | **str** |  | 

## Example

```python
from openapi_client.models.point_geometry import PointGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of PointGeometry from a JSON string
point_geometry_instance = PointGeometry.from_json(json)
# print the JSON string representation of the object
print PointGeometry.to_json()

# convert the object into a dict
point_geometry_dict = point_geometry_instance.to_dict()
# create an instance of PointGeometry from a dict
point_geometry_form_dict = point_geometry.from_dict(point_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



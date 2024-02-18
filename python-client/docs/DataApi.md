# openapi_client.DataApi

All URIs are relative to *http://localhost/weatherapi/locationforecast/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classic_format_get**](DataApi.md#classic_format_get) | **GET** /classic.{format} | 
[**classic_get**](DataApi.md#classic_get) | **GET** /classic | 
[**compact_format_get**](DataApi.md#compact_format_get) | **GET** /compact.{format} | 
[**compact_get**](DataApi.md#compact_get) | **GET** /compact | 
[**complete_format_get**](DataApi.md#complete_format_get) | **GET** /complete.{format} | 
[**complete_get**](DataApi.md#complete_get) | **GET** /complete | 
[**status_format_get**](DataApi.md#status_format_get) | **GET** /status.{format} | 
[**status_get**](DataApi.md#status_get) | **GET** /status | 


# **classic_format_get**
> str classic_format_get(lat, lon, format, altitude=altitude)



Weather forecast for a specified place

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/weatherapi/locationforecast/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/weatherapi/locationforecast/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataApi(api_client)
    lat = 3.4 # float | Latitude
    lon = 3.4 # float | Longitude
    format = 'format_example' # str | format code (file extension)
    altitude = 56 # int | Whole meters above sea level (optional)

    try:
        api_response = api_instance.classic_format_get(lat, lon, format, altitude=altitude)
        print("The response of DataApi->classic_format_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->classic_format_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **format** | **str**| format code (file extension) | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | 204 No Content |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | 422 Unprocessable Entity |  -  |
**429** | 429 Too Many Requests |  -  |
**500** | 500 Internal Server Error |  -  |
**502** | 502 Bad Gateway |  -  |
**503** | 503 Service Unavailable |  -  |
**504** | 504 Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **classic_get**
> str classic_get(lat, lon, altitude=altitude)



Weather forecast for a specified place

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/weatherapi/locationforecast/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/weatherapi/locationforecast/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataApi(api_client)
    lat = 3.4 # float | Latitude
    lon = 3.4 # float | Longitude
    altitude = 56 # int | Whole meters above sea level (optional)

    try:
        api_response = api_instance.classic_get(lat, lon, altitude=altitude)
        print("The response of DataApi->classic_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->classic_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | 204 No Content |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | 422 Unprocessable Entity |  -  |
**429** | 429 Too Many Requests |  -  |
**500** | 500 Internal Server Error |  -  |
**502** | 502 Bad Gateway |  -  |
**503** | 503 Service Unavailable |  -  |
**504** | 504 Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compact_format_get**
> METJSONForecast compact_format_get(lat, lon, format, altitude=altitude)



Weather forecast for a specified place

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.metjson_forecast import METJSONForecast
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/weatherapi/locationforecast/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/weatherapi/locationforecast/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataApi(api_client)
    lat = 3.4 # float | Latitude
    lon = 3.4 # float | Longitude
    format = 'format_example' # str | format code (file extension)
    altitude = 56 # int | Whole meters above sea level (optional)

    try:
        api_response = api_instance.compact_format_get(lat, lon, format, altitude=altitude)
        print("The response of DataApi->compact_format_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->compact_format_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **format** | **str**| format code (file extension) | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

[**METJSONForecast**](METJSONForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | 204 No Content |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | 422 Unprocessable Entity |  -  |
**429** | 429 Too Many Requests |  -  |
**500** | 500 Internal Server Error |  -  |
**502** | 502 Bad Gateway |  -  |
**503** | 503 Service Unavailable |  -  |
**504** | 504 Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compact_get**
> METJSONForecast compact_get(lat, lon, altitude=altitude)



Weather forecast for a specified place

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.metjson_forecast import METJSONForecast
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/weatherapi/locationforecast/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/weatherapi/locationforecast/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataApi(api_client)
    lat = 3.4 # float | Latitude
    lon = 3.4 # float | Longitude
    altitude = 56 # int | Whole meters above sea level (optional)

    try:
        api_response = api_instance.compact_get(lat, lon, altitude=altitude)
        print("The response of DataApi->compact_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->compact_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

[**METJSONForecast**](METJSONForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | 204 No Content |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | 422 Unprocessable Entity |  -  |
**429** | 429 Too Many Requests |  -  |
**500** | 500 Internal Server Error |  -  |
**502** | 502 Bad Gateway |  -  |
**503** | 503 Service Unavailable |  -  |
**504** | 504 Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_format_get**
> METJSONForecast complete_format_get(lat, lon, format, altitude=altitude)



Weather forecast for a specified place

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.metjson_forecast import METJSONForecast
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/weatherapi/locationforecast/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/weatherapi/locationforecast/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataApi(api_client)
    lat = 3.4 # float | Latitude
    lon = 3.4 # float | Longitude
    format = 'format_example' # str | format code (file extension)
    altitude = 56 # int | Whole meters above sea level (optional)

    try:
        api_response = api_instance.complete_format_get(lat, lon, format, altitude=altitude)
        print("The response of DataApi->complete_format_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->complete_format_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **format** | **str**| format code (file extension) | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

[**METJSONForecast**](METJSONForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | 204 No Content |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | 422 Unprocessable Entity |  -  |
**429** | 429 Too Many Requests |  -  |
**500** | 500 Internal Server Error |  -  |
**502** | 502 Bad Gateway |  -  |
**503** | 503 Service Unavailable |  -  |
**504** | 504 Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_get**
> METJSONForecast complete_get(lat, lon, altitude=altitude)



Weather forecast for a specified place

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.metjson_forecast import METJSONForecast
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/weatherapi/locationforecast/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/weatherapi/locationforecast/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataApi(api_client)
    lat = 3.4 # float | Latitude
    lon = 3.4 # float | Longitude
    altitude = 56 # int | Whole meters above sea level (optional)

    try:
        api_response = api_instance.complete_get(lat, lon, altitude=altitude)
        print("The response of DataApi->complete_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->complete_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

[**METJSONForecast**](METJSONForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | 204 No Content |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | 422 Unprocessable Entity |  -  |
**429** | 429 Too Many Requests |  -  |
**500** | 500 Internal Server Error |  -  |
**502** | 502 Bad Gateway |  -  |
**503** | 503 Service Unavailable |  -  |
**504** | 504 Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_format_get**
> str status_format_get(format)



Weather forecast for a specified place

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/weatherapi/locationforecast/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/weatherapi/locationforecast/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataApi(api_client)
    format = 'format_example' # str | format code (file extension)

    try:
        api_response = api_instance.status_format_get(format)
        print("The response of DataApi->status_format_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->status_format_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| format code (file extension) | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | 204 No Content |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | 422 Unprocessable Entity |  -  |
**429** | 429 Too Many Requests |  -  |
**500** | 500 Internal Server Error |  -  |
**502** | 502 Bad Gateway |  -  |
**503** | 503 Service Unavailable |  -  |
**504** | 504 Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> str status_get()



Weather forecast for a specified place

### Example


```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/weatherapi/locationforecast/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/weatherapi/locationforecast/2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DataApi(api_client)

    try:
        api_response = api_instance.status_get()
        print("The response of DataApi->status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | 204 No Content |  -  |
**400** | 400 Bad Request |  -  |
**401** | 401 Unauthorized |  -  |
**403** | 403 Forbidden |  -  |
**404** | 404 Not Found |  -  |
**422** | 422 Unprocessable Entity |  -  |
**429** | 429 Too Many Requests |  -  |
**500** | 500 Internal Server Error |  -  |
**502** | 502 Bad Gateway |  -  |
**503** | 503 Service Unavailable |  -  |
**504** | 504 Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


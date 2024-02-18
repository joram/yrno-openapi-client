# openapi_client.MetadataApi

All URIs are relative to *http://localhost/weatherapi/locationforecast/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changelog_get**](MetadataApi.md#changelog_get) | **GET** /changelog | 
[**healthz_get**](MetadataApi.md#healthz_get) | **GET** /healthz | 
[**schema_get**](MetadataApi.md#schema_get) | **GET** /schema | 


# **changelog_get**
> changelog_get()



RSS feed of changes to this product

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
    api_instance = openapi_client.MetadataApi(api_client)

    try:
        api_instance.changelog_get()
    except Exception as e:
        print("Exception when calling MetadataApi->changelog_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **healthz_get**
> healthz_get()



Check health status for product

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
    api_instance = openapi_client.MetadataApi(api_client)

    try:
        api_instance.healthz_get()
    except Exception as e:
        print("Exception when calling MetadataApi->healthz_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema_get**
> schema_get()



Schema for XML data

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
    api_instance = openapi_client.MetadataApi(api_client)

    try:
        api_instance.schema_get()
    except Exception as e:
        print("Exception when calling MetadataApi->schema_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


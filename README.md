# OpenAPI/Swagger client for yr.no API

## Usage
you should be able to run the commands: 
```bash
make build_typescript_client
make build_python_client
```
and it creates client code for the API.

### Issue
- Currently `build_typescript_client` fails with the following error:
```
Could not process model 'WeatherSymbol'.Please make sure that your schema is correct!
```

- A small issue as well is the missing host/servers variable.

either make command gets the following warning:
```
'host' (OAS 2.0) or 'servers' (OAS 3.0) not defined in the spec. Default to [http://localhost] for server URL [http://localhost/weatherapi/locationforecast/2.0]
```
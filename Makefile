build_python_client:
	mkdir -p python-client
	# build using docker from an openapi spec
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:latest generate \
		-i https://api.met.no/weatherapi/locationforecast/2.0/swagger \
		-g python \
		-o /local/python-client

build_typescript_client:
	mkdir -p typescript-client
	# build using docker from an openapi spec
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:latest generate \
		-i https://api.met.no/weatherapi/locationforecast/2.0/swagger \
		-g typescript-fetch \
		-o /local/python-client


build_all: build_python_client build_typescript_client
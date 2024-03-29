# coding: utf-8

"""
    Locationforecast

    Weather forecast for a specified place

    The version of the OpenAPI document: 2.0
    Contact: weatherapi-adm@met.no
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.forecast_time_period import ForecastTimePeriod

class TestForecastTimePeriod(unittest.TestCase):
    """ForecastTimePeriod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ForecastTimePeriod:
        """Test ForecastTimePeriod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ForecastTimePeriod`
        """
        model = ForecastTimePeriod()
        if include_optional:
            return ForecastTimePeriod(
                air_temperature_max = 17.1,
                air_temperature_min = 11.1,
                precipitation_amount = 1.71,
                precipitation_amount_max = 4.32,
                precipitation_amount_min = 4.32,
                probability_of_precipitation = 37.0,
                probability_of_thunder = 54.32,
                ultraviolet_index_clear_sky_max = 1.0
            )
        else:
            return ForecastTimePeriod(
        )
        """

    def testForecastTimePeriod(self):
        """Test ForecastTimePeriod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

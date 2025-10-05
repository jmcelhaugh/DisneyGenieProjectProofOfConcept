
import time
import openapi_client
from pprint import pprint
from openapi_client.api import destinations_api
from openapi_client.model.destinations_response import DestinationsResponse
# Defining the host is optional and defaults to https://api.themeparks.wiki/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.themeparks.wiki/v1"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = destinations_api.DestinationsApi(api_client)
    
    try:
        # Get a list of supported destinations available on the live API
        api_response = api_instance.get_destinations()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DestinationsApi->get_destinations: %s\n" % e)

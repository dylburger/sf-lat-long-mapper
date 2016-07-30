""" Class to manage a LatLong (latitude, longitude) object

    Constructor accepts (lat, long)
    Given a LatLong object, we expose class methods to get:
        San Francisco ZIP Code
        San Francisco Neighborhood

    Note that this will only work for (lat, long) data within
    the city limits of San Francisco, CA. Un-tested on geos
    outside of San Francisco.
"""
import helpers
import json
import requests

SF_DATA_HOST = "https://data.sfgov.org"
NEIGHBORHOOD_BOUNDARIES_RESOURCE_ID = "6ia5-2f8k"

GEONAMES_HOST = "http://api.geonames.org"
POSTAL_CODE_MAPPING_ENDPOINT = "findNearbyPostalCodesJSON"


class LatLong:

    # Constructor
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.socrata_api_token = helpers.read_socrata_app_token()
        self.geonames_username = helpers.read_geonames_username()

    def get_neighborhood(self):
        """ Hit the Socrata SF Data API to get a neighborhood
            for a given (lat, long)

            See more info about dataset here:

            https://data.sfgov.org/Geographic-Locations-and-Boundaries/SF-Find-Neighborhoods/pty2-tcw4
        """
        # Make a request to the SF Data Socrata API endpoint for neighborhood data
        formatted_url = SF_DATA_HOST + '/resource/' + NEIGHBORHOOD_BOUNDARIES_RESOURCE_ID + \
                        ".json?$where=intersects(the_geom,'POINT+(" + str(self.longitude) + '+' + \
                        str(self.latitude) + ")')"
        # Pass the Socrata API token
        headers = {'X-App-Token': self.socrata_api_token}
        r = requests.get(formatted_url, headers=headers)
        neighborhood = json.loads(r.content)[0]['name']

        return neighborhood

    def get_zip_code(self):
        """ Hit the GeoNames API to get a ZIP code
            for a given (lat, long)

            See more info about the API endpoint here:

            http://www.geonames.org/export/web-services.html
        """
        # Make a request to the GeoNames API for the closest ZIP
        # to the given (lat, long)
        formatted_url = GEONAMES_HOST + '/' + POSTAL_CODE_MAPPING_ENDPOINT + \
                        '?lat=' + str(self.latitude) + '&lng=' + str(self.longitude) + \
                        '&username=' + self.geonames_username
        r = requests.get(formatted_url)
        # The first postal code returned from the API is the closest in distance
        zip_code = json.loads(r.content)['postalCodes'][0]['postalCode']

        return zip_code

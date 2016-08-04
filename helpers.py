""" Set of classes and methods to help with random tasks
"""
import yaml

SOCRATA_APP_TOKEN_FILE = ".socrata_app_token"
GEONAMES_USERNAME_FILE = ".geonames_username"


def read_socrata_app_token(app_token_file=SOCRATA_APP_TOKEN_FILE):
    """ Accepts a YAML file containing the Socrata app token
        Returns the app token as a string for use in passing to
        the Socrata API

        More info about Socrata app tokens here:

        https://dev.socrata.com/docs/app-tokens.html
    """
    with open(app_token_file) as app_token_file_handle:
        # Load app token from disk, handling basic exceptions
        try:
            app_token_dict = yaml.load(app_token_file_handle)
        except yaml.YAMLError as exc:
            print("Your app token file doesn't appear to contain valid "
                  "YAML: ", exc)

        # If everything worked, return the app token
        return app_token_dict['token']


def read_geonames_username(geonames_username_file=GEONAMES_USERNAME_FILE):
    """ Accepts a YAML file containing the GeoNames username,
        required for interacting with the API
        Returns the username as a string for use in passing to
        the GeoNames API

        Sign up for a GeoNames account here:

        http://www.geonames.org/login

        Then enable access to the webservice here:

        http://www.geonames.org/manageaccount
    """
    with open(geonames_username_file) as geonames_username_file_handle:
        # Load app token from disk, handling basic exceptions
        try:
            geonames_dict = yaml.load(geonames_username_file_handle)
        except yaml.YAMLError as exc:
            print("Your username file doesn't appear to contain valid "
                  "YAML: ", exc)

        # If everything worked, return the username
        return geonames_dict['username']

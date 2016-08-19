""" Set of classes and methods to help with random tasks
"""
from __future__ import print_function
import yaml

SOCRATA_APP_TOKEN_FILE = ".socrata_app_token"
GEONAMES_USERNAME_FILE = ".geonames_username"


def read_socrata_app_token(app_token_file=SOCRATA_APP_TOKEN_FILE):
    """ Accepts a YAML file containing the Socrata app token
        Returns the app token as a string for use in passing to
        the Socrata API

        More info about Socrata app tokens here:

        https://dev.socrata.com/docs/app-tokens.html

        If the API token is malformed, we attempt to notify the
        user through a specific exception.

        If the API token file doesn't exist at all, we return
        None, which the client should handle accordingly.
    """
    # Load app token from disk, handling basic exceptions
    try:
        app_token_file_handle = open(app_token_file, 'r')
        app_token_dict = yaml.load(app_token_file_handle)
        token = app_token_dict['token']
    except yaml.YAMLError as exc:
        print("Your app token file doesn't appear to contain valid "
              "YAML: ", exc)
    except:
        # If any general exceptions occured, return None, which
        # the client should handle accordingly
        return None
    else:
        # If everything worked, return the app token
        return token
    finally:
        app_token_file_handle.close()


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
        else:
            # If everything worked, return the username
            return geonames_dict['username']


def bytes_to_str(data):
    """ In Python 3, we need a function to decode binary to Unicode
    """
    if isinstance(data, bytes):
        value = data.decode('utf-8')
    else:
        value = data
    return value

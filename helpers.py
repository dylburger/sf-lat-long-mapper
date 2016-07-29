""" Set of classes and methods to help with random tasks
"""
import yaml

SOCRATA_APP_TOKEN_FILE = ".socrata_app_token"


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
            print "Your app token file doesn't appear to contain valid " \
                   "YAML: ", exc

        # If everything worked, return the app token
        return app_token_dict['token']

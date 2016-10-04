# San Francisco Lat Long Mapper

This repo contains Python code for retrieving a San Francisco neighborhood, and ZIP code, given
(lat, long) coordinate pairs. It has been tested on Python versions 3.5.1 and 2.7.10.

The neighborhood data comes from the City of San Francisco, through the [SF OpenData Socrata API service](https://data.sfgov.org).

ZIP codes come from [GeoNames](http://www.geonames.org/), a free geo database service.

**Important Notes**

* This API is meant to work for San Francisco (lat, long) coordinates only. It will fail to work on 
coordinate pairs outside of the San Francisco city limits.
* This code interacts with two APIs to get its data - Socrata and GeoNames. As with any third party API,
please be mindful of the number of requests you make against their services.
* This code is new, and fragile. Please report any bugs / requests through Github.

## Signing up for the services, storing credentials for use

### Socrata API

The Socrata API doesn't _require_ credentials, but without an [App Token](https://dev.socrata.com/docs/app-tokens.html),
you'll quickly be rate limited. As the page notes, please do not make an unlimited number of requests to the API. 
Rate limit yourself to a reasonable degree, or reach out to their team to discuss your use case.

Once you've [registered your application](https://dev.socrata.com/register) and received an App Token, store the token
in a file in this repository named _.socrata\_app\_token_ in the following format:

    token: <token>

The _.gitignore_ file in this repo already contains the name of this file, removing it from tracking in git.
**Please never commit your App Token to git. There are automated agents scraping Github and related git hosting 
services for API tokens of many varieties. They can and will steal your credentials.**

### GeoNames API

GeoNames require that you pass only your username in API requests. First, [create a GeoNames account](http://www.geonames.org/login),
then enable the web service (API) near the bottom of [this page](http://www.geonames.org/manageaccount).

After you've created a username and enabled API access, store the username in a file named _.geonames\_username_ in the following format:

    username: <username>

Again, the _.gitignore_ file contains the name of this file. **Do not commit this file to version control**.

## Usage

The code to get a neighborhood, or ZIP, given a (lat, long) pair, is very simple. Here's an 
example from within iPython:

    In [1]: from LatLong import LatLong

    In [2]: testLatLong = LatLong(latitude=37.7755316484116, longitude=-122.437512719511)

    In [3]: testLatLong
    Out[3]: LatLong(37.7755316484116,-122.437512719511)

    In [4]: testLatLong.get_neighborhood()
    Out[4]: u'Alamo Square'

    In [5]: testLatLong.get_zip_code()
    Out[5]: u'94117'

Try it on your own San Francisco (lat, long) coordinates and let us know if you have any trouble! The code is still very new, 
and doesn't handle common error conditions, so it's likely bugs are lingering.

import urllib
import urllib.request as something
import urllib.error as er
import json
import oauth2
import pprint as pp

# Please assign following values with the credentials found in your Yelp account, 
# you can find them here: http://www.yelp.com/developers/manage_api_keys 
CONSUMER_KEY = 'g0-BEXAw3LW1r2XCD6g-3A'
CONSUMER_SECRET = 'r19gHp74hpDid2MfLvWHrJjPXt8'
TOKEN = '_jTS-vWVbAHyr2MXJNKvZpmU3TwDrJBV'
TOKEN_SECRET = 'cVyromwIWLXW5E7d-1A-vz8AL6s'

# yelp_req() function description:
# The input is a url link, which you use to make request to Yelp API, and the 
# return of this function is a JSON object or error messages, including the information 
# returned from Yelp API.
# For example, when url is 'http://api.yelp.com/v2/search?term=food&location=San+Francisco'
# yelp_req(url) will return a JSON object from the Search API

def yelp_req(url, offset):
    """ Pass in a url that follows the format of Yelp API,
        and this function will return either a JSON object or error messages.
    """
    # Create URL
    # source: http://letstalkdata.com/2014/02/how-to-use-the-yelp-api-in-python/
    params = {}
    params["term"] = "restaurants"
    params["location"] = "San Francisco, CA"
    params["offset"] = offset
    params["sort"] = "2"
    oauth_request = oauth2.Request('GET', url, parameters=params)
    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    conn = something.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read().decode('utf-8'))
    finally:
        conn.close()

    return response

#################################################################################
# Your code goes here

def main():
    # Create a dictionary of the results
    url = 'https://api.yelp.com/v2/search?'
    final_dict = {}
    offset_list = [0, 20]
    for i in offset_list:
        # source: http://stackoverflow.com/questions/5607551/python-urlencode-querystring
        results = yelp_req(url, offset=i)
        restaurant_names = results['businesses']
        # Add the restaurants and their counts to the dictionary.
        for i in range(len(restaurant_names)):
            restaurant = restaurant_names[i]['name']
            review_count = restaurant_names[i]['review_count']
            final_dict[restaurant] = review_count
    # Create a sorted list of restaurants by count.
    # source: http://pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
    # source: http://bytesizebio.net/2013/04/03/stupid-python-tricks-3296-sorting-a-dictionary-by-its-values/
    sorted_list = sorted(final_dict, key=final_dict.__getitem__, reverse=True)
    # print(sorted_list)
    # Open a file to write the results
    with open('restaurants2.anna.cho.txt', 'w') as f:
        for restaurant in sorted_list:
            f.write('{},{}\n'.format(restaurant, final_dict[restaurant]))

if __name__ == '__main__':
    main()

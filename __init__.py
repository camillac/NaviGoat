#! /usr/bin/python3

from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)
app.secret_key = 'coses'

client_id = 'XHm5ttlMqrgKLihC4Si0sw'
api_key = 'hgVUt5D7hnJnDcNLUf-SsJelvvRVjbJRR0msc1LJZImetqDxKOKHGf7HY4ojuKSQE1_\
XAenVCmAN8msHDASMGVkfkkaIgH423Z4Gn_bsA3lVk_zxAYygxtsxYBpcXnYx'
headers = {'Authorization': 'Bearer %s' % api_key}


@app.route('/')
def main():
    return render_template('welcome.html')

@app.route('/search')
def search():
    search_term = request.args['search']
    location = request.args['location']

    params = {}

    if (location == ''):
        # If location not given, default to New York City
        location = 'New York City'

        # Try geolocation
        if (request.args['geo_lat'] != '' or request.args['geo_lng'] != ''):
            geo_lat = request.args['geo_lat']
            geo_lng = request.args['geo_lng']
            params = {'term': search_term,
                     'latitude': geo_lat,
                     'longitude': geo_lng,
                     'radius': 10000,
                     'rating': 5}
            location = "you"
        else:
            # if not, search near 'New York City'
            params = {'term': search_term,
                     'location': location,
                     'radius': 10000,
                     'rating': 5}

    # Use given location
    else:
        params = {'term': search_term,
                 'location': location,
                 'radius': 10000,
                 'rating': 5}


    url = 'https://api.yelp.com/v3/businesses/search'

    req = requests.get(url, params=params, headers=headers)

    #turned request object to text
    text = req.text

    # turns req txt into a dictionary for easy access
    req_dict = json.loads(text)

    # # use if not centered around user
    # region = {'latitude': req_dict['region']['center']['latitude'],
    #          'longitude': req_dict['region']['center']['longitude']}


    # return str(text)
    return render_template('search.html', search = search_term, loc=location, req = req_dict)



if __name__ == '__main__':
    app.debug = True
    app.run()

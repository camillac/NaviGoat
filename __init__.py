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

    # Use geolocation instead
        if (request.args['latitude'] != '' and request.args['longitude'] != ''):
            lat = request.args['latitude']
            long = request.args['longitude']
            params = {'term': search_term,
                     'latitude': lat,
                     'longitude': long}
            location = "you"
    # Use given location
    else:
        params = {'term': search_term,
                 'location': location}


    url = 'https://api.yelp.com/v3/businesses/search'

    req = requests.get(url, params=params, headers=headers)

    #turned request object to text
    text = req.text

    # turns req txt into a dictionary for easy access
    req_dict = json.loads(text)

    names = []
    businesses = req_dict['businesses']
    for b in businesses:
        names.append(b['name'])

    # return str(text)
    return render_template('search.html', search = search_term, loc=location, req = req_dict)

# @app.route('/location')
# def location():
#


if __name__ == '__main__':
    app.debug = True
    app.run()

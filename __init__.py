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


@app.route('/submit')
def submit():
    search_term = request.args['search']
    #
    # url = 'https://api.yelp.com/v3/businesses/search'
    #
    # params = {'term': search_term,
    #          'location': 'New York City'}
    #
    # req = requests.get(url, params=params, headers=headers)
    #
    # #turned request object to text
    # text = req.text
    #
    # # turns req txt into a dictionary for easy access
    # req_dict = json.loads(text)
    #
    # names = [];
    # businesses = req_dict['businesses']
    # for b in businesses:
    #     names.append(b['name'])

    # return str(names)
    return render_template('home.html', search = search_term)



if __name__ == '__main__':
    app.debug = True
    app.run()
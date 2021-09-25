import json

from flask import Flask
app = Flask(__name__)
_countryList = [{'name': 'Canada', 'id': 1, 'continent':'North America'}, {'name': 'Sri Lanka', 'id': 88, 'continent':'Asia'}, {'name': 'India', 'id': 99, 'continent':'Asia'}, {'name': 'USA', 'id': 1, 'continent':'America'}, {'name': 'Japan', 'id': 11, 'continent':'Asia'},
                {'name': 'German', 'id': 15, 'continent':'Europe'}, {'name': 'Russia', 'id': 66, 'continent':'Asia'}, {'name': 'Nepal', 'id': 145, 'continent':'Asia'}]

@app.route('/')
def country_list():
   global _countryList
   _countryListJson = json.dumps(_countryList)
   return _countryListJson
app.add_url_rule('/getcl', 'getcl', country_list)
app.add_url_rule('/countries', 'countries', country_list)

@app.route('/country/<int:coid>')
def country_by_id(coid):
   global _countryList
   _nameList = [{'name': 'None', 'id':coid}]
   for c in _countryList:
      if c.get("id") == coid:
         _nameList = c

   _countryListJson = json.dumps(_nameList)
   return _countryListJson

@app.route('/client')
def client():
  return 'Hello World!'

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=int("5000"), debug=False)#debug = True

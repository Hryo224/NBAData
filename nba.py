from methods import methods as m
from constants import BASE_DATA_URL as base
import json
import urllib.request
import pprint


def get_data(url):
    r = urllib.request.urlopen(url)
    data =  json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    return data

def call_function(function, param1="", param2=""):
    func_obj = ""
    for key in m:
        if m.get(key).get('function') == function:
            func_obj = m.get(key)
    url = base + func_obj.get('endpoint')
    if param1 != "":
        url = url % param
    return get_data(url)

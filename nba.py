from methods import methods as m
from constants import BASE_DATA_URL as base
import json
import urllib.request
import pprint


def get_data(url):
    r = urllib.request.urlopen(url)
    data =  json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    return data

def nba_data(function, *args):
    func_obj = ""
    for key in m:
        if m.get(key).get('function') == function:
            func_obj = m.get(key)
    if func_obj == "":
        return "Function not supported"
    url = base + func_obj.get('endpoint')
    if len(args) > 0:
        url = url % tuple(args)
    print(url)
    return get_data(url)


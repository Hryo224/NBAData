from NBAData.data_methods import methods as m
from NBAData.constants import BASE_DATA_URL as base
import json
import urllib.request

def get_data(url):
    r = urllib.request.urlopen(url)
    data =  json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    return data

def print_method_list():
    for key in m:
        print(m.get(key).get('function'))

def get_method_list():
    methods = []
    for key in m:
        methods.append(m.get(key).get('function'))
    return methods

def get_params(function):
    for key in m:
        if m.get(key).get('function') == function:
            return m.get(key).get('params')

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
    return get_data(url)


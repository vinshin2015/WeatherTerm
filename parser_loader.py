import re
import os
import inspect

#First, the _get_parser_list function is executed and returns a list of all files located in weatherterm/parsers;
# it will filter the files based on the rules of the parser described previously.
# After returning a list of files, it is time to import the module.
# This is done by the _import_parsers function, which first imports the weatherterm.parsers module and makes use of the inspect package in the standard library to find the parser classes within the module.
#The inspect.getmembers function returns a list of tuples where the first item is a key representing a property in the module, and the second item is the value, which can be of any type. In our scenario, we are interested in a property with a key ending with parser and with the value of type class.
#Assuming that we already have a parser in place in the weatherterm/parsers  directory, the value returned by the inspect.getmembers(_modules) will look something like this:
#[('WeatherComParser',
#<class 'weatherterm.parsers.weather_com_parser.WeatherComParser'>),
# ...]

def _get_parser_list(dirname):
    files = [f.replace('.py', '')
             for f in os.listdir(dirname)
             if not f.startswith('__')]
    return files


def _import_parsers(parserfiles):
    m = re.compile('.+parser$', re.I)

    _modules = __import__('weatherterm.parsers',
                          globals(),
                          locals(),
                          parserfiles,
                          0)
    _parsers = [(k,v)for k, v in inspect.getmembers(_modules)
                if inspect.ismodule(v) and m.match(k)]

    _classes = dict()

    for k, v in _parsers:
        _classes.update({k: v for k, v in inspect.getmembers(v)
                         if inspect.isclass(v) and m.match(k)})
    return _classes

def load(dirname):
    parserfiles = _get_parser_list(dirname)
    return _import_parsers(parserfiles)


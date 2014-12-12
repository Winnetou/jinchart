#!/usr/bin/env python
# -*- coding: utf-8 -*-

from markupsafe import Markup

#from jinja2 import environmentfilter

def turn_to_well_formatted_dict(data):
    '''
    : Returns dict with the following keys:
    : 'id': use Python id for unique html id
    : 'labels': these will be labels in the chart, value: list of strings
    : 'options': for passing general options for the chart, value: dict
    : one or more dicts with data, key: data label (by default dataset_<number>)
    :
    '''
    default_options = {}
    #if no options provided

    new_data = {}
    #let us be romantic
    if isinstance(data, dict):
        new_data['id'] = data.get('id', str(id(data)))#html id - unique!
    if isinstance(data, (list, tuple))):
        #it can be a list od dicts
        if all(isinstance(element, dict) for element in data):
            pass
        #else: it a list where one element is a list of labels, another data
        if all(isinstance(element, (list, tuple)) for element in data):
            pass
        raise TypeError("Invalid argument: must be a dict, a list or a tuple.")
    else:
        raise TypeError("Invalid argument: must be a dict, a list or a tuple.")

    return new_data

def render_common_pie(data):
    ''' Renders common part of pie/doughnut and polar charts
    '''
    data = turn_to_well_formatted_pie_dict(data)


def render_common(data):
    ''' Renders common part of bar, line, radar charts
    '''

    data = turn_to_well_formatted_dict(data)

    begin = '''
    <canvas id="%(id)s" width="?EY?" height="?EY?">  </canvas>
    <script>
    var ctx_%(id)s = document.getElementById("%(id)s").getContext("2d");
    var data = {
    labels: %(labels)s,
    datasets: ['''%(data)

    common = begin
    middle = \
            '''                {
                                label: "%(label)s",
                                fillColor: "%(labels)s",
                                strokeColor: "%(labels)s",
                                highlightFill: "%(labels)s",
                                highlightStroke: "%(labels)s",
                                data: %(dataset)s
                            },'''
    for evry_dict in data:
        if not evry_dict.has_key('labels')\
        and not evry_dict.has_key('options'):
            common += middle%(evry_dict)
    end = '''
                ]
            }

    var chart_%(id)s = new Chart(ctx_%(id)s)'''%(data)
    common += end
    return common

#@environmentfilter
def barchart(data):
    ''' Generates BarChart from a dict with minimum two keys:
    labels and dataset.'''

    common = render_common(data)
    end = '''.Bar(data);
    </script>'''
    #TODO variable name! unique
    result = common+end
    return Markup(result)

#@environmentfilter
def linechart(data):
    ''' '''

    common = render_common(data)
    end = '''..Line(data, options);
    </script>'''
    #TODO variable name! unique
    result = common+end
    return Markup(result)

#@environmentfilter
def piechart(data):
    ''' '''

    common = render_common(data)
    raise TypeError("Common part for pie, doughnut and polararea is different than for bar and linechart")
    end = '''
                ]
            }

    var myNewChart = new Chart(ctx).Bar(data);
    </script>'''
    #TODO variable name! unique
    result = common+end
    return Markup(result)

#@environmentfilter
def radarchart(data):
    ''' '''

    common = render_common(data)
    end = '''
                ]
            }

    var myNewChart = new Chart(ctx).Radar(data, options);
    </script>'''
    #TODO variable name! unique
    result = common+end
    return Markup(result)

#@environmentfilter
def polararea(data):
    ''' '''

    common = render_common(data)
    end = '''
                ]
            }

    var myNewChart = new Chart(ctx).PolarArea(data);
    </script>'''
    #TODO variable name! unique
    result = common+end
    return Markup(result)


#@environmentfilter
def doughnut(data):
    ''' '''

    common = render_common(data)
    end = '''
                ]
            }

    var myNewChart = new Chart(ctx).Doughnut(data);
    </script>'''
    #TODO variable name! unique
    result = common+end
    return Markup(result)

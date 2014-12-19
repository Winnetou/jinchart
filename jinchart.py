#!/usr/bin/env python
# -*- coding: utf-8 -*-

from markupsafe import Markup

from random import choice

from datetime import datetime, date, time

from defaultchartoptions import ( barchart_default_options,\
                                  linechart_default_options,\
                                  radarchart_default_options,\
                                  polararea_default_options,\
                                  doughnut_default_options,\
                                  piechart_default_options,)



def get_random_rgba_color_set():
    ''' Returns random rgba color set
    as the aptly given name suggests'''

    #TODO: avoid white otherwise user will see jackshit
    a,b,c = str(choice(range(257))), str(choice(range(257))), str(choice(range(257))),
    colorset = ["rgba(%s,%s,%s,%s)"%(a,b,c,d) for d in ['0.1', '0.3', '0.5', '0.7', '0.9', '1']]

    return colorset


def turn_to_well_formatted_dict(data, default_options):
    '''
    : Perfroms unification of data passed to the
    : barchart, linechart or radarchart Filter
    : for easy string formatting
    : Returns a dict with the following keys:
    : 'id':  if not provided, uses Python's object id for unique html id,
    : 'labels': these will be labels in the chart, value: list of either
    : strings, datetime objects, date or time objects
    : 'options': for passing general options for the chart, value: dict
    : one or more dicts with data, key: data label
    : (by default dataset_<number>), value: dict with fillColor, strokeColor etc
    :
    '''
    if isinstance(data, (list, tuple)) and all(isinstance(element, (list, tuple)) for element in data):
        # all tuples - we guess what's data, what's labels, and we change from this:
        # [["jan", "feb", "mar"], [20, 30, 10]]
        # to this:
        # {"labels":["jan", "feb", "mar"], "dataset_1": {'label': "dataset_1", data': [20, 30, 10]} }
        tmp_data = {}
        # so that id is that of data, not the tmp_data created
        tmp_data['id'] = str(id(data))
        number = 1
        for element in data: #for every list
            if all(isinstance(chunk, (basestring, datetime, date, time)) for chunk in element):
                # we can safely assume that these are labels
                tmp_data['labels'] = element
            else:
                dataset_name = 'dataset_' + str(number)#dataset has no name - we give it one
                tmp_data[dataset_name] = {'label': dataset_name , 'data' : element}
                number +=1
        data = tmp_data
        #By now data is a dict
    if isinstance(data, dict):
        new_data = {} # po cholere tworzyc nowy slownik?
        # FIRST - we need the id
        new_data['id'] = data.get('id', str(id(data)))
        #NEXT - options
        new_data['options'] = {}
        if data.has_key('options'):
            if not isinstance(data['options'], dict):
                raise TypeError('Options must be a dict')# TODO - try better, eh?
                # a man may want to provide just few options, not all
                #then take which option there is, use default for those not provided
            new_data['options'] = data['options']
            for key in default_options.keys():
                if not key in data['options'].keys():
                    new_data['options'][key] = default_options[key]
        else:
            new_data['options'] = default_options

        #if there is any other key in data, it must be a dict with values:
        for key in data.keys():
            if key not in ('id','options', 'labels'):#we assume its data
                # this may be 'roses': [1,2,3] or 'roses':{'data':[1,2,3], 'color':"#A986D"}
                if isinstance(data[key], dict):
                    new_data[key] = {}

                    new_data[key]['data'] = data[key].get('data', [0,])
                    new_data[key]['label'] = data[key].get('label', key)
                    a, b, c, d, e, f = get_random_rgba_color_set()
                    #color values used by all three
                    new_data[key]['fillColor'] = data[key].get('fillColor', d)
                    new_data[key]['strokeColor'] = data[key].get('strokeColor', e)
                    #two colour values used just by barchart
                    new_data[key]['highlightFill'] = data[key].get('highlightFill', c)
                    new_data[key]['highlightStroke'] = data[key].get('highlightStroke', f)
                    #four colour values used just both by radarchart and linechart
                    new_data[key]['pointColor'] = data[key].get('pointColor', b)
                    new_data[key]['pointStrokeColor'] = data[key].get('pointStrokeColor', a)
                    new_data[key]['pointHighlightFill'] = data[key].get('pointHighlightFill', a)
                    new_data[key]['pointHighlightStroke'] = data[key].get('pointHighlightStroke', b)
                elif isinstance(data[key], (list, tuple)):
                    new_data[key] = {}
                    new_data[key]['data'] = data[key]
                    new_data[key]['label'] = key
                    a, b, c, d, e, f = get_random_rgba_color_set()
                    #color values used by all three
                    new_data[key]['fillColor'] = d
                    new_data[key]['strokeColor'] = e
                    #two colour values used just by barchart
                    new_data[key]['highlightFill'] = c
                    new_data[key]['highlightStroke'] = f
                    #four colour values used just both by radarchart and linechart
                    new_data[key]['pointColor'] = b
                    new_data[key]['pointStrokeColor'] = a
                    new_data[key]['pointHighlightFill'] = a
                    new_data[key]['pointHighlightStroke'] = b
                else:
                    raise TypeError('Got some invalid arguments: expected dict, list or tuple')
        # now labels - not to forget turning date/time into str
        if data.has_key('labels'):
            new_data['labels'] = [str(labl) for labl in data['labels']]
        else:
            new_data['labels'] = []
            default_empty_labels = ["" for w in the_longest_data_array]
            # we deal with labels at the end cause now we know the longest data - and if labels shorter, we fill the gap with whitespace
            #if max(len(data_elmnt['data']) for data_elmnt in [k for k in new_data.keys() if k not in ('id','options', 'labels')]])# if labels shorter than the shortest data array, fill with whitespace
            #TODO!

    else:
        raise TypeError("Invalid argument: must be a dict, a list or a tuple.")
    return new_data


def turn_to_well_formatted_pie_dict(data, default_options):
    '''
    : Perfroms unification of data passed to the
    : piechart, doughnutchart or polararea Filter
    : for easy string formatting
    : Returns dict with the following keys:
    : 'id': use Python id for unique html id
    : 'options': for passing general options for the chart, value: dict
    : one or more nested dicts with data, key: data label
    : value: dict with value, label, color, highlight
    '''

    if isinstance(data, (list, tuple)) and all(isinstance(element, dict) for element in data):
        tmp_data = {}
        tmp_data['id'] = str(id(data))
        # so that id is that of data, not the tmp_data created
        for dictionary in data:
            # it may be like [{"green": 20},{'red':10}]
            # turn into {"green":{'value' : 20}, 'red':{'value':10}}
            if len(dictionary.items())==1:
                tmp_data[dictionary.items()[0][0]] = {'value': dictionary.items()[0][1], 'label': dictionary.items()[0][0]}
            else:
                # or like {"value": 20, 'label':"roses" "color":"#F7464A"}
                # turn into {'roses':{"green":20}}
                tmp_data[dictionary.get('label', 'label_'+str(id(dictionary)))] = dictionary
        data = tmp_data
        # HERE DATA IS ALREADY A DICT
    if isinstance(data, dict):
        new_data = {}
        new_data['id'] = data.get('id', str(id(data)))
        new_data['options'] = {}
        if data.has_key('options'):
            if not isinstance(data['options'], dict):
                raise TypeError('Options must be a dict')# TODO - try better, eh?
                # a man may want to provide just few options, not all
                #then take which option there is, use default for those not provided
            new_data['options'] = data['options']
            for key in default_options.keys():
                if not key in data['options'].keys():
                    new_data['options'][key] = default_options[key]
        else:
            new_data['options'] = default_options
        for key in data.keys():
            if key not in ('id','options'):#we assume its data
                color_set = get_random_rgba_color_set()
                light, dark  = color_set[2], color_set[-2]
                #but it may be a dict or a int/float eg {'green:10} or {'green':{'value':20}}
                if isinstance(data[key], dict):
                    new_data[key] = {}
                    new_data[key]['value'] = data[key].get('value', 0)
                    new_data[key]['label'] = data[key].get('label', key)
                    new_data[key]['color'] = data[key].get('color', dark)
                    new_data[key]['highlight'] = data[key].get('highlight', light)
                elif isinstance(data[key], (int, float)):
                    #thats for {'green:10}
                    new_data[key] = {}
                    new_data[key]['value'] = data[key]
                    new_data[key]['label'] = key
                    new_data[key]['color'] = dark
                    new_data[key]['highlight'] = light
                else:
                    raise TypeError('Got some invalid arguments: expected dict, list or tuple')

    else:
        raise TypeError("Invalid argument: must be a dict, a list of dicts or a tuple of dicts.")

    return new_data

def render_common(data):
    '''
    Renders common part of bar, line, radar charts
    '''
    beginning = {}
    # pie and doughnut have the same beggining, remaining 3 - another
    beginning['Doughnut'] = beginning['Pie'] =  beginning['PolarArea'] = \
    '''<canvas id="%(id)s" width="400px" height="400px">  </canvas>
       <script>
       var ctx_%(id)s = document.getElementById("%(id)s").getContext("2d");
       var data = [
         '''

    beginning['Bar'] = beginning['Line'] = beginning['Radar'] = \
    '''<canvas id="%(id)s" width="400px" height="400px">  </canvas>
       <script>
       var ctx_%(id)s = document.getElementById("%(id)s").getContext("2d");
       var data = {
       labels: %(labels)s,
       datasets: ['''

    middle = {}
    middle['Doughnut'] = middle['Pie'] = middle['PolarArea'] = \
    '''
                {
                    value: %(value)s,
                    color: "%(color)s",
                    highlight: "%(highlight)s",
                    label: "%(label)s",
               },'''


    middle['Bar'] = \
    '''
                    {
                        label: "%(label)s",
                        fillColor: "%(fillColor)s",
                        strokeColor: "%(strokeColor)s",
                        highlightFill: "%(highlightFill)s",
                        highlightStroke: "%(highlightStroke)s",
                        data: %(data)s
                    },'''
    middle['Line'] = middle['Radar'] = \
    '''
                    {
                        label: "%(label)s",
                        fillColor: "%(fillColor)s",
                        strokeColor: "%(strokeColor)s",
                        pointColor: "%(pointColor)s",
                        pointStrokeColor: "%(pointStrokeColor)s",
                        pointHighlightFill: "%(pointHighlightFill)s",
                        pointHighlightStroke: "%(pointHighlightStroke)s",
                        data: %(data)s
                    },'''
    options ={}
    options['Doughnut'] = options['Pie'] = options['PolarArea'] = \
    '''
            ]
    var options = {'''
    options['Bar'] = options['Line'] = options['Radar'] = \
    '''
                ]
            };
    var options = {'''



    begin = beginning[data['charttype']]%(data)
    #data['charttype'] tells you which chart type are we rendering
    # hence you know which key to pick from the ``beginning`` dict
    # defined above

    for key in data.keys():
        if key not in ('id','labels', 'options', 'charttype'):
            begin += middle[data['charttype']]%(data[key])
            # explain: data['charttype'] tells you which chart are we rendering
            # hence you know which key to pick from the ``middle`` dict
            # defined above
    optionsection = options[data['charttype']]

    for key in data['options'].keys():#iteritems - 2to3 issue
        if key != 'legendTemplate':
            #TODO FIXME - escape legendTemplate
            optionsection += "\n" + "    "+key+" : "+data['options'][key]+","

    end = \
    '''
        }

       var chart_%(id)s = new Chart(ctx_%(id)s).%(charttype)s(data, options);
       </script>'''%(data)
    begin += optionsection
    begin += end
    return begin

def barchart(data):
    '''
    : Filter for generating Charts.js BarChart
    : accepts following arguments:
    : - a dict - eg. {'labels':["Jan", "Feb", "March"], 'data':[100,200,150]}
    : - a list of dicts - eg. [{'labels':["Jan", "Feb", "March"]}, {'totalvalue':[100,200,150]} ]
    : - a list or a tuple - eg. [["Jan", "Feb", "March"], [100,200,150]]
    '''

    data = turn_to_well_formatted_dict(data, barchart_default_options)
    data['charttype'] = 'Bar'
    result = render_common(data)
    return Markup(result)

def linechart(data):
    '''
    : Filter for generating Charts.js LineChart
    : accepts following arguments:
    : - a dict - eg. {'labels':["Jan", "Feb", "March"], 'data':[100,200,150]}
    : - a list of dicts - eg. [{'labels':["Jan", "Feb", "March"]}, {'totalvalue':[100,200,150]} ]
    : - a list or a tuple - eg. [["Jan", "Feb", "March"], [100,200,150]]
    '''

    data = turn_to_well_formatted_dict(data, linechart_default_options)
    data['charttype'] = 'Line'
    result = render_common(data)
    return Markup(result)

def radarchart(data):
    ''' '''

    data = turn_to_well_formatted_dict(data, radarchart_default_options)
    data['charttype'] = 'Radar'
    result = render_common(data)
    return Markup(result)

def piechart(data):
    ''' '''
    print 'data from piechart', data
    data = turn_to_well_formatted_pie_dict(data, piechart_default_options)
    data['charttype'] = 'Pie'
    result = render_common(data)
    return Markup(result)

def doughnutchart(data):
    ''' '''

    data = turn_to_well_formatted_pie_dict(data, doughnut_default_options)
    data['charttype'] = 'Doughnut'
    result = render_common(data)
    return Markup(result)

def polararea(data):
    ''' '''

    data = turn_to_well_formatted_pie_dict(data, polararea_default_options)
    data['charttype'] = 'PolarArea'
    result = render_common(data)
    return Markup(result)

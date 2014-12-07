#!/usr/bin/env python
# -*- coding: utf-8 -*-

from markupsafe import Markup

#from jinja2 import environmentfilter


#@environmentfilter
def BarChart(data):
    ''' Generates BarChart from a dict with minimum two keys:
    labels and dataset.'''

    result = '''
    <canvas id="myChart" width="400" height="400">  </canvas>
    <script>
    var ctx = document.getElementById("myChart").getContext("2d");
    var data = {
    labels: %(labels)s,
    datasets: [
                    {
                        label: "My First dataset",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: %(dataset)s
                    },

                ]
            }

    var myNewChart = new Chart(ctx).Bar(data);
    </script>
    '''%(data)

    return Markup(result)
#@environmentfilter
def LineChart(data):
    ''' '''
    result = '''
    '''
    return Markup(result)

#@environmentfilter
def PieChart(data):
    ''' '''

    result = '''
    '''

    return Markup(result)


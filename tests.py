#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import re

from random import choice

from datetime import date, time, datetime

from jinchart import (barchart, linechart, radarchart,\
                      piechart, doughnutchart,
                      turn_to_well_formatted_dict,
                      turn_to_well_formatted_pie_dict)

class JinChartTest(unittest.TestCase):

    def setUp(self):
        raise AssertionError("All the fucking colours  have been severely fucked up - you get random, there's no way to test'em!")


    def tearDown(self):
        print "bye bye!"

### UNITTESTS FOR GUT-FUNCTIONS ###
    def test_passing_dict_to_turn_to_well_formatted_dict(self):
        ''' test that dicts passed to turn_to_well_formatted_dict
        will be what it shall be
        '''
        example = {'mydata':[1,2,3] 'labels':['jan', 'feb', 'mar'], 'options':{'segmentStrokeWidth' : 2}}
        result = turn_to_well_formatted_dict(example)
        assert isinstance(result, dict)
        assert len(result.keys())>=4
        assert result.has_key('id')
        assert result['id'] == str(id(example))
        assert result.has_key('options')
        assert result['options']['segmentStrokeWidth'] == 2
        assert len(result['options'].keys()) >=9
        assert result.has_key('labels')
        assert result['labels'] == ['jan', 'feb', 'mar']
        assert result.has_key('mydata')
        assert result['mydata'] == [1,2,3]
        raise AssertionError("Not finished!")

    def test_passing_a_list_of_dicts_to_turn_to_well_formatted_dict(self):
        ''' test that dicts passed to turn_to_well_formatted_dict
        will be what it shall be
        '''
        example = [{'mydata':[1,2,3]} ,{'labels':['jan', 'feb', 'mar']}, {'options':{'segmentStrokeWidth' : 2}}]
        result = turn_to_well_formatted_dict(example)
        assert isinstance(result, dict)
        assert len(result.keys())>=4
        assert result.has_key('id')
        assert result['id'] == str(id(example))
        assert result.has_key('options')
        assert result['options']['segmentStrokeWidth'] == 2
        assert len(result['options'].keys()) >=9
        assert result.has_key('labels')
        assert result['labels'] == ['jan', 'feb', 'mar']
        assert result.has_key('mydata')
        assert result['mydata'] == [1,2,3]
        raise AssertionError("Not finished!")

    def test_passing_a_list_to_turn_to_well_formatted_dict(self):
        ''' test that dicts passed to turn_to_well_formatted_dict
        will be what it shall be
        '''
        example = [[1,2,3], ['jan', 'feb', 'mar']]
        result = turn_to_well_formatted_dict(example)
        assert isinstance(result, dict)
        assert len(result.keys())>=4
        assert result.has_key('id')
        assert result['id'] == str(id(example))
        assert result.has_key('options')
        assert result['options']['segmentStrokeWidth'] == 2
        assert len(result['options'].keys()) >=9
        assert result.has_key('labels')
        assert result['labels'] == ['jan', 'feb', 'mar']
        assert result.has_key('mydata')
        assert result['mydata'] == [1,2,3]
        raise AssertionError("Not finished!")

    def test_turn_to_well_formatted_pie_dict(data):
        raise AssertionError("Not finished!")


### BARCHART, LINECHART AND RADARCHART #####

 #BARCHART SECTION#

    def test_barchart_with_dict(self):
        ''' pass a dict to barchart - when you don't want to
        play with rgba colours or anything, just quick chart with defaults'''
        #TODO
        dict1 = {"id":"unique_id_no_12", "labels":["A", "B", "C"], "dataset":[1,2,3]}
        dict2 = {"labels":["A", "B", "C"], "dataset_1":[1,2,3], "dataset_2":[4,5,6]}
        result1 = barchart(dict1)
        result2 = barchart(dict2)
        # that unique id issue should go to separate test, shouldn't it?
        expected1= '''
        <canvas id="unique_id_no_12" width="400" height="400">  </canvas>
        <script>
        var ctx_unique_id_no_12 = document.getElementById("unique_id_no_12").getContext("2d");
        var data = {
        labels: ["A", "B", "C"],
        datasets: [
                    {
                        label: "dataset",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3]
                    },
                ]
            };

        var chart_unique_id_no_12 = new Chart(ctx_unique_id_no_12).Bar(data, options);
        </script>
        '''
        the_id = str(id(dict2))
        expected2 = '''
        <canvas id="'''+the_id+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id+''' = document.getElementById("'''+the_id+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C"],
        datasets: [
                    {
                        label: "dataset_1",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3]
                    },
                    {
                        label: "dataset_2",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [4,5,6]
                    },
                ]
            };

        var chart_'''+the_id+''' = new Chart(ctx_'''+the_id+''').Bar(data, options);
        </script>
        '''
        # first some specific asserts
        #assert labels are taken from dict keys
        label_1 = re.findall('label: ".*?",', expected1)
        label_2 = re.findall('label: ".*?",', expected2)
        assert dict1.has_hey(label_1[0][8:-1])
        assert dict2.has_hey(label_2[0][8:-1])
        # now general assert
        assert result1 == expected1
        assert result2 == expected2

    def test_barchart_with_list_of_dicts(self):
        ''' pass a dict to barchart for the deluxe edition -
        all colours, stroke and other options under your control'''
        #TODO
        dict1 = [{"labels":["A", "B", "C"]}, {"dataset":[1,2,3], "fillColor": "rgba(200,404,200,0.2)" }]
        dict2 = [{"labels":["A", "B", "C"]}, {"roses":[1,2,3], "fillColor": "rgba(200,404,200,0.2)",},\
         {"violas":[4,5,6], "fillColor": "rgba(222,404,200,0.2)", 'strokeColor': "rgba(151,187,205,0.8)",}]
        result1 = barchart(dict1)
        result2 = barchart(dict2)
        the_id_1 = str(id(dict1))
        the_id_2 = str(id(dict2))
        expected1= '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C"],
        datasets: [
                    {
                        label: "dataset",
                        fillColor: "rgba(200,404,200,0.2)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Bar(data, options);
        </script>
        '''# TODO: that can't be var chart_ - together with id, these vars must be unique
        expected2= '''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C"],
        datasets: [
                    {
                        label: "roses",
                        fillColor: "rgba(200,404,200,0.2)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [4,5,6]
                    },
                    {
                        label: "violas",
                        fillColor: "rgba(222,404,200,0.2)",
                        strokeColor: "rgba(151,187,205,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3]
                    },
                ]
            };

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Bar(data, options);
        </script>
        '''
        # now assert that
        assert result1 == expected1
        assert result2 == expected2
        assert result2.index('roses')>result2.index('violas')
        # there must be some predictable order in passing datasets,
        #preferably, alphabetically, hence rose go before violas
        label_1 = re.findall('label: ".*?",', expected1)
        label_2 = re.findall('label: ".*?",', expected2)
        assert dict1.has_hey(label_1[0][8:-1])
        assert dict1.has_hey(label_1[0][8:-1])
        #raise AssertionError("Not finished yet!")

    def test_barchart_with_list_or_tuple(self):
        ''' pass a list or a tuple to barchart'''
        #TODO
        some_list = [['label_1','label_2','label_3','label_4'], [1,2,3,4], [5,6,4,2]]
        some_tuple = (('label_1','label_2','label_3','label_4'), (1,2,3,4), (5,6,4,2))
        result1 = barchart(some_list)
        result2 = barchart(some_tuple)
        the_id_1 = str(id(some_list))
        the_id_2 = str(id(some_tuple))
        expected1= '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ['label_1','label_2','label_3','label_4'],
        datasets: [
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,4]
                    },
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [5,6,4,2]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Bar(data, options);
        </script>
        '''
        expected2 = '''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = {
        labels: ['label_1','label_2','label_3','label_4'],
        datasets: [
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,4]
                    },
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [5,6,4,2]
                    },
                ]
            };

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Bar(data, options);
        </script>
        '''
        assert result1 == expected1
        assert result2 == expected2

## LINECHART SECTION ##

    def test_linechart_with_dict(self):
        ''' pass a dict to linechart'''

        dict1 = {"labels":["A", "B", "C"], "dataset":[1,2,3]}
        the_id_1 = str(id(dict1))
        result1 = linechart(dict1)
        expected1 = '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C",],
        datasets: [
                    {
                        label: "dataset",
                        fillColor: "rgba(220,220,220,0.2)",
                        strokeColor: "rgba(220,220,220,1)",
                        pointColor: "rgba(220,220,220,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(220,220,220,1)",
                        data: [1, 2, 3]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Line(data, options);
        </script>
        '''
        assert result1 == expected1
        #raise AssertionError("Not finished yet!")

    def test_linechart_with_list_of_dicts(self):
        ''' pass a list containing dicts to linechart for full options'''
        #isn't that completely redundant?

        dict1 = [{"labels":["A", "B", "C"]}, {"dataset":[1,2,3], "fillColor": "rgba(200,404,200,0.2)" }]
        the_id_1 = str(id(dict1))
        result1 = linechart(dict1)
        expected1 = '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C",],
        datasets: [
                    {
                        label: "dataset",
                        fillColor: "rgba(200,404,200,0.2)",
                        strokeColor: "rgba(220,220,220,1)",
                        pointColor: "rgba(220,220,220,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(220,220,220,1)",
                        data: [1, 2, 3]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Line(data, options);
        </script>
        '''
        assert result1 == expected1
        #raise AssertionError("Not finished yet!")

    def test_linechart_with_list_or_tuple(self):
        ''' pass a list or a tuple to linechart'''

        some_list = [['label_1','label_2','label_3','label_4'], [1,2,3,4], [5,6,4,2]]
        some_tuple = (('label_1','label_2','label_3','label_4'), (1,2,3,4), (5,6,4,2))

        result1 = linechart(some_list)
        result2 = linechart(some_tuple)

        the_id_1 = str(id(some_list))
        the_id_2 = str(id(some_tuple))

        expected1= '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ['label_1','label_2','label_3','label_4'],
        datasets: [
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,4]
                    },
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [5,6,4,2]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Line(data, options);
        </script>
        '''
        expected2 = '''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = {
        labels: ['label_1','label_2','label_3','label_4'],
        datasets: [
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,4]
                    },
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [5,6,4,2]
                    },
                ]
            };

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Line(data, options);
        </script>
        '''
        assert result1 == expected1
        assert result2 == expected2


## RADARCHART SECTION ##

    def test_radarchart_with_dict(self):
        ''' pass a dict to radarchartchart'''

        dict1 = {"labels":["A", "B", "C"], "dataset":[1,2,3]}
        the_id_1 = str(id(dict1))
        result1 = polararea(dict1)
        expected1 = '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C",],
        datasets: [
                    {
                        label: "dataset",
                        fillColor: "rgba(220,220,220,0.2)",
                        strokeColor: "rgba(220,220,220,1)",
                        pointColor: "rgba(220,220,220,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(220,220,220,1)",
                        data: [1, 2, 3]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Radar(data, options);
        </script>
        '''
        assert result1 == expected1
        #raise AssertionError("Not finished yet!")

    def test_radarchart_with_list_of_dicts(self):
        ''' pass a list containing dicts to radarchart for full options'''
        #isn't that completely redundant?

        dict1 = [{"labels":["A", "B", "C"]}, {"dataset":[1,2,3], "fillColor": "rgba(200,404,200,0.2)" }]
        the_id_1 = str(id(dict1))
        result1 = radarchart(dict1)
        expected1 = '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C",],
        datasets: [
                    {
                        label: "dataset",
                        fillColor: "rgba(200,404,200,0.2)",
                        strokeColor: "rgba(220,220,220,1)",
                        pointColor: "rgba(220,220,220,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(220,220,220,1)",
                        data: [1, 2, 3]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Radar(data, options);
        </script>
        '''
        assert result1 == expected1
        #raise AssertionError("Not finished yet!")

    def test_radarchart_with_list_or_tuple(self):
        ''' pass a list or a tuple to radarchart'''

        some_list = [['label_1','label_2','label_3','label_4'], [1,2,3,4], [5,6,4,2]]
        some_tuple = (('label_1','label_2','label_3','label_4'), (1,2,3,4), (5,6,4,2))
        result1 = radarchart(some_list)
        result2 = radarchart(some_tuple)

        the_id_1 = str(id(some_list))
        the_id_2 = str(id(some_tuple))

        expected1= '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ['label_1','label_2','label_3','label_4'],
        datasets: [
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,4]
                    },
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [5,6,4,2]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Radar(data, options);
        </script>
        '''
        expected2 = '''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = {
        labels: ['label_1','label_2','label_3','label_4'],
        datasets: [
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,4]
                    },
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [5,6,4,2]
                    },
                ]
            };

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Radar(data, options);
        </script>
        '''
        assert result1 == expected1
        assert result2 == expected2
        #TODO
        #raise AssertionError("Not finished yet!")



########  PIE and DOUGHNUT CHARTS  ##########

## PIECHART SECTION ##

    def test_piechart_with_dict(self):
        ''' pass a dict to piechart'''

        dict1 = {"Red":300, "Green":200}
        result1 = piechart(dict1)
        the_id_1 = str(id(dict1))
        expected1 =  '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = [
                    {
                        value: 300
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: "Red"
                    },
                    {
                        value: 200
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: "Green"
                    }
                ]

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Pie(data, options);
        </script>
        '''
        assert result1 == expected1
        #raise AssertionError("Not finished yet!")

    def test_piechart_with_list_of_dicts(self):
        ''' pass a list containing dicts to piechart for full options'''

        dict1 = [{'label': "Blue","value":120, "color": "rgba(200,404,200,0.2)", 'highlight': "rgba(120,120,120,1)" },\
         {'label': "Green","value":100, "color": "rgba(160,210,210,1)", 'highlight': "rgba(220,220,220,1)" }]
        result1 = piechart(dict1)
        the_id_1 = str(id(dict1))
        expected1 =  '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = [
                    {
                        value: 120
                        color: "rgba(220,404,200,0.2)",
                        highlight: "rgba(120,120,120,1)",
                        label: "Blue"
                    },
                    {
                        value: 100
                        color: "rgba(160,210,210,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: "Green"
                    }
                ]

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Pie(data, options);
        </script>
        '''
        assert result1 == expected1

    def test_piechart_with_list_or_tuple(self):
        ''' pass a list or a tuple to piechart'''

        some_list =  [120,60]
        some_tuple =  (120,60)
        result1 = piechart(some_list)
        result2 = piechart(some_tuple)
        the_id_1 = str(id(some_list))
        the_id_2 = str(id(some_tuple))
        expected1 =  '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = [
                    {
                        value: 120
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: ""
                    },
                    {
                        value: 60
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: ""
                    }
                ]

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Pie(data, options);
        </script>
        '''
        expected2 =  '''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = [
                    {
                        value: 120
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(120,120,120,1)",
                        label: ""
                    },
                    {
                        value: 60
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: ""
                    }
                ]

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Pie(data, options);
        </script>
        '''
        assert result1 == expected1
        assert result2 == expected2

        #raise AssertionError("Not finished yet!")


## DOUGHNUT SECTION ##

    def test_doughnutchart_with_dict(self):
        ''' pass a dict to doughnutchart'''

        dict1 = {"Red":300, "Green":200}
        result1 = doughnutchart(dict1)
        the_id_1 = str(id(dict1))
        expected1 =  '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = [
                    {
                        value: 300
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: "Red"
                    },
                    {
                        value: 200
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: "Green"
                    }
                ]

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Doughnut(data, options);
        </script>
        '''
        assert result1 == expected1
        #raise AssertionError("Not finished yet!")

    def test_doughnutchart_with_list_of_dicts(self):
        ''' pass a list containing dicts to doughnutchart for full options'''

        dict1 = [{'label': "Blue","value":120, "color": "rgba(200,404,200,0.2)", 'highlight': "rgba(120,120,120,1)" },\
         {'label': "Green","value":100, "color": "rgba(160,210,210,1)", 'highlight': "rgba(220,220,220,1)" }]
        result1 = piechart(dict1)
        the_id_1 = str(id(dict1))
        expected1 =  '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = [
                    {
                        value: 120
                        color: "rgba(220,404,200,0.2)",
                        highlight: "rgba(120,120,120,1)",
                        label: "Blue"
                    },
                    {
                        value: 100
                        color: "rgba(160,210,210,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: "Green"
                    }
                ]

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Doughnut(data, options);
        </script>
        '''
        assert result1 == expected1

    def test_doughnutchart_with_list_or_tuple(self):
        ''' pass a list or a tuple to doughnutchart'''

        some_list =  [120,60]
        some_tuple =  (120,60)
        result1 = doughnutchart(some_list)
        result2 = doughnutchart(some_tuple)
        the_id_1 = str(id(some_list))
        the_id_2 = str(id(some_tuple))
        expected1 =  '''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = [
                    {
                        value: 120
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: ""
                    },
                    {
                        value: 60
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: ""
                    }
                ]

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Doughnut(data, options);
        </script>
        '''
        expected2 =  '''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = [
                    {
                        value: 120
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(120,120,120,1)",
                        label: ""
                    },
                    {
                        value: 60
                        color: "rgba(220,220,220,1)",
                        highlight: "rgba(220,220,220,1)",
                        label: ""
                    }
                ]

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Doughnut(data, options);
        </script>
        '''
        assert result1 == expected1
        assert result2 == expected2

        #raise AssertionError("Not finished yet!")



### GENERAL ISSUES APPLYING TO ALL CHARTS ###
    def test_passing_unordered_args(self):
        '''We want to make sure that order doesn't matter'''

        some_list = [[1,2,3,], ['A','B','C'], [5,6,4,]]
        result1 = BarChart(some_list)
        the_id = str(id(some_list))
        expected1 = '''
        <canvas id="'''+the_id+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id+''' = document.getElementById("'''+the_id+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C"],
        datasets: [
                    {
                        label: "dataset_1",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3]
                    },
                    {
                        label: "dataset_2",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [4,5,6]
                    },
                ]
            };

        var chart_'''+the_id+''' = new Chart(ctx_'''+the_id+''').Bar(data, options);
        </script>
        '''
        assert result1 == expected1

    def test_passing_no_labels(self):
        '''When no labels use just whitespace for any barchart'''

        some_list = [[1,2,3,4], [5,6,4,2]]
        some_dict = {"roses":[1,2,3,4,5,6]}
        result1 = barchart(some_list)
        result2 = barchart(some_dict)
        the_id_1 = str(id(some_list))
        the_id_2 = str(id(some_dict))

        expected1 ='''
        <canvas id="'''+the_id_1+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_1+''' = document.getElementById("'''+the_id_1+'''").getContext("2d");
        var data = {
        labels: ["", "", "",""],
        datasets: [
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,4]
                    },
                    {
                        label: "",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [5,6,4,2]
                    },
                ]
            };

        var chart_'''+the_id_1+''' = new Chart(ctx_'''+the_id_1+''').Bar(data);
        </script>
        '''
        expected2 ='''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = {
        labels: ["", "", "", "", "", ""],
        datasets: [
                    {
                        label: "roses",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,4,5,6]
                    },
                ]
            };

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Bar(data, options);
        </script>
        '''
        assert result1 = expected1
        assert result2 = expected2
        #TODO
        #raise AssertionError("Not finished yet!")

    def test_filling_gaps_in_labels_with_whitespace():
        '''When list of labels is shorter use whitespace
        rather than truncate '''
        #raise StupidProgrammerError()

        dict2 = [{"labels":["A", "B", ]}, {"roses":[1,2,3] }]
        result2 = barchart(dict2)
        the_id_2 = str(id(some_dict))
        expected2 ='''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "",],
        datasets: [
                    {
                        label: "roses",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2,3,]
                    },
                ]
            };

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Bar(data, options);
        </script>
        '''
        assert result2 == expected2
        #raise AssertionError("Not finished yet!")

    def test_floats(self):
        '''test that passing floats and floats with ints works '''

        dict2 = [{"labels":["A", "B", "C"]}, {"roses":[1,2.2,3.1] }]
        result2 = barchart(dict2)
        the_id_2 = str(id(some_dict))
        expected2 ='''
        <canvas id="'''+the_id_2+'''" width="400" height="400">  </canvas>
        <script>
        var ctx_'''+the_id_2+''' = document.getElementById("'''+the_id_2+'''").getContext("2d");
        var data = {
        labels: ["A", "B", "C",],
        datasets: [
                    {
                        label: "roses",
                        fillColor: "rgba(220,220,220,0.5)",
                        strokeColor: "rgba(220,220,220,0.8)",
                        highlightFill: "rgba(220,220,220,0.75)",
                        highlightStroke: "rgba(220,220,220,1)",
                        data: [1,2.2,3.1,]
                    },
                ]
            };

        var chart_'''+the_id_2+''' = new Chart(ctx_'''+the_id_2+''').Bar(data, options);
        </script>
        '''
        assert result2 == expected2
        #raise AssertionError("Not finished yet!")

    #def test_live_charts()
    #   for version 0.1.0.0: live charts with ajax TODO!


    def test_unique_ids(self):
        '''Every canvas element must have an unique id
        for a man may want to use more than just one
        chart on a page, we need to give
        each bloody canvas unique id
        if a man does not provide it
        the best way to do that is to use
        python object's id converting it to str
        '''
        dict1 = {"labels":["A", "B", "C"], "dataset":[1,2,3]}
        dict2 = [{"labels":["A", "B", "C"]}, {"dataset_1":[1,2,3]}, {"dataset_2":[4,5,6]}]
        some_list = [['label_1','label_2','label_3','label_4'], [1,2,3,4], [5,6,4,2]]
        expected_id_1 = str(id(dict1))
        expected_id_2 = str(id(dict2))
        expected_id_3 = str(id(some_list))

        result1 = barchart(dict1)
        result2 = barchart(dict2)
        result3 = barchart(some_list)
        id_1 = re.findall('<canvas id=".*?" ', result1)[0][12:-1]
        id_2 = re.findall('<canvas id=".*?" ', result2)[0][12:-1]
        id_3 = re.findall('<canvas id=".*?" ', result3)[0][12:-1]
        assert id_1!=id_2!=id_3
        assert id_1 == expected_id_1
        assert id_2 == expected_id_2
        assert id_3 == expected_id_3
        #now we test variable names
        assert "var chart_"+expected_id_1 in result1
        assert "var chart_"+expected_id_2 in result2
        assert "var chart_"+expected_id_3 in result3

    def test_datetime_objects_as_labels(self):
        ''' Pass datetime, convert to str and use as labels '''

        dict1 = {"labels":[datetime(2014,10,1,12,0,0), datetime(2014,11,1,12,0,0), datetime(2014,12,1,12,0,0)], "dataset":[1,2,3]}
        dict2 = [[datetime(2014,10,1,12,0,0), datetime(2014,11,1,12,0,0), datetime(2014,12,1,12,0,0)], [1,2,3]]
        result1 = barchart(dict1)
        result2 = barchart(list2)
        assert 'labels: ["2014-10-01 12:00:00", "2014-11-01 12:00:00", "2014-12-01 12:00:00"]' in result1
        assert 'labels: ["2014-10-01 12:00:00", "2014-11-01 12:00:00", "2014-12-01 12:00:00"]' in result2

    def test_date_objects_as_labels(self):
        ''' with barchart and linechart it would be nice to pass date objects as labels'''

        dict1 = {"labels":[date(2014,10,1), date(2014,11,1), date(2014,12,1)], "dataset":[1,2,3]}
        list2 = [[date(2014,10,1), date(2014,11,1), date(2014,12,1)], [1,2,3]]
        result1 = barchart(dict1)
        result2 = barchart(list2)
        assert 'labels: ["2014-10-01", "2014-11-01", "2014-12-01"]' in result1
        assert 'labels: ["2014-10-01", "2014-11-01", "2014-12-01"]' in result2

        raise AssertionError("NOT finished")

    def test_time_objects_as_labels(self):
        ''' with barchart and linechart it would be nice to pass also time objects as labels'''

        dict1 = {"labels":[time(10,0,0), time(11,0,0), time(12,0,0)], "dataset":[1,2,3]}
        list2 = [[time(10,0,0), time(11,0,0), time(12,0,0)], [1,2,3]]
        result1 = barchart(dict1)
        result2 = barchart(list2)
        assert 'labels: ["10:00:00", "11:00:00", "12:00:00"]' in result1
        assert 'labels: ["10:00:00", "11:00:00", "12:00:00"]' in result2

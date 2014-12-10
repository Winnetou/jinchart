#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import re

from random import choice

from jinchart import BarChart, LineChart, PieChart

class JinChartTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        print "bye bye!"

    def test_unique_ids(self):
        '''Every canvas element must have an unique id
        for a man may want to use more than just one
        chart on a page, we need to give
        each bloody canvas unique id
        the best way to do that is not known yet!
        '''
        dict1 = {"labels":["A", "B", "C"], "dataset":[1,2,3]}
        dict2 = {"labels":["A", "B", "C"], "dataset_1":[1,2,3], "dataset_2":[4,5,6]}
        some_list = [['label_1','label_2','label_3','label_4'], [1,2,3,4], [5,6,4,2]]

        result1 = BarChart(dict1)
        result2 = BarChart(dict2)
        result3 = BarChart(some_list)
        id_1 = re.findall('<canvas id=".*?" ', result1)
        assert len(id_1)==1
        id_2 = re.findall('<canvas id=".*?" ', result2)
        assert len(id_2)==1
        id_3 = re.findall('<canvas id=".*?" ', result3)
        assert len(id_3)==1
        assert id_1[0]!=id_2[0]!=id_3[0]
        if "var myNewChart" in result1:
            assert "var myNewChart" not in result2 and "var myNewChart" not in result3
            #explanation: in case of multiple charts on one page, give'm different vars names
            # to avoid overriding and other mess
        if "var myNewChart" in result2:
            assert "var myNewChart" not in result1 and "var myNewChart" not in result3
        if "var myNewChart" in result3:
            assert "var myNewChart" not in result2 and "var myNewChart" not in result1



    def test_barchart_with_dict(self):
        ''' pass a dict to barchart - when you don't want to
        play with rgba colours or anything, just quick chart with defaults'''
        #TODO
        dict1 = {"labels":["A", "B", "C"], "dataset":[1,2,3]}
        dict2 = {"labels":["A", "B", "C"], "dataset_1":[1,2,3], "dataset_2":[4,5,6]}
        result1 = BarChart(dict1)
        result2 = BarChart(dict2)
        expected1= '''
        <canvas id="?" width="400" height="400">  </canvas>
        <script>
        var ctx = document.getElementById("?").getContext("2d");
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

        var myNewChart = new Chart(ctx).Bar(data);
        </script>
        '''
        expected2 = '''
        <canvas id="?" width="400" height="400">  </canvas>
        <script>
        var ctx = document.getElementById("?").getContext("2d");
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

        var myNewChart = new Chart(ctx).Bar(data);
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
        ''' pass a dict to barchart for the deluxe edition - all colours,
        stroke and other options under your control'''
        #TODO
        dict1 = [{"labels":["A", "B", "C"]}, {"dataset":[1,2,3], "fillColor": "rgba(200,404,200,0.2)" }]
        dict2 = [{"labels":["A", "B", "C"]}, {"roses":[1,2,3], "fillColor": "rgba(200,404,200,0.2)",},\
         {"violas":[4,5,6], "fillColor": "rgba(222,404,200,0.2)", 'strokeColor': "rgba(151,187,205,0.8)",}]
        result1 = BarChart(dict1)
        result2 = BarChart(dict2)
        expected1= '''
        <canvas id="?" width="400" height="400">  </canvas>
        <script>
        var ctx = document.getElementById("?").getContext("2d");
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

        var myNewChart_? = new Chart(ctx).Bar(data);
        </script>
        '''# TODO: that can't be var myNewChart - together with id, these vars must be unique
        expected2= '''
        <canvas id="?" width="400" height="400">  </canvas>
        <script>
        var ctx = document.getElementById("?").getContext("2d");
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

        var myNewChart = new Chart(ctx).Bar(data);
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
        raise AssertionError("Not finished yet!")

    def test_barchart_with_list_or_tuple(self):
        ''' pass a list or a tuple to barchart'''
        #TODO
        some_list = [['label_1','label_2','label_3','label_4'], [1,2,3,4], [5,6,4,2]]
        some_tuple = (('label_1','label_2','label_3','label_4'), (1,2,3,4), (5,6,4,2))
        result1 = BarChart(dict1)
        result2 = BarChart(dict2)
        expected1= '''
        <canvas id="?" width="400" height="400">  </canvas>
        <script>
        var ctx = document.getElementById("?").getContext("2d");
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

        var myNewChart_? = new Chart(ctx).Bar(data);
        </script>
        '''
        expected2= ""
        # now assert that
        assert result1 == expected1 == result2 == expected2

        #raise AssertionError("Not finished yet!")


    def test_linechart_with_dict(self):
        ''' pass a dict to linechart'''

        expected1 = '''
        var data = {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
                    {
                        label: "My First dataset",
                        fillColor: "rgba(220,220,220,0.2)",
                        strokeColor: "rgba(220,220,220,1)",
                        pointColor: "rgba(220,220,220,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(220,220,220,1)",
                        data: [65, 59, 80, 81, 56, 55, 40]
                    },
                    {
                        label: "My Second dataset",
                        fillColor: "rgba(151,187,205,0.2)",
                        strokeColor: "rgba(151,187,205,1)",
                        pointColor: "rgba(151,187,205,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(151,187,205,1)",
                        data: [28, 48, 40, 19, 86, 27, 90]
                    },
                ]
            };

        var myNewChart_? = new Chart(ctx).Line(data);
        </script>
        '''
        raise AssertionError("Not finished yet!")

    def test_linechart_with_list_of_dicts(self):
        ''' pass a list containing dicts to linechart for full options'''
        #TODO
        raise AssertionError("Not finished yet!")

    def test_piechart_with_dict(self):
        ''' pass a dict to piechart'''
        #TODO
        raise AssertionError("Not finished yet!")

    def test_piechart_with_list_of_dicts(self):
        ''' pass a list containing dicts to piechart for full options'''
        #TODO
        raise AssertionError("Not finished yet!")


    def test_linechart_with_list_or_tuple(self):
        ''' pass a list or a tuple to linechart'''
        some_list = [['label_1','label_2','label_3','label_4'], [1,2,3,4], [5,6,4,2]]
        some_tuple = (('label_1','label_2','label_3','label_4'), (1,2,3,4), (5,6,4,2))

        #TODO
        raise AssertionError("Not finished yet!")

    def test_piechart_with_list_or_tuple(self):
        ''' pass a list or a tuple to piechart'''
        #TODO
        some_list = [['label_1','label_2','label_3','label_4'], [1,2,3,4], [5,6,4,2]]
        some_tuple = (('label_1','label_2','label_3','label_4'), (1,2,3,4), (5,6,4,2))

        raise AssertionError("Not finished yet!")

    def test_passing_unordered_args(self):
        '''We want to make sure that order doesn't matter'''
        some_list = [[1,2,3,4], ['label_1','label_2','label_3','label_4'], [5,6,4,2]]
        some_tuple = ((1,2,3,4), (5,6,4,2), ('label_1','label_2','label_3','label_4')))
        expected2= '''
        <canvas id="?" width="400" height="400">  </canvas>
        <script>
        var ctx = document.getElementById("?").getContext("2d");
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

        var myNewChart = new Chart(ctx).Bar(data);
        </script>
        '''

        #TODO
        raise AssertionError("Not finished yet!")

    def test_passing_no_labels(self):
        '''When no labels use just whitespace eg for barchart'''
        some_list = [[1,2,3,4], [5,6,4,2]]
        some_dict = {"roses":[1,2,3,4,5,6]}
        #TODO
        raise AssertionError("Not finished yet!")

    def test_labels_fill_with_whitespace(self):
        '''When list of labels is shorter use whitespace
        rather than truncate '''
        some_list = [['label_1','label_2','label_3',], [1.0,2.1,2.2,1.3], [1.1,0.6,0.4,1.2]]
        dict1 = [{"labels":["A", "B", ]}, {"dataset":[1.2,2.2,3.1], "fillColor": "rgba(200,404,200,0.2)" }]
        #TODO
        raise AssertionError("Not finished yet!")

    def test_floats(self):
        '''test that passing floats and floats with ints works '''
        some_list = [['label_1','label_2','label_3','label_4'], [1.0,2.1,2.2,1.3], [1.1,0.6,0.4,1.2]]
        dict1 = [{"labels":["A", "B", "C"]}, {"dataset":[1.2,2.2,3.1], "fillColor": "rgba(200,404,200,0.2)" }]
        #TODO
        raise AssertionError("Not finished yet!")
    #def test_live_charts()
    #   for version 0.1.0.0: live charts with ajax TODO!u
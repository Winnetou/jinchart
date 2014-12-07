#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from random import choice

from jinchart import BarChart, LineChart, PieChart

class JinChartTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        print "bye bye!"

    def test_unique_ids(self):
        '''Every canvas must have an unique id
        for someone may want to use more than just one
        chart on a page, we need to figure out how to give
        each bloody canvas unique yet persistent ie
        not random-on-the-fly-generated id'''
        #TODO
        raise AssertionError

    def test_barchart_with_dict(self):
        ''' pass a dict to barchart - when you dont want to
        play with rgba colours or anything, just quick chart with defaults'''
        #TODO
        dict1 = {"labels":["A", "B", "C"], "dataset":[1,2,3]}
        dict2 = {"labels":["A", "B", "C"], "dataset_1":[1,2,3], "dataset_2":[4,5,6]}
        result1 = BarChart(dict1)
        result2 = BarChart(dict2)
        expected1= ""
        expected2= ""
        # now assert that
        assert result1 == expected1
        assert result2 == expected2
        raise AssertionError

    def test_barchart_with_list_of_dicts(self):
        ''' pass a dict to barchart for the deluxe edition - all colours,
        stroke and other options under your control'''
        #TODO
        dict1 = [{"labels":["A", "B", "C"]}, {"dataset":[1,2,3], "fillColor": "rgba(200,404,200,0.2)" }]
        dict2 = [{"labels":["A", "B", "C"]}, {"roses":[1,2,3], "fillColor": "rgba(200,404,200,0.2)",},\
         {"violas":[4,5,6], "fillColor": "rgba(200,404,200,0.2)"}]
        result1 = BarChart(dict1)
        result2 = BarChart(dict2)
        expected1= ""
        expected2= ""
        # now assert that
        assert result1 == expected1
        assert result2 == expected2
        raise AssertionError

    def test_linechart_with_dict(self):
        ''' pass a dict to linechart'''
        #TODO
        raise AssertionError

    def test_linechart_with_list_of_dicts(self):
        ''' pass a dict to linechart'''
        #TODO
        raise AssertionError

    def test_piechart_with_dict(self):
        ''' pass a dict to piechart'''
        #TODO
        raise AssertionError

    def test_piechart_with_list_of_dicts(self):
        ''' pass a dict to piechart'''
        #TODO
        raise AssertionError


    def test_barchart_with_list_or_tuple(self):
        ''' pass a list or a tuple to barchart'''
        #TODO
        raise AssertionError

    def test_linechart_with_list_or_tuple(self):
        ''' pass a list or a tuple to linechart'''
        #TODO
        raise AssertionError

    def test_piechart_with_list_or_tuple(self):
        ''' pass a list or a tuple to piechart'''
        #TODO
        raise AssertionError

    def test_passing_unordered_args(self):
        '''We want to make sure that order doesn't matter'''
        #TODO
        raise AssertionError

    def test_passing_no_labels(self):
        '''When no labels use just whitespace eg for barchart'''
        pass
        #TODO
        raise AssertionError

    def test_labels_fill_with_whitespace(self):
        '''When list of labels shorter use whitespace '''
        pass
        #TODO
        raise AssertionError

    def test_floats(self):
        '''test that passing floats and floats with ints works '''
        pass
        #TODO
        raise AssertionError
    #def test_live_charts()
    #   for version 0.1.0.0: live charts with ajax TODO!
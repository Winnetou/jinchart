jinchart
========

Jinchart module contains set of Jinja2 filters to create ChartJS charts directly from your data,
without getting your hands dirty with JavaScript. Quick, easy, fully customizable.

How to use it in Flask:
first, import:

    from Jinchart.jinchart import barchart

next, register the filter

    app.jinja_env.filters['barchart'] = barchart

get your data:

    lines_of_code_written = { 'labels':['January', 'February', 'March'], "Jacques" : [3400, 5700, 9800], "Thomas" : [4100, 1700, 2800] }

and in your template:

    {{lines_of_code_written|barchart}}


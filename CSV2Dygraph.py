#!/usr/bin/env python
import os
import sys
import csv
import argparse

"""
Author:
----------------------------------------------------------------------------------------
  Michael Ewald <mewald@GeomaticsResearch.com>
  GeomaticsResearch LLC
  http://geomaticsresearch.com

Filename:
    CSV2Dygraph.py

Last Revision:
    2015-05-20 (M. Ewald)

Purpose:
    Convert a CSV to a DYgraph array datatype

References:
    http://dygraphs.com/
    http://dygraphs.com/data.html#array


WARNING:
ASSUMES that the first column in the CSV is a date/time. Appends the rest of the columns to the array.


License:
----------------------------------------------------------------------------------------
Copyright (c) 2014. Michael Ewald, GeomaticsResearch LLC.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

def main(input_filepath, output_filepath = None):
    csv_fh = csv.reader(open(input_filepath, 'r'))
    headers = next(csv_fh, None)
    print headers
    
    array_rows = list()
    for row in csv_fh:
        col_length = len(row)
        date = 'new Date("{0}")'.format(row[0])
        
        data = list()
        for d in row[1:col_length]:
            if d == "": d = "null"
            data.append(d)
        out_val = "[{0},{1}],".format(date, ",".join(data))
        array_rows.append(out_val)
    array_rows[len(array_rows)-1] = array_rows[-1][0:-1]
    
    
    out_fh = open(output_filepath, 'w')
    out_fh.write('[{0}]'.format("\n".join(array_rows)))
    out_fh.close()
    print "Done"

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="The input CSV")
    parser.add_argument("output", help="The output DYgraph .js file")
    args = parser.parse_args()
    main(args.input, args.output)
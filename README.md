# DXFGeoConverter

## Summary
DXFGeoConverter generate xy points list from dxf file.
This program made for FabAcademy Machine Learning Assignment.
You can use this program for generating data for Gestalt project.

## Get started
$ python setup.py develop

$ python

from dxfconverter import DXFConverter as df

file = './sampledata/cat.dxf'

df.get_xy(file)



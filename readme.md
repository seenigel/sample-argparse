# Sample Argparse

This is a simple demo of python's argparse module.

The script does the following:
- Look through an input csv (the `in` file) for a list of presidents and years
- Write sentences based on the csv data to an output file (the `out` file)
    
    
The argeparse lets me pass the input and output file locations through the CLI as follows: 

`python write-presidents.py -in presidents.csv -out list.txt`

The outfile can be named whatever you'd like
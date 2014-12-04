Agent Audit Analysis
=============

Overview
-------------

A simple python script that aggregates rows from Agent_Audit and outputs a single line for each job run that did work.
Used and tested for: DQ / DQ 1.5.2 / List Upload
May not work for others, as the values of collumn 'status' seem a little variable across job types.

Input
-------------
Data from Agent_Audit in CSV format with headings defined in file: header_line.txt.
Expects rows to be sequential, grouped by job run.

Run
-------------
./parse_csv.py [input_file.csv] > [output_file.csv]

Output
-------------
start_time, end_time, records processed,time (sec), rate (records/sec)


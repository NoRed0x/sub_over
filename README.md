## sub_over tool :-
================

this tool take a list of subdomain and get cname for every subdomain and take snapshot from webside that has cname
and output file contain url that has cname,and folder contains screenshot

<img src="/cname.PNG" alt="Getting-gz" width="1100" height="400">

## Install :-
==============

1. git clone https://github.com/NoRed0x/sub_over 
2. pip3 install -r requirements.txt
3. sudo apt-get install eyewitness


## Usage :-
============

The tool take one argument which is the file contain subdomains list and doesn't work on single subdomain 

## EX :-
========

python sub_over.py -d subdomains.txt

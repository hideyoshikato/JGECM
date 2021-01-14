#!/usr/bin/env python3 -u
# Copyright (c) 2021, Hideyoshi Kato.
# All rights reserved.
#

import os
import sys
import argparse
import csv
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('basedir', help='place of `C-XML`')
    parser.add_argument('--output', help='output filename')
    parser.add_argument('--sep', help='sep (0 or 1)')

    args = parser.parse_args()

    ORGDATANAME = 'JGECM_org.csv'
    if os.path.isfile(os.path.join(os.getcwd(), ORGDATANAME)):
        orgdatapath = os.path.join(os.getcwd(), ORGDATANAME)
    else:
        print('No such file %s' % ORGDATANAME)
        sys.exit(0)

    base0 = os.path.split(args.basedir) + ('C-XML','VARIABLE','PN','PN')
    basedir = os.path.join(*base0)

    if args.output is None:
        outputfile = os.path.join(os.getcwd(), 'JGECM.csv')
    else:
        outputfile = args.output

    with open(orgdatapath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        orgd = [row for row in reader]
        
    outputcsv = []
    outputheader = ['tgt', 'src', 'type']
    outputcsv.append(outputheader)
    for i in range(1,len(orgd)):
        print(i, end='\r')
        bccwjfpath = os.path.join(basedir, orgd[i][0])
        orgsentence = ''
        with open(bccwjfpath, 'r') as bccwcd:
            soup = BeautifulSoup(bccwcd, 'html.parser') 
            sentences = soup.find_all('sentence')
            orgsentence = sentences[int(orgd[i][1])].string.replace('\u3000', '')
        
        if args.sep == '1':
            srcsentence = \
            orgsentence[:int(orgd[i][3])] + \
            '[' + orgd[i][2] + ']' + \
            orgsentence[-int(orgd[i][4]):]
        else:
            srcsentence = \
            orgsentence[:int(orgd[i][3])] \
            + orgd[i][2] \
            + orgsentence[-int(orgd[i][4]):]
        
        outputcsv.append([orgsentence, srcsentence, orgd[i][5]])
    
    with open(outputfile, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(outputcsv)
    
    
if __name__ == "__main__":
    main()

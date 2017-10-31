#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:24:03 2017

@author: Felipe
"""
from collections import defaultdict;
import heapq
import datetime
import statistics

def read_political(fpath ='input/itcont.txt'):

	"""
	Description:
		Reads in data from itcont.txt and uses heap median algorithm to calculate runnin medium
	
	Input : fpath [string] - Filepath for itcont.txt
	
	
	"""
	
    # initialize variables 
	maxh = defaultdict(list);
	minh = defaultdict(list);
	donor_date = defaultdict(list);
	donor_count = defaultdict(int);
	out1 = open('output/medianvals_by_zip.txt', 'w');
	out2 = open('output/medianvals_by_date.txt', 'w');
	
	
                         
	with open(fpath, 'r') as infile:
	
		for line in infile:
            
			flier_ID = line.split('|')[0]
			if len(line.split('|')[10])>4:
        			zip_code = line.split('|')[10][0:5]
			else:
        			zip_code = []
			if len(line.split('|')[13])==8:
        			transaction_date = line.split('|')[13]
			else:
        			transaction_date=[]
                
			transaction_amt = float(line.split('|')[14])
			other_id = line.split('|')[15]
            

			if not other_id and zip_code and transaction_amt and flier_ID:
        			out1.write(flier_ID)
        			out1.write('|')
        			out1.write(zip_code)
        			out1.write('|')
                    
                        # Begin keeping track of median by inserting first streaming value
        			if not maxh[flier_ID+zip_code] and not minh[flier_ID+zip_code]:
        				heapq.heappush(maxh[flier_ID+zip_code], -transaction_amt)
        				out1.write(str(round((transaction_amt))))  
                            #print float(val)
        			elif maxh[flier_ID+zip_code]:
                    
                            # Add other values to median list as needed
        				if transaction_amt>=-maxh.get(flier_ID+zip_code)[0]:
        				    heapq.heappush(minh[flier_ID+zip_code],transaction_amt)
        				elif transaction_amt<-maxh.get(flier_ID+zip_code)[0]:
        				    heapq.heappush(maxh,-transaction_amt)
                    
                             #Calculate the median
        				if len(maxh[flier_ID+zip_code])==len(minh[flier_ID+zip_code]):
#        				   
        				    out1.write(str(round((-maxh.get(flier_ID+zip_code)[0]+minh.get(flier_ID+zip_code)[0])/2)))
        				    
        				elif len(maxh[flier_ID+zip_code])==len(minh[flier_ID+zip_code])+1:
        				    out1.write(str(round(-maxh.get(flier_ID+zip_code)[0])))
        				    
        				elif len(minh[flier_ID+zip_code])==len(maxh[flier_ID+zip_code])+1:
        				    out1.write(str(round(minh.get(flier_ID+zip_code)[0])))
                            
                            # if list of values is unsymetric move value to keep symmetry
        				elif len(minh[flier_ID+zip_code])==len(maxh[flier_ID+zip_code])+2:
        				    heapq.heappush(maxh[flier_ID+zip_code],-heapq.heappop(minh[flier_ID+zip_code]))
                                
        				elif len(maxh[flier_ID+zip_code])==len(minh[flier_ID+zip_code])+2:
        				    heapq.heappush(minh[flier_ID+zip_code],-heapq.heappop(maxh[flier_ID+zip_code]))
                                
                                
        			out1.write('|')
        			out1.write(str(len(minh[flier_ID+zip_code])+len(maxh[flier_ID+zip_code])))
        			out1.write('|')
        			out1.write(str(round(-sum(maxh.get(flier_ID+zip_code))+sum(minh.get(flier_ID+zip_code)))) + '\n')
                  
                    
                    
			if not other_id and transaction_date and transaction_amt and flier_ID:
            
        			donor_date[flier_ID, transaction_date].append(transaction_amt)               
        			donor_count[flier_ID, datetime.date.toordinal(datetime.datetime.strptime(transaction_date,'%m%d%Y'))] += 1
           
	sorted_list = sorted(donor_date.items(), key=lambda x: (x[0], x[1] )) 
	
	for i in sorted_list:
        			out2.write(str(i[0][0]))
        			out2.write('|')
        			out2.write((str(i[0][1])))
        			out2.write('|')
        			out2.write(str(round(statistics.median(i[1][:]))))
        			out2.write('|')
        			out2.write(str(len(i[1][:])))
        			out2.write('|')
        			out2.write(str(round(sum(i[1][:])))+ '\n')
                    
read_political()
                                
                                
                     
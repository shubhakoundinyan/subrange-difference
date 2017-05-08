#! /usr/bin/python

# python created with: Sublime Text3
# Author: Shubha Koundinyan
# Date: 02/18/2017

import time
import sys
from sys import platform

# Some Significant Definitions in the Problem
# ===========================================
# N = Days of Average Home Sale Price Data
# K = Fixed Window Size
# Line 1 in the text file to be read = Integers N and K
# Line 2 in the text file to be read = Avg. Home Sale Price < 1,000,000

# This function opens the input text file, and reads the content

def readl():
	with open('Input.txt','r') as f:
		t = f.readlines()
		a = []
		a1 = []
		a2 = []
		for line in t[0]:
			a = line.split()
			for element in a:
				if element.isdigit==False:
					continue
				a1.append(element)
				a1 = map(int, a1)

		print "\n DIFFERENCE between Increasing and Decreasing Subranges : \n"
		
		for line in t:
			b = line.split(" ")
			
			for element in b:
				if element.isdigit==False:
					continue
				a2.append(element)
				a2 = map(int, a2)

		# Condition Check 1: Days of Avg. Home Sale Price > Window Size

		if a2[0]<a2[1]:
			print "Input given invalid!Average days should be > Window size" 
			sys.exit()

		# Condition Check 2: Whether N (Line 1) == Number (Data Elements in Line 2)

		if a2[0] != len(a2[2:]):
			print "Average home sale prize data elements does not match the N days input in Line1"
			sys.exit()

		#Condition Check 3: Constraints 1<=N<=200,000 days

		if a2[0] <1 or a2[0]>200000:
			print "N value is not correctly entered!"
			sys.exit()  
		for x in chunks(a2[2:], int(a2[1])):
			print x
	f.close()

# Sublist division and diffs calculation

def chunks(iterable, n):
	
	result1 = []
	l = iterable
	n = int(n)
	
	print "Each chunk generated below is stored in Array 'result1' as displayed below: \n "
	
	for i in range(0, len(l)-n+1 , 1):
		 yield l[i:i+n]
		 result1.append(l[i:i+n])
	print result1
		
	length_r = len(result1)
	g1 = 0
	l1 = 0
	set1 =0
	set2 =0
	for index in range(length_r):
		
		t1 = []
		t1= (result1[index])
		
		for i in range(0,len(t1)):
			
			for j in range(i+1,len(t1)):
				
				if t1[i] < t1[j]:
					for k in range(j+1, len(t1)):
						if t1[j] < t1[k]:
							g1 = g1 + 1
					g1 = g1 + 1
					break
				elif t1[i] > t1[j]:
					l1 = l1 +1
					break
		print "\n Subrange Diff: " +str(int(g1-l1))
		g1 = 0
		l1 = 0

# Memory usage calculation

import os

_proc_status = '/proc/%d/status' % os.getpid()

_scale = {'kB': 1024.0, 'mB': 1024.0*1024.0,
          'KB': 1024.0, 'MB': 1024.0*1024.0}

def _VmB(VmKey):
    
    global _proc_status, _scale
    try:
        t = open(_proc_status)
        v = t.read()
        t.close()
    except:
        return 0.0
    i = v.index(VmKey)
    v = v[i:].split(None, 3)
    if len(v) < 3:
        return 0.0
    return float(v[1]) * _scale[v[2]]

def memory(since=0.0):
 
    t =  _VmB('VmSize:') - since
    print "\n Memory Usage in Bytes: "+str(t)
    return t

# Main Function

if __name__ == "__main__":
	start = time.time() 
	readl()
	time_taken = time.time()-start
	print "\n Code execution time = %g seconds"%(time_taken)
	# NOTE: The memory calculation works only on the Linux platform
	if platform == "linux" or platform == "linux2":
		memory()

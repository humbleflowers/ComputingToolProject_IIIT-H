#!/usr/bin/python
import MySQLdb as mdb
import matplotlib.pyplot as p
import numpy as np
print "Restriction enzymes to choose from -> "
print "====================================================="
print "EcoRI|BamHI|MseI|AluI|PstI|SmaI|BfaI|BstuI|DpnI|AciI|"
print "Sau3a|MspI|NlaIII|NotI|RsaI|HindIII" 
print "====================================================="                 
def DNA(enzyme,site): 	        
        counter=0
	init = 0
        enzyme_sites=[]
        fi=open(f)
        line = fi.read().splitlines()
        line.pop(0)
        line=''.join(line)
        line.upper()     
        for i in range(0,line.count(site)):
        		position = line.find(site)
        		real_position=(position + 1) + init
        		print "%s Site is at position %d" %(enzyme,real_position)
        		enzyme_sites.append(real_position)
                        line = line[(position + 1):]
        		init = (position + 1)
                	counter += 1
        print "The Total number of %s sites on the DNA is %r " %(enzyme,counter)
       
def Restriction_db(enzyme):
	conn= mdb.connect("localhost", "vinay","123456","DNA_Sites")          # Open database connection
	with conn: 
		cursor = conn.cursor()                
		sql = "SELECT * FROM Restriction_enzyme WHERE Enzyme = '%s' " %enzyme
		cursor.execute(sql)
		results = cursor.fetchall()                  
                print "_____________"   
		print "Name  |  Site"
		for row in results:

			print "%s | %s" % (row[0], row[1])
                print "-------------"
                DNA(row[0],row[1])

def main():
        import os 
        while True:
                global f 
		f=raw_input("Enter your file name: ")
                if os.path.isfile(f):
                	  enzyme = raw_input("Enter the name of enzyme: ")
		          Restriction_db(enzyme)
                          break
                else:
                          print "No such file exist!"
main() 


#!/usr/bin/python
import os, re
P={}
P['A'] = ['A', 142,   83]
P['R'] = ['R',  98,   93]
P['N'] = ['N', 101,   54]
P['D'] = ['D',  67,   89]
P['C'] = ['C',  70,  119]
P['E'] = ['E', 151,   37]
P['Q'] = ['Q', 111,  110]
P['G'] = ['G',  57,   75]
P['H'] = ['H', 100,   87]
P['I'] = ['I', 108,  160]
P['L'] = ['L', 121,  130]
P['K'] = ['K', 114,   74]
P['M'] = ['M', 145,  105]
P['F'] = ['F', 113,  138]
P['P'] = ['P',  57,   55]
P['S'] = ['S',  77,   75]
P['T'] = ['T',  83,  119]
P['W'] = ['W', 108,  137]
P['Y'] = ['Y',  69,  147]
P['V'] = ['V', 106,  170]

filename = raw_input("Enter file name: ")
def read(filename):
    f=open(filename,'r')
    seq = ""
    for line in f:
        if line.startswith(">"):
            pass
        else:
            seq += re.sub("\n","",line)
    return seq
  

def a_helix(seq):
	begin = 0
	total = []
	found = False
	found_list = []
	while (begin < len(seq)):		
		if (P[seq[begin]][1] > 100):
			found = True
			found_list.append(seq[begin])
		else:
			if(found == True):
				if(len(found_list) >= 4 ):
                                        
					total.append(found_list)
			found = False
			found_list = []
		begin = begin + 1
	print "\nTotal alpha_helices : %d \n " %(len(total))
	for i in range(len(total)):
                c=''.join(total[i])
        	print "The alpha helix is  %s  is at positions  %d " %(c,seq.find(c)+1)

a_helix(read(filename))

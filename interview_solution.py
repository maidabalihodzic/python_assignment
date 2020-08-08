import csv
import json
import math
import os
import sys


class my_dictionary(dict):  
   
    def __init__(self):  
        self = dict()  
          
    def add(self, key, value):  
        self[key] = value  

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Need 2 more arguments.\n Try $python3 interview_solution.py -h or $python3 interview_solution.py --help')

    elif len(sys.argv) < 3 and sys.argv[1] != '-h' and sys.argv[1] != '--help' :
        sys.exit('Need 1 more argument. \n Try $python3 interview_solution.py -h or $python3 interview_solution.py --help')
    
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
          sys.exit('Need 2 arguments. In following order: \n $python3 nameofscript.py -c nameoffile.csv')

    elif sys.argv[1] == '-c' and sys.argv[2].split(".")[1] == "csv":
       inputfile=sys.argv[2]
       try:
           f = open(inputfile)
           f.close()
           with open(inputfile, 'r') as file: 
               outputfile=inputfile.split(".")[0]+".json"
               with open(outputfile, 'w') as write_file:
                    pair = my_dictionary() 
                    reader = csv.reader(file)
                    for row in reader:                    
                       if row[0] !=  "Temp" and row[0]!= "(degC)": 
                        input1 = float (row[0])   
                        if input1 >= 0 and input1 <=100:
                         if input1 % 5 == 0 or input1 == 0:
                          pair.add((float(row[0])), float(row[2]))
    
                    json.dump(pair, write_file, indent=4, sort_keys=True)

       except FileNotFoundError:
           print('Input file does not exist.')
    
    elif sys.argv[2].split(".")[1] != "csv":
         print ('Input file has to be CSV file.')

    else:  
          print ('Try $python3 interview_solution.py -h or $python3 interview_solution.py --help')

   



from bs4 import BeautifulSoup
import os
import csv

outfile = open("nameGenAuthOutput.csv","a")

w=csv.writer(outfile)
w.writerow(["PMID ", "First name", "Last name","gender"])

nameDict=open("nameGender.csv")

infile=open("2NERoutput.csv","r")
        datareader=csv.reader(infile)

        for row in datareader:
                pmid=row[0]
                persons=" "
                ack=BeautifulSoup(str(row))
                if ack.findAll("person"):
                        
                        people=ack.findAll("person")
                        for i in people:
                                dude=i.get_text().encode("latin-","ignore")
#                                persons=persons + dude + " , "
                                w.writerow([pmid, str(dude)])

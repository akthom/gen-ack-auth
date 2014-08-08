gen-ack-auth
============
developing scripts for project studying relaitonship between authorship, acknowledgement and gender in schol comm

**AuthorAckExtract.py** : 1) this script crawls a directory containgin PMC files; mines the JATS mark up for different parts of the journal article; and then outputs this into a series of files for later processing (named entity recognition and gender ID)

**NERExtractor.py** : after running _forNER.csv_ through the Stanford NER (currently using the GUI for testing), this script pulls the <PERSON> entities out and spits them into a separate file

**genderID.py** : not yet written; will ID gender of authors and acknowledged entities

output files:

step 1 (out of **AuthorAckExtract.py**)-- rough information extraction

*log.txt* : logs the efficancy of the acknowledgement extractor (or maybe more accurately, the messiness of the JATS: not all articles use the <ack> tag as the should)

*fullExtraction.csv* : this summarizes the initial output; might not be necessary

*authorByPMID.csv* : lists each author name by the PMID it was found in -- for input into gender ID script

*forNER.csv* : for input into Stanford NER

step 2 -- named entity recognition

- run forNER.csv through Stanford NER to get

*NERoutput.csv* : basically just *forNER.csv* with <pointy brackets> 

then run _NERoutput.csv_ through **NERExtractor.py** to get

*ackDetail.csv* : which lists each NERed acknowledgee and a PMID

step 3 -- gender ID

http://ptigas.com/blog/2012/01/21/name2gender-in-python/



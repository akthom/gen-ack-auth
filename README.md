gen-ack-auth
============
simple scripts for project studying relationship between authorship, acknowledgement and gender in schol comm


**nameGender.txt** contains the names and genders*

**AuthorAckExtract.py** : 1) this script crawls a directory containgin PMC files; mines the JATS mark up for different parts of the journal article; and then outputs this into a series of files for later processing (named entity recognition and gender ID)

**NERExtractor.py** : after running _forNER.csv_ through the Stanford NER (currently using the GUI for testing), this script pulls the <PERSON> entities out and spits them into a separate file

**parsenames.py** -  ID gender of authors and acknowledged entities


output files:
============
step 1 
==
run **AuthorAckExtract.py** -- rough information extraction.  This extracts author names, author ranks, acknowledgment text; ID's author gender; counts total number of authors; and produces:

*log.txt* : logs the efficancy of the acknowledgement extractor (or maybe more accurately, the messiness of the JATS: not all articles use the <ack> tag as the should)

*fullExtraction.csv* : this summarizes the initial output; might not be necessary

*authorByPMID.csv* : lists each author name by the PMID it was found in.

*forNER.csv* : for input into Stanford NER

Still need to figure out if all these outputs are really necessary


step 2 - named entity recognition
= 

- run *forNER.csv* through Stanford NER to get text (*NERoutput.csv* )with entities IDed with < pointy brackets > . 

then run _NERoutput.csv_ through **NERExtractor.py** to get

*ackDetail.csv* : which lists each NERed acknowledgee, their gender and a PMID


*gender ID scripts forked from [@ptigas] who doesn't seem to have this in a repo<br>
pulls names from social security "most popular US baby names" into a csv:
http://ptigas.com/blog/2012/01/21/name2gender-in-python/

Resulting HTML processed in excel: I made a pivot table to count how many years a name was a male or female name.  I assigned a gender to a name if was male or female >55% of the time; for those within the 45-55% range I left them ambiguous.
- We could possibly reduce the error if we constrain the temporal range of names a bit more; if the earliest paper in our corpus was published in 2000, then it's reasonable to say that a publishing author wouldn't be older than, say, 80, or younger than 20 -- meaning we could pull names from 1920-2000 and see if that makes gender more precise.  Might be way overthinking it though
- Could also be more conservative with the ambiguous names -- move the % to 45-55%. 
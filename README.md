gen-ack-auth
============
simple scripts for project studying relationship between authorship, acknowledgement and gender in schol comm

**AuthorAckExtract.py** : this script: 

- crawls a directory containgin PMC files; 
- mines the JATS mark up for different parts of the journal article (authors lists and acknowledgement statements
- uses Stanford NER to ID people in the acknowledgment statements
- ID's the gender of each author and acknowledgee
- outputs this into a series of files for later analysis (review for precision and recall of the acknowledgement extraction and gender ID).

**nameGender.txt** contains the names and genders*


~~**NERExtractor.py** : after running _forNER.csv_ through the Stanford NER (currently using the GUI for testing), this script pulls the <PERSON> entities out and spits them into a separate file~~

~~**parsenames.py** -  ID gender of authors and acknowledged entities~~



gender identification
==
*gender ID scripts forked from [@ptigas] who doesn't seem to have this in a repo<br>
pulls names from social security "most popular US baby names" into a csv:
http://ptigas.com/blog/2012/01/21/name2gender-in-python/

Resulting HTML processed in excel: I made a pivot table to count how many years a name was a male or female name.  I assigned a gender to a name if was male or female >55% of the time; for those within the 45-55% range I left them ambiguous.
- We could possibly reduce the error if we constrain the temporal range of names a bit more; if the earliest paper in our corpus was published in 2000, then it's reasonable to say that a publishing author wouldn't be older than, say, 80, or younger than 20 -- meaning we could pull names from 1920-2000 and see if that makes gender more precise.  Might be way overthinking it though
- Could also be more conservative with the ambiguous names -- move the % to 45-55%. 

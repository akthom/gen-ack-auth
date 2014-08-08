gen-ack-auth
============
developing scripts for project studying relaitonship between authorship, acknowledgement and gender in schol comm

*AuthorAckExtract.py* : 1) this script crawls a directory containgin PMC files; mines the JATS mark up for different parts of the journal article; and then outputs this into a series of files for later processing (named entity recognition and gender ID)

input files:
*gendermatchCurl.txt* : here for provenance: this is the script used (borrowed from someone else) to DL names and genders from social security

output files:
*log.txt* : logs the efficancy of the acknowledgement extractor (or maybe more accurately, the messiness of the JATS: not all articles use the <ack> tag as the should)
*technoScienceSubsetExtraction.csv* : results from inital mass mine of a subset of journals; might be too messy to be usable right now though

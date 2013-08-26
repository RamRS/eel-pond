#! /usr/bin/env python
# take an NCBI file and make a dumpd connecting identifier with description.
from cPickle import dump
import screed
import sys

# the name-db
outfile = "names.db"
seqFile = sys.argv[1]

d = {}
e = {}
for record in screed.open(seqFile):
    if record.name.startswith('gi|'):
       ident = record.name.split('|')[3]
    else:
       ident = record.name
    d[ident] = record.description
    e[ident] = record.name

fp = open(outfile, 'w')
dump(seqFile, fp)
dump(d,fp)

fp = open('fullnames.db', 'w')
dump(e, fp)
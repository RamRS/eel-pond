import cPickle
import screed

data_names = cPickle.load('names.db')
data_fullname = cPickle.load(open('fullnames.db'))
data_seqs = screed.ScreedDB(cPickle.load('names.db'))

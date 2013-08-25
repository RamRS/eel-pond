import cPickle
import screed

data = cPickle.load('names.db')

data_names = data.get('names',[])
data_fullname = cPickle.load(open('fullnames.db'))
data_seqs = screed.ScreedDB(data.get('seqs'),[])

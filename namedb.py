import cPickle
import screed

data_names = cPickle.load(open(sys.argv[4]))
fullname = "%s.fullname" % sys.argv[4]
data_fullname = cPickle.load(open(fullname))
data_seqs = screed.ScreedDB(sys.argv[5])

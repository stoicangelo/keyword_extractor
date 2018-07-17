import sys

from nlp_rake import rake

stoppath = 'data/stoplists/SmartStoplist.txt'

rake_object = rake.Rake(stoppath, 5, 3, 4)


sample_file = open(sys.argv[1], 'r')
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Keywords:", keywords)
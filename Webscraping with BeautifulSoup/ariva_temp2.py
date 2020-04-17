import re
# regex = re.compile("test")
#if regex.search("askdtestljfaöltes"): print ("matched")

import re
regex = re.compile("^((?!Quartal).)*$")
if regex.search("guv0Quarta"): print ("matched")



#import re
#word = 'fubar'
#regexp = re.compile(r'ba[rzd]')
#if regexp.search(word):
#  print ('matched')
#print(regexp.search(word))
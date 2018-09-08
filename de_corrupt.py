'''
a script to be invoked to de corrupt a json file
it replaces the following:
]
[
with a comma :
,

the corruption results from scrapy starting a new json formatted file everytime it is invoked
'''
corrupted_json=open('data.json').read()
correct_json=corrupted_json.replace('\n][',',')
open('data.json','w').write(correct_json)
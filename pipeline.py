import os

#data collection
page_count=2
categories=['سياسة/319/','فن/48/','أخبار-الرياضة/298/','اقتصاد-وبورصة/297/','صحة-وطب/245/','علوم-و-تكنولوجيا/328/']
labels=['0','1','2','3','4','5']


command='scrapy crawl youm -o data.json -a label={} -a pages={} -a category={}'
for i in range(len(categories)):
    os.system(command.format(labels[i],page_count,categories[i]))
#data collection ended



#decorruption
corrupted_json=open('data.json').read()
correct_json=corrupted_json.replace('\n][',',')
open('data.json','w').write(correct_json)
#decorruption ended



#converting to csv, and adding the length column, and removing articles less than 150 characters in length
import json
import pandas as pd
json_data=json.loads(open('data.json').read())
df=pd.DataFrame(json_data)
df['length']=df.apply(lambda x:len(x['article']),axis=1)
df1=pd.DataFrame(df[df['length']>150])
df1.to_csv('data.csv',index=False)
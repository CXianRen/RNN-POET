'''
用于生成训练用的数据集
'''
#从数据集中提取　唐诗　－　绝句　－　五言
print("#从数据集中提取　唐诗　－　绝句　－　五言")
from config import *
import glob
import json
#from zhconv import convert
import csv

#获取目录下所有唐诗json文件
'''
glob.glob
函数功能：匹配所有的符合条件的文件，并将其以list的形式返回。跟使用windows下的文件搜索差不多。
”*”匹配0个或多个字符；
”?”匹配单个字符；
”[]”匹配指定范围内的字符，如：[0-9]匹配数字。
'''
file_path_list = glob.glob(search_path)
print("查找到的文件：",file_path_list)

'''
数据的基本格式:
{   
    "dynasty": "Ming", 
    "author": "陈献章", 
    "content": "拍月萦炉一小舟|欲穷仙岛路何由|须君一见安期老|指点苍茫为汝谋", 
    "title": "杂咏 其四", 
    "keywords": "苍茫 安期 指点 小舟"
}
我们只要绝句(只有４句)，所以我们会过滤掉　paragraphs　超过４的
并且我们要　五言绝句，　所以我们会过滤掉　首句字数超过５的
'''
poet_5jueju_objs=[]
for file_path in file_path_list:
    with open(file_path) as f:
        for line in f.readlines():
            poet=json.loads(line)
            if len(poet['content'].split('|'))==4 : #绝句
                _is5jueju=True
                for i in range(4):
                    if(len(poet['content'].replace('|',''))!=20):
                        _is5jueju=False  
                if(_is5jueju): #五言
                    #简繁体转换
                    #simple_paragraphs=[]
                    # for s in poet['paragraphs']:
                    #     simple_paragraphs.append(convert(s,'zh-hans'))
                    #poet['paragraphs']=simple_paragraphs
                    poet_5jueju_objs.append(poet)

print("共%d首"%(len(poet_5jueju_objs)))
print("提取诗句保存到:%s"%(poet_output_path))

#重新写入到文件
with open(poet_output_path,'w',encoding="utf-8") as f:
    json.dump(poet_5jueju_objs,f,sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False)


print("生成 关键词－诗 对 csv文件")
with open(poet_key_pait_path,'w',encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    for poet_obj in poet_5jueju_objs:
        pair = [poet_obj['keywords'],poet_obj['content'].replace(' ',',')]
        writer.writerow(pair)
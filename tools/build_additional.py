import json,pathlib,sys,re
sys.path.insert(0,'/tmp/hsk-python')
from PIL import Image
R=pathlib.Path(__file__).resolve().parent.parent
out={str(i):[] for i in range(1,11)}
def grouped(file):
 d={};c=0
 for row in (R/'source'/file).read_text().splitlines():
  if row.startswith('#'):c=int(row[1:]);d[c]=[]
  elif row:d[c].append(row.split('|'))
 return d
cloze=grouped('cloze.tsv');tasks=grouped('tasks.tsv')
pages=[20,31,42,54,66,78,90,102,114,127]
picwords=['申请 通知 压力','房东 毛巾 理想','结账 密码 身份证','重 心情 提','午餐 辣 汤','排队 体温 难受','调查 能力 细心','市区 景色 交通','精彩 友情 错过','暖和 浪费 后悔']
sentences='''
他想申请去中国学习。|He wants to apply to study in China.
老师正在看通知。|The teacher is reading a notice.
他的工作压力很大。|He is under great pressure at work.
房东正在介绍房子。|The landlord is showing the home.
这里有很多不同颜色的毛巾。|There are many towels in different colours here.
去这所大学学习是我的理想。|Studying at this university is my dream.
他正在用手机结账。|He is paying with his phone.
他把密码写下来了。|He wrote down the password.
她正在用身份证。|She is using her identity card.
这个东西很重，他们一起拿。|This thing is heavy; they carry it together.
她看着花，心情很好。|She looks at the flowers and feels happy.
她提着两个袋子。|She is carrying two bags.
今天的午餐有很多菜。|Today's lunch has many dishes.
这道菜看起来很辣。|This dish looks spicy.
这碗汤看起来很好喝。|This bowl of soup looks delicious.
大家都在排队。|Everyone is queuing.
他正在检查体温。|He is checking the person's temperature.
他生病了，觉得很难受。|He is ill and feels very unwell.
他们正在做调查。|They are conducting a survey.
她的工作能力很好。|She is very capable at work.
这个孩子写作业很细心。|This child is careful with homework.
市区有很多高楼。|There are many tall buildings in the city centre.
这里的景色很美。|The scenery here is beautiful.
这里交通很方便。|Transport here is convenient.
这场比赛很精彩。|This match is exciting.
她们的友情很好。|They have a close friendship.
他错过了飞机。|He missed his flight.
春天来了，天气暖和了。|Spring has arrived and the weather is warm.
不要浪费食物。|Do not waste food.
她后悔没有认真学习。|She regrets not studying seriously.
'''.strip().splitlines()
bonus={4:('中国城市中的便民服务','Convenience services in Chinese cities',55),5:('中国的地方美食','Local flavours of China',67),6:('中医与中国人的日常健康观念','Traditional Chinese medicine and everyday health beliefs',79),7:('中国职场流行语：从“小白”到“大牛”','Chinese workplace expressions: from beginner to expert',91),8:('中国长城','The Great Wall of China',103),9:('中国人的婚礼仪式','Wedding ceremonies in China',115),10:('哈尔滨的冰雪艺术',"Harbin’s ice and snow art",128)}
for c in range(1,11):
 row=cloze[c][0];z,en,*rest=row;answers=rest[-1].split();opts=rest[:-1]
 blocks=[{'heading':'Choose the appropriate content','zh':z,'en':en}]
 for i in range(4):blocks.append({'heading':chr(65+i),'zh':opts[i*2],'en':opts[i*2+1]})
 for i,a in enumerate(answers):j=ord(a)-65;blocks.append({'heading':f'Gap {i+1}','zh':f'第{i+1}空：____','en':f'Choose A, B, C or D for gap {i+1}.','input':True,'solution':a,'answers':[{'zh':opts[j*2],'en':f'{a} · {opts[j*2+1]}'}]})
 out[str(c)].append({'id':'cloze','title':'Complete the passage','intro':'Read the passage, choose from A–D, and write a letter in each box.','blocks':blocks,'sourcePages':[pages[c-1]]})
 blocks=[{'image':f'c{c}-exercise.jpg','alt':f'Original chapter {c} picture-writing exercise'}]
 for i,w in enumerate(picwords[c-1].split()):
  z,en=sentences[(c-1)*3+i].split('|');blocks.append({'heading':f'Picture {i+1}','zh':w,'en':'Write a sentence using this word and the picture.','input':True,'answers':[{'zh':z,'en':en}]})
 out[str(c)].append({'id':'picture-writing','title':'Look & write','intro':'Use the original book pictures to write your own sentences. The answers are examples; other accurate sentences are welcome.','blocks':blocks,'sourcePages':[pages[c-1]]})
 a,b,d,e,z,en=tasks[c][0]
 speaking=(R/'source/speaking.tsv').read_text().splitlines()[c-1].split('|')
 speaking_answers=[{'zh':speaking[j],'en':speaking[j+1]} for j in range(0,6,2)]
 out[str(c)].append({'id':'tasks','title':'Task-based activities','blocks':[{'heading':'Speak together','zh':a,'en':b,'input':True,'answers':speaking_answers},{'heading':'Writing · at least 120 characters','zh':d,'en':e,'input':True,'minChars':120,'answers':[{'zh':z,'en':en}]}],'sourcePages':[pages[c-1]+(1 if c in [3,4,5,9] else 0)]})
 if c in bonus:
  z,en,p=bonus[c];out[str(c)].append({'id':'bonus','title':"Xiaoyu’s bonus content",'intro':'The book gives this companion-video topic. The video itself is not embedded in the supplied PDF. Use your book’s digital resources to watch it, then keep your notes here.','blocks':[{'zh':z,'en':en}],'sourcePages':[p],'note':'My notes after watching'})
(R/'source/additional.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))

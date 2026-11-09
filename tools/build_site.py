import sys,json,pathlib,re,shutil
sys.path.insert(0,'/tmp/hsk-python')
from PIL import Image
from pypinyin import lazy_pinyin,Style,load_phrases_dict
R=pathlib.Path(__file__).resolve().parent.parent
load_phrases_dict({'还给':[['huán'],['gěi']],'了解':[['liǎo'],['jiě']],'便宜':[['pián'],['yi']],'种花':[['zhòng'],['huā']],'种树':[['zhòng'],['shù']],'长大':[['zhǎng'],['dà']],'音乐':[['yīn'],['yuè']],'快乐':[['kuài'],['lè']],'银行':[['yín'],['háng']],'出差':[['chū'],['chāi']],'一方面':[['yì'],['fāng'],['miàn']],'另一方面':[['lìng'],['yì'],['fāng'],['miàn']],'不够':[['bú'],['gòu']],'不是':[['bú'],['shì']],'一个':[['yí'],['gè']],'一会儿':[['yí'],['huì'],['r']],'一点儿':[['yì'],['diǎn'],['r']],'一下':[['yí'],['xià']],'不得':[['bù'],['dé']],'得穿':[['děi'],['chuān']],'得选择':[['děi'],['xuǎn'],['zé']],'得节约':[['děi'],['jié'],['yuē']],'不说':[['bù'],['shuō']],'咳嗽':[['ké'],['sou']],'暖和':[['nuǎn'],['huo']],'主意':[['zhǔ'],['yi']],'熟悉':[['shú'],['xī']],'好让':[['hǎo'],['ràng']],'不管':[['bù'],['guǎn']],'来得及':[['lái'],['de'],['jí']],'来不及':[['lái'],['bu'],['jí']],'受不了':[['shòu'],['bu'],['liǎo']]})
load_phrases_dict({w:[[v] for v in p.split()] for w,p in {'都会':'dōu huì','都能':'dōu néng','都要':'dōu yào','还可以':'hái kě yǐ','还要':'hái yào','还会':'hái huì','很长':'hěn cháng','更快地':'gèng kuài de','更多地':'gèng duō de','努力地':'nǔ lì de','好好地':'hǎo hǎo de','得很':'de hěn','哪儿':'nǎr','聊天儿':'liáo tiānr','点儿':'diǎnr','不了':'bu liǎo','得了':'de liǎo','难受':'nán shòu'}.items()})
def py(s):return ' '.join(lazy_pinyin(s,style=Style.TONE)).replace(' 。','。').replace(' ，','，').replace(' ？','？').replace(' ！','！')
def line(s,en=None):
 if en is None:s,en=s.split('|',1)
 return {'zh':s,'py':py(s),'en':en}
meta=[
('我们来中国学习了','We have come to China to study',11,['任何','要是……就……','随着','一方面……另一方面……']),
('租到了合适的房子','I have rented a suitable apartment',22,['就是了','……不过……','并','由于']),
('手机扫一下','Just scan with your phone',33,['……是……不过……','不仅……还……','甚至','于是']),
('很高兴能帮到你',"I’m glad I could help you",45,['动词 + 得 / 不了','再说','既……又……','来得及 / 来不及']),
('“不怕辣”和“怕不辣”','Not afraid of spicy, or afraid of not spicy?',57,['至少','够','各……各的','等']),
('我陪你去看病','I will go with you to see the doctor',69,['厉害','有什么（好……）的','偶尔','……好……']),
('在工作中学习','Learning on the job',81,['在……方面','既然……就……','拿……来说','使']),
('该放松时就放松',"Relax when it’s time to relax",93,['不管……都……','否则','跟……相比','有A有B']),
('遇见你，刚刚好','Meeting you, just perfect',105,['不……也……','尽管……但是……','此','从来']),
('南方不懂北方的冷',"Southerners just don’t get the Northern cold",117,['说什么也得','有的是','而','再次'])]
chapters=[{'id':i+1,'title':m[0],'en':m[1],'page':m[2],'grammar':m[3],'words':[],'warmup':[],'pictures':[],'questions':[],'sections':[]} for i,m in enumerate(meta)]
dictionary=json.loads((R/'source/reference-dictionary.json').read_text())
# Reuse the user's previous project's word glosses, but generate this book independently.
for c in chapters:
 c['sourceRange']=[c['page'],(chapters[c['id']]['page']-1 if c['id']<10 else 129)]
word_pinyin={'嗯':'ǹg','种':'zhòng','熟':'shú / shóu','倒':'dào','当':'dāng','转':'zhuǎn','重':'zhòng','还':'hái / huán','间':'jiān','好':'hǎo','啊':'ā','和':'hé','得':'de / dé / děi','着':'zhe','过':'guo','地':'de / dì','少':'shǎo','干':'gàn','觉':'jué','乐':'lè','长':'cháng / zhǎng'}
chapter=0
for row in (R/'source/vocabulary.tsv').read_text().splitlines():
 if row.startswith('#'):chapter=int(row[1:]);continue
 if not row:continue
 zh,en,sent,tr=row.split('|');c=chapters[chapter-1]
 gram=next((g for g in c['grammar'] if any(k in sent for k in re.split('[…… /+（）]+',g) if len(k)>1)),c['grammar'][0])
 w={'zh':zh,'en':en,'py':word_pinyin.get(zh,py(zh)),'example':line(sent,tr),'grammar':gram}
 c['words'].append(w);dictionary[zh]={'py':w['py'],'en':en,'chapter':chapter}
# Warm-up source picture order is top-left to bottom-right; only chapter 5 uses four pictures.
banks=['证件 博士 食堂 材料 教师 加油','客厅 种 收拾 毕业 厨房 价格','法律 扫码支付 网购 快递员 管 保护','袋子 感谢 早餐 乘客 鲜花 电动车','辣子鸡 红烧羊肉 松鼠鳜鱼 酸汤米线 酸 甜 咸 辣','汗 醒 护士 打针 咳嗽 大厅','市场 想法 打扰 谈 计划 出差','参观 加班 下降 风景 乘坐 帽子','浪漫 人生 巧克力 支持 耐心 祝','寒假 温度 误会 植物 拒绝 垃圾']
orders=[[4,2,5,3,0,1],[3,2,0,4,5,1],[5,1,2,3,4,0],[5,3,0,4,1,2],[2,1,3,0],[2,5,0,1,3,4],[2,5,1,3,4,0],[1,3,2,4,0,5],[4,3,0,5,1,2],[1,3,0,4,5,2]]
crop_coords={1:([255,510,760],[870,1036],170,149),2:([258,514,768],[841,1008],170,150),3:([258,512,765],[867,1033],170,150),4:([258,512,764],[837,1005],170,150),5:([139,375,612,848],[902],165,149),6:([254,508,762],[839,1005],169,150),7:([254,496,737],[864,1030],160,148),8:([253,500,744],[858,1026],162,149),9:([238,495,749],[839,1007],170,149),10:([253,504,751],[872,1040],166,149)}
extras={'扫码支付':'scan a code to pay','快递员':'delivery worker','辣子鸡':'spicy chicken','红烧羊肉':'red-braised lamb','松鼠鳜鱼':'squirrel-shaped mandarin fish','酸汤米线':'rice noodles in sour soup','甜':'sweet'}
for w,en in extras.items():dictionary[w]={'py':py(w),'en':en}
raw_warm='''
她是一位教师。|She is a teacher.
我们在食堂吃饭。|We eat in the dining hall.
大家给他们加油。|Everyone cheers them on.
这些材料很多。|There are a lot of these materials.
他给我们看证件。|He shows us his identity documents.
他是一位博士。|He has a doctorate.
他们毕业了。|They have graduated.
她在收拾房间。|She is tidying the room.
客厅里有沙发。|There is a sofa in the living room.
厨房很干净。|The kitchen is clean.
这些东西的价格不同。|These items have different prices.
他在种树。|He is planting a tree.
我们要保护家人。|We need to protect our family.
她用手机扫码支付。|She scans a code with her phone to pay.
她在网购。|She is shopping online.
快递员在工作。|The delivery workers are working.
妈妈在管孩子。|The mother is managing her child.
法律很重要。|The law is important.
这是一辆电动车。|This is an electric bike.
车上有很多乘客。|There are many passengers on the train.
这个袋子很好看。|This bag looks nice.
这些鲜花很好看。|These flowers are pretty.
她感谢大家。|She thanks everyone.
桌子上有很多早餐。|There is a lot of breakfast food on the table.
这个松鼠鳜鱼又酸又甜。|This squirrel-shaped mandarin fish is sour and sweet.
这个红烧羊肉是咸的。|This red-braised lamb is savoury.
这个酸汤米线是酸的。|These rice noodles in sour soup are sour.
这个辣子鸡很辣。|This spicy chicken is hot.
护士在工作。|The nurse is working.
大厅里没有人。|There is nobody in the lobby.
他出了很多汗。|He is sweating a lot.
他刚醒。|He has just woken up.
她在打针。|She is getting an injection.
他在咳嗽。|He is coughing.
孩子在打扰妈妈。|The child is disturbing his mother.
他要去出差。|He is leaving on a business trip.
他有一个想法。|He has an idea.
他们在谈工作。|They are talking about work.
他写好了计划。|He has written the plan.
市场里有很多东西。|There are many things in the market.
他们晚上还在加班。|They are still working overtime at night.
这里的风景很好。|The scenery here is beautiful.
这里的价格下降了。|The prices here have fallen.
她乘坐火车。|She is taking a train.
他们在参观。|They are visiting a place.
这里有帽子。|There are hats here.
她很有耐心。|She is patient.
大家互相支持。|Everyone supports one another.
他们很浪漫。|They are romantic.
他们祝他生日快乐。|They wish him a happy birthday.
人的年龄随着人生变化。|A person's age changes through life.
盘子里有巧克力。|There is chocolate on the plate.
今天温度很高。|The temperature is high today.
这里有很多植物。|There are many plants here.
寒假他们去外面玩。|They go out to play during winter vacation.
他拒绝了。|He refused.
这里有很多垃圾。|There is a lot of rubbish here.
他们之间有误会。|There is a misunderstanding between them.
'''.strip().splitlines()
wi=0
for c,bank,order in zip(chapters,banks,orders):
 c['warmup']=[{'zh':w,**dictionary[w]} for w in bank.split()]
 xs,ys,w,h=crop_coords[c['id']];im=Image.open(f'/tmp/hsk-scan-{c["page"]:03}.jpg')
 for i,(y,x) in enumerate((y,x) for y in ys for x in xs):
  name=f'c{c["id"]}-warm-{i+1}.jpg';im.crop((x,y,x+w,y+h)).save(R/'site/assets'/name,quality=95)
  p={'image':name,'answer':order[i],'sentence':line(raw_warm[wi])};wi+=1
  if c['id']==5:p['flavors']=[[4,5],[6],[4],[7]][i]
  c['pictures'].append(p)
for p in range(11,130):shutil.copyfile(f'/tmp/hsk-scan-{p:03}.jpg',R/'site/assets'/f'page-{p}.jpg')
# Author-reviewed questions and responses.
qs=(R/'source/questions.tsv').read_text().strip().splitlines()
for row in qs:
 if row.startswith('#'):c=chapters[int(row[1:])-1];continue
 parts=row.split('|');q=line(parts[0],parts[1]);q['answers']=[line(parts[i],parts[i+1]) for i in range(2,8,2)];c['questions'].append(q)
# Sections are built from editorial source files, one block per Chinese/English pair.
for file in ['sections.json']:
 if (R/'source'/file).exists():
  sections=json.loads((R/'source'/file).read_text())
  for c in chapters:c['sections']=sections[str(c['id'])]
def enrich(o):
 if isinstance(o,dict):
  if o.get('zh') and 'py' not in o:o['py']=py(o['zh'])
  for v in o.values():enrich(v)
 elif isinstance(o,list):
  for v in o:enrich(v)
enrich(chapters)
for c in chapters:
 for section in c['sections']:
  for b in section.get('blocks',[]):
   for a in b.get('answers',[]):
    if a.get('en','').startswith('Answer: '):a['en']=dictionary.get(a['zh'],{}).get('en',a['en'])
# Complete missing dictionary entries only from the curated phrase supplement.
if (R/'source/dictionary-extra.tsv').exists():
 for row in (R/'source/dictionary-extra.tsv').read_text().splitlines():
  if '|' in row:
   w,en=row.split('|',1);dictionary[w]={'py':word_pinyin.get(w,py(w)),'en':en}
for w,p in word_pinyin.items():
 if w in dictionary:dictionary[w]['py']=p
out={'title':'New HSK Course 4A','chapters':chapters,'dictionary':dictionary}
(R/'site/data.js').write_text('window.HSK_DATA = '+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n')
(R/'source/course.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('Built',len(chapters),'chapters,',sum(len(c['words']) for c in chapters),'words,',sum(len(c['pictures']) for c in chapters),'pictures')

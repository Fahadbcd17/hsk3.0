"""Reviewed textbook content for lessons 14–16; generated examples are labelled models."""
import json,re
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parent.parent
META={c['id']:c for c in json.loads((R/'source/4b/meta.json').read_text())}
def L(z,e):return {'zh':z,'en':e}
def pairs(s):return [L(*r.split('|',1)) for r in s.strip().splitlines() if r]
def make(n):
 c=dict(META[n]);c.update(book='4B',sourceRange=[c['page'],META.get(n+1,{'page':128})['page']-1],words=[],warmup=[],pictures=[],questions=[],sections=[]);return c
def section(c,id,title,blocks,pages,intro=None,note=None):
 s={'id':id,'title':title,'blocks':blocks,'sourcePages':pages}
 if intro:s['intro']=intro
 if note:s['note']=note
 c['sections'].append(s);return s
def words(c,s,g=0):
 for row in s.strip().splitlines():
  w,e,z,tr=row.split('|');c['words'].append(dict(zh=w,en=e,example=L(z,tr),grammar=c['grammar'][g]))
def warm(c,s,order,page,coords):
 c['warmup']=pairs(s);im=Image.open(R/f'assets/4b/page-{page:03}.jpg')
 for i,(a,box) in enumerate(zip(order,coords)):
  path=f'4b/c{c["id"]}-warm-{i}.jpg';im.crop(box).save(R/'assets'/path,quality=92)
  c['pictures'].append({'image':path,'answer':a,'sentence':{}})
def warm_sent(c,s):
 for p,l in zip(c['pictures'],pairs(s)):p['sentence']=l
 def_unused=0
def discussion(c,z,e,models):c['questions'].append(dict(**L(z,e),answers=pairs(models)))
def listening(c,rows):
 blocks=[]
 for i,row in enumerate(rows.strip().splitlines()):
  z,e,opts,translations,key=row.split('|');zs=opts.split('/');es=translations.split('/');j=ord(key)-65
  blocks.append(dict(**L(z,e),heading=f'Choose the answer · Text {i//2+1}, question {i%2+1}',choices=[L(a,b)for a,b in zip(zs,es)],answers=[L(zs[j],key+' · '+es[j])],input=True,solution=key))
 section(c,'listening','Listen / read & choose',blocks,[])
def text(c,n,body,questions,pages,retell=None):
 blocks=pairs(body)
 for i,row in enumerate(questions.strip().splitlines()):
  z,e,a,ae=row.split('|');blocks.append(dict(**L(z,e),heading=f'Read & answer {i+1}',input=True,answers=[L(a,ae)]))
 s=section(c,f'text{n}',f'Text {n}',blocks,pages,'Role-play the dialogue.' if n<3 else 'Read the text aloud.','Retell this text in your own words')
 if retell:
  z,e,a,ae,p=retell;s['retelling']={'pages':p,'prompt':L(z,e),'answer':L(a,ae)}
 return s
def grammar(c,n,explanation,examples,practice,pages):
 blocks=pairs(examples)
 for i,row in enumerate(practice.strip().splitlines()):
  z,e,a,ae=row.split('|');blocks.append(dict(**L(z,e),heading=f'Book practice · {i+1}',input=True,answers=[L(a,ae)]))
 section(c,f'grammar{n}',f'Grammar {n} · {c["grammar"][n-1]}',blocks,pages,explanation,'My sentence using this grammar')
def gaps(c,rows,pages):
 banks={14:['暂时|temporarily\n表示|state\n减|reduce\n态度|attitude\n两|liang; 50 grams\n缺|be short of','许多|many\n者|person; suffix\n不光|not only\n分为|divide into\n友好|friendly\n顾客|customer'],15:['考虑|consider\n笔试|written exam\n不论|regardless of\n消息|news\n肯定|certainly\n负责人|person in charge','能够|be able to\n理发|get a haircut\n答案|answer\n工厂|factory\n激动|excited\n职业|career'],16:['等到|wait until\n关键|key\n例子|example\n本来|originally\n确实|indeed\n可惜|a pity','约|arrange to meet\n标准|standard\n相反|opposite\n详细|detailed\n无法|unable\n一切|everything']}
 originals={14:[
 ('这家饭馆不仅菜好吃，服务员服务____也特别好，所以我们经常来。','This restaurant has delicious food and excellent service ____, so we come often.'),
 ('茶叶一次不用买太多，买六____就够喝一段时间了。','There is no need to buy too much tea; six ____ will last a while.'),
 ('马上到景区了，大家准备下车，不需要的东西可以____放在车上。','We are arriving at the scenic area. Prepare to get off; unneeded items can be left on the bus ____.'),
 ('网上商店正在做活动，除了直接降价外，还有满100____30的活动，挺值的。','The online shop has price reductions and a spend-100, take-30-____ offer; it is good value.'),
 ('我要买的那个手机现在____货，过几天再去看看来没来货。','The phone I want is out of ____; I will check again in a few days.'),
 ('高医生____，病人过几天如果没什么问题就可以出院了。','Dr Gao ____ that the patient can leave hospital in a few days if there are no problems.'),
 ('A：您的学生学习都很好！B：是的，他们____学习成绩优秀，还经常帮助别人。','A: Your students all study well! B: Yes, they ____ get excellent grades but also often help others.'),
 ('A：这家店人真多！B：嗯，他们的商品种类多、价格合适，服务还特别好，所以很多____都喜欢来这里买东西。','A: This shop is crowded! B: It offers variety, suitable prices and excellent service, so many ____ enjoy shopping here.'),
 ('A：您能简单介绍一下武汉长江大桥吗？B：这座桥全长1670米，____上下两层，是长江上的第一座大桥。','A: Could you introduce the Wuhan Yangtze River Bridge? B: It is 1,670 metres long, ____ two levels, and was the first bridge over the Yangtze.'),
 ('A：这个动物园虽然比较远，但动物特别多，有____我以前没见过的动物。B：是吗？有机会我也去看看。','A: This zoo is far away but has many animals, including ____ I have never seen. B: Really? I will visit when I can.'),
 ('A：你这次去那儿玩感觉怎么样？B：挺不错的，那里的人都很热情、____，也给了我们很多帮助。','A: How was your visit? B: Good; the people were welcoming and ____, and helped us a lot.'),
 ('A：电子邮件发出后，我才发现会议时间写错了。B：那你快给参会____重新发邮件，向他们道歉，并告诉他们正确的时间。','A: After sending the email, I noticed the meeting time was wrong. B: Email the meeting particip____ again, apologise and give the correct time.')],
 15:[
 ('你这么努力，这次考试____能通过。','You work so hard; you will ____ pass this exam.'),
 ('您有什么问题，可以直接跟____联系。','For any questions, contact the ____ directly.'),
 ('____你同不同意，我都会按照计划去做。','____ you agree or not, I will follow the plan.'),
 ('这件事比较重要，我需要再认真____一下。','This is important; I need to ____ it carefully again.'),
 ('我们要先进行____，了解一下大家的专业能力。','We first hold a ____ to assess professional abilities.'),
 ('我已经等了好几天了，还是没有收到他的____。','I have waited several days but still have no ____ from him.'),
 ('A：你知道这道题的____吗？B：知道，我已经写在纸上了。','A: Do you know the ____ to this question? B: Yes, I have written it down.'),
 ('A：听说你获得奖学金了？B：是的，我____得昨天晚上都没睡好。','A: I heard you won a scholarship? B: Yes, I was so ____ that I slept badly last night.'),
 ('A：你现在中文说得怎么样了？B：我已经____和中国朋友进行简单交流了。','A: How is your Chinese now? B: I am ____ to communicate simply with Chinese friends.'),
 ('A：下午我去____，你想跟我一起去吗？B：好呀，我最近头发有点儿长了，正好下午有时间。','A: I am getting a ____ this afternoon. Want to come? B: Yes, my hair is long and I am free then.'),
 ('A：你对自己的____发展有什么打算？B：我希望先去大公司工作，积累一些经验，然后自己开一家公司。','A: What are your ____ plans? B: I hope to gain experience at a large company before starting my own.'),
 ('A：听说你哥哥换工作了，他现在在哪儿工作？B：他现在在一家____工作，主要负责检查产品的质量。','A: Where does your brother work after changing jobs? B: At a ____, mainly checking product quality.')]
 }
 b=[]
 for i,r in enumerate(rows.strip().splitlines()):
  z,e,a,ae=r.split('|')
  if c['id'] in originals:z,e=originals[c['id']][i]
  if i%6==0:
   bank=pairs(banks[c['id']][i//6]);b.append(dict(**L('　'.join(chr(65+j)+' '+o['zh'] for j,o in enumerate(bank)),' · '.join(chr(65+j)+' '+o['en'] for j,o in enumerate(bank))),heading=f'Word bank · questions {i+1}–{i+6}'))
  b.append(dict(**L(z,e),heading=f'Fill in the blank · {i+1}',input=True,solution=a,answers=[L(a,ae)]))
 section(c,'exercises','Comprehensive exercises',b,pages,'Choose from the word banks in the original exercise. Each word is used once in its group.')
def cloze(c,z,e,opts,solution,pages):
 options=pairs(opts);blocks=[L(z,e)]+[dict(**o,heading=chr(65+i))for i,o in enumerate(options)]
 for i,k in enumerate(solution):blocks.append(dict(**L(f'第{i+1}空：____',f'Gap {i+1}: choose A, B, C or D.'),input=True,solution=k,answers=[dict(options[ord(k)-65])]))
 section(c,'cloze','Complete the passage',blocks,pages)
def picture(c,page,box,rows):
 path=f'4b/c{c["id"]}-exercise.jpg';Image.open(R/f'assets/4b/page-{page:03}.jpg').crop(box).save(R/'assets'/path,quality=92)
 blocks=[{'image':path,'alt':f'Original chapter {c["id"]} picture-writing exercise'}]
 for i,r in enumerate(rows.strip().splitlines()):
  z,e,a,ae=r.split('|');blocks.append(dict(**L(z,e),heading=f'Picture {i+1}',input=True,answers=[L(a,ae)]))
 section(c,'picture-writing','Look & write',blocks,[page])
def tasks(c,z,e,models,w,we,answer,ae,pages):
 section(c,'tasks','Task-based activities',[dict(**L(z,e),heading='Speak together',input=True,answers=pairs(models)),dict(**L(w,we),heading='Writing · at least 140 characters',input=True,minChars=140,answers=[L(answer,ae)])],pages)
def extra(c,id,title,lines,pages):return section(c,id,title,pairs(lines),pages)
def finish(c):
 if c['id']==16:
  for w in c['words']:
   z=w['example']['zh'];w['grammar']=c['grammar'][3] if '却' in z else c['grammar'][1] if '并且' in z else c['grammar'][2] if '说不定' in z else c['grammar'][0]
 assert len(c['questions'])==2 and len(c['pictures'])==6
 assert len(next(s for s in c['sections']if s['id']=='listening')['blocks'])==8
 for s in c['sections']:
  for b in s['blocks']:
   if b.get('minChars'):assert len(re.findall('[\u3400-\u9fff]',b['answers'][0]['zh']))>=b['minChars']
 (R/f'source/4b/chapters/{c["id"]}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print(c['id'],len(c['words']),len(c['sections']))
c=make(14)
words(c,'''茶叶|tea leaves|你究竟想买哪种茶叶？|Which tea leaves exactly do you want to buy?
究竟|exactly; after all|你究竟想买什么？|What exactly do you want to buy?
分为|divide into|这些东西究竟分为几种？|How many kinds exactly are these things divided into?
抱歉|sorry|你究竟为什么觉得抱歉？|What exactly are you sorry about?
暂时|temporarily|他究竟为什么暂时不来了？|Why exactly is he not coming for now?
满|reach a limit; full|这个班究竟满了没有？|Is this class full or not?
两|liang; 50 grams|你究竟要买几两茶？|How many liang of tea exactly do you want?
超过|exceed|人数究竟超过一百了没有？|Has the number of people exceeded one hundred?
盒子|box|你究竟把盒子放在哪里了？|Where exactly did you put the box?
装|put into; pack|你究竟把衣服装在哪里了？|Where exactly did you pack the clothes?
各位|everyone; ladies and gentlemen|各位究竟想先看什么？|What exactly would everyone like to see first?
顾客|customer|这位顾客究竟需要什么？|What exactly does this customer need?
本|this; our own|本店究竟几点关门？|What time exactly does our shop close?
假日|holiday|这个假日你究竟去不去？|Are you going this holiday or not?
低价|low price|这件低价的衣服究竟好不好？|Is this low-priced item of clothing good or not?
促销|promote sales|这次促销究竟到什么时候结束？|When exactly does this promotion end?
广播|broadcast|广播里究竟说了什么？|What exactly did the broadcast say?
减|reduce; subtract|价格究竟减了多少？|How much exactly was the price reduced?
广告|advertisement|这个广告究竟是什么意思？|What exactly does this advertisement mean?
首先|first|你究竟想首先做什么？|What exactly would you like to do first?
牌子|brand|你究竟喜欢哪个牌子？|Which brand exactly do you like?
降价|reduce the price|这件衣服究竟降价了没有？|Has this item of clothing been reduced in price?
样式|style|你究竟喜欢哪种样式？|Which style exactly do you like?
价钱|price|这个东西的价钱究竟是多少？|What exactly is the price of this item?
商业|business; commerce|商业区究竟在哪里？|Where exactly is the business district?
商品|goods; product|你究竟想看哪种商品？|Which kind of product exactly do you want to see?
种类|type; kind|这些东西究竟有多少种类？|How many kinds of these things are there?
盲盒|blind box|这个盲盒里究竟是什么？|What exactly is inside this blind box?
缺|lack; be short of|家里究竟缺什么东西？|What exactly is missing at home?
许多|many|许多人究竟为什么喜欢来这里？|Why exactly do so many people like coming here?
表示|express; indicate|他说的话究竟表示什么意思？|What exactly do his words mean?
加上|in addition; plus|加上车票，究竟要多少钱？|Including the ticket, how much exactly does it cost?
态度|attitude|他的态度究竟怎么样？|What exactly is his attitude like?
友好|friendly|他究竟对谁不友好？|Who exactly is he unfriendly to?
使得|cause; make|什么究竟使得他这么高兴？|What exactly made him so happy?
者|person who; -er|这位工作者究竟是谁？|Who exactly is this worker?
仔细|careful|你究竟仔细看过没有？|Have you actually looked carefully?
对于|regarding|对于这件事，你究竟怎么想？|What exactly do you think about this matter?
不光|not only|他不光会中文，究竟还会什么语言？|Besides Chinese, what other languages exactly does he know?
外套|coat|这件外套究竟是谁的？|Whose coat exactly is this?
袜子|socks|我的袜子究竟在哪里？|Where exactly are my socks?''')
warm(c,'盒子|box\n茶叶|tea leaves\n降价|price reduction\n外套|coat\n装|pack\n抱歉|sorry',[1,2,0,5,4,3],42,[(276,844,434,994),(517,844,675,994),(758,844,920,994),(276,1013,434,1165),(517,1013,675,1165),(758,1013,920,1165)])
warm_sent(c,'''这些茶叶闻起来很香。|These tea leaves smell fragrant.
这件衣服降价了。|This item of clothing has been reduced in price.
这里有一个空盒子。|There is an empty box here.
她对朋友说抱歉。|She says sorry to her friend.
他把食物装进袋子里。|He puts the food in a bag.
这件红色外套很好看。|This red coat looks nice.''')
discussion(c,'当你想买一个东西时，会不会等它降价的时候才买？','When you want something, do you wait until its price drops?','''会，我想先等一等，这样能少花一点儿钱。|Yes. I wait so I can spend less.
如果现在就需要，我不会等。|If I need it now, I will not wait.
我会先比较价格，再决定什么时候买。|I compare prices before deciding when to buy.''')
discussion(c,'买东西时，你觉得质量和价格哪个更重要？','When shopping, which matters more: quality or price?','''我觉得质量更重要，因为好的东西可以用很久。|Quality matters more because good things last longer.
对我来说，价格也很重要，我没有很多钱。|Price matters too because I do not have much money.
两个都重要，我想买质量好、价格合适的东西。|Both matter. I want good quality at a suitable price.''')
listening(c,'''安妮想知道什么？|What does Annie want to know?|红茶的价格/绿茶的价格/有没有红茶/买哪种茶合适|the price of black tea/the price of green tea/whether black tea is available/which tea to buy|D
安妮最后买了什么？|What did Annie finally buy?|半两绿茶/五两绿茶/六两绿茶/一斤绿茶|half a liang of green tea/five liang of green tea/six liang of green tea/one jin of green tea|C
商场做的运动鞋促销活动是什么？|What is the sports-shoe promotion?|打一折/打五折/打七折/打八五折|90% off/50% off/30% off/15% off|B
关于运动鞋，王一飞更重视什么？|What does Wang Yifei care more about in sports shoes?|价格高不高/质量好不好/降价没降价/好看不好看|whether they are expensive/whether quality is good/whether the price fell/whether they look nice|B
徐前店里卖的东西怎么样？|What are the goods in Xu Qian’s shop like?|不是很多/都很便宜/种类很多/只有游戏机|not many/all cheap/many types/only game consoles|C
来徐前店里的顾客主要是谁？|Who mainly shops at Xu Qian’s shop?|小孩子/年轻人/中年人/老年人|children/young people/middle-aged people/older people|B
冷静购物者买东西时会怎么做？|What do careful shoppers do?|想买就买/喜欢就买/需要才买/很少买东西|buy whenever they want/buy what they like/buy only when needed/rarely shop|C
买东西时王一飞会怎么做？|How does Wang Yifei shop?|只看广告/问售货员/比较一下就买/仔细比较后才买|only look at adverts/ask sales staff/buy after a quick comparison/buy only after careful comparison|D''')
text(c,1,'''售货员：您要什么茶？|Salesperson: What tea would you like?
安妮：我先看看。这里茶叶这么多，究竟买哪种好呢？|Annie: I’ll look first. There is so much tea here—which kind should I buy?
售货员：茶叶主要分为红茶、绿茶等，看您喜欢喝哪种。|Salesperson: Tea is mainly divided into black tea, green tea and so on. It depends on what you like.
安妮：我想买一些自己喝，再买些送人。这种绿茶还有吗？|Annie: I want some for myself and some as gifts. Do you still have this green tea?
售货员：抱歉，暂时没有。如果自己喝，可以买这个绿茶，今天满二两送半两，超过半斤再送小礼物；如果送人，可以买个盒子装进去。|Salesperson: Sorry, it is temporarily unavailable. For yourself, you could buy this green tea: buy two liang today and get half a liang free, plus a gift for purchases over half a jin. For a gift, you can buy a box to pack it in.
安妮：嗯。那就先买六两这种绿茶吧，再买一个盒子。请帮我分着装，盒子里装半斤，剩下的用纸包一下就行。|Annie: Then I’ll buy six liang of this green tea and a box. Please pack them separately: half a jin in the box and the rest wrapped in paper.''','''安妮为什么要买茶叶？|Why does Annie buy tea?|她想买一些自己喝，再买些送人。|She wants some for herself and some as gifts.
关于买茶叶送人，售货员有什么建议？|What does the salesperson suggest for tea gifts?|可以买个盒子把茶叶装进去。|She can buy a box to put the tea in.''',[43,44],('安妮到茶叶店买茶叶，售货员问她……。她不知道究竟买……，售货员向她介绍了不同的茶叶。安妮想买一些茶……，再……。但她想买的一种绿茶……。售货员向她介绍说，自己喝的话，可以……，今天……，超过半斤再送……；送人的话，可以买个……。安妮最后买了……，盒子里……，……用纸包起来了。','Annie went to buy tea. The assistant asked…. She was unsure which…. She wanted tea for … and…. The desired green tea was…. The assistant recommended … and explained the offer…. Annie bought …, put … in a box and wrapped … in paper.','安妮到茶叶店买茶，想买一些自己喝，再买些送人。她想买的绿茶暂时没有。售货员推荐另一种绿茶，今天满二两送半两，超过半斤还有小礼物；送人的茶可以装进盒子。安妮最后买了六两绿茶和一个盒子，盒子里装半斤，剩下的用纸包起来。','Annie wanted tea for herself and gifts. Her chosen tea was unavailable. The assistant recommended another green tea with a buy-two-liang, get-half-free offer and a gift for purchases over half a jin. Annie bought six liang and a box, packing half a jin in the box and wrapping the rest in paper.',[44]))
grammar(c,1,'究竟 is used in questions to press for the truth or a definite answer.','''这里茶叶这么多，究竟买哪种好呢？|There is so much tea here; which kind should I buy?
我一直没找到他，他究竟去哪里了呢？|I still cannot find him. Where exactly has he gone?
究竟是对还是错？我现在也不清楚。|Is it right or wrong? I am not sure either.''','''A：这件衣服她究竟____呢？ B：她说她很喜欢。|A: What does she really think of this clothing? B: She says she likes it.|喜不喜欢|whether she likes it
A：你____？ B：我快写完了，请再等两天。|A: Ask when the work will be finished. B: I have almost finished; please wait two more days.|究竟什么时候能写完|When exactly can you finish writing?
A：____？ B：我还没决定，我再想想吧。|A: Ask for a definite choice. B: I have not decided; let me think.|你究竟想买哪一个|Which one exactly do you want to buy?''',[44])
text(c,2,'''广播员：各位顾客，本商场正在举办运动鞋假日低价促销活动，全场五折。|Announcer: Dear customers, our mall is holding a holiday sports-shoe sale, with everything at half price.
王一雪：一飞，广播里说价格减了一半呢，咱们过去看看？|Wang Yixue: Yifei, the announcement says prices are halved. Shall we look?
王一飞：好的。不过咱们也不能只听广告说什么，还得看质量。|Wang Yifei: Yes, but we cannot only listen to advertising; we must check quality.
王一雪：对，首先看样子喜不喜欢，然后再看质量怎么样、价格合适不合适。|Wang Yixue: Right. First see whether we like the style, then check quality and price.
售货员：二位看看喜欢哪双？这个牌子质量很好，今天又降价，一双减300块。|Salesperson: Which pair do you like? This brand is good quality and is reduced by 300 yuan per pair today.
王一雪：嗯，我知道这个牌子。一飞，你喜欢吗？你看，这个鞋的样式很新，价钱也不高。|Wang Yixue: I know this brand. Yifei, do you like it? The style is new and the price is not high.
王一飞：你喜欢就买吧。我再看看别的。|Wang Yifei: Buy it if you like it. I’ll look at others.
王一雪：好的。请给我拿一双37号的吧。|Wang Yixue: All right. Please bring me a size 37 pair.''','''听了广播后，王一雪为什么要过去看看？|Why does Wang Yixue want to look after hearing the announcement?|因为运动鞋的价格减了一半。|Because sports shoes are half price.
王一雪是怎么决定买那双运动鞋的？|How does she decide to buy those shoes?|她知道这个牌子，觉得样式很新，质量好，价钱也不高。|She knows the brand and finds the style new, quality good and price low.''',[45,46])
grammar(c,2,'首先……然后／其次…… expresses sequence or the distinction between primary and secondary points.','''首先看样子喜不喜欢，然后再看质量怎么样、价格合适不合适。|First consider the style, then the quality and price.
遇到问题，首先想想问题为什么出现，然后再积极想办法解决。|When problems arise, first consider their cause, then actively seek a solution.
请大家首先读一遍课文，然后根据课文完成课后练习。|First read the text once, then complete the exercises based on it.''','''A：请说说你们的计划。 B：我们的计划是，首先去做市场调查，____。|Explain the next step after market research.|然后根据结果准备材料|then prepare materials based on the results
A：你们寒假是怎么安排的？ B：____；其次，____。|Describe two winter-holiday arrangements.|首先我们要复习功课；其次，我们想去看家人|First we will review our lessons; then visit our families.
A：能谈谈你为什么觉得自己适合这份工作吗？ B：首先我的专业是儿童教育，____。|Add a second reason for being suitable for the job.|其次我很喜欢和孩子们在一起|Second, I enjoy spending time with children.''',[46])
s=text(c,3,'''李文的朋友徐前在商业区开了家小店，专门卖年轻人喜欢的东西。他的店里商品种类不少，既有几十年前的老游戏机，也有最近流行的盲盒等等，很吸引年轻人。|Li Wen’s friend Xu Qian opened a small shop in a business district selling things young people like. It offers many kinds of goods, from old game consoles to fashionable blind boxes, attracting young customers.
徐前说，自己就是年轻人，知道年轻人喜欢什么。他也常和来店里的年轻顾客聊天儿，了解他们的兴趣爱好。前段时间刚进的盲盒很快就卖到了缺货。许多年轻人表示，在徐前的店里能感受到快乐。小店虽然小，但东西适合年轻人，加上店员态度友好，使得小店的生意越来越好。李文觉得自己的朋友真会做生意。|Xu says that as a young person he knows young people’s tastes. He often talks with customers to learn their interests. Newly stocked blind boxes quickly sold out. Customers say the shop makes them happy. Suitable goods and friendly staff have made business increasingly successful. Li thinks his friend is good at business.''','''年轻人为什么喜欢徐前店里的东西？|Why do young people like the shop’s goods?|因为商品种类多，适合年轻人的兴趣爱好。|Because there is variety and the goods match young people’s interests.
徐前店里的生意做得怎么样？|How is business at Xu’s shop?|生意越来越好，盲盒很快就卖到了缺货。|Business is improving; blind boxes quickly sold out.''',[47,48],('李文的朋友徐前在商业区……，专门卖……。他的店里商品……，既有几十年前的……，也有……等等，很吸引年轻人。徐前说，自己……，知道年轻人……。他也常和来店里的……，了解……。前段时间刚进的盲盒很快就……。许多年轻人表示，在徐前的店里能……。小店虽然小，但东西……，加上店员……，使得小店的生意……。李文觉得自己的朋友……。','Complete the account of Xu’s shop: its location, products, customers, sold-out blind boxes, friendly staff and successful business.','徐前在商业区开了家小店，专门卖年轻人喜欢的东西。店里既有老游戏机，也有流行的盲盒。他自己就是年轻人，也经常和顾客聊天儿，所以知道他们的兴趣爱好。盲盒很快就卖到了缺货。东西适合年轻人，加上店员态度友好，使得生意越来越好。李文觉得徐前很会做生意。','Xu opened a shop in a business district for young customers, selling old game consoles and popular blind boxes. As a young person who talks with customers, he understands their interests. Blind boxes sold out quickly. Suitable products and friendly staff made business improve. Li thinks Xu is skilled at business.',[48]))
grammar(c,3,'加上 adds another factor to the previous clause, leading to a result.','''小店虽然小，但东西适合年轻人，加上店员态度友好，使得小店的生意越来越好。|The shop is small, but suitable goods and friendly staff make business improve.
虽然这里是郊区，但周围交通很方便，加上房租便宜，所以很多年轻人都在这里租房子。|Although it is outside the city, convenient transport and cheap rent attract young renters.
他很聪明，加上一直非常努力，所以最后考上了理想的大学。|He is intelligent and consistently hardworking, so he entered his ideal university.''','''这些茶叶闻着很香，____，我一下就买了两斤。（促销）|The tea smells fragrant; add a reason involving a promotion.|加上商店正在促销|and the shop was running a promotion
这个话剧很有名，____，来剧院看演出的观众____。（超过）|Add a reason and a result using “exceed”.|加上票价不高；超过了一千人|and tickets are inexpensive; exceeded one thousand
这位售货员很专业，____，很快就卖出去了好几个手机。（态度）|Add a reason about attitude.|加上态度友好|and has a friendly attitude''',[48])
text(c,4,'''关于购物，你是一位冷静购物者，还是不冷静购物者？一般来说，冷静购物者往往是真正需要一件东西时才买。购买时，还会从质量、价格等各方面仔细比较。不冷静购物者看见一个东西时，只要感觉喜欢就买，不管需要不需要，结果常常买完就后悔，买的东西也成了“垃圾”，还不环保。王一飞说，她从来不随便买东西。对于想买的东西，她不光看质量，还看价格。无论是一件外套，还是一条裤子，甚至一双袜子，都是仔细比较后才决定买不买。|Are you a careful or impulsive shopper? Careful shoppers buy only when something is genuinely needed and compare quality, price and other factors. Impulsive shoppers buy what they like regardless of need, often regretting it and creating waste. Wang Yifei never buys casually. She checks both quality and price, carefully comparing even coats, trousers and socks before deciding.
其实，不仅是买东西，人生的很多事情都一样，选择合适的才是最好的。|This applies not only to shopping but to many things in life: choosing what suits you is best.''','''冷静购物者和不冷静购物者最大的不同是什么？|What is the main difference between careful and impulsive shoppers?|冷静购物者需要才买，不冷静购物者喜欢就买。|Careful shoppers buy when needed; impulsive shoppers buy when they like something.
王一飞是冷静购物者吗？为什么？|Is Wang Yifei a careful shopper? Why?|是，她仔细比较质量和价格后才决定买不买。|Yes. She compares quality and price before deciding.''',[49,50])
grammar(c,4,'对于 introduces the specific person, matter or object that an action or opinion concerns.','''对于想买的东西，她不光看质量，还看价格。|For things she wants to buy, she checks both quality and price.
对于他的做法，大家都很支持。|Everyone supports his approach.
对于你们提的这个建议，我们一定好好研究。|We will carefully study your suggestion.''','''对于这份工作，____。|Complete your view of this job.|我很感兴趣|I am very interested
____，你们觉得怎么样？|Introduce a matter to ask about.|对于这个计划|Regarding this plan
____购物，你是想____还是____？|Ask about shopping preferences using 对于.|对于；去商场买；在网上买|Regarding shopping, would you like to shop at a mall or online?''',[50])
gaps(c,'''这家饭馆不仅菜好吃，服务员服务____也特别好。|This restaurant has good food and staff service ____.|态度|attitude
茶叶一次不用买太多，买六____就够喝一段时间了。|Buying six ____ of tea is enough for a while.|两|liang; 50-gram units
马上到景区了，不需要的东西可以____放在车上。|Unneeded items can be left on the bus ____.|暂时|temporarily
网上商店有满100____30的活动。|The online shop offers 30 yuan ____ for every 100 yuan spent.|减|off; reduced
我要买的那个手机现在____货。|The phone I want is out of ____.|缺|lack; be short of
高医生____，病人过几天就可以出院了。|Dr Gao ____ that the patient can leave hospital in a few days.|表示|stated
他们____学习成绩优秀，还经常帮助别人。|They ____ get excellent grades but also help others.|不光|not only
很多____都喜欢来这里买东西。|Many ____ enjoy shopping here.|顾客|customers
这座桥全长1670米，____上下两层。|The bridge is 1,670 metres long and ____ two levels.|分为|divided into
有____我以前没见过的动物。|There are ____ animals I have never seen before.|许多|many
那里的人都很热情、____。|People there are welcoming and ____.|友好|friendly
你快给参会____重新发邮件。|Send the meeting particip____ another email.|者|participant suffix''',[50,51])
cloze(c,'吴红在一家公司上班，工资挺高的。和许多女孩子一样，她喜欢买衣服。____，她的想法是：不需要的就不买，只买对的，不买贵的。以前，吴红喜欢去商场买衣服，____。网上的选择多，每次看到喜欢的，____，看颜色、大小、样子是不是自己满意的，都看好了才付钱。这样买东西，____，又能买到自己喜欢的。每次穿上新衣服，她都挺开心的。','Wu Hong earns a good salary and enjoys buying clothes. ____, she buys only what she needs and what suits her. She used to shop at malls, ____. Online there is more choice; when she sees something she likes, ____ to check its colour, size and style before paying. This way she ____ and buys what she likes. New clothes make her happy.','对于买衣服这件事|Regarding buying clothes\n但现在她更喜欢在网上买|but now she prefers shopping online\n她都会仔细看商品介绍|she carefully reads the product description\n既不浪费钱|neither wastes money','ABCD',[51])
picture(c,52,(190,180,1005,410),'商品|goods|商店里有很多商品。|There are many products in the shop.\n仔细|careful|他仔细地看着这里的东西。|He looks carefully at the things here.\n友好|friendly|她对老人很友好。|She is friendly to the older woman.')
tasks(c,'两人一组，一人扮演顾客，一人扮演售货员。顾客想买一个手机，售货员向顾客做介绍，最后顾客觉得合适，买下了这个手机。','Work in pairs as a customer and salesperson. Recommend a phone, compare it and complete a suitable purchase.','我想买一个价格合适、质量好的手机。|I want a reasonably priced, good-quality phone.\n这个牌子质量不错，今天还降价了。|This brand is good quality and discounted today.\n我先比较一下，如果合适就买。|I will compare first and buy if it suits me.','你平时一般怎么购物？请根据你去超市或商场买东西的经历，写一篇短文，不少于140字。','Describe how you usually shop, using a supermarket or mall experience. Write at least 140 Chinese characters.','我平时买东西以前，首先想一想自己究竟需要什么，然后再去商场比较。有一次，我想买一件外套。商场里很多商品都在促销，一件红色外套的价格减了一半。我没有马上买，而是先看质量，再试一试大小。售货员的态度很友好，也给我介绍了别的样式。最后我发现另一件外套更适合我，虽然贵一点儿，但是可以穿很久。我觉得购物时不光要看价格，还要看自己需不需要。只买合适的东西，既能少花钱，也不会让家里放满没有用的商品。','Before shopping I consider what I need and compare products. Once I needed a coat and saw a red one at half price. I checked quality and fit instead of buying immediately. A friendly salesperson showed other styles. Another coat suited me better and would last longer despite costing more. Shopping means considering need as well as price; buying suitable things saves money and avoids clutter.',[52])
extra(c,'objectives','Chapter objectives','能够听懂并交流线下购物时打折、商品比较等相关信息。|Understand and discuss discounts and product comparisons in shops.\n能够口头或书面表达购买意愿。|Express purchase intentions orally and in writing.\n了解中国人的消费观。|Understand Chinese views on spending.',[42])
extra(c,'self-assessment','Book learning summary','我能使用“顾客、促销、减、牌子、降价、商品”等词语谈论购物。|I can discuss shopping with the chapter vocabulary.\n我能理解并运用本课四个语言点。|I can understand and use the four grammar points.\n我能讲述“合适的才是最好的”故事，表达自己的看法。|I can tell a story illustrating that what suits you is best and express my opinion.',[53])
finish(c)
c=make(15)
words(c,'''期中|midterm|期中考试以后，我再也没迟到过。|Since the midterm exam I have never been late again.
医药|medicine; pharmaceuticals|我再也没去过那家医药公司。|I have never visited that pharmaceutical company again.
应聘|apply for a job|我再也不想一个人去应聘了。|I never want to apply for a job alone again.
招聘|recruit; hire|那家公司再也没来学校招聘。|That company has not returned to recruit at school.
实习|do an internship|实习以后，我再也不觉得工作很简单了。|After my internship I no longer think work is easy.
考虑|consider|我再也不考虑买那种手机了。|I will never consider buying that kind of phone again.
单位|work unit; organisation|我再也没回过以前的单位。|I have never returned to my former workplace.
毕业生|graduate|那位毕业生再也没来过这里。|That graduate has never come here again.
经历|experience; undergo|有了这次经历，我再也不着急了。|After this experience I no longer feel anxious.
消息|news; message|我再也没收到他的消息。|I have never heard from him again.
报名|sign up|我再也不忘记提前报名了。|I will never forget to sign up in advance again.
填写|fill in|我再也不着急填写这些材料了。|I will never rush to fill in these forms again.
笔试|written examination|我再也不怕参加笔试了。|I am no longer afraid of written exams.
面试|interview|我再也没参加过那家公司的面试。|I have never interviewed at that company again.
答|answer|我再也不随便答老师的问题了。|I will never answer the teacher carelessly again.
由|by|这件事再也不由他负责了。|He will no longer be responsible for this matter.
部门|department|我再也没去过那个部门。|I have never visited that department again.
负责人|person in charge|我再也没见过那位负责人。|I have never seen that person in charge again.
不论|regardless of|不论多忙，我再也不忘记吃早饭了。|However busy I am, I will never forget breakfast again.
肯定|certainly; sure|我肯定再也不会迟到了。|I am sure I will never be late again.
短信|text message|我再也没收到他的短信。|I have never received another text from him.
激动|excited|我再也没有这么激动过。|I have never been this excited again.
扔|throw|我再也不随便扔东西了。|I will never throw things carelessly again.
理发|get a haircut|我再也没去过那家理发店。|I have never visited that hairdresser again.
镜子|mirror|我再也不把镜子放在这里了。|I will never put the mirror here again.
自我|oneself; self-|我再也不怕做自我介绍了。|I am no longer afraid to introduce myself.
能够|be able to|我希望能够再也不让家人担心。|I hope I can stop making my family worry.
运用|apply; use|学会运用这个方法后，我再也不怕了。|After learning to use this method I am no longer afraid.
工厂|factory|我再也没去过那个工厂。|I have never visited that factory again.
规定|rule; stipulate|我再也不忘记公司的规定了。|I will never forget the company rules again.
课堂|classroom; class|我再也不在课堂上玩手机了。|I will never play on my phone in class again.
完全|completely|完全理解以后，我再也不问这个问题了。|After understanding completely I will not ask this again.
例如|for example|我改了很多习惯，例如再也不熬夜了。|I changed many habits; for example, I no longer stay up late.
不如|not as good as; better to|我觉得坐车不如走路，再也不开车去公园了。|I prefer walking to taking transport and will not drive to the park again.
细节|detail|我再也不忘记这些重要的细节了。|I will never forget these important details again.
答案|answer|我再也不直接看答案了。|I will never look straight at the answers again.
职业|occupation; career|我再也不随便选择职业了。|I will never choose a career carelessly again.''')
warm(c,'工厂|factory\n镜子|mirror\n理发|get a haircut\n面试|interview\n短信|text message\n毕业生|graduate',[2,0,4,1,3,5],54,[(286,884,447,1035),(530,884,692,1035),(775,884,938,1035),(286,1054,447,1206),(530,1054,692,1206),(775,1054,938,1206)])
warm_sent(c,'他正在理发。|He is getting a haircut.\n这是一家工厂。|This is a factory.\n他正在看短信。|He is reading a text message.\n她手里拿着一面镜子。|She is holding a mirror.\n他正在参加面试。|He is attending an interview.\n这些毕业生很高兴。|These graduates are happy.')
discussion(c,'你以前实习过吗？是在哪儿实习的？','Have you done an internship? Where?','我在一家小公司实习过，学到了很多东西。|I interned at a small company and learned a lot.\n我还没有实习过，希望今年有机会。|I have not interned yet and hope to this year.\n我在学校实习过，帮老师准备材料。|I interned at a school, helping teachers prepare materials.')
discussion(c,'你觉得面试的时候需要注意哪些方面？','What should you pay attention to in an interview?','要按时到，先准备好自我介绍。|Arrive on time and prepare a self-introduction.\n我觉得要认真听问题，说清楚自己的想法。|Listen carefully and explain your ideas clearly.\n穿的衣服要合适，对别人要有礼貌。|Dress suitably and be polite.')
listening(c,'''李文最近在忙什么？|What has Li Wen been busy doing?|去公司应聘/在公司实习/准备期中考试/为毕业做准备|applying to a company/interning at a company/preparing for midterms/preparing to graduate|A
很多单位招聘毕业生时，比较重视什么？|What do employers value when recruiting graduates?|身体情况/学习成绩/实习经历/毕业的学校|health/grades/internship experience/university attended|C
李文应聘时，第一步做的是什么？|What was Li’s first application step?|参加笔试/参加面试/在网上报名/给负责人打电话|written exam/interview/online registration/calling the manager|C
公司的笔试主要考什么？|What did the written exam mainly test?|外语水平/专业知识/兴趣爱好/对工作的想法|foreign languages/professional knowledge/interests/views about work|B
李文收到的短信内容是什么？|What did the text message say?|他通过面试了/他周末得加班/他明天要开始工作/他下周工作任务多|he passed the interview/he must work overtime at the weekend/he starts tomorrow/he has many tasks next week|A
李文做了什么准备？|What preparation did Li make?|搬到了公司附近/买了一个新手机/买了一身新衣服/去商场买礼物了|moved near the company/bought a new phone/bought a new outfit/bought gifts at the mall|C
为什么很多大学生要去实习？|Why do many students intern?|想认识新朋友/便于了解社会/想减轻经济压力/为了达到毕业要求|to make friends/to understand society/to reduce financial pressure/to meet graduation requirements|B
在实习中，学生们会有什么发现？|What do students discover during internships?|工作比学习更简单/书上的知识没有用/学习时要注意细节/有的问题要慢慢理解|work is easier than study/book knowledge is useless/details matter only in study/some problems take time to understand|D''')
text(c,1,'''陈天中：李文，期中考试后就再也没见过你了，你这段时间在忙什么呢？|Chen Tianzhong: Li Wen, I haven’t seen you since the midterms. What have you been busy with?
李文：我最近去一家医药公司应聘了，他们正在招聘实习生。|Li Wen: I applied to a pharmaceutical company recruiting interns.
陈天中：你这么早就考虑实习了？|Chen: Are you considering an internship so early?
李文：现在很多单位在招聘毕业生时，都很重视有没有实习经历，所以我想提前去锻炼一下，积累一些经验。|Li: Many employers value internship experience when hiring graduates, so I want to gain experience early.
陈天中：那现在有结果了吗？|Chen: Do you have a result yet?
李文：我还在等消息，希望能有好结果。|Li: I’m still waiting for news and hoping for a good result.''','''李文为什么现在就想去实习？|Why does Li want an internship now?|因为很多单位重视实习经历，他想提前积累经验。|Employers value internships and he wants early experience.
李文应聘成功了吗？|Was his application successful?|还不知道，他正在等消息。|He does not know yet; he is waiting for news.''',[55,56],('陈天中很久没有……。他问李文这段时间……。李文说他最近去……，因为那家公司……。他觉得现在很多单位在……时，都很重视……，所以他想提前……，积累……。陈天中又问李文现在……。李文说他还在……，希望……。','Retell why Li applied, why internships matter, and why he is still waiting.','陈天中很久没有见过李文，问他最近忙什么。李文说，他去一家招聘实习生的医药公司应聘了。很多单位招聘毕业生时重视实习经历，所以他想提前锻炼，积累经验。他现在还在等消息，希望有好结果。','Chen had not seen Li for a long time and asked about his activities. Li had applied to a pharmaceutical company recruiting interns. Employers value experience, so he wanted to gain it early. He was still waiting and hoping for good news.',[56]))
grammar(c,1,'再也不 means something will never happen again; 再也没 means it has not happened again since a past point.','期中考试后就再也没见过你了。|I have not seen you since the midterms.\n对不起，我以后再也不迟到了。|Sorry, I will never be late again.\n我出国以后就再也没给他打过电话。|I have not called him since going abroad.','''A：你和小王还有联系吗？ B：毕业以后，____。|Do you still contact Xiao Wang? Complete using 再也没.|再也没和他联系过|I have not contacted him again
A：你以后千万要注意保护好眼睛。 B：知道了，我以后____。|Promise to protect your eyes.|再也不长时间玩手机了|will never spend long periods on my phone again
A：你还常去太阳公园散步吗？ B：搬家以后离公园太远了，____。|Explain that you stopped visiting the park after moving.|我再也没去过了|I have never been there again''',[56])
text(c,2,'''陈天中：李文，你是怎么应聘的？|Chen: Li, how did you apply?
李文：我先在网上报名，填写个人信息，然后等公司通知我去参加笔试。|Li: I registered online and filled in personal details, then waited for the company to invite me to a written exam.
陈天中：笔试都考些什么？|Chen: What did the written exam test?
李文：主要是一些专业知识。考完没多久，他们就让我去面试了。|Li: Mainly professional knowledge. Soon afterward they invited me to an interview.
陈天中：看来你笔试答得不错，那你面试得怎么样？|Chen: Your written answers must have been good. How was the interview?
李文：那天是由部门负责人来面试的，我有点儿紧张。他让我介绍了自己的学习经历、兴趣爱好和对工作的想法。|Li: The department head interviewed me. I was nervous. He asked about my education, interests and ideas about work.
陈天中：听起来挺正式的。|Chen: It sounds formal.
李文：是啊，我觉得这次经历很有用。不论结果怎么样，对我以后找工作肯定有帮助。|Li: Yes. It was useful. Whatever the result, it will certainly help my future job search.''','''李文面试的内容是什么？|What did Li discuss in the interview?|他介绍了学习经历、兴趣爱好和对工作的想法。|His education, interests and ideas about work.
李文觉得这次应聘经历怎么样？|How does Li feel about the application experience?|很有用，不论结果怎么样，都对以后找工作有帮助。|It is useful and will help future job hunting regardless of the result.''',[57,58])
grammar(c,2,'由 introduces the person or organisation performing an action.','那天是由部门负责人来面试的，我有点儿紧张。|The department head interviewed me that day and I was nervous.\n这个问题究竟由谁来负责解决？|Who exactly is responsible for resolving this problem?\n这次活动是由他们公司来安排的。|Their company arranged this event.','''A：这个工作是谁完成的？ B：____。|Who completed this work?|这个工作是由我们部门完成的|Our department completed it.
A：这些节目是谁准备的？ B：____。|Who prepared these programmes?|这些节目是由学生们准备的|The students prepared them.
A：这期交流活动是谁举办的？ B：____。|Who organised this exchange event?|是由我们学校举办的|Our school organised it.''',[58])
text(c,3,'''一天下午，李文突然收到一条短信，说他通过了面试，让他下周一到公司实习。李文看到信息后，激动得把手机扔到床上，在屋子里跳了起来。之后的几天，李文忙着做各种准备。为了给大家留个好印象，他去理发店把头发理了理，又去商店买了一身正式的衣服，还打算在镜子前把自我介绍练一练。|One afternoon Li received a text saying he had passed the interview and should start his internship next Monday. He was so excited that he threw his phone onto the bed and jumped around. Over the following days he prepared: a haircut, a formal outfit and plans to rehearse his self-introduction in front of a mirror.
在他看来，这次实习是一个新的开始。他希望不仅能够运用专业知识完成任务，还能够积累更多经验，为将来找工作打下基础。|He saw the internship as a new beginning. He hoped to apply his professional knowledge, complete tasks and gain experience to build a foundation for future work.''','''李文看到信息后做什么了？|What did Li do after reading the message?|他激动得把手机扔到床上，在屋子里跳了起来。|He threw his phone onto the bed and jumped excitedly.
李文是怎么看这次实习的？|How did Li view the internship?|他觉得这是新的开始，可以运用知识、积累经验，为找工作打基础。|As a new beginning to apply knowledge and gain experience for future employment.''',[59,60],('李文收到了一条短信，告诉他……，让他下周一……。他看到信息后，激动得……，在屋子里……。为了给大家……，他去理发店……，又去商店……，还打算在镜子前……。他觉得这次实习是……。他希望不仅能够……，还能够……，为将来找工作……。','Retell the message, Li’s reaction and preparations, and his hopes for the internship.','李文收到短信，知道自己通过了面试，下周一可以去公司实习。他很激动，把手机扔到床上，在屋子里跳了起来。他去理发，买了正式的衣服，还准备在镜子前练习自我介绍。他觉得实习是新的开始，希望运用专业知识，积累经验，为将来找工作打下基础。','Li learned that he had passed the interview and would start on Monday. He threw his phone onto the bed and jumped with excitement. He got a haircut, bought formal clothes and planned to rehearse his introduction. He hoped to use his knowledge and gain experience for future work.',[60]))
grammar(c,3,'In 把 sentences, repeated verbs (VV, V一V or V了V) describe brief or light actions.','他去理发店把头发理了理。|He went to the hairdresser for a trim.\n你先把作业检查检查，然后再交给老师。|Check your homework before handing it to the teacher.\n上课前，我把今天要学习的内容看了看。|Before class I looked over today’s material.','''我____，也说出了自己的看法。（想）|Use 想 with a repeated verb.|把这个问题想了想|thought about this problem a little
看到办公室有点儿脏，他打算____。（扫）|The office is dirty; use 扫.|把办公室扫一扫|give the office a sweep
我建议你每次先____，然后再开始写作业。（复习）|Recommend reviewing before homework.|把今天学的内容复习复习|review today’s material briefly''',[60])
text(c,4,'''在中国，很多大学生在毕业前都会去实习。实习的地方有公司、工厂，也有学校和医院。学生们通过实习，可以积累工作经验，熟悉工作内容和单位的管理规定，提前了解并适应社会。|Many Chinese university students intern before graduation at companies, factories, schools or hospitals. Internships help them gain experience, learn tasks and workplace rules, and understand and adapt to society.
在实习中，学生常常会发现，课堂上学到的知识和实际工作并不完全一样。例如：有些事情，在课本上学不如自己做一遍，因为只有在做的时候，才会发现有很多细节需要注意；还有一些问题，在书上找不到答案，只能通过日常工作慢慢理解。在这样的过程中，学生能够对学到的知识有更好的认识，也更清楚自己的职业发展方向。|Students often discover that classroom knowledge and real work differ. Some things are better learned by doing because details emerge only in practice. Other problems have no textbook answer and become clear through daily work. This improves students’ understanding and clarifies their career direction.''','''通过实习，学生可以学到什么？|What can students learn from internships?|可以积累经验，了解工作内容和规定，适应社会，明确职业方向。|They gain experience, learn duties and rules, adapt to society and clarify career goals.
为什么说有些事情需要自己做一遍？|Why should some things be tried personally?|只有在做的时候，才会发现需要注意的细节。|Only practice reveals details that need attention.''',[61,62])
grammar(c,4,'A不如B means A is not as good as B; with an adjective it compares that quality.','有些事情，在课本上学不如自己做一遍。|Some things are better learned by doing than from a textbook.\n这家店不如那家店环境好。|This shop’s surroundings are not as good as that shop’s.\n我觉得坐公交不如坐地铁方便。|I find buses less convenient than the subway.','''你多走走吧，坐车____。|Recommend walking rather than riding.|不如走路对身体好|is less healthy than walking
不知道怎么解决问题时，自己想____。|Compare thinking alone with asking others.|不如问问有经验的人|is not as good as asking experienced people
我更愿意在家做饭，因为在外面吃饭____。|Explain a preference for cooking at home.|不如在家吃饭便宜|is more expensive than eating at home''',[62])
gaps(c,'''你这么努力，这次考试____能通过。|You work hard and will ____ pass.|肯定|certainly
您有什么问题，可以直接跟____联系。|Contact the ____ directly with questions.|负责人|person in charge
____你同不同意，我都会按照计划去做。|____ you agree or not, I will follow the plan.|不论|regardless of whether
这件事比较重要，我需要再认真____一下。|This is important; I need to ____ it carefully.|考虑|consider
我们要先进行____，了解大家的专业能力。|We first hold a ____ to assess professional ability.|笔试|written exam
等了好几天，还是没有收到他的____。|After several days I still have no ____ from him.|消息|news
你知道这道题的____吗？|Do you know the ____ to this question?|答案|answer
我____得昨天晚上都没睡好。|I was so ____ that I slept badly.|激动|excited
我已经____和中国朋友进行简单交流了。|I am already ____ to have simple conversations with Chinese friends.|能够|able
下午我去____，你想跟我一起去吗？|I am getting a ____ this afternoon. Want to come?|理发|haircut
你对自己的____发展有什么打算？|What are your ____ development plans?|职业|career
他现在在一家____工作，负责检查产品质量。|He works in a ____ checking product quality.|工厂|factory''',[62,63])
cloze(c,'王明是一名大三学生，最近正在找实习机会。____，选了一家自己感兴趣的单位报名。为了顺利通过面试，他提前准备了很多内容，比如了解公司的情况，____。面试那天，他刚开始有点儿紧张，不过慢慢放松了一些。____，他觉得自己的表现没有那么好。虽然最后没有通过面试，但是他认为这次应聘的经历很有用，____，也让他在交流方面更有信心了。','Wang Ming, a third-year student, is seeking an internship. ____, and selected an organisation to apply to. He prepared by researching the company and ____. At the interview he was initially nervous but relaxed. ____, he felt his performance could have been better. Although unsuccessful, the experience was useful: ____ and increased his communication confidence.','面试结束后|After the interview\n练习介绍自己的学习经历|practising describing his education\n不仅让他了解了应聘的过程|it not only taught him the application process\n他在网上看到了几条招聘信息|he saw several job advertisements online','DBAC',[63])
picture(c,63,(165,1220,1003,1440),'扔|throw|他把垃圾扔进垃圾桶。|He throws rubbish into the bin.\n答案|answer|她正在想这道题的答案。|She is thinking about the answer.\n激动|excited|他看到消息后非常激动。|He is excited after reading the message.')
tasks(c,'两人一组，一人扮演面试官，一人扮演应聘者，模拟面试的过程。面试官询问学习经历、能力和想法；应聘者介绍基本情况、应聘原因和优缺点。','Role-play an interviewer and applicant. Discuss education, abilities, motivation, strengths and weaknesses.','请先介绍一下你的学习经历。|Please first describe your education.\n我学的是经济，希望在这里积累工作经验。|I study economics and hope to gain experience here.\n我的优点是做事认真，不过工作经验还不够。|I work carefully, but still lack experience.','你的一个朋友要去一家国际公司应聘。请给他／她写一份应聘建议清单，不少于140字。','Write at least 140 Chinese characters of application advice for a friend applying to an international company.','听说你准备去一家国际公司应聘，我想给你一些建议。首先，你应该提前了解公司的情况，看看这个工作需要什么能力，再认真填写个人信息。其次，准备好自我介绍，把自己的学习经历和实习经历说清楚。你可以在镜子前练一练，也可以请朋友听一听。面试那天，要穿合适的衣服，按时到，不要让负责人等你。回答问题时，先认真听，再说明自己的想法。如果有不懂的地方，可以有礼貌地问一问。不论最后的结果怎么样，这次经历都会帮助你了解自己，为以后找工作积累经验。','Research the company and required abilities, complete personal information carefully and prepare a clear introduction covering education and internships. Rehearse in a mirror or with a friend. Dress suitably and arrive on time. Listen before answering and ask politely when unsure. Whatever the outcome, the experience will help you understand yourself and prepare for future job hunting.',[64])
extra(c,'objectives','Chapter objectives','能够听懂并交流应聘、面试、实习等信息。|Understand and discuss applications, interviews and internships.\n能够口头或书面表达求职经历。|Describe job-hunting experiences orally and in writing.\n了解中国大学生的实习情况及意义。|Understand Chinese university internships and their significance.',[54])
extra(c,'self-assessment','Book learning summary','我能使用“单位、经历、部门、负责人”等词语谈论实习。|I can use the chapter vocabulary to discuss internships.\n我能理解并运用本课四个语言点。|I can understand and use the four grammar points.\n我能交流应聘、面试等信息。|I can discuss applications and interviews.\n我能表达个人的求职经历。|I can describe my job-hunting experience.',[65])
section(c,'bonus','Xiaoyu’s bonus content',[L('走出校园之前：中国大学生如何找工作','Before graduation: how Chinese university students find their first job')],[64],'The book gives this companion-video topic. The video is not embedded in the supplied PDF.','My notes after watching')
finish(c)
c=make(16)
words(c,'''本来|originally|我本来想去公园，却没有去。|I originally wanted to go to the park, but did not go.
只好|have no choice but|天很冷，他却只好出门。|It is cold, but he has no choice but to go out.
赶上|catch up with|我跑得很快，却没有赶上车。|I ran fast but did not catch the bus.
旅行|travel|我想去旅行，却没有时间。|I want to travel but have no time.
推迟|postpone|他把会议推迟了。|He postponed the meeting.
取消|cancel|我把今天的课取消了。|I cancelled today’s class.
可惜|a pity; regrettable|虽然有点儿可惜，我却不后悔。|Although it is a pity, I do not regret it.
确实|indeed; really|他确实很忙，却每天都来看我。|He is indeed busy, but visits me every day.
等到|by the time; wait until|等到天黑，他却还没有回来。|It is dark now, but he has still not returned.
早晨|morning|我早晨把衣服洗了。|I washed the clothes in the morning.
忽然|suddenly|我准备出门，天却忽然下雨了。|I was ready to go out, but it suddenly started raining.
增加|increase; add|我增加了工作时间，却没做完。|I increased my working hours, but did not finish.
调整|adjust|我把学习时间调整了。|I adjusted my study schedule.
错误|mistake; wrong|我把这个错误改了。|I corrected this mistake.
并且|and; furthermore|她喜欢看书，并且喜欢写字。|She likes reading and also likes writing.
例子|example|他讲得很清楚，并且给了一个例子。|He explained clearly and gave an example.
关键|key; crucial|他知道问题的关键，却不告诉我。|He knows the key to the problem but does not tell me.
详细|detailed|他详细地介绍了情况，并且回答了问题。|He described the situation in detail and answered questions.
时间表|schedule|我把时间表改了。|I changed the schedule.
把握|confidence; certainty|他很有把握，却还是检查了一遍。|He was confident but still checked once more.
相反|on the contrary|我喜欢早起，他却相反。|I like getting up early, but he is the opposite.
部分|part; portion|这部分很难，他却做对了。|This part is hard, but he got it right.
轻松|relaxed; easy|这个工作很轻松，并且离家很近。|This job is easy and very close to home.
标准|standard|他知道标准，却没有做好。|He knows the standard but did not do well.
严格|strict|老师很严格，却很关心我们。|The teacher is strict but cares about us.
取得|achieve; gain|他取得了好成绩，却没有休息。|He achieved good results but did not rest.
说不定|perhaps; maybe|他现在不来，说不定明天会来。|He is not coming now; perhaps he will come tomorrow.
灵活|flexible|时间可以灵活安排，并且可以在家工作。|The hours are flexible, and one can work from home.
一切|everything|我准备好了一切，却没出发。|I prepared everything but did not leave.
却|but; however|他很累，却不想休息。|He is tired but does not want to rest.
不得不|have to|我想出去，却不得不在家学习。|I want to go out, but have to study at home.
约|arrange to meet|我约了朋友，却忘了时间。|I arranged to meet a friend, but forgot the time.
不便|inconvenient|这里交通不便，房租却很便宜。|Transport here is inconvenient, but the rent is cheap.
失望|disappointed|他有点儿失望，却没有放弃。|He is a little disappointed but has not given up.
也许|perhaps|也许他很忙，却还是来了。|Perhaps he is busy, but he came anyway.
逛|stroll; browse|我去商店逛了逛，却什么也没买。|I browsed the shops but bought nothing.
有趣|interesting|这本书很有趣，并且很便宜。|This book is interesting and cheap.
观看|watch|我们观看了比赛，并且拍了照片。|We watched the match and took photos.
部|measure word for films, etc.|这部电影很长，他却看完了。|This film is long, but he finished watching it.
无法|be unable to|他想帮忙，却无法过来。|He wants to help but cannot come.
接受|accept|我听懂了，却不想接受。|I understood but do not want to accept it.''',3)
warm(c,'时间表|schedule\n观看|watch\n增加|increase\n早晨|morning\n旅行|travel\n失望|disappointed',[4,3,0,1,2,5],66,[(294,887,449,1035),(534,887,688,1035),(773,887,931,1035),(294,1055,449,1205),(534,1055,688,1205),(773,1055,931,1205)])
warm_sent(c,'他们一起去旅行。|They travel together.\n早晨，她打开了窗户。|She opened the window in the morning.\n他写好了今天的时间表。|He has written today’s schedule.\n她在家观看电视节目。|She watches a television programme at home.\n他的钱增加了。|His money has increased.\n他觉得很失望。|He feels disappointed.')
discussion(c,'你平时经常做计划吗？一般会做哪些计划？','Do you often make plans? What kinds of plans?','我每天做学习计划。|I make study plans every day.\n我旅行前会做计划。|I plan before travelling.\n我很少做计划，想到什么就做什么。|I rarely plan; I do whatever comes to mind.')
discussion(c,'你觉得做计划重要吗？为什么？','Do you think planning is important? Why?','很重要，计划能帮助我按时完成任务。|It is important because plans help me finish on time.\n很重要，我可以知道先做什么。|It is important; I can know what to do first.\n我觉得不一定，灵活安排也很好。|Not always; flexible arrangements are good too.')
listening(c,'''白家月本来计划周末做什么？|What had Bai originally planned for the weekend?|去旅游/买机票/订酒店/在家复习|Travel/Buy plane tickets/Book a hotel/Revise at home|A
王一雪建议白家月什么时候去旅游？|When does Wang suggest Bai travel?|明天/这个周末/下个周末/考试结束后|Tomorrow/This weekend/Next weekend/After the exam|D
杨同乐接到了什么通知？|What notice did Yang receive?|会议时间变化了/会议材料要调整/会议地点变化了/会议内容增加了|The meeting time changed/The materials need adjusting/The venue changed/The content increased|A
王一雪让杨同乐做什么？|What does Wang ask Yang to do?|检查细节问题/重新准备材料/通知会议地点/安排会议时间|Check details/Prepare materials again/Announce the venue/Arrange the time|A
有的人为什么喜欢做计划？|Why do some people like planning?|可以省钱/可以省时间/做事更有把握/感觉比较轻松|It saves money/It saves time/They feel more confident/They feel more relaxed|C
根据课文，不做计划可能会有什么结果？|What can happen without plans?|带来新的发现/让任务变简单/提前完成任务/增加工作压力|New discoveries/Tasks become simple/Tasks finish early/More work pressure|A
根据课文，变化可能会带来什么影响？|What can changes bring?|心情变得更加愉快/以后不用再做计划/让事情更容易完成/给生活带来新可能|A happier mood/No need for future plans/Easier tasks/New possibilities in life|D
面对变化，人们应该怎么做？|How should people respond to changes?|随意地安排计划/坚持本来的计划/发现并解决问题/接受并适应变化|Plan casually/Keep the original plan/Find and solve problems/Accept and adapt to changes|D''')
text(c,1,'''王一雪：家月，周末你还打算去南京旅游吗？我去年去过那里，可以给你介绍一下。|Wang: Jiayue, are you still going to Nanjing this weekend? I went last year and can tell you about it.
白家月：本来都计划好了，可是昨天突然接到通知，下周学校要安排一次考试，所以周末只好在家复习了。|Bai: Everything was planned, but yesterday the school suddenly announced an exam next week, so I have to revise at home this weekend.
王一雪：真是计划赶不上变化啊！看来你的旅行计划只能推迟了。|Wang: Plans really cannot keep up with changes! It looks like you must postpone your trip.
白家月：是的，我已经把机票和酒店取消了。虽然有点儿可惜，但学习更重要。|Bai: Yes. I have cancelled the flights and hotel. It is a pity, but studying matters more.
王一雪：学习确实要放在第一位。等到考试结束后，你再找个时间去。|Wang: Study really must come first. Find another time to go after the exam.
白家月：我也是这么想的，以后肯定还有很多机会。|Bai: That is what I think too. There will certainly be plenty of chances later.''','''白家月为什么周末不能去南京了？|Why can Bai no longer go to Nanjing this weekend?|下周有考试，她周末只好在家复习。|She has an exam next week, so must revise at home.
旅行计划推迟后，白家月做什么了？|What did Bai do after postponing the trip?|她把机票和酒店取消了。|She cancelled the flights and hotel.''',[67,68],('白家月本来计划……，可是昨天突然……，下周学校要……。她周末需要……，旅游计划……。她已经把……，虽然……，但学习……。她打算……后，找个时间……。','Retell Bai’s original plan, the school notice, her cancellations and her new plan.','白家月本来计划周末去南京旅游，可是昨天突然接到通知，下周学校要考试。她周末需要在家复习，旅游计划只能推迟。她已经把机票和酒店取消了，虽然有点儿可惜，但学习更重要。她打算考试结束后，找个时间再去。','Bai planned to visit Nanjing, but a school exam notice meant she had to revise. She postponed her trip and cancelled the flights and hotel. Study matters more, so she will go after the exam.',[68]))
grammar(c,1,'Subject + 把 + definite object + verb + 了 describes a completed action affecting that object.','我已经把机票和酒店取消了。|I have cancelled the flights and hotel.\n你把灯关了吧，我想睡觉了。|Please switch off the light; I want to sleep.\n你别忘了把衣服洗了，明天还得穿呢。|Do not forget to wash the clothes; you need them tomorrow.','''A：____。B：好，我也觉得房间里挺热的。|A: ____. B: Yes, I also think it is hot in the room.|你把窗户打开吧|Please open the window.
A：____。B：放心吧，我一会儿就去图书馆。|A: ____. B: Do not worry; I will go to the library soon.|你别忘了把书还了|Do not forget to return the books.
A：快____，这样你才能快点儿好。B：好的，吃完药我再睡一觉。|A: Quickly ____, so you can recover sooner. B: Okay, then I will sleep.|把药吃了|take the medicine''',[68])
text(c,2,'''杨同乐：刚接到通知，明天早晨的会议，时间改到下周了。|Yang: I just received notice that tomorrow morning’s meeting has moved to next week.
王一雪：啊？时间都安排好了，怎么说变就变了？|Wang: What? The time was already arranged. Why has it changed so suddenly?
杨同乐：是啊，没想到忽然要改时间。|Yang: Yes, I did not expect the sudden change.
王一雪：好吧，那再看看有没有新的安排，或者增加的会议内容。|Wang: All right. Check for new arrangements or additional meeting topics.
杨同乐：好的。会议材料还需要调整吗？|Yang: Okay. Do the meeting materials need adjusting too?
王一雪：再检查一下有没有细节上的错误，并且试着增加一些例子，把内容准备得更全一些。|Wang: Check for errors in the details and try adding examples to make the content more complete.
杨同乐：没问题，这样效果肯定会更好。看来有时候变化不一定是坏事，关键是我们怎么去适应变化。|Yang: No problem. That will certainly work better. Sometimes change is not necessarily bad; the key is how we adapt.''','''王一雪建议怎么调整会议材料？|How does Wang suggest adjusting the materials?|检查细节上的错误，并且增加一些例子。|Check detailed errors and add examples.
对于变化，王一雪是怎么看的？|What is Wang’s attitude towards changes?|她接受变化，建议利用时间把材料准备得更全一些。|She accepts the change and suggests using the time to improve the materials.''',[69,70])
grammar(c,2,'并且 links actions or situations and adds further information.','再检查一下有没有细节上的错误，并且试着增加一些例子。|Check for errors in the details and try adding examples.\n他按时完成了任务，并且做得很好。|He finished on time and did a good job.\n人们的生活水平提高了，并且生活方式也发生了很大的变化。|Living standards improved, and lifestyles also changed greatly.','''A：你觉得小王这个人怎么样？B：____。|What do you think of Xiao Wang?|他很认真，并且很关心别人|He is careful and cares about others.
A：为什么你建议我看这本书？B：____。|Why do you recommend this book?|这本书很有趣，并且对学习有帮助|It is interesting and helpful for study.
A：明天的会议，你做好准备了吗？B：____。|Are you ready for tomorrow’s meeting?|我准备好了材料，并且检查了一遍|I prepared the materials and checked them once.''',[70])
text(c,3,'''在生活和工作中，有的人喜欢做计划，他们会提前安排好每天要做的事情，然后按照详细的时间表去完成任务，觉得这样做更有把握。相反，也有一部分人不爱做计划，他们认为随意一些也很好，想到什么就去做什么，感觉这样比较轻松。|In life and work, some people like to plan. They arrange each day’s tasks in advance and follow a detailed schedule because that feels more certain. Others dislike planning; they prefer doing whatever comes to mind and find that more relaxing.
其实，事前做计划是好是坏没有标准答案。严格按照计划做事，常常能取得不错的效果；而不做计划，说不定也会带来新的发现。无论做不做计划，只要既能按时完成任务，又能根据情况灵活调整，就是适合自己的方式。|There is no standard answer to whether advance planning is good or bad. Following plans strictly often works well, while not planning may bring new discoveries. Whether you plan or not, a method suits you if you finish on time and adjust flexibly to circumstances.''','''喜欢做计划的人一般是怎么安排事情的？|How do people who like planning usually arrange things?|他们提前安排每天要做的事情，按照详细的时间表完成任务。|They arrange daily tasks in advance and follow a detailed schedule.
事前做计划是好是坏？为什么？|Is advance planning good or bad, and why?|没有标准答案。能按时完成任务，又能灵活调整，就是适合自己的方式。|There is no standard answer; finishing on time and adjusting flexibly are what matter.''',[71,72],('在生活和工作中，有的人喜欢做计划，他们会……，然后按照……，觉得这样做……。相反，也有一部分人……，他们认为……，想到什么……，感觉……。\n其实，事前做计划是好是坏……。严格按照计划做事，常常能……；而不做计划，说不定……。无论做不做计划，只要既能……，又能……，就是……。','Retell the two approaches to planning and the conditions for a suitable method.','有的人喜欢提前安排每天的事情，按照时间表完成任务，觉得这样更有把握。相反，有的人不爱做计划，想到什么就做什么，觉得比较轻松。做计划好不好没有标准答案。按照计划做事常常能取得不错的效果，不做计划也可能带来新的发现。只要能按时完成任务，又能灵活调整，就是适合自己的方式。','Some plan daily tasks and follow schedules for certainty; others prefer spontaneity and feel relaxed. Neither approach is always better. Plans can bring good results, while spontaneity may bring discoveries. A suitable method allows timely completion and flexible adjustment.',[72]))
grammar(c,3,'说不定 means perhaps or maybe and expresses a guess about a possible situation or result.','不做计划，说不定也会带来新的发现。|Not planning may also bring new discoveries.\n今天这么阴，说不定会下雨。|It is so cloudy today; perhaps it will rain.\n你再试一次，说不定就成功了。|Try once more; perhaps you will succeed.','''他今天没来，____。（有事）|He did not come today; perhaps... Use 有事.|说不定有事|perhaps something came up
____，再等一会儿吧。（路上）|Perhaps..., so wait a little longer. Use 路上.|他现在说不定还在路上|Perhaps he is still on his way.
这件事你找经理说吧，____。（同意）|Talk to the manager about it; perhaps... Use 同意.|说不定他会同意|perhaps he will agree''',[72])
text(c,4,'''人们常说“计划赶不上变化”。有时候，你准备好了一切，却突然出现了新情况，让你不得不改变计划。比如准备出去旅行，可能因为有事而取消；约好见朋友，可能因为天气不好而推迟。|People often say plans cannot keep up with changes. Sometimes everything is ready, but a new situation suddenly forces you to change plans. A trip may be cancelled because something comes up; meeting a friend may be postponed because of bad weather.
虽然变化经常打乱计划，给我们带来不便，甚至让人感到失望，但这些变化也许会给生活带来新的可能。比如没去成旅行，于是在家门口的小公园逛了逛，发现那里也很有趣；没见到朋友，于是在家观看了一部电影，心情也变得很愉快。|Changes often disrupt plans, cause inconvenience and even disappointment, but may bring new possibilities. Instead of travelling, you might discover an interesting local park. Instead of meeting a friend, you might enjoy a film at home.
生活中很多变化是无法提前知道的，我们要做的就是学会接受变化、适应变化，在变化中找到新的解决办法。这样不仅能锻炼自己在面对不同情况时解决问题的能力，也能让我们的生活更轻松。|Many changes cannot be predicted. We must learn to accept and adapt to them and find new solutions. This develops our ability to solve problems in different circumstances and makes life more relaxed.''','''“计划赶不上变化”是什么意思？|What does “plans cannot keep up with changes” mean?|新情况可能突然出现，让人不得不改变本来的计划。|New situations can appear suddenly and force changes to original plans.
我们为什么应该积极适应变化？|Why should we actively adapt to change?|这样可以找到新办法，提高解决问题的能力，让生活更轻松。|It helps us find new methods, improve problem-solving and live more easily.''',[73,74])
grammar(c,4,'却 is an adverb introducing an unexpected contrast; it usually follows the subject and precedes the predicate.','你准备好了一切，却突然出现了新情况，让你不得不改变计划。|You prepared everything, but a new situation suddenly forced you to change plans.\n他通过了面试，却一点儿也不激动。|He passed the interview but was not excited at all.\n她长得很像她姐姐，性格却完全不同。|She looks like her sister, but their personalities are completely different.','''他没有做太多准备，____。|He did not prepare much, but...|却取得了很好的成绩|still achieved very good results
我觉得这个电影很有趣，____。|I find this film interesting, but...|他却觉得很无聊|he finds it boring
这些打折的商品虽然便宜，____。|These discounted goods are cheap, but...|质量却不太好|their quality is not very good''',[74])
gaps(c,'''要想提高成绩，____是坚持每天复习。|To improve results, the ____ is daily revision.|关键|key
他____说得很对，我也同意他的看法。|He is ____ right; I agree.|确实|indeed
你没能参加文化节活动，真是太____了。|It is such a ____ that you missed the cultural festival.|可惜|pity
____工作不那么忙了，我想和家人去旅游。|____ work is less busy, I want to travel with my family.|等到|When
我____打算周末出去玩，可是后来有事，就没去成。|I ____ planned to go out, but something came up.|本来|originally
王老师讲课时常常会用一些____，帮助学生们更好地理解。|Teacher Wang often uses ____ to help students understand.|例子|examples
A：这次公司招聘的____是什么？B：至少有五年的工作经验，并且有较强的个人工作能力。|What is the hiring ____? At least five years’ experience and strong ability.|标准|standard
A：老师，这个问题可以讲得再____一点儿吗？B：好的，我再给你讲一遍。|Could you explain in more ____? Yes, I will explain again.|详细|detail
A：很久没有见到你了，你最近过得怎么样？B：还不错，____都很顺利。|How have you been? Fine; ____ is going smoothly.|一切|everything
A：我以为他会同意，没想到结果正好____。B：是啊，看来他还是不太愿意参加。|I expected agreement, but the result was the ____. Yes, he seems unwilling.|相反|opposite
A：你什么时候有时间？我想____你喝杯咖啡。B：好啊，我也正想跟你聊聊呢。明天中午怎么样？|When are you free? I want to ____ you for coffee. How about tomorrow noon?|约|meet
A：经理，我明天有事，____参加会议，想跟您请假。B：好的，那你提前把工作安排好吧。|I have something tomorrow and am ____ to attend. Okay, arrange your work in advance.|无法|unable''',[75])
cloze(c,'小李周末本来计划和朋友去爬山，还提前准备好了水和食物。可是周六早晨，____，看起来可能会下雨。为了安全，____。____，但小李重新做了计划，用原来爬山的时间完成了一些学习任务。周末结束后，他觉得这样安排也不错。这次经历让他明白，遇到变化时，____。只要灵活调整计划，就能把事情安排好，让自己过得轻松、愉快。','Xiao Li planned to climb a mountain with friends and prepared water and food. On Saturday morning, ____, and rain looked likely. For safety, ____. ____, but he made a new plan and used the time to complete study tasks. He felt this was a good arrangement. The experience taught him that when changes happen, ____. Flexible planning can keep life organised, relaxed and happy.','虽然有点儿失望|Although a little disappointed\n天气忽然变阴了|the sky suddenly became overcast\n他只好取消了爬山的计划|he had to cancel the climb\n需要学会接受新的情况|one must learn to accept new circumstances','BCAD',[75])
picture(c,76,(185,187,1018,388),'逛|stroll; browse|他们一起逛商店。|They browse the shop together.\n有趣|interesting|妈妈给孩子讲有趣的故事。|The mother tells her child an interesting story.\n错误|mistake|他指出了材料中的错误。|He pointed out the mistake in the materials.')
tasks(c,'全班分成两组，以“做计划是好是坏”为主题进行辩论。各组先准备自己的观点和理由，然后进行辩论。正方：做计划更好。反方：随意些更好。','Divide into two groups to debate whether planning is good or bad. Prepare arguments first. Pro: planning is better. Con: being more spontaneous is better.','我觉得做计划更好，因为这样做事更有把握。|I think planning is better because it gives more confidence.\n我觉得随意一些更好，因为生活常常有变化。|I think spontaneity is better because life often changes.\n我们可以做计划，也可以根据情况灵活调整。|We can plan and adjust flexibly to circumstances.','你的一个朋友最近总是完不成任务。请你根据上面辩论的内容，给他／她写一份建议，不少于140字。','A friend has been struggling to finish tasks. Use the debate arguments to write at least 140 Chinese characters of advice.','听说你最近总是完不成任务，我想给你一些建议。首先，你可以每天早晨写一个时间表，把当天要做的事情分清楚，先做最重要的事。每完成一件事，就在时间表上做个记号，这样会更有把握。其次，不要把一天安排得太满，要留一些时间休息，也要准备应对突然出现的新情况。如果计划需要调整，不必太失望，更不要放弃所有的任务。你可以先想一想哪些事情必须今天完成，哪些可以推迟。做计划并不是要求一切都不能改变，关键是找到适合自己的方式。只要每天坚持，并且灵活调整，你一定能做得越来越好。','Write a daily schedule and do important tasks first. Mark completed tasks to build confidence. Leave time for rest and unexpected situations. If plans change, do not lose hope or abandon everything. Decide what must be done today and what can wait. Planning need not mean refusing all change; find a method that suits you. Consistent effort and flexible adjustment will help you improve.',[76])
extra(c,'tips','Xiaoyu’s tip','“说＋动词／形容词＋就＋动词／形容词”表示动作、状态或变化出现得快。例如：（他）说去就去、（天气）说冷就冷、（安排）说变就变。|说 + verb/adjective + 就 + the same verb/adjective means an action or change happens quickly or unexpectedly: going immediately, suddenly becoming cold, or plans changing suddenly.',[69])
extra(c,'objectives','Chapter objectives','能够听懂并交流生活和工作中的计划与变化。|Understand and discuss plans and changes in life and work.\n能够口头或书面表达自己的计划安排和调整方式。|Describe plans, arrangements and adjustments orally and in writing.\n了解人们对做计划的不同看法以及如何应对变化。|Understand different views on planning and ways of coping with changes.',[66])
extra(c,'self-assessment','Book learning summary','我能使用“本来、推迟、取消、时间表、不得不、不便”等词语谈论计划与变化。|I can use the chapter vocabulary to discuss plans and changes.\n我能理解并运用本课四个语言点。|I can understand and use the four grammar points.\n我能交流计划安排等内容。|I can discuss schedules and plans.\n我能表达对变化的看法和应对方式。|I can express views on changes and how to cope with them.',[77])
section(c,'bonus','Xiaoyu’s bonus content',[L('中国职场新哲学——你有“松弛感”吗？','New workplace philosophy: do you have a sense of ease?')],[76],'The book gives this companion-video topic. The video is not embedded in the supplied PDF.','My notes after watching')
finish(c)

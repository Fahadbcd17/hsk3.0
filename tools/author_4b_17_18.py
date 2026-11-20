import json,re
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parent.parent
meta={c['id']:c for c in json.loads((R/'source/4b/meta.json').read_text())}
def L(s):
 z,e=s.split('|',1);return {'zh':z,'en':e}
def lines(s):return [L(x) for x in s.strip().splitlines() if x.strip()]
def init(n):return {**meta[n],'book':'4B','sourceRange':[meta[n]['page'],89 if n==17 else 102],'words':[],'warmup':[],'pictures':[],'questions':[],'sections':[]}
def sec(c,id,title,blocks,pages,intro=None,note=None):
 s={'id':id,'title':title,'blocks':blocks,'sourcePages':pages}
 if intro:s['intro']=intro
 if note:s['note']=note
 c['sections'].append(s);return s
def vocab(c,s):
 for row in s.strip().splitlines():
  w,en,example,ee,g=row.split('|');c['words'].append({'zh':w,'en':en,'example':L(example+'|'+ee),'grammar':c['grammar'][int(g)-1]})
def question(c,q,answers):
 c['questions'].append({**L(q),'answers':lines(answers)})
def mcqs(c,rows):
 bs=[]
 for i,row in enumerate(rows.strip().splitlines()):
  q,en,opts,oes,answer=row.split('|');zs=opts.split('/');es=oes.split('/');j=ord(answer)-65
  bs.append({**L(q+'|'+en),'heading':f'Choose the answer · Text {i//2+1}, question {i%2+1}','choices':[L(z+'|'+e) for z,e in zip(zs,es)],'input':True,'solution':answer,'answers':[L(zs[j]+'|'+answer+' · '+es[j])]})
 sec(c,'listening','Listen / read & choose',bs,[])
def text(c,n,s,qs,pages,retell=None):
 bs=lines(s)
 for j,row in enumerate(qs.strip().splitlines()):
  z,e,a,ae=row.split('|');bs.append({**L(z+'|'+e),'heading':f'Read & answer {j+1}','input':True,'answers':[L(a+'|'+ae)]})
 item=sec(c,f'text{n}',f'Text {n}',bs,pages,'Role-play the dialogue.' if n<3 else 'Read the text aloud.','Retell this text in your own words')
 if retell:
  prompt,answer,rpages=retell;item['retelling']={'prompt':L(prompt),'answer':L(answer),'pages':rpages}
 return item
def grammar(c,n,explain,examples,practice,pages):
 bs=lines(examples)
 for i,row in enumerate(practice.strip().splitlines()):
  z,e,a,ae=row.split('|');bs.append({**L(z+'|'+e),'heading':f'Book practice · {i+1}','input':True,'answers':[L(a+'|'+ae)]})
 sec(c,f'grammar{n}',f'Grammar {n} · '+c['grammar'][n-1],bs,pages,explain,'My sentence using this grammar')
def gaps(c,banks,rows,pages):
 bs=[{'heading':f'Word bank {i+1}',**L(s)} for i,s in enumerate(banks)]
 for i,row in enumerate(rows.strip().splitlines()):
  z,e,a,ae=row.split('|');bs.append({**L(z+'|'+e),'heading':f'Fill in the blank · {i+1}','input':True,'solution':a,'answers':[L(a+'|'+ae)]})
 sec(c,'exercises','Comprehensive exercises',bs,pages)
def cloze(c,passage,options,answer,pages):
 opts=lines(options);bs=[L(passage)]+[{'heading':chr(65+i),**v} for i,v in enumerate(opts)]
 for i,a in enumerate(answer):bs.append({'heading':f'Gap {i+1}','zh':f'第{i+1}空：____','en':f'Choose A, B, C or D for gap {i+1}.','input':True,'solution':a,'answers':[{**opts[ord(a)-65],'en':a+' · '+opts[ord(a)-65]['en']}]})
 sec(c,'cloze','Complete the passage',bs,pages)
def warm(c,page,words,order,sentences,coords):
 c['warmup']=lines(words);im=Image.open(R/f'assets/4b/page-{page:03}.jpg')
 for i,(answer,sent,box) in enumerate(zip(order,lines(sentences),coords)):
  name=f'4b/c{c["id"]}-warm-{i}.jpg';im.crop(box).save(R/'assets'/name,quality=92);c['pictures'].append({'image':name,'answer':answer,'sentence':sent})
def picture(c,page,box,rows):
 name=f'4b/c{c["id"]}-exercise.jpg';Image.open(R/f'assets/4b/page-{page:03}.jpg').crop(box).save(R/'assets'/name,quality=92)
 bs=[{'image':name,'alt':f'Original chapter {c["id"]} picture-writing exercise'}]
 for i,row in enumerate(rows.strip().splitlines()):
  w,e,a,ae=row.split('|');bs.append({'heading':f'Picture {i+1}','zh':w,'en':e,'input':True,'answers':[L(a+'|'+ae)]})
 sec(c,'picture-writing','Look & write',bs,[page])
c=init(17)
vocab(c,'''路过|pass by|你走你的吧，我还要路过学校。|Go ahead; I still need to pass the school.|1
趟|measure word for a trip|你忙你的吧，我去一趟学校。|Carry on with your work; I will make a trip to school.|1
健身房|gym|你吃你的吧，我去健身房。|Go ahead and eat; I am going to the gym.|1
健身|keep fit; work out|你忙你的吧，我去健身。|Carry on working; I am going to work out.|1
体重|body weight|老师表扬他认真记录自己的体重。|The teacher praised him for carefully recording his weight.|3
会员|member|你看你的吧，我去办会员卡。|Keep looking; I will get a membership card.|1
饼干|biscuit|你吃你的饼干吧，我不饿。|Go ahead and eat your biscuits; I am not hungry.|1
酸奶|yogurt|你喝你的酸奶吧，我喝水。|Go ahead and drink your yogurt; I will have water.|1
果汁|fruit juice|你喝你的果汁吧，我不想喝。|Go ahead and drink your juice; I do not want any.|1
教练|coach|教练表扬他每天都来运动。|The coach praised him for coming to exercise every day.|3
动作|movement|老师表扬他的动作做得好。|The teacher praised him for doing the movements well.|3
科学|scientific; science|连小孩子都知道要科学地运动，大人更应该知道。|Even children know exercise should be scientific; adults should know even better.|4
受伤|be injured|他连走路都会受伤，跑步就更难了。|He can get injured even walking; running is even harder.|4
操场|playground; sports field|你玩你的吧，我去操场。|Go ahead and play; I am going to the sports field.|1
其中|among them|他们一高一矮，其中高的是我哥哥。|One is tall and one short; the tall one is my brother.|2
之|literary linking particle; of|老师表扬他成为好学生之一。|The teacher praised him for becoming one of the good students.|3
火|popular; fire|连爷爷都知道这家店很火，年轻人就更清楚了。|Even Grandfather knows this shop is popular; young people know even better.|4
好处|benefit|连孩子都知道运动的好处，大人更应该知道。|Even children know the benefits of exercise; adults should know even better.|4
设备|equipment|你练你的吧，我看看这里的设备。|Keep practising; I will look at the equipment here.|1
全身|whole body|他连走路都觉得全身疼，跑步就更困难了。|His whole body hurts even when walking; running is even harder.|4
准确|accurate|他说得一清二楚，回答也很准确。|He explained it very clearly and answered accurately.|2
仅仅|only|老师表扬他仅仅用一天就完成了工作。|The teacher praised him for finishing the work in only one day.|3
表扬|praise|老师表扬我认真学习。|The teacher praised me for studying carefully.|3
进步|make progress; progress|老师表扬他取得了进步。|The teacher praised him for making progress.|3
鼓励|encourage|老师表扬我取得了进步，还鼓励我继续学习。|The teacher praised my progress and encouraged me to keep studying.|3
帅|handsome|这两个小伙子一高一矮，都很帅。|The two young men, one tall and one short, are both handsome.|2
乒乓球|table tennis|你打你的乒乓球吧，我看书。|Go ahead and play table tennis; I will read.|1
队|team|教练表扬我们队认真练习。|The coach praised our team for practising carefully.|3
项|measure word for an item or event|老师表扬他完成了这项任务。|The teacher praised him for completing this task.|3
赢得|win; gain|教练表扬他赢得了比赛。|The coach praised him for winning the match.|3
叫作|be called|连孩子都知道这叫作乒乓球，大人就更知道了。|Even children know this is called table tennis; adults know even better.|4
梦|dream|你睡你的吧，我想把刚才的梦写下来。|Go back to sleep; I want to write down the dream I just had.|1
不断|continuously|老师表扬他不断努力。|The teacher praised him for working hard continuously.|3
队员|team member|教练表扬队员按时来训练。|The coach praised the team members for arriving on time to train.|3
训练|train; training|你训练你的吧，我先回家。|Go ahead with your training; I will go home first.|1
球队|ball-game team|老师表扬我们的球队赢得了比赛。|The teacher praised our team for winning the match.|3
球迷|sports fan|连爷爷都是球迷，我就更喜欢看比赛了。|Even Grandfather is a fan; I enjoy watching matches even more.|4
梦想|dream; ambition|老师表扬她为了梦想而努力。|The teacher praised her for working hard for her dream.|3
大赛|major competition|连小孩子都知道这次大赛，大人就更知道了。|Even children know about this major competition; adults know even better.|4
赢|win|教练表扬我们赢了比赛。|The coach praised us for winning the match.|3
连|even|连我都能做这道题，你就更不用担心了。|Even I can do this question, so you have even less reason to worry.|4''')
warm(c,78,'酸奶|yogurt\n饼干|biscuit\n果汁|fruit juice\n教练|coach\n操场|sports field\n健身房|gym',[2,3,0,4,5,1],'''杯子里有果汁。|There is fruit juice in the glass.
他是一位教练。|He is a coach.
这碗酸奶看起来很好吃。|This bowl of yogurt looks delicious.
我们可以在操场跑步。|We can run on the sports field.
这里是一家健身房。|This is a gym.
桌子上有一些饼干。|There are some biscuits on the table.''',[(262,897,427,1051),(512,897,678,1051),(762,897,931,1051),(262,1069,427,1224),(512,1069,678,1224),(762,1069,931,1224)])
question(c,'你去过健身房吗？你喜欢去健身房锻炼身体吗？|Have you been to a gym? Do you like exercising at a gym?', '''我去过，那里很方便。|I have; it is convenient there.
我没去过，我喜欢在公园跑步。|I have not; I like running in the park.
我喜欢和朋友一起去运动。|I like going to exercise with friends.''')
question(c,'你喜欢看什么体育比赛？你有喜欢的运动员或球队吗？|What sports competitions do you like watching? Do you have a favourite athlete or team?', '''我喜欢看足球比赛。|I like watching football matches.
我喜欢看篮球，我哥哥打得很好。|I like watching basketball; my older brother plays well.
我不常看比赛，不过我喜欢游泳。|I do not often watch matches, but I like swimming.''')
sec(c,'objectives','Chapter objectives',lines('''能够听懂并交流健身方式、锻炼习惯等内容。|Understand and discuss fitness routines and exercise habits.
能够口头或书面表达自己的健身经历和喜爱的运动。|Share your fitness experiences and favourite sports orally or in writing.
了解乒乓球在中国的发展和影响。|Understand the development and impact of table tennis in China.'''),[78])
mcqs(c,'''杨同乐一会儿要做什么？|What will Yang Tongle do shortly?|加班/去健身/办会员卡/开车送王一雪回家|Work overtime/Work out/Get a membership card/Drive Wang Yixue home|B
关于那家健身房，下列哪项正确？|Which statement about the gym is correct?|是新开的/非常便宜/离单位比较远/总有打折活动|It is newly opened/It is very cheap/It is far from work/It always has discounts|A
杨同乐为什么不去家附近的健身房？|Why does Yang not go to the gym near home?|太贵了/没有教练/环境不好/要花不少时间|Too expensive/No coach/Poor environment/It would take considerable time|D
公司附近那家健身房的教练怎么样？|What are the coaches at the gym near work like?|很专业/力气大/讲得不清楚/动作不标准|Professional/Strong/Unclear explanations/Incorrect movements|A
杨同乐喜欢用什么方式锻炼？|How does Yang like to exercise?|打球/游泳/去操场跑步/去健身房健身|Play ball games/Swim/Run on the sports field/Work out at the gym|D
关于杨同乐，下列哪项正确？|Which statement about Yang is correct?|身体更健康了/觉得课程简单/不喜欢他的教练/不想坚持健身了|He is healthier/He finds the classes easy/He dislikes his coach/He wants to stop working out|A
中国乒乓球队为什么被叫作“梦之队”？|Why is China's table-tennis team called the Dream Team?|队员很多/队员很年轻/经常赢得比赛/训练时间很长|Many players/Very young players/Often wins matches/Trains for a long time|C
关于乒乓球在中国的情况，下列哪项正确？|Which statement about table tennis in China is correct?|老人最喜欢打乒乓球/只有运动员打乒乓球/年轻人不喜欢打乒乓球/乒乓球是最常见的运动之一|It is older people's favourite sport/Only athletes play/Young people dislike it/It is one of the most common sports|D''')
text(c,1,'''王一雪：下班了！同乐，我今天正好要路过你们家那边，用不用我开车送你？|Wang: Work is over! Tongle, I happen to be passing your neighbourhood today. Would you like a lift?
杨同乐：谢谢一雪姐，不过您走您的吧，我一会儿还要去一趟健身房。|Yang: Thank you, Yixue, but go ahead without me. I need to go to the gym shortly.
王一雪：去健身房？你什么时候开始健身的？|Wang: The gym? When did you start working out?
杨同乐：我上个星期发现单位旁边新开了一家健身房。我最近体重增加了不少，正好想运动一下，就进去看了看。|Yang: Last week I noticed a new gym next to work. I have gained quite a lot of weight lately and wanted some exercise, so I went in to look around.
王一雪：感觉怎么样？|Wang: What did you think?
杨同乐：挺不错的。当时正好有打折活动，我就办了一张会员卡。|Yang: It was pretty good. They happened to have a discount, so I got a membership card.''','''杨同乐为什么想健身？|Why did Yang want to work out?|因为他最近体重增加了不少。|Because he had gained quite a lot of weight recently.
杨同乐为什么办了会员卡？|Why did Yang get a membership card?|因为健身房不错，当时正好有打折活动。|Because the gym was good and happened to offer a discount.''',[79,80],('下班时，王一雪问杨同乐……，因为她今天开车会……。不过，杨同乐不回家，他要先……。他上个星期发现……，就进去……。他最近……，正好想……。那家健身房……，当时……，他就……。|At the end of work, Wang asked Yang … because she would drive past…. However, Yang was going to … first. Last week he noticed … and went in to…. Recently he … and wanted to…. The gym was …; at the time …, so he….','下班时，王一雪问杨同乐要不要她开车送他，因为她今天会路过他家那边。不过，杨同乐要先去健身房。他上个星期发现单位旁边新开了一家健身房，就进去看了看。他最近体重增加了不少，正好想运动。那家健身房挺不错，当时有打折活动，他就办了一张会员卡。|Wang offered Yang a lift after work because she would pass his neighbourhood. Yang wanted to go to the gym first. Last week he had noticed a new gym next to work and looked around. He had gained weight and wanted to exercise. The gym was good and offered a discount, so he obtained a membership card.',[80]))
grammar(c,1,'“你×你的吧” means each person can carry on separately. It often politely declines an offer or invitation.','''您走您的吧，我一会儿还要去一趟健身房。|Go ahead; I still need to visit the gym shortly.
你忙你的吧，我自己就能完成。|Carry on with your work; I can finish this myself.
你们玩你们的吧，我今天想在家休息。|Go ahead and have fun; I want to rest at home today.''','''A：你几点回来？我等你一起吃饭吧。 B：____。|What time will you return? I will wait to eat with you.|你吃你的吧，我可能很晚才回来。|Go ahead and eat; I may return very late.
A：我有点儿累了，不想继续看这个电影了。 B：好，____。|I am a little tired and do not want to keep watching this film. All right, ….|你休息你的吧，我再看一会儿。|Go and rest; I will watch a little longer.
A：你____，我去接个电话。 B：好，我写完告诉你。|You …; I will answer a call. All right, I will tell you when I finish writing.|写你的吧|carry on writing''',[80])
text(c,2,'''王一雪：同乐，你晚上不吃饭就去健身，不会饿吗？|Wang: Tongle, won't you get hungry working out without dinner?
杨同乐：我带了饼干、酸奶和果汁，一会儿吃完了再去。|Yang: I brought biscuits, yogurt and juice. I will have them before going.
王一雪：那你为什么不在家附近找健身房？吃完晚饭，休息一下再去，不是更好吗？|Wang: Why not find a gym near home? Wouldn't it be better to go after dinner and a rest?
杨同乐：离我家最近的健身房也要坐两站公交车，一来一回得半个小时，太浪费时间了。|Yang: Even the nearest gym to my home is two bus stops away. The round trip takes half an hour, which wastes too much time.
王一雪：确实。那这家健身房的教练怎么样？|Wang: True. What are the coaches at this gym like?
杨同乐：教练很热情，也非常专业，动作讲得很清楚。|Yang: They are friendly and professional and explain the movements very clearly.
王一雪：听你这么一说，我也想试试了。我现在都是在家看着视频练，动作不一定标准。|Wang: Hearing that makes me want to try it too. I currently exercise at home with videos, and my movements may not be correct.
杨同乐：好啊，那您也来吧。锻炼要科学，否则容易受伤。|Yang: Great, come along. Exercise must be done scientifically, or it is easy to get injured.''','''杨同乐去健身房前要做什么？|What will Yang do before going to the gym?|他要先吃饼干、喝酸奶和果汁。|He will first have biscuits, yogurt and juice.
王一雪为什么也想去健身房锻炼？|Why does Wang also want to exercise at the gym?|因为教练很专业，能帮助她把动作做标准。|Because the professional coaches can help her perform the movements correctly.''',[81,82])
grammar(c,2,'“一A一B” describes two parallel or contrasting aspects; A and B are single-character words.','''一来一回得半个小时，太浪费时间了。|The round trip takes half an hour; it wastes too much time.
她说话的声音不大，但是一字一句说得很清楚。|Her voice is not loud, but she says every word clearly.
记者和运动员一问一答，谈到了很多比赛中的事情。|The journalist and athlete discussed many things from the competition through questions and answers.''','''A：你怎么没去医院看病？ B：只是点儿小问题，而且____，所以就没去。|Why did you not go to hospital? It was minor, and …, so I did not go.|一来一回要两个小时|the round trip would take two hours
A：这两个房间怎么安排？ B：____，你们两个人住大的，我自己住小的。|How shall we allocate these rooms? …; you two take the big room and I will take the small one.|房间一大一小|one room is big and the other small
A：您看这条裤子，怎么左腿和右腿____？ B：实在抱歉，我现在就给您换一条。|Look at these trousers: why are the two legs …? Sorry; I will exchange them now.|一长一短|one long and one short''',[82])
text(c,3,'''有人爱在操场跑步，有人喜欢通过打球锻炼身体，还有一部分人愿意去健身房健身，杨同乐就是其中之一。|Some people like running on the sports field, some exercise through ball games, and others prefer the gym. Yang Tongle is one of the latter.
杨同乐认为健身房火起来是因为它有很多好处——环境好、设备全，可以锻炼全身。另外，健身房里一般还有专业教练，能帮助大家把动作做准确，练习的效果也更好。|Yang believes gyms have become popular because they offer many benefits: a pleasant environment, complete equipment and whole-body exercise. Professional coaches usually help people perform movements accurately, improving the results.
仅仅经过一个月左右的锻炼，杨同乐就感觉自己的身体比以前更健康了。教练也表扬他取得了很大的进步，并鼓励他坚持下去，还说随着身体越来越好，人看起来也会更帅。|After only about a month of exercise, Yang felt healthier. His coach praised his great progress, encouraged him to continue and said that as his health improved, he would also look more handsome.''','''健身房为什么会火起来？|Why have gyms become popular?|因为环境好、设备全，还有专业教练，可以让锻炼的效果更好。|Because they offer a good environment, complete equipment and professional coaches, improving exercise results.
教练为什么表扬杨同乐？|Why did the coach praise Yang?|因为他经过一个月左右的锻炼，取得了很大的进步。|Because he made great progress after about a month of exercise.''',[82,83],('有人爱……，有人喜欢……，还有一部分人……，杨同乐就是……。杨同乐认为健身房……是因为……——环境……、设备……，可以……。另外，健身房里一般还……，能帮助大家……，……也更好。仅仅经过……，杨同乐就感觉自己的身体……。教练也表扬他……，并鼓励……，还说随着……，人看起来也会……。|Some people enjoy …, others like …, and some …; Yang is…. He thinks gyms … because …: the environment …, equipment … and people can…. They also have … who help people …, improving…. After only …, he felt…. The coach praised him for …, encouraged … and said that as …, he would look….','有人爱跑步，有人喜欢打球，还有一部分人喜欢去健身房，杨同乐就是其中之一。他认为健身房很火是因为环境好、设备全，可以锻炼全身，还有专业教练帮助大家把动作做准确。仅仅经过一个月左右的锻炼，他就感觉身体更健康了。教练表扬他取得了进步，并鼓励他坚持下去，还说身体好了，人看起来也会更帅。|Some like running, others ball games, and others the gym; Yang is one of them. He thinks gyms are popular because of the good environment, equipment and coaches who improve movements. After about a month he felt healthier. His coach praised his progress, encouraged him to continue and said better health would also make him look more handsome.',[84]))
grammar(c,3,'Use 主语＋表扬／批评＋人＋动作 to evaluate what someone has done. The person is both the object of praise/criticism and the subject of the following action.','''教练也表扬他取得了很大的进步。|The coach also praised him for making great progress.
老师表扬白家月坚持每天学习中文。|The teacher praised Bai Jiayue for studying Chinese every day.
经理批评他没有按时完成工作。|The manager criticised him for failing to finish work on time.''','''经理表扬他____。（细心）|The manager praised him for … (careful).|工作很细心|being very careful at work
今天老师表扬我____。（成绩）|Today the teacher praised me for … (results).|取得了好成绩|achieving good results
妈妈总是批评我____。（房间）|Mother always criticises me for … (room).|不收拾房间|not tidying my room''',[84])
text(c,4,'''中国乒乓球队非常有名，常在各项比赛中赢得第一名，被叫作“梦之队”。为了不断提高自己的水平，队员们每天都要进行严格的训练。正因为这样，球队才能在比赛中取得更好的成绩，获得更多球迷的喜爱。许多年轻的乒乓球运动员都有一个梦想，那就是进入国家队，参加世界大赛，为球队赢下比赛。|China's table-tennis team is famous for frequently winning first place and is called the Dream Team. Players train rigorously every day to keep improving. This helps them achieve better results and gain more fans. Many young table-tennis players dream of joining the national team, competing internationally and winning for their team.
在中国，除了专业运动员，喜欢打乒乓球的普通人也特别多。连一些年龄比较大的老人都坚持打球，年轻人更是把它作为一种日常锻炼的方式。可以说，乒乓球是中国人生活中最常见的运动之一。|In China, many ordinary people as well as professional athletes enjoy table tennis. Even some elderly people keep playing, and young people use it as regular exercise. It is one of the most common sports in Chinese daily life.''','''乒乓球队为什么每天都要进行严格的训练？|Why does the table-tennis team train rigorously every day?|为了不断提高水平，在比赛中取得更好的成绩。|To keep improving and achieve better results in competitions.
许多年轻的乒乓球运动员有什么梦想？|What dream do many young table-tennis players have?|他们梦想进入国家队，参加世界大赛，为球队赢下比赛。|They dream of joining the national team, competing internationally and winning for their team.''',[84,85,86])
grammar(c,4,'“连……也／都……，……更……” uses an extreme example to emphasise that another situation is even more so.','''连一些年龄比较大的老人都坚持打球，年轻人更是把它作为一种日常锻炼的方式。|Even some elderly people keep playing; young people especially use it as regular exercise.
我有时候连老师说的话也听不懂，听广播就更难了。|Sometimes I cannot even understand my teacher, so understanding broadcasts is even harder.
今天早上他连脸都没来得及洗，更没有时间准备早饭了。|He did not even have time to wash his face this morning, much less prepare breakfast.''','''受伤以后，他连走路都困难，____。|After the injury, even walking is difficult for him, ….|跑步就更困难了|running is even harder
他连这么难的事情都能解决，____。|He can solve even such difficult matters, ….|这个小问题就更不用担心了|so this small problem is even less worth worrying about
他____，硕士研究生课程就更难了。|He …; master's courses would be even harder.|连本科课程都觉得很难|finds even undergraduate courses difficult''',[86])
gaps(c,['趟、科学、路过、会员、酸奶、健身|trip; science; pass by; member; yogurt; work out','队、赢、准确、梦想、其中、不断|team; win; accurate; dream; among them; continuously'],'''随着____的发展，人们的生活方式发生了很大的变化。|With the development of …, people's lifestyles have changed greatly.|科学|science
昨天我在回家的路上____了一家新开的咖啡店。|Yesterday I … a newly opened café on my way home.|路过|passed by
我吃完晚饭后都会去____，已经坚持两年多了。|I … after dinner and have kept it up for over two years.|健身|work out
她早上一般都会喝杯____，觉得这样对身体有好处。|She usually has a cup of … in the morning, believing it healthy.|酸奶|yogurt
明天我要去一____上海，咱们下周再约时间见面吧。|I will make a … to Shanghai tomorrow; let's meet next week.|趟|trip
楼下新开了一家超市，正在做活动，办____还送小礼物。|The new supermarket downstairs gives small gifts to people who become ….|会员|members
A：昨天的比赛结果怎么样？ B：三比二，我们球队最后____了。|How did yesterday's match end? Three to two; our team ….|赢|won
A：你儿子以后想做什么工作？ B：他的____是当一名医生。|What job does your son want? His … is to become a doctor.|梦想|dream
A：您看我这个句子写得对吗？ B：不太____，你再检查一下吧。|Is my sentence correct? Not quite …; check again.|准确|accurate
A：你最近工作怎么样？ B：公司给我们的任务____增加，我们越来越忙了。|How is work? Our tasks … increase and we grow busier.|不断|continuously
A：他们班参加羽毛球比赛的人多吗？ B：挺多的，____还有几个水平很高的。|Are many in their class playing badminton? Quite a few, with several excellent players ….|其中|among them
A：听说你进入了学校的乒乓球____？ B：没错，我很喜欢打乒乓球，而且打得很好。|I hear you joined the school's table-tennis …? Yes, I love it and play well.|队|team''',[86,87])
cloze(c,'小张以前不太爱运动，下班以后常常在家看电视或玩手机，很少锻炼身体。时间长了，他感觉自己的身体越来越差，____，工作的时候还容易觉得累。后来在朋友的建议下，____。教练先教了他一些最简单的动作。____，但他慢慢练、慢慢改，最后还是坚持了下来。现在，小张已经养成了运动的习惯。他觉得，____，并且坚持锻炼，就一定能取得不错的效果。|Xiao Zhang used to dislike exercise and watched TV or used his phone after work. Over time his health worsened, …, and he tired easily at work. Following advice from a friend, …. A coach taught him simple movements. …, but he gradually practised and improved. Now exercise is a habit. He feels that …, combined with persistence, will bring good results.','''只要方法科学|as long as the method is scientific
体重也一直增加|his weight also kept increasing
他决定去健身房锻炼|he decided to work out at a gym
虽然他刚开始做得还不太标准|although his movements were not quite correct at first''','BCDA',[87])
picture(c,87,(145,1204,995,1429),'''赢得|win|他赢得了比赛，非常高兴。|He won the match and is very happy.
受伤|be injured|她的腿受伤了，需要休息。|Her leg is injured and she needs rest.
球迷|sports fan|球迷们正在给球队加油。|The fans are cheering for their team.''')
sec(c,'tasks','Task-based activities',[{**L('请在班级中做一个调查，了解同学们的运动情况，包括是否有锻炼的习惯、锻炼的方式、选择这种方式的原因、每周锻炼的次数以及每次多长时间等等。|Survey classmates about exercise habits, activities, reasons, weekly frequency and the length of each session.'),'heading':'Survey','input':True,'answers':lines('我每周跑步三次，每次半个小时，因为跑步很方便。|I run three times a week for half an hour because it is convenient.\n我每周和朋友打两次篮球，每次一个小时。|I play basketball with friends twice a week for an hour each time.\n我每天晚饭后散步，身体比以前更好了。|I walk after dinner every day and feel healthier than before.')},*[{**L(f'同学{i}：姓名；是否有锻炼习惯；锻炼方式；原因；每周次数和时长。|Classmate {i}: name; regular exercise habit; activity; reason; weekly frequency and session length.'),'heading':f'Survey record {i}','input':True} for i in range(1,5)],{**L('学校运动会就要到了，老师希望了解同学们的运动情况。请你根据上面调查的内容，写一份调查报告，不少于140字。|The school sports meet is approaching. Write a survey report on classmates’ exercise habits in at least 140 Chinese characters.'),'heading':'Writing · at least 140 characters','input':True,'minChars':140,'answers':lines('为了了解同学们的运动情况，我问了四位同学。他们都觉得运动很重要，不过选择的方式不一样。两位同学喜欢跑步，每周去操场三次，每次半个小时，因为不用花钱，也很方便。一位同学喜欢打篮球，每周和朋友打两次，每次一个小时。他说和朋友一起运动很快乐。另一位同学平时学习很忙，但每天晚上都会散步二十分钟。通过这次调查，我发现大家都有锻炼的习惯。只要选择适合自己的方式，并且坚持下去，身体就会越来越健康。|I surveyed four classmates. All valued exercise but chose different activities. Two ran on the sports field three times weekly for half an hour because it was free and convenient. One played basketball with friends twice weekly for an hour, enjoying their company. The fourth was busy studying but walked twenty minutes every evening. All had exercise habits. Choosing a suitable activity and persisting can improve health.')}],[88])
sec(c,'bonus','Xiaoyu’s bonus content',lines('从公园到手机：中国人的健身日常|From Parks to Apps: Everyday Fitness in China'),[88],'Companion-video topic from the book. Use the book’s digital resources to watch the video.','My notes after watching')
sec(c,'summary','Book learning summary',[{**L(z),'heading':'Rate: No problem / It’s OK / Need to improve','input':True} for z in ['能使用本课“健身房、体重、会员、教练、动作、受伤”等词语，谈论健身和运动的话题。|Use the chapter vocabulary to discuss fitness and sports.','能理解并运用“你×你的吧”“一A一B”“主语＋表扬／批评＋宾语1＋动词＋宾语2”“连……也／都……，……更……”等语言点。|Understand and use the four grammar patterns in this chapter.','能交流健身方式和锻炼习惯等内容。|Discuss fitness routines and exercise habits.','能表达自己的健身经历和喜欢的运动。|Share personal fitness experiences and favourite sports.']],[89])
(R/'source/4b/chapters/17.json').write_text(json.dumps(c,ensure_ascii=False,indent=2))
c=init(18)
vocab(c,'''猜|guess|你到底在猜什么？|What exactly are you guessing?|3
共享单车|shared bicycle|这辆共享单车让他骑走了。|He rode this shared bicycle away.|2
出口|exit|出口到底在哪儿？|Where exactly is the exit?|3
推|push|我推着车走了一小段路。|I pushed the bicycle for a short stretch.|1
对|direct at; towards|你到底对着谁说话？|Who exactly are you talking towards?|3
二维码|QR code|这个二维码到底怎么用？|How exactly do we use this QR code?|3
注册|register|你到底注册了没有？|Have you registered or not?|3
费用|cost; expense|这次旅行的费用到底是多少？|Exactly how much does this trip cost?|3
说明|instructions; explain|使用说明让他拿走了。|He took the instructions away.|2
办事|run errands; handle affairs|我想出去办事，然而外面下大雨了。|I wanted to go out on errands, but it started raining heavily.|4
差点儿|almost|我差点儿忘了一大包衣服。|I almost forgot a large bag of clothes.|1
拍|shoot; photograph|这个视频到底是谁拍的？|Who exactly shot this video?|3
各个|each; every|各个小组到底准备得怎么样了？|How exactly is each group getting on with its preparations?|3
小组|small group|我们小组到底有几个人？|Exactly how many people are in our group?|3
讨论|discuss|你们到底在讨论什么？|What exactly are you discussing?|3
演|play a role; perform|这位老师到底演谁？|Who exactly is this teacher playing?|3
厨师|cook; chef|厨师做了一大碗面条。|The chef made a large bowl of noodles.|1
各地|various places|各地的天气到底有什么不同？|How exactly does the weather differ across places?|3
著名|famous|这家饭馆很著名，然而我没去过。|This restaurant is famous, but I have never been there.|4
小吃|snack; local delicacy|他买了一大包小吃。|He bought a large bag of snacks.|1
互联网|internet|互联网到底给我们带来了什么？|What exactly has the internet brought us?|3
点赞|click Like|你到底给谁点赞了？|Whose post exactly did you like?|3
AI眼镜|AI glasses|这副AI眼镜到底怎么用？|How exactly do these AI glasses work?|3
3D打印机|3D printer|这台3D打印机让老师搬走了。|The teacher moved this 3D printer away.|2
上门|visit someone at home|他到底什么时候上门服务？|Exactly when will he come to provide the home service?|3
到底|exactly; after all (emphasis in questions)|你到底想买什么？|What exactly do you want to buy?|3
仅|only|我们仅走了一小段路。|We walked only a short stretch.|1
多样|varied; diverse|这里的小吃丰富多样，然而我吃不下了。|The snacks here are varied, but I cannot eat any more.|4
推出|release; introduce|这个新计划到底什么时候推出？|Exactly when will this new plan be introduced?|3
预约|make an appointment|我想预约，然而今天已经没有时间了。|I wanted to make an appointment, but there were no times left today.|4
取|fetch; collect|快递让妈妈取走了。|Mother collected the parcel.|2
原因|reason|他不来的原因到底是什么？|What exactly is the reason he is not coming?|3
然而|however|我想去旅行，然而没有时间。|I want to travel, but I have no time.|4
不必|need not|你不必买了，面包都让他买回来了。|You need not buy any; he has already brought the bread home.|2
亲戚|relative|我的亲戚送来了一大包水果。|My relatives brought a large bag of fruit.|1
按|according to; press|你到底有没有按说明做？|Did you follow the instructions or not?|3
提出|propose; raise|这个问题到底是谁提出的？|Who exactly raised this question?|3
大大|greatly|这大大方便了大家，然而还有一些问题。|This made things much more convenient, but some problems remain.|4
现有|existing; currently available|现有的东西到底够不够？|Are the things currently available enough or not?|3''')
warm(c,90,'厨师|chef\n推|push\n小吃|snack\n拍|shoot a video\n取|fetch\n3D打印机|3D printer',[4,2,0,1,5,3],'''他在取东西。|He is collecting something.
这里有很多好吃的小吃。|There are many delicious snacks here.
这位厨师正在做饭。|This chef is cooking.
他推着车往前走。|He is pushing the cart forward.
这是一台3D打印机。|This is a 3D printer.
他用手机拍视频。|He is shooting a video with his phone.''',[(294,908,458,1059),(541,908,705,1059),(789,908,953,1059),(294,1077,458,1231),(541,1077,705,1231),(789,1077,953,1231)])
question(c,'你喜欢看什么样的短视频？|What kinds of short videos do you like watching?', '''我喜欢看做饭的视频。|I like cooking videos.
我喜欢看中国各地的风景。|I like seeing scenery from different places in China.
我喜欢看教中文的视频，可以一边看一边学。|I like Chinese teaching videos because I can learn while watching.''')
question(c,'你拍过短视频吗？如果拍过，请介绍一下你拍的短视频；如果没拍过，你想不想试试拍短视频？|Have you made a short video? If so, describe it; if not, would you like to try?', '''我拍过一次，是和朋友一起吃饭的时候拍的。|I made one once while eating with friends.
我还没拍过，但是想介绍一下我的学校。|I have not yet, but I want to introduce my school.
我喜欢看视频，不过现在还不想自己拍。|I enjoy watching videos, but I do not want to make my own yet.''')
sec(c,'objectives','Chapter objectives',lines('''能够听懂并交流新技术应用、科技进步改变生活等方面的话题。|Understand and discuss new technologies and how technological progress changes life.
能够口头或书面表达怎样拍摄短视频、对短视频的看法等。|Explain how to make short videos and express opinions about them orally or in writing.
了解中国的共享单车、短视频、上门经济等新经济形态。|Understand China's bike-sharing, short videos and on-demand home-service economy.'''),[90])
mcqs(c,'''安妮是怎么到白家月的学校的？|How did Annie reach Bai's university?|先骑车后坐地铁/先坐地铁后骑车/先骑车后坐公交车/先坐公交车后骑车|Bicycle then subway/Subway then bicycle/Bicycle then bus/Bus then bicycle|D
第一次骑共享单车，需要扫码后再在App上：|After scanning the code for a first shared-bike ride, what must you do in the app?|进行支付/完成注册/查看信息/找回密码|Pay/Register/View information/Recover a password|B
老师留的短视频作业是关于什么的？|What was the assigned short video about?|中国美食/饮料广告/校园生活/著名景点|Chinese food/Drink advertising/Campus life/Famous sights|A
大家觉得安妮他们小组拍的短视频怎么样？|What did people think of Annie's group video?|有些无聊/效果一般/非常精彩/让人感动|A little boring/Average/Excellent/Moving|C
安妮和朋友们怎么看科技的发展？|What do Annie and her friends think about technological development?|科技发展很快/科技不影响世界/科技改变了人们的生活/科技能帮人减轻工作压力|Technology develops quickly/Technology does not affect the world/Technology changes people's lives/Technology reduces work pressure|C
安妮他们的短视频是用什么拍的？|What did Annie's group use to shoot the video?|相机/手机/电脑/电视|Camera/Mobile phone/Computer/Television|B
根据课文，上门服务怎么预约？|According to the text, how are home services booked?|直接打电话/在网上预约/在线下预约/让服务员预约|By telephone/Online/Offline/Through a waiter|B
赵女士觉得上门服务怎么样？|What does Ms Zhao think of home services?|很方便/难预约/价格低/不安全|Convenient/Hard to book/Cheap/Unsafe|A''')
text(c,1,'''白家月：安妮，我们在这儿呢。|Bai: Annie, we are over here.
安妮：天中、家月，你们猜我是怎么过来的？|Annie: Tianzhong, Jiayue, guess how I got here.
白家月：坐公交车吗？|Bai: By bus?
安妮：我先坐的公交车，然后骑共享单车，快到那边那个出口时又推了一小段。|Annie: I took the bus first, then rode a shared bike. Near that exit, I pushed it for a short distance.
白家月：我看很多人都骑共享单车，我还没骑过呢。|Bai: I see many people riding shared bikes, but I have not tried one.
陈天中：我骑过，很方便的。第一次骑的时候，你打开微信，对着共享单车上的二维码扫一下，在App上完成注册就可以了，怎么使用、费用标准什么的App上都有说明。|Chen: I have; they are convenient. The first time, open WeChat, scan the bike's QR code and register in the app. The app explains how to use it, the charges and so on.
白家月：好啊！哪天我出去办事时也试试。|Bai: Great! I will try it one day when I go out on errands.''','''白家月骑过共享单车吗？如果没骑过，她想什么时候骑？|Has Bai ridden a shared bike? If not, when would she like to?|她没骑过，想哪天出去办事时试试。|She has not, and wants to try one when she goes out on errands.
第一次骑共享单车时应该做些什么？了解些什么？|What should you do and learn before your first shared-bike ride?|应该打开微信扫码，在App上注册，并了解使用方法和费用标准。|Open WeChat, scan the code, register in the app and learn how to use it and what it costs.''',[91,92],('安妮到白家月和陈天中的学校玩，她先坐……，然后……，快到一个出口时又……。白家月说她看很多人……，但她……呢。陈天中介绍说，他骑过共享单车，……。第一次……，打开微信，对着……扫一下，在App上……就可以了，而且，怎么使用、……什么的App上……。白家月听完表示，她哪天出去……。|Annie visited her friends’ university. She first took …, then …, and near an exit she…. Bai had seen many people … but had not…. Chen said shared bikes were…. The first time, open WeChat, scan … and … in the app, which also explains use and…. Bai said she would … when going out….','安妮到白家月和陈天中的学校玩，她先坐公交车，然后骑共享单车，快到出口时又推了一小段。白家月还没骑过共享单车。陈天中说共享单车很方便，第一次骑时，打开微信扫码，在App上完成注册就可以了。App上有使用方法和费用标准的说明。白家月想哪天出去办事时试试。|Annie took a bus and then a shared bike to visit her friends, pushing it briefly near the exit. Bai had never tried one. Chen explained that shared bikes are convenient: scan the code with WeChat and register in the app, which explains use and fees. Bai wanted to try one when running errands.',[92]))
grammar(c,1,'“数词＋形容词＋量词” emphasises size or amount, often with 一 and 大／小 in spoken Chinese: 一大碗、一小段.','''快到那边那个出口时又推了一小段。|Near that exit, I pushed it for a short stretch.
今天早上我没吃饭就去上班了，中午饿极了，吃了一大碗面条儿。|I went to work without breakfast, was very hungry at noon and ate a large bowl of noodles.
我今天又收到了妈妈寄来的快递，打开一看，除了衣服外，里边还有一大包巧克力。|Mother sent another parcel today. Besides clothes, it contained a large bag of chocolate.''','''A：这____，够热闹的。 B：今天是我生日，请朋友们来家里一起聚聚，热闹热闹。|What a lively …! It is my birthday, so I invited friends over.|一大屋子人|whole roomful of people
A：最近天气有些热，我天天喝绿茶。 B：我也是，昨天又买了____。|It has been hot, so I drink green tea daily. Me too; yesterday I bought another ….|一大包茶叶|large packet of tea leaves
A：您太客气了，怎么做了____？ B：不客气，你们好不容易来一次，我特别开心。|You are so kind; why did you prepare …? You rarely visit, so I am delighted.|一大桌子菜|a whole tableful of dishes''',[92])
text(c,2,'''安妮：差点儿忘了，我给你们看个短视频。|Annie: I nearly forgot. Let me show you a short video.
白家月：啊？你们拍的？真不错！|Bai: Oh, did you make it? It is really good!
安妮：对！前段时间老师留了个作业，叫各个小组拍个短视频，介绍中国美食。我们小组讨论后决定，由AI小语演厨师，做出中国各地的著名小吃。拍完后，老师说很不错。|Annie: Yes! Our teacher assigned each group a short video introducing Chinese food. We decided that AI Xiaoyu would play a chef making famous snacks from around China. The teacher liked the finished video.
陈天中：嗯，语言也很幽默！|Chen: The language is humorous too!
安妮：后来这个视频让我同学放到了互联网上，很多人都来点赞。|Annie: A classmate later posted it online, and many people liked it.
白家月：看来大家都喜欢这个视频。|Bai: It seems everyone likes the video.
安妮：后边我们打算拍第二个、第三个，让小语带大家到中国各地走一走、看一看。|Annie: We plan to make a second and third video, with Xiaoyu showing people different parts of China.
陈天中：这样大家就能通过你们的视频了解中国了，我支持你们！|Chen: Then people can learn about China through your videos. You have my support!''','''老师留作业后，安妮和同学们拍了什么样的短视频？|What video did Annie and her classmates make?|他们让AI小语演厨师，介绍中国各地的著名小吃。|They had AI Xiaoyu play a chef introducing famous snacks from around China.
安妮后边还想拍什么短视频？|What videos does Annie want to make next?|她想让小语带大家到中国各地走一走、看一看。|She wants Xiaoyu to show people different parts of China.''',[93,94])
grammar(c,2,'“主语＋让／叫＋宾语＋动词＋其他成分” expresses the passive voice. The subject receives the action; the person after 让／叫 performs it. It is common in conversation.','''后来这个视频让我同学放到了互联网上。|Later this video was posted online by my classmate.
门叫小明给关上了。|The door was closed by Xiaoming.
不好意思，月饼都让我吃了。|Sorry, I ate all the mooncakes.''','''A：那双鞋你没买到吗？ B：对，____买去了。|Did you miss out on those shoes? Yes, … bought them.|那双鞋让别人|someone else
A：杯子在哪儿呢？ B：杯子____。|Where is the cup? The cup ….|让妈妈拿走了|was taken away by Mother
A：你的手机呢？ B：____。|Where is your phone?|我的手机叫弟弟拿去看视频了。|My younger brother took my phone to watch videos.''',[94,95])
text(c,3,'''安妮骑共享单车到了白家月、陈天中的学校，三人从共享单车聊到AI眼镜和3D打印机，从绿色经济聊到上门经济。科技到底对世界产生了怎样的影响？他们都认为，科技确实改变了人们的生活。|Annie rode a shared bike to her friends’ university. The three discussed shared bikes, AI glasses, 3D printers, the green economy and home services. What impact has technology had on the world? They all agreed it has changed people's lives.
接着，安妮给大家看了她和同学们拍的短视频。安妮说，短视频是用手机拍的，他们装了一些免费的App，仅用几天就拍完了。视频里，小语做的小吃丰富多样，看起来好吃极了。短视频推出后，大家认为非常精彩，白家月和陈天中看后也特别喜欢，并且表示支持他们拍更多的视频。|Annie then showed the video she and her classmates made. They installed free apps on their phones and completed filming in just a few days. Xiaoyu's varied snacks looked delicious. Viewers found the released video excellent. Bai and Chen also loved it and supported making more.''','''安妮和同学们的短视频是怎么拍的？|How did Annie and her classmates make their video?|他们用手机，装了一些免费的App，仅用几天就拍完了。|They used phones with free apps and finished in just a few days.
对于安妮他们拍的短视频，白家月和陈天中有什么想法？|What did Bai and Chen think of the video?|他们特别喜欢，并支持安妮他们拍更多的视频。|They loved it and supported making more videos.''',[95,96],('安妮骑……到了白家月、陈天中的学校，三人从……聊到AI眼镜和3D打印机，从……聊到上门经济。科技到底对世界产生了怎样的影响？他们都认为，……。接着，安妮给大家看了……。安妮说，短视频是……，他们装了一些……，仅用几天就……。视频里，……做的小吃……，看起来……。短视频推出后，大家认为……，白家月和陈天中看后也……，并且表示……。|Annie rode … to the university. They discussed …, AI glasses, 3D printers, … and home services, agreeing that…. She showed them…. It was filmed with … using … and finished in…. In the video, … made snacks that were … and looked…. After release, viewers thought …; her friends also … and supported….','安妮骑共享单车到朋友们的学校，大家从共享单车聊到AI眼镜和3D打印机，从绿色经济聊到上门经济。他们认为科技改变了人们的生活。接着安妮给大家看了她和同学们拍的短视频。他们用手机和免费的App，仅用几天就拍完了。视频里，小语做的小吃丰富多样，看起来很好吃。大家都觉得视频很精彩，白家月和陈天中也支持他们拍更多的视频。|Annie and her friends discussed shared bikes, AI glasses, 3D printers and new economic models, agreeing that technology changes life. She showed a video made with phones and free apps in only a few days. Xiaoyu prepared varied, delicious-looking snacks. Everyone found it excellent, and Bai and Chen supported more videos.',[96]))
sec(c,'tips','Xiaoyu’s Tips',lines('绿色经济是兼顾经济发展、节约资源和保护环境的经济模式。|A green economy balances economic development, resource conservation and environmental protection.'),[95])
grammar(c,3,'“到底” is used in questions for persistent inquiry or emphasis: what exactly, who on earth, or whether something really is the case.','''科技到底对世界产生了怎样的影响？|What exactly has technology's impact on the world been?
你们到底还来不来？|Are you coming or not?
你到底是怎么想的？为什么不同意？|What exactly are you thinking? Why do you disagree?''','''你们____呢？（点赞）|What exactly …? (click Like)|到底给谁点赞了|whose post did you like
这个AI眼镜____？还是请他____。（说明）|These AI glasses …? We had better ask him to … (explain).|到底怎么用；说明一下|how exactly do they work; explain
这次旅行____？咱们还是一起算一下吧。（费用）|This trip …? Let's calculate it together. (cost)|费用到底是多少|exactly how much does it cost''',[96,97])
text(c,4,'''随着互联网技术的发展，现在又出现了一种新的服务方式——上门经济，就是预约者通过网上预约，让服务人员在合适的时间到家里或者约好的地点服务，服务内容有上门做饭、照顾小动物、取东西等。赵女士养了一只猫，由于工作等原因，她需要经常出差，然而又很担心猫的安全。有了上门服务后，她觉得方便多了，不必再找亲戚帮忙。每次出差，在网上预约并支付费用后，服务人员就会按她提出的要求上门照顾小猫，大大减轻了她的压力，赵女士也特别满意。|Internet technology has enabled the home-service economy. Customers book online for workers to visit their home or another agreed location at a suitable time. Services include cooking, pet care and collecting items. Ms Zhao has a cat and travels often for work, worrying about its safety. Home services mean she no longer needs relatives to help. Before each trip she books and pays online, and workers care for the cat according to her requests. This greatly reduces her stress, and she is satisfied.
当然，上门经济也有一些问题，特别是现有服务人员有些还不够专业，需要重新学习，提高服务质量。|Of course, home services also face problems. Some current workers are not sufficiently professional and need further learning to improve service quality.''','''什么是上门经济？|What is the home-service economy?|顾客在网上预约，让服务人员到家里或约好的地点提供服务。|Customers book online for workers to provide services at their home or an agreed location.
上门经济还有什么问题？|What problems remain with home services?|有些服务人员还不够专业，需要学习并提高服务质量。|Some workers need more professional skills and training to improve service quality.''',[97,98])
grammar(c,4,'“然而” begins a contrasting clause: what follows contrasts with the earlier situation or goes against expectations.','''由于工作等原因，她需要经常出差，然而又很担心猫的安全。|She needs to travel often for work, but worries about her cat's safety.
毕业旅行现在越来越流行，然而由于学生没什么社会和生活经验，可能会遇到各种问题。|Graduation trips are increasingly popular, but students may face problems because they lack social and life experience.
春天应该是花开的季节，然而由于前一段时间下大雪，现在花都没开。|Spring should be the flowering season, but because of recent heavy snow, the flowers have not bloomed.''','''我们计划了一周，____，天却下起了大雨。|We planned for a week, …, but it began to rain heavily.|然而刚准备出发|but just as we were ready to leave
他想站起来，____，怎么也站不起来。|He wanted to stand, …, and could not get up.|然而腿受伤了|but his leg was injured
他很想出去旅行，____。|He really wants to travel, ….|然而最近工作太忙了|but he has been too busy at work lately''',[98,99])
gaps(c,['互联网、猜、提出、按、差点儿、各地|internet; guess; propose; according to; almost; various places','推出、不必、到底、讨论、仅、取|release; need not; exactly; discuss; only; collect'],'''请大家____一下，我手里拿的是什么东西？|Please … what I am holding.|猜|guess
你从手机上打开使用说明，____说明一步一步做就行了。|Open the instructions on your phone and follow them step by step, … the instructions.|按|according to
春节前，____火车站都增加了服务人员，保证大家出行安全。|Before Spring Festival, stations in … increased staff for safe travel.|各地|various places
他们____了一个能够更好地保护环境的建议。|They … a suggestion to better protect the environment.|提出|proposed
由于早上起晚了，他们____没赶上飞机。|They woke late and … missed the plane.|差点儿|almost
____让我们的生活越来越方便，我们可以在网上购物，也可以和在外地的父母视频聊天儿。|The … makes life more convenient, enabling shopping and video calls with distant parents.|互联网|internet
A：经理，这次调查发现，还是有一些客人对我们酒店的服务不太满意。 B：我们周五开个会，____一下怎么解决这个问题。|Some surveyed guests remain dissatisfied with our hotel service. Let's meet Friday to … a solution.|讨论|discuss
A：这是什么菜？味道真好，我以前都没吃过。 B：您好，这是我们新____的一道菜，叫香辣鱼块。|What is this delicious dish? It is our newly … spicy fish.|推出|introduced
A：你们的这个小船____是不是用纸做的？ B：是用纸做的，但不是普通的纸。|Is this little boat really made of paper? Yes, but not ordinary paper.|到底|really; exactly
A：我去____个快递，顺便买个早餐，你想吃什么？ B：给我带两个包子吧。|I will … a parcel and buy breakfast. What would you like? Two buns, please.|取|collect
A：这把伞我明天就还给你。 B：你用吧，____还给我了，我还有一把。|I will return your umbrella tomorrow. Keep it; you … return it, as I have another.|不必|need not
A：这道题我们都做不出来，他____用不到五分钟就做出来了。 B：我知道他特别聪明。|None of us could solve it, but he used … less than five minutes. I know he is clever.|仅|only''',[99])
cloze(c,'随着科技的发展，社会上有了一种新的看病方式——线上看病，互联网医院就这样出现了。____，就可以在互联网医院线上看病。____：首先病人根据病情选择好医院和科室，然后在网上填写姓名、身体情况和看病经历等，____。互联网医院的出现，____，这种方式也越来越受到欢迎。|Technology has brought online medical consultations and internet hospitals. …, patients can consult online. …: first choose a hospital and department according to the condition, then enter personal details, health information and medical history online, …. Internet hospitals …, and this approach is becoming more popular.','''线上看病一般分为以下几步|online consultations generally involve the following steps
病人只要有手机和网络|as long as patients have a phone and internet access
给人们看病提供了方便|have made medical consultations more convenient
最后才能和医生线上交流|only then can they speak with the doctor online''','BADC',[100])
picture(c,100,(192,632,1030,829),'''小组|small group|我们小组正在讨论工作。|Our group is discussing work.
亲戚|relative|亲戚们聚在一起吃饭。|The relatives have gathered for a meal.
办事|handle affairs|他正在银行办事。|He is handling business at the bank.''')
sec(c,'tasks','Task-based activities',[{**L('三至四人一组，根据亲身经历，谈谈科技的发展给人们生活带来的便利，讨论后由一人报告小组讨论结果。|In groups of three or four, discuss personal experiences of how technology makes life convenient, then have a representative report the results.'),'heading':'Group discussion','input':True,'answers':lines('我可以在网上买东西，不用出门。|I can shop online without leaving home.\n我每天和家人视频聊天儿，觉得我们没有离得很远。|I video-chat with my family daily and do not feel far away.\n手机地图能帮助我找到想去的地方。|Phone maps help me find places I want to visit.')},{**L('安妮和同学们拍的短视频很有意思，很多人点赞。请以“我也想拍个短视频”为题目，写一篇短文，谈谈你想拍什么样的短视频，想怎么拍，不少于140字。|Write at least 140 Chinese characters titled “I Want to Make a Short Video, Too”, explaining what you want to film and how.'),'heading':'Writing · at least 140 characters','input':True,'minChars':140,'answers':lines('我也想拍个短视频，向朋友们介绍我的学校。我打算和两位同学一起完成这个任务。首先，我们要讨论内容，选好拍摄的时间和地点。然后，我用手机拍学校的教室、图书馆和操场，一位同学负责介绍，另一位同学帮我们检查声音。我们还想请老师说几句话，让大家了解学校的课程。拍完以后，我们会用免费的App把视频做好，加上简单的中文和英文说明。最后，我们把视频发给家人和朋友，请他们提出建议。我希望通过这个视频，让更多人喜欢我们的学校，也让自己的中文口语取得进步。|I want to make a short video introducing my school with two classmates. We will discuss content, timing and locations. I will film classrooms, the library and sports field on my phone; one classmate will present and the other check sound. We will invite a teacher to introduce courses. Afterwards we will edit with a free app and add simple Chinese and English explanations. We will share it with family and friends for feedback. I hope more people will like our school and that my spoken Chinese will improve.')}],[100,101])
sec(c,'bonus','Xiaoyu’s bonus content',lines('中国的共享经济新形态——“租享万物”|China’s New Sharing Economy: Everything for Rent'),[101],'Companion-video topic from the book. Use the book’s digital resources to watch the video.','My notes after watching')
sec(c,'summary','Book learning summary',[{**L(z),'heading':'Rate: No problem / It’s OK / Need to improve','input':True} for z in ['能使用本课“共享单车、拍、互联网、上门、推出、预约、不必、现有”等词语，谈论科技改变生活方面的话题。|Use the chapter vocabulary to discuss how technology changes life.','能理解并运用“数词＋形容词＋量词”“主语＋让／叫＋宾语＋动词＋其他成分”“到底”“……，然而……”等语言点。|Understand and use the four chapter grammar patterns.','能介绍如何骑共享单车、拍短视频等信息。|Explain how to use shared bicycles and make short videos.','能表达对新经济形态的看法。|Express opinions about new economic models.']],[101,102])
(R/'source/4b/chapters/18.json').write_text(json.dumps(c,ensure_ascii=False,indent=2))

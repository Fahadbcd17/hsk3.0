import sys
sys.path.insert(0,'tools')
from book4b_author import *
c=chapter(12)
words(c,'''毛衣|sweater|这件毛衣不怎么贵。|This sweater is not very expensive.
样子|appearance; style|我不怎么喜欢这个样子。|I do not much like this style.
适合|suit; be suitable|这件衣服不怎么适合我。|These clothes do not really suit me.
售货员|shop assistant|无论客人买不买，售货员都很热情。|The assistant is friendly whether customers buy or not.
质量|quality|这件衣服的质量不怎么好。|The quality of these clothes is not very good.
强|better; strong|无论谁更强，我们都要认真比赛。|Whoever is stronger, we must compete seriously.
年底|end of the year|无论工作多忙，年底我都会回家。|However busy work is, I go home at year-end.
全|whole; all|为了全家高兴而认真准备吧。|Prepare carefully for the whole family’s happiness.
打折|give a discount|这家店不怎么打折。|This shop seldom gives discounts.
值|worth; be worth|为了家人高兴而花这些钱很值。|Spending this money for the family’s happiness is worthwhile.
估计|estimate; guess|我不是不知道，我估计他明天来。|It is not that I do not know; I think he comes tomorrow.
期|session; issue|无论哪一期活动，我都想参加。|Whichever session it is, I want to join.
听力|hearing; listening ability|为了提高听力而每天练习。|Practise daily to improve listening.
烦|annoyed; bothered|无论多烦，都要好好说话。|However annoyed you are, speak kindly.
脱|take off|为了不弄湿衣服，他不得不脱下外衣。|To keep his clothes dry, he had to take off his coat.
挂|hang|我不得不把衣服挂在房间里。|I have to hang the clothes in the room.
脾气|temper|他不怎么发脾气。|He seldom loses his temper.
伤心|sad|无论多伤心，我都会陪着你。|However sad you are, I will stay with you.
批评|criticise|老师不怎么批评他。|The teacher seldom criticises him.
道歉|apologise|做错了事，不能不道歉。|If you do wrong, you must apologise.
老家|hometown|无论走多远，我都会想起老家。|However far I travel, I think of my hometown.
自|since; from|自毕业后，我就不怎么回学校了。|Since graduating I rarely return to school.
父母|parents|无论我做什么，父母都关心我。|Whatever I do, my parents care about me.
父子|father and son|这对父子不怎么一起出去。|This father and son seldom go out together.
母子|mother and son|无论住在哪里，这对母子都常联系。|Wherever they live, this mother and son stay in touch.
无论|no matter; regardless|无论下不下雨，我都会来。|Whether it rains or not, I will come.
条件|condition|无论条件怎么样，我们都要努力。|Whatever the conditions, we must work hard.
允许|allow|学校不允许我们这样做，我们不得不改变计划。|The school does not allow this, so we must change plans.
另外|in addition; separately|为了大家吃得好，我另外买了一些水果。|To help everyone eat well, I bought extra fruit.
卫生|hygiene; cleanliness|无论多忙，都要注意卫生。|However busy you are, pay attention to hygiene.
母亲|mother|无论我去哪里，母亲都很关心我。|Wherever I go, my mother cares about me.
待|stay|我不怎么待在家里。|I do not often stay home.
将|object-marking preposition, like 把|为了让妈妈高兴，他将房间打扫干净了。|To please his mother, he cleaned the room.
闻|smell|我不怎么闻得到花香。|I can hardly smell the flowers.
味道|taste; smell|这个味道不怎么好。|This does not taste very good.
冷静|calm|无论发生什么，都要冷静。|Whatever happens, stay calm.
鼻子|nose|我的鼻子不怎么舒服。|My nose feels rather uncomfortable.
父亲|father|无论多晚，父亲都会等我回来。|However late it is, my father waits for me.
城|city|这座城不怎么大。|This city is not very large.
鲜|fresh; delicious|这碗汤不怎么鲜。|This soup is not particularly tasty.
暖|warm|为了让房间更暖，他关上了窗户。|To make the room warmer, he closed the window.
勇敢|brave|无论有多难，我们都要勇敢面对。|However difficult it is, face it bravely.
商量|discuss; consult|遇到重要的事，不能不和家人商量。|For important matters, you must consult your family.''','不怎么／无论……都……／为了……而……')
c['warmup']=lines('''打折|discount
毛衣|sweater
鼻子|nose
勇敢|brave
脱|take off
伤心|sad''')
c['questions']=questions('''过节时，你会给家人买什么礼物？|What gifts do you buy your family for festivals?|我会买他们爱吃的东西。|I buy food they enjoy.|我想给妈妈买一件衣服。|I want to buy my mother some clothes.|我会先问问他们需要什么。|I ask what they need first.
你的家人因为一些事情伤心时，你会怎么办？|What do you do when a family member is upset?|我会陪他聊聊天儿。|I chat with them.|我会听他说，不急着提建议。|I listen without rushing to advise.|我会和他一起想办法。|I help them think of a solution.''')
listening(c,'''杨同乐认为毛衣的颜色怎么样？|What does Yang think of the sweater’s colour?|很合适|Very suitable|不合适|Unsuitable|正流行|Fashionable|太深了|Too dark|B
商场年底有什么活动？|What year-end offer does the shop have?|买一送一|Buy one get one free|买二送一|Buy two get one free|全场七折|30 percent off everything|免费送货|Free delivery|C
爷爷、奶奶下午去做什么了？|What did the grandparents do in the afternoon?|打扫卫生|Clean|在家睡觉|Sleep at home|接小明放学|Collect Xiaoming|参加老年班活动|Attend a senior-class activity|D
王一雪批评小明，是因为他：|Why did Wang criticise Xiaoming?|总是迟到|Always late|不打扫房间|Does not clean|对奶奶发脾气|Lost his temper with grandmother|考试前不复习|Does not revise|C
杨同乐每个周末都会做什么？|What does Yang do every weekend?|回上海|Return to Shanghai|去北京出差|Visit Beijing for work|带父母旅游|Travel with parents|给父母打电话|Phone his parents|D
刘明的母亲身体变差后，刘明和王一雪：|What did Liu and Wang do when his mother’s health declined?|不再工作了|Stopped working|请别人帮忙照顾|Hired care|带父母回了老家|Took parents home|把父母接到了自己家|Brought parents to live with them|D
林静静下班回家后热的是：|What did Lin heat after work?|奶茶|Milk tea|鸡汤|Chicken soup|包子|Steamed buns|米饭|Rice|B
父母给林静静寄了什么？|What did Lin’s parents send?|好用的|Useful things|好吃的|Good food|好玩的|Fun things|好看的|Pretty things|B''')
text(c,1,'''王一飞：你觉得老妈穿这件毛衣怎么样？|Wang: How would this sweater look on Mum?
杨同乐：样子不错，就是颜色好像不怎么适合她。|Yang: The style is nice, but the colour may not suit her.
售货员：老年人穿这种颜色的衣服正合适，颜色不深，质量还特别好。您看那位阿姨正试着呢，是不是很好看？|Assistant: This colour suits older people. It is not dark, and the quality is excellent. Look at that lady trying it; doesn’t it look good?
王一飞：嗯，是挺不错的。同乐，我印象中，老妈也常穿这种颜色的衣服，她应该会喜欢的，买一件吧。|Wang: Yes. I remember Mum wearing this colour often. She should like it; let’s buy one.
杨同乐：好的，老妈高兴比什么都强。|Yang: All right. Mum’s happiness matters most.
售货员：就是，老人开心最重要。我们店正好年底有活动，全场打七折呢，挺值的。|Assistant: Exactly. We have a year-end offer: thirty percent off everything, excellent value.''','''售货员认为老人穿那件毛衣怎么样？|What does the assistant think of the sweater for an older person?|颜色正合适，不深，质量也好。|The colour suits them, is not dark, and the quality is good.
杨同乐最后为什么愿意买那件毛衣了？|Why does Yang agree to buy it?|因为母亲应该会喜欢，母亲高兴最重要。|His mother should like it, and her happiness matters most.''',[18,19],dict(pages=[19],prompt=line('杨同乐和王一飞去商场给父母买衣服。王一飞选了一件毛衣后问杨同乐……，杨同乐觉得样子还可以，但是颜色……。售货员说老年人穿这种颜色……，……，质量也好。王一飞也觉得不错，认为老妈也常穿……，她会……。杨同乐说，老妈高兴……。售货员告诉他们，现在店里正好……，全场……，挺值的。','They shop for their parents. Wang asks…. Yang likes the style but…. The assistant says the colour…and quality…. Mum often wears…and should…. Her happiness…. The shop has…and everything is….'),answer=line('杨同乐和王一飞给母亲买毛衣。杨同乐觉得样子不错，但颜色不怎么适合母亲。售货员说颜色正合适，不深，质量很好。王一飞说母亲常穿这种颜色，应该会喜欢。杨同乐觉得母亲高兴最重要。商场年底全场打七折，所以很值。','Yang and Wang buy a sweater for Mum. He doubts the colour, but the assistant says it suits older people and has good quality. Wang remembers Mum wearing that colour. Yang agrees her happiness matters most. The year-end thirty-percent discount makes it good value.')))
text(c,2,'''刘明：爷爷、奶奶还没回来呢？|Liu: Haven’t Grandpa and Grandma returned?
王一雪：没呢，估计快了。下午老年班举办一期听力保护活动，他们去参加活动了。|Wang: Not yet, probably soon. They attended a hearing-protection activity at the senior class this afternoon.
刘明：他们的活动还挺丰富的！|Liu: Their activities are quite varied!
王一雪：嗯。小明最近要考试，心里有点儿烦，昨天因为脱、挂衣服这点儿小事，就对奶奶发脾气了。|Wang: Xiaoming is bothered about his exams. Yesterday he lost his temper with Grandma over taking off and hanging up clothes.
刘明：是吗？他这样做老人该伤心了。|Liu: Really? That must have upset her.
王一雪：就是啊。他也不是不知道自己错了，我批评他以后，他马上说放学回来就向奶奶道歉。|Wang: Yes. He knows he was wrong. After I criticised him, he promised to apologise after school.
刘明：好的，我也再跟他聊聊。|Liu: I will talk to him too.
王一雪：那就更好了。|Wang: That would be even better.''','''小明因为什么对奶奶发了脾气？|Why did Xiaoming lose his temper?|因为脱、挂衣服的小事，也因为考试前心里烦。|Over taking off and hanging clothes, while stressed about exams.
小明发脾气后，王一雪和小明都做了什么？|What did Wang and Xiaoming do afterward?|王一雪批评他，他答应放学后向奶奶道歉。|She criticised him; he promised to apologise after school.''',[20,21])
text(c,3,'''杨同乐的老家在上海，他自毕业后一直在北京工作。虽然没和父母生活在一起，但父子、母子关系特别好。杨同乐很关心父母，无论平时工作有多忙，他每个周末都会给父母打电话。条件允许时，他会回上海看父母。|Yang’s hometown is Shanghai, but he has worked in Beijing since graduation. Though living apart, he is very close to his parents. However busy he is, he calls every weekend and visits Shanghai when possible.
刘明和王一雪结婚后，一直没有和父母生活在一起，他们平时会另外找时间去看父母，帮父母做做饭，打扫打扫卫生。这两年，刘明的母亲身体不太好，他们很担心，就把父母接到了自己家里照顾。父母待在他们身边，他们也终于能放心地去工作了。|After marriage, Liu and Wang lived separately from their parents but visited to cook and clean. When Liu’s mother’s health declined over the past two years, they brought the parents into their home. Having them nearby allowed them to work with peace of mind.''','''杨同乐是怎么关心父母的？|How does Yang care for his parents?|每个周末给他们打电话，条件允许时回上海看他们。|He calls every weekend and visits Shanghai when possible.
刘明和王一雪为什么要把父母接到自己家里？|Why did Liu and Wang bring their parents home?|因为母亲身体不好，他们想照顾父母。|His mother was unwell and they wanted to care for them.''',[22,23],dict(pages=[23],prompt=line('杨同乐的老家……，他自毕业后一直在……。虽然没和父母……，但……特别好。杨同乐很关心父母，无论……，他每个周末都会……。条件允许时，他会……。刘明和王一雪结婚后，一直没有和父母……，他们平时会……去看父母，帮父母……，……。这两年，刘明的……，他们……，就把父母……。父母待在他们身边，他们也终于能……。','Yang’s hometown is…and he works…. Although living apart, their relationship…. Regardless of…, he calls…. When possible he…. Liu and Wang visited their parents to…and…. When his mother…, they brought them…. Now they can….'),answer=line('杨同乐的老家在上海，毕业后一直在北京工作。他和父母关系很好，无论多忙，每周末都打电话，条件允许时就回上海看父母。刘明和王一雪原来另外找时间看父母，帮他们做饭、打扫卫生。后来刘明的母亲身体不好，他们把父母接到家里照顾，这样终于可以放心地工作。','Yang works in Beijing and keeps close contact with his parents in Shanghai through calls and visits. Liu and Wang used to visit to cook and clean; when his mother became unwell, they brought both parents home and could work reassured.')))
text(c,4,'''下班回家，林静静将父母从老家寄来的鸡汤热了热，当闻到从小就熟悉的味道时，平时冷静的她鼻子还是酸了。|After work, Lin Jingjing heated chicken soup sent by her parents. Its familiar childhood aroma brought tears to the usually composed woman.
林静静一个人来北京工作三年了，父母总是担心她为了节约时间而不好好吃饭，所以每个月都给她寄各种好吃的。这次母亲专门做了林静静最爱喝的鸡汤，为了让食物新鲜，父亲选择了城里最快的快递，上午寄出，下午就能收到。|She has worked alone in Beijing for three years. Worried she neglects meals to save time, her parents send food monthly. Her mother made her favourite soup; her father chose the fastest courier so it arrived the same afternoon, fresh.
鸡汤很鲜，林静静心里更暖，她觉得父母好像就在身边。都说“儿行千里母担忧”，父母总对她说：“遇到困难别害怕，要勇敢面对，任何时候都可以和父母商量。”尽管在大城市生活压力有些大，但每当想到父母的这些话，尝到来自老家熟悉的味道，她就觉得又能笑着面对生活了。|The tasty soup warmed her heart, as though her parents were beside her. Parents worry when children travel far. They tell her to face difficulties bravely and consult them anytime. Despite city pressures, their words and familiar food restore her ability to face life with a smile.''','''父亲为什么选择最快的快递？|Why did her father choose the fastest courier?|为了让食物新鲜，下午就能收到。|To keep food fresh and have it arrive that afternoon.
是什么让林静静能“笑着面对生活”？|What helps Lin face life with a smile?|父母关心她的话和老家熟悉的味道。|Her parents’ caring words and familiar tastes from home.''',[24,25])
grammar(c,1,'不怎么 means “not very” or “not often”, expressing a low degree or frequency.','''样子不错，就是颜色好像不怎么适合她。|The style is nice, but the colour does not really suit her.
他总是在图书馆看书，不怎么出去玩。|He reads at the library and seldom goes out for fun.
我爱吃饺子、包子，不怎么喜欢吃米饭。|I love dumplings and buns but do not much like rice.''','''A：今天天气怎么样了？B：挺不错的，____。|How is today’s weather? Quite good,….|不怎么冷|not very cold
A：你看起来好像____。B：是的，____。|You seem…. Yes,….|不怎么高兴。是的，我今天不怎么想说话|not very happy. Yes, I do not feel like talking today
A：你常去体育馆打球吗？B：____。|Do you often play ball at the gym?|我不怎么去|I seldom go''',[19])
grammar(c,2,'Double negatives affirm more strongly: 不是不 = it is not that…not; 不能不 = must; 不得不 = have no choice but.','''他也不是不知道自己错了。|It is not that he does not know he was wrong.
今天是我们毕业后第一次同学聚餐，你又是班长，不能不来啊！|This is our first reunion and you were class monitor; you must come!
由于天气不好，飞机不能起飞，爸爸不得不改变计划，明天再去上海。|Bad weather grounded the plane, so Dad had to postpone Shanghai until tomorrow.''','''A：家里的东西太多了，____。B：是啊，搬家是很不容易。|There are too many things at home,…. Yes, moving is hard.|不得不请朋友帮忙|we have to ask friends for help
A：这么重要的活动你不参加吗？B：____，是实在没有时间。|Are you missing such an important event? …, I truly have no time.|我不是不想参加|It is not that I do not want to join
A：你们学校真大啊！B：为了能准时上课，____。|Your campus is huge! To reach class on time,….|我们不得不早点儿出门|we have to leave earlier''',[21,22])
grammar(c,3,'无论……都／也…… indicates that the result stays the same under any circumstances.','''无论平时工作有多忙，他每个周末都会给父母打电话。|However busy he is, he calls his parents every weekend.
只要你努力了，无论你考多少分，你在我们眼里都是最优秀的。|If you tried, whatever your score, you are the best in our eyes.
无论你遇到什么困难，我都会在你身边。|Whatever difficulties you face, I will be beside you.''','''她很爱读书，____，都要带上一本书。（待）|She loves reading and takes a book wherever…. (stay)|无论在哪里待|wherever she stays
父亲无论多忙，周末____。（陪）|However busy Dad is, on weekends…. (accompany)|都会陪我们|he always spends time with us
____，我都相信我们能成功。（条件）|…, I believe we can succeed. (conditions)|无论条件怎么样|Whatever the conditions''',[23,24])
grammar(c,4,'为了 introduces a purpose; 而 introduces the action taken to achieve it.','''父母总是担心她为了节约时间而不好好吃饭。|Her parents worry she neglects meals to save time.
我们都在为了生活幸福而努力工作着。|We all work hard for a happy life.
他们为了保护环境而拒绝使用纸杯。|They refuse paper cups to protect the environment.''','''我为了这次比赛____。|For this competition I….|而认真准备了很久|prepared carefully for a long time
他____而努力学中文。|He studies Chinese hard in order to….|为了在中国工作|work in China
____努力练习。|…practises hard.|她为了提高成绩而|She, to improve her results,''',[25])
section(c,'objectives','Chapter objectives',lines('''能够听懂并交流关于幸福家庭的话题。|Understand and discuss happy families.
能够口头或书面讲述幸福家庭的生活故事。|Tell stories of happy family life orally and in writing.
了解中国人的亲情文化特点。|Understand Chinese family and kinship culture.'''),[17])
section(c,'tips','Xiaoyu’s Tips',lines('''“老妈”是口语中对母亲的一种亲切、亲昵的称呼。|老妈 is an affectionate informal term for one’s mother.
在中国家庭中，常常会按照孩子的辈分来称呼家庭成员，这样更亲切，也方便孩子理解家庭关系。|Chinese families often use the child’s perspective when addressing relatives, making relationships clearer and warmer.
“儿行千里母担忧”的意思是孩子长大后无论去哪里，父母都担心、牵挂着。|“A mother worries when her child travels far” means parents care about their grown children wherever they go.'''),[18,20,24])
ex=questions('''这位护士工作认真，最大的优点是遇到任何事情都很____。|This diligent nurse’s strength is remaining … in any situation.|冷静|calm
这家饭馆的汤味道特别____，每次来我都要点。|This restaurant’s soup is particularly …; I order it each time.|鲜|tasty
____你多大，在父母眼里，你一直都是那个需要被照顾的孩子。|…your age, to your parents you remain a child needing care.|无论|Regardless of
看到母亲那么喜欢这件毛衣，我觉得花多少钱都____了。|Seeing Mum love the sweater makes any price….|值|worthwhile
小徐____2006年就离开了老家，在上海读大学，毕业后又在那儿工作了。|Xiao Xu has been away …2006, studying and working in Shanghai.|自|since
我们换条路走吧，前面那个路口不____右转。|Let’s change routes; that junction does not … right turns.|允许|allow
A：我想买这条裤子送给妈妈。B：颜色很适合她，____也不错。|I want these trousers for Mum. The colour suits her and the … is good.|质量|quality
A：你好像不太开心。B：昨天我的银行卡丢了，我现在心里很____。|You seem unhappy. I lost my bank card and feel….|烦|annoyed
A：排队的人这么多，____得等很长时间。B：他家的包子好吃又便宜。|So many people; I …we will wait a long time. Their buns are good and cheap.|估计|guess
A：对不起，我刚刚不应该对你发____。B：没关系。|Sorry, I should not have lost my …with you. It’s all right.|脾气|temper
A：请加一碗米饭，____再加一双筷子。B：好的。|Please add rice and …a pair of chopsticks. Sure.|另外|also
A：周末时我喜欢去公园散步，不喜欢在家____着。B：我也喜欢出去活动。|I like park walks rather than …at home. I also enjoy going out.|待|staying''')
for i,b in enumerate(ex):b['heading']=f'Fill in the blank · {i+1}'
section(c,'exercises','Comprehensive exercises',[dict(heading='Word bank · Questions 1–6',**line('自　无论　允许　冷静　值　鲜','since; regardless; allow; calm; worth; tasty'))]+ex[:6]+[dict(heading='Word bank · Questions 7–12',**line('估计　另外　待　烦　质量　脾气','guess; additionally; stay; annoyed; quality; temper'))]+ex[6:],[26])
opts=lines('''忘记了今天是自己的生日|forgot it was his birthday
没想到送餐地址是自己家|did not expect the delivery address to be his home
外卖员的眼睛红了|the delivery worker’s eyes reddened
要注意身体|take care of your health''')
bs=[line('中午，一个外卖员到奶茶店取餐，拿到后一看，____，上面还写着：“爸爸，生日快乐！天气很热，____。”原来，外卖员忙着工作，____，但他的女儿没有忘。看着这份生日礼物，____。他喝了奶茶，又继续努力工作。','At noon a delivery worker collected milk tea and saw ____. The note read: “Happy birthday, Dad! It is hot; ____.” Busy with work, he ____, but his daughter remembered. Seeing the gift, ____. He drank it and continued working.')]+[dict(heading=chr(65+i),**o) for i,o in enumerate(opts)]
for i,a in enumerate('BDAC'):bs.append(dict(heading=f'Gap {i+1}',zh=f'第{i+1}空：____',en=f'Gap {i+1}',input=True,solution=a,answers=[dict(opts[ord(a)-65],en=a+' · '+opts[ord(a)-65]['en'])]))
section(c,'cloze','Complete the passage',bs,[26])
section(c,'picture-writing','Look & write',[dict(image='4b/c12-exercise.jpg',alt='Original chapter 12 picture-writing prompts')]+questions('''老家|Use 老家 to describe picture 1.|我的老家有一条河。|There is a river in my hometown.
烦|Use 烦 to describe picture 2.|她听到这些声音，觉得很烦。|She feels annoyed by these sounds.
商量|Use 商量 to describe picture 3.|他们正在商量一件事。|They are discussing something.'''),[27])
bs=questions('''三人一组，一人扮演杨同乐，两人扮演他的父母。周末晚上，杨同乐给父母打电话聊天儿。|In groups of three, role-play Yang phoning his parents on a weekend evening.|爸爸、妈妈，你们最近身体怎么样？|Dad and Mum, how have you been feeling?|我们很好，你工作再忙也要好好吃饭。|We are well. Eat properly however busy work gets.|好的，我有时间就回去看你们。|I will visit when I have time.
你喜欢大家庭，还是小家庭？请写一篇短文说明理由，不少于140字。|Do you prefer an extended or nuclear family? Explain why in at least 140 Chinese characters.|我比较喜欢大家庭，因为一家人住在一起，可以互相照顾。爷爷、奶奶有很多生活经验，我遇到问题时，喜欢听听他们的想法。父母工作忙的时候，家里其他人也能帮忙。晚上大家一起吃饭，聊聊一天发生的事，我觉得很幸福。当然，住在一起也可能有不同的意见。无论谁不开心，我们都应该先冷静下来，好好商量，不能因为一点儿小事就发脾气。如果自己做错了，就要勇敢道歉。我认为幸福的家庭不是从来没有问题，而是每个人都愿意关心别人，为了全家的幸福而一起努力。|I prefer an extended family because we can care for one another. Grandparents offer experience and others help when parents are busy. Shared dinners make me happy. Differences still arise, so we should stay calm, discuss them and apologise for mistakes. A happy family is not problem-free; its members care for others and work together.''')
bs[0]['heading']='Role-play';bs[1].update(heading='Writing · at least 140 characters',minChars=140)
section(c,'tasks','Task-based activities',bs,[27])
section(c,'bonus','Xiaoyu’s bonus content',lines('中国人的家庭观念|The Chinese concept of family'),[27],intro='The companion-video topic is provided in the book. Watch using the book’s digital resources, then save your notes.',note='My notes after watching')
section(c,'summary','Book self-assessment',[dict(**line(z,e),input=True,heading='No problem / It’s OK / Need to improve') for z,e in [('能使用本课词语谈论幸福家庭。','I can discuss happy families using this chapter’s words.'),('能理解并运用本课语言点。','I can use the chapter grammar.'),('能表达幸福的家庭应该是什么样子的，能讲述幸福家庭的故事。','I can describe a happy family and tell family stories.')]], [28])
from PIL import Image
im=Image.open(R/'assets/4b/page-017.jpg')
sentences=lines("""这是我的鼻子。|This is my nose.
他很勇敢。|He is brave.
她正在脱衣服。|She is taking off her clothes.
这家店的东西打折了。|The goods in this shop are discounted.
这件毛衣很好看。|This sweater looks nice.
她很伤心。|She is very sad.""")
for i,a in enumerate([2,3,4,0,1,5]):
 x=[264,511,755][i%3];y=[879,1046][i//3];path=f'4b/c12-warm-{i}.jpg'
 im.crop((x,y,x+161,y+149)).save(R/'assets'/path,quality=92)
 c['pictures'].append(dict(image=path,answer=a,sentence=sentences[i]))
Image.open(R/'assets/4b/page-027.jpg').crop((185,185,975,368)).save(R/'assets/4b/c12-exercise.jpg',quality=92)
save(c)

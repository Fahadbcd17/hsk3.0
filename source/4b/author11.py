import sys
sys.path.insert(0,'tools')
from book4b_author import *
c=chapter(11)
words(c,'''老年|old age|即使到了老年，他也每天学习。|Even in old age, he studies every day.
散步|take a walk|即使很忙，我也每天散步。|Even when busy, I take a walk every day.
丰富|rich; varied|生活不是没意思，而是很丰富。|Life is not boring but full of variety.
羡慕|admire; envy|即使你羡慕他，也要做好自己的事。|Even if you envy him, do your own work well.
即使|even if|即使下雨，我也要去学校。|Even if it rains, I will go to school.
活|live; lively; work|他不是只为了工作而活，而是想过好自己的生活。|He does not live only for work; he wants a good life.
继续|continue|即使很难，我也会继续学习。|Even if it is difficult, I will keep studying.
网友|online friend|就是不能见面，我也能和网友聊天儿。|Even if we cannot meet, I can chat with online friends.
无聊|boring; bored|这本书不是无聊，而是很有意思。|This book is not boring; it is interesting.
数字|digital; number|就是不去学校，我也能用数字教室学习。|Even without going to school, I can study in a digital classroom.
点名|call the roll|即使人很多，老师也会一个一个点名。|Even with many people, the teacher calls each name.
教授|professor|即使很忙，教授也会回答学生的问题。|Even when busy, the professor answers students’ questions.
线上|online|就是在家，我也能在线上学习。|Even at home, I can study online.
线下|offline; in person|我们不是打电话，而是在线下见面。|We are meeting in person rather than talking on the phone.
视频|video|就是不去那里，我也能看视频了解情况。|Even without going there, I can learn about it from a video.
记录|record|这个记录不是我的，而是老师的。|This record is the teacher’s, not mine.
资料|material; information|即使资料很多，我也要认真看。|Even with a lot of material, I will read it carefully.
自学|study on one’s own|就是没有老师，我也可以自学。|Even without a teacher, I can study on my own.
口语|spoken language|即使说得不好，我也每天练口语。|Even if I speak poorly, I practise speaking every day.
科技|science and technology|科技改变生活，就是说，生活会越来越方便。|Technology changes life; that is, life becomes more convenient.
获取|obtain|就是在家，我们也能获取知识。|Even at home, we can acquire knowledge.
礼貌|courtesy; polite|即使不喜欢他，也要有礼貌。|Even if you dislike him, be polite.
打招呼|greet|即使不认识，我也会和他打招呼。|Even if I do not know him, I will greet him.
家长|parent|家长不是只关心学习，而是关心孩子的生活。|Parents care about their children’s lives, not just their studies.
成功|successful; succeed|即使这次不成功，我也要再试试。|Even if I do not succeed this time, I will try again.
分数|score; mark|即使分数不高，我也不会放弃。|Even with a low score, I will not give up.
目的|purpose|我的目的不是买东西，而是看看朋友。|My purpose is to visit friends, not shop.
养成|develop a habit|即使很忙，我也要养成读书的习惯。|Even when busy, I want to develop a reading habit.
留|leave; reserve; stay|即使工作多，我也会留时间休息。|Even with much work, I leave time to rest.
做法|way of doing something|我不是不喜欢你，而是不喜欢这个做法。|I dislike this approach, not you.
棒|excellent; great|你的中文很棒，就是说，你说得很好。|Your Chinese is great; that is, you speak very well.
一生|one’s whole life|学习是一生的事，就是说，我们要一直学习。|Learning is lifelong; that is, we should keep learning.
快速|rapid; fast|即使事情快速变化，我也会认真准备。|Even if things change rapidly, I will prepare carefully.
优秀|excellent|即使已经很优秀，他也每天学习。|Even though already excellent, he studies daily.
律师|lawyer|律师不是老师，而是帮助人解决法律问题的人。|A lawyer helps solve legal problems rather than teaching.
仍|still|即使已经很晚，他仍在学习。|Even though it is late, he is still studying.
准时|punctual; on time|即使下雨，我也会准时到。|Even if it rains, I will arrive on time.
网页|webpage|就是在家，我也能打开这个网页。|Even at home, I can open this webpage.
弹|play a musical instrument|即使练习时间不多，她也弹得很好。|Even with little practice time, she plays very well.
钢琴|piano|就是没有钢琴，我也可以先看书学习。|Even without a piano, I can begin learning from books.
重新|again; anew|即使做错了，我也可以重新开始。|Even if I make a mistake, I can start again.''','即使……也……／不是……而是……／就是说')
c['warmup']=lines('''分数|score
资料|materials
自学|self-study
钢琴|piano
网页|webpage
家长|parent''')
for i,(a,z,e) in enumerate([(1,'桌上有一些学习资料。','There are study materials on the desk.'),(5,'家长陪孩子去学校。','The parents accompany their child to school.'),(0,'他的分数是一百分。','His score is one hundred.'),(4,'我们可以打开网页学习。','We can open a webpage to study.'),(3,'这里有一架钢琴。','There is a piano here.'),(2,'她在家自学。','She studies on her own at home.')]):c['pictures'].append(dict(image=f'4b/c11-warm-{i}.jpg',answer=a,sentence=line(z,e)))
c['questions']=questions('''你上过线上课吗？你觉得怎么样？|Have you taken online classes? What did you think?|上过，在家学习很方便。|Yes. Studying at home is convenient.|上过，但是我更喜欢在教室里学习。|Yes, but I prefer studying in a classroom.|没有，我想试一试。|No. I would like to try.
在你的国家，老年人都怎么生活？|How do older people live in your country?|他们常常去公园走走。|They often walk in the park.|有些人帮孩子照顾家人。|Some help their children care for family members.|他们也和朋友聊天儿、一起学习。|They also chat and learn with friends.''')
listening(c,'''白家月觉得公园里老年人的生活怎么样？|What does Bai think of the older people’s lives?|很开心|Happy|很丰富|Varied|很辛苦|Hard|很无聊|Boring|B
李文的爷爷每周去老年班做什么？|What does Li’s grandfather study weekly?|学电脑|Computers|学唱歌|Singing|学写字|Writing|学太极拳|Tai chi|A
白家月认为线上点名怎么样？|What does Bai think of online attendance checks?|节约时间|Saves time|不太方便|Inconvenient|比较随意|Casual|很吸引学生|Attracts students|A
对安妮来说，线上上课时，自己不用急着做的事情是：|What need Annie not rush to do online?|写作业|Homework|找资料|Find materials|记笔记|Take notes|提问题|Ask questions|C
以前，王一雪和刘明认为孩子的人生怎样才是成功的？|What once defined success for their children?|变得有名|Become famous|有很多钱|Have much money|上个好大学|Attend a good university|有个好工作|Have a good job|C
后来，王一雪和刘明认为教育是为了让孩子：|What did they later think education should do?|获得高分|Get high marks|按时做作业|Do homework on time|有个好身体|Be physically healthy|养成好习惯|Develop good habits|D
“学而不厌”是孔子什么时候说的？|When did Confucius speak of tireless learning?|二十多年前|Over twenty years ago|两百多年前|Over two hundred years ago|两千多年前|Over two thousand years ago|五千多年前|Over five thousand years ago|C
坚持学习，爷爷觉得怎么样？|How does continued learning make grandfather feel?|很开心|Happy|有点儿累|A little tired|更健康了|Healthier|年轻起来了|Younger|D''')
text(c,1,'''白家月：这里的老年人真不少。|Bai: There are many older people here.
李文：嗯，住在附近的老年人都会来这儿，有的散步，有的唱歌、跳舞，还有的打太极拳。|Li: Older people nearby come here. Some walk, some sing and dance, and others practise tai chi.
白家月：他们的生活真丰富，让人羡慕。|Bai: Their lives are so varied. I envy them.
李文：是的。有些人即使年龄大了，也坚持去老年班学习。|Li: Yes. Some keep attending classes even at an advanced age.
白家月：真是活到老学到老啊。|Bai: You are never too old to learn.
李文：对，我爷爷就每周都去老年班学电脑。他总说，老年人也要继续学习，“你看，我都七八十岁了，还上网和网友们聊天儿呢，生活一点儿都不无聊。”|Li: My grandfather studies computers every week. He says older people must keep learning: “I’m in my seventies or eighties and still chat with online friends. Life is not boring at all.”''','''在公园里，老年人都会做些什么活动？|What activities do older people do in the park?|有的散步，有的唱歌、跳舞，还有的打太极拳。|Some walk, sing or dance; others practise tai chi.
李文的爷爷为什么去老年班学习？|Why does Li’s grandfather attend classes?|因为他觉得老年人也要继续学习，生活才不无聊。|He feels older people should keep learning so life is not boring.''',[6,7],dict(pages=[7],prompt=line('李文和白家月在公园里散步。白家月觉得公园里的老年人……。李文说，住在附近的老年人都……，有的……，有的……、……，还有的……。白家月说，这里的老年人生活……，让人……。李文告诉她，有些老年人即使……，也坚持……。比如，他爷爷每周都去老年班……。爷爷说：“你看，我都……，还上网……呢，生活……。”','Li and Bai walk in the park. Bai thinks there are…. Nearby older people all…; some…, some…and…, and others…. Their lives are…and make her…. Even when…, some keep…. His grandfather studies…weekly. He says, “I am already…, but still…online; life….”'),answer=line('李文和白家月在公园里散步。白家月觉得老年人很多，生活很丰富，让人羡慕。李文说，他们有的散步，有的唱歌、跳舞，还有的打太极拳。有些人即使年龄大了，也坚持学习。李文的爷爷每周去老年班学电脑。他都七八十岁了，还上网和网友聊天儿，生活一点儿都不无聊。','Li and Bai walk in the park. Bai admires the many older people’s varied lives. Some walk, sing, dance or practise tai chi. Some keep learning despite their age. Li’s grandfather attends computer classes weekly and chats online in his seventies or eighties; he is never bored.')))
text(c,2,'''安妮：家月，我们今天的课是在数字教室上的，感觉挺不一样的。|Annie: Jiayue, our class in a digital classroom felt very different today.
白家月：是的，数字教室可以拍照点名，教授在线上点名，不用像线下那样一个个叫名字，特别节约时间。|Bai: Yes, it takes a picture to check attendance. The professor need not call names individually, saving time.
李文：最方便的是，课上没听明白时，课后还能在学校网站上找到视频记录看。|Li: Most conveniently, if you miss something, you can watch the recorded video on the school website later.
安妮：对，上课我都不用着急记笔记了。|Annie: Right. I need not rush to take notes.
李文：不仅数字教室很方便，现在网上到处是学习资料，想查什么都能查到，自学也更方便了。|Li: Besides digital classrooms, learning materials are everywhere online, making information searches and self-study easier.
白家月：是的，只要有手机或电脑，我就是不在教室，也可以学习中文，和同学一起练口语。|Bai: With a phone or computer I can study Chinese and practise speaking with classmates even outside the classroom.
安妮：科技真是让获取知识变得简单多了。|Annie: Technology makes acquiring knowledge much simpler.''','''李文说，线上上课时，如果没听懂，课后还可以怎么做？|What can you do after an online class if you did not understand?|可以在学校网站上找到视频记录看。|Watch the recording on the school website.
人们自学为什么变得越来越方便了？|Why is self-study becoming easier?|因为网上到处是学习资料，想查什么都能查到。|Learning materials and information are widely available online.''',[8,9])
text(c,3,'''今天星期六，我们去了一雪姐姐家。姐姐家的两个孩子很有礼貌，我们一进门，就马上和我们打招呼。|Today, Saturday, we visited Yixue. Her two children greeted us politely as soon as we entered.
在姐姐家，我们也聊到了孩子的教育。姐姐说，以前他们和很多家长一样，觉得孩子上个好大学，人生才是成功的。所以，他们只关心孩子的分数，结果孩子压力特别大，每天都很不开心。后来，他们认识到，教育的目的不是让孩子考高分，而是帮助孩子养成好习惯。于是，他们做出改变，每天都给孩子留出时间外出锻炼身体，或者看些自己感兴趣的书。|We discussed children’s education. Like many parents, they once thought success meant attending a good university. Focusing only on scores made the children stressed and unhappy. They later realised education should develop good habits rather than merely high marks. They changed, leaving time daily for exercise or books the children enjoyed.
我觉得他们的做法真棒。|I think their approach is excellent.''','''以前，王一雪的孩子为什么不开心？|Why were Wang’s children unhappy before?|因为家长只关心分数，孩子压力很大。|Their parents focused only on scores, causing great pressure.
王一雪和刘明做出了什么样的改变？|What changes did Wang and Liu make?|他们每天给孩子留时间锻炼身体或看自己感兴趣的书。|They left time each day for exercise or enjoyable reading.''',[10,11],dict(pages=[11],prompt=line('星期六，白家月和李文去了……。王一雪的两个孩子……，他们一进门，两个孩子就……。在王一雪家，他们也聊到了……。王一雪说，以前他们……，觉得孩子……，人生才是成功的。所以，他们只关心……，结果孩子……，每天都……。后来，他们认识到，教育的目的不是……，而是帮助孩子……。于是，他们……，每天都给孩子……外出锻炼身体，或者看些……。白家月觉得王一雪和刘明的做法……。','On Saturday Bai and Li visited…. The children were…and greeted them…. They discussed…. The parents once thought…and focused on…, making the children…. They later realised education should not…but…. They changed by giving time for…and…. Bai thought their approach….'),answer=line('星期六，白家月和李文去了王一雪家。两个孩子很有礼貌，马上和他们打招呼。他们聊到了孩子的教育。以前王一雪和刘明只关心分数，觉得上好大学才是成功的，结果孩子压力很大。后来，他们认为教育不是让孩子考高分，而是帮助孩子养成好习惯。他们每天给孩子留时间运动或读喜欢的书。白家月觉得这个做法很棒。','Bai and Li visited Wang on Saturday. The polite children greeted them. They discussed education: the parents had focused on scores and university success, causing stress. They later valued good habits, allowing time for exercise and enjoyable reading. Bai approved.')))
text(c,4,'''“学而不厌”是两千多年前中国教育家孔子说过的话，意思是人要一直坚持学习，就是说，学习是人一生的事情，要活到老学到老。在世界快速变化的今天，“学而不厌”变得更加重要。|Confucius spoke of tireless learning over two thousand years ago: learning is lifelong. In today’s rapidly changing world this matters even more.
我有一位很优秀的律师朋友，他一直在学习新的法律知识。他说，这不仅是律师的要求和责任，也是提高自己能力的重要方法。|An excellent lawyer friend continually studies new legal knowledge. It is both a professional responsibility and an important way to improve his abilities.
同时我也认为，人就是不再工作了，坚持学习仍很重要。就像我爷爷，虽然七十多岁了，每天还准时去老年大学上课，学习做网页、弹钢琴。他说，重新当一回学生，生活更有意思了，也感觉自己变年轻了。|I also think continued learning matters even after retirement. My grandfather, in his seventies, attends senior university punctually to study webpage creation and piano. Becoming a student again makes life more interesting and makes him feel younger.''','''“活到老学到老”是什么意思？|What does “never too old to learn” mean?|学习是一生的事情，人要一直坚持学习。|Learning is lifelong and we should keep learning.
那位律师为什么一直坚持学习法律知识？|Why does the lawyer keep studying law?|这是工作的要求和责任，也是提高能力的方法。|It is a professional duty and a way to improve his abilities.''',[12,13])
grammar(c,1,'即使 introduces an unfavourable or extreme hypothetical condition; 也 shows that the outcome or decision remains unchanged.','''有些人即使年龄大了，也坚持去老年班学习。|Some people keep attending senior classes even when older.
即使明天下大雨，我们也会按时出发。|Even if it rains heavily tomorrow, we will leave on time.
即使大家都说很难，我也要试一试。|Even if everyone says it is difficult, I want to try.''','''A：门前的花长得真不错！B：是的，即使缺水，____。|A: The flowers are growing well! B: Yes, even without enough water,….|也能长得很好|they can still grow well
A：即使不在一个学校了，____？B：当然！平时没时间，假期也要多聚聚。|A: Even if we attend different schools, …? B: Of course! We can meet during holidays.|我们也会常联系吧|we will keep in touch, right
A：任务这么重，你们能完成吗？B：____。|A: Can you finish such a heavy task? B:….|即使很难，我们也会认真完成|Even if it is difficult, we will complete it carefully''',[7])
grammar(c,2,'就是……也…… expresses “even if” in spoken Chinese; the second clause stays true despite an extreme condition.','''我就是不在教室，也可以学习中文，和同学一起练口语。|Even outside the classroom I can study Chinese and practise speaking with classmates.
锻炼身体很重要，就是再忙，也要坚持运动。|Exercise matters; however busy you are, keep exercising.
明天开会需要这份材料，我就是今晚不睡觉，也要把它改完。|We need this document tomorrow; even if I stay awake all night, I must finish revising it.''','''A：经理不来，我们怎么办呢？B：经理就是不来，____。|A: What if the manager does not come? B: Even if the manager does not come,….|我们也要按时开始|we must start on time
A：外边下小雨呢，我们还去吗？B：____，我们也得去。|A: It is drizzling. Are we still going? B: …, we must go.|就是下大雨|Even if it rains heavily
A：李教授不在北京，这个问题咱们怎么解决呢？B：____。咱们可以和他在线上交流。|A: Professor Li is away. How can we solve this? B:…. We can talk online.|他就是不在北京，也可以帮助我们|Even outside Beijing, he can help us''',[9,10])
grammar(c,3,'不是……而是…… denies the first possibility and affirms the second, emphasising their contrast.','''教育的目的不是让孩子考高分，而是帮助孩子养成好习惯。|Education aims to develop good habits rather than just high scores.
我不是想喝茶，而是想喝水。|I want water, not tea.
我放学后不是直接回家，而是先去超市买笔。|After school I go to the supermarket for pens rather than straight home.''','''他们不是在聊天儿，____。（线上会议）|They are not chatting; … (online meeting).|而是在开线上会议|they are having an online meeting
他____，而是在练口语。（游戏）|He …; he is practising speaking. (game)|不是在玩游戏|is not playing games
____，而是____。（礼貌）|… rather than…. (polite)|他不是不喜欢你，而是希望你更有礼貌|He does not dislike you; he hopes you will be more polite''',[11,12])
grammar(c,4,'就是说 restates or clarifies the preceding information: “that is” or “in other words”.','''人要一直坚持学习，就是说，学习是人一生的事情，要活到老学到老。|People should keep learning; in other words, learning is lifelong.
别着急写，就是说，别着急动笔，想好后再写。|Do not rush to write; think first and then begin.
这份工作的工资是根据你工作的完成情况来发的，就是说，你完成得越多，工资越高。|Pay depends on completed work; the more you finish, the more you earn.''','''他想了想才回答，就是说，____。|He thought before answering; in other words,….|他没有马上回答|he did not answer immediately
____，我们要注意学习方法。|…, we should pay attention to study methods.|就是说|In other words
____，休息好，你的病才能快点儿好起来。|…, only with good rest can you recover quickly.|就是说，你要多休息|In other words, you need more rest''',[13])
section(c,'objectives','Chapter objectives',lines('''能够听懂并交流终身教育、线上教学、网络学习等话题。|Understand and discuss lifelong education, online teaching and online learning.
能够口头或书面表达终身教育、网络学习的意义。|Explain the significance of lifelong and online learning orally or in writing.
了解中国人的教育观。|Understand Chinese perspectives on education.'''),[5])
ex=questions('''即使每天工作很忙，我也会____出时间读书。|Even when busy, I … time to read.|留|leave
我刚坐下，她就过来和我____。|As soon as I sat down, she came to … me.|打招呼|greet
他____只做了一件事，那就是研究数学，最后他成为了一位很有名的数学家。|He spent his … studying mathematics and became a famous mathematician.|一生|whole life
小雪很喜欢____钢琴，每天都会练习至少两个小时。|Xiaoxue likes … the piano and practises for at least two hours daily.|弹|playing
他非常____，把任务交给他，我很放心。|He is very …; I trust him with the task.|优秀|excellent
老王工作三十年了，有很____的工作经验，这个问题他能解决。|Old Wang has … experience from thirty years of work and can solve this.|丰富|rich
A：你们还要____加班吗？B：对，今天必须要把这些货全部发出去。|A: Must you … overtime? B: Yes, all goods must be sent today.|继续|continue
A：你觉得怎样才能学好外语？B：开始学习时要特别重视____，多听多说。|A: How can one learn a language well? B: Focus on … initially; listen and speak more.|口语|speaking
A：你女儿真有____！B：谢谢，从小我们就教她要尊重别人。|A: Your daughter is so …! B: Thank you; we teach her respect.|礼貌|polite
A：你们做____的，平时工作一定很忙吧？B：也不一定。|A: You … must be very busy? B: Not always.|律师|lawyers
A：姐姐，我太____你的工作了！从来不加班，而且工资高。B：可是我们经常出差，很累的。|A: I … your well-paid job without overtime! B: But frequent business trips are tiring.|羡慕|envy
A：真是____社会啊，我要的信息马上就查到了。B：现在很多事情都可以在网上解决了。|A: What a … society! I found the information immediately. B: Much can be handled online.|数字|digital''')
for i,b in enumerate(ex):b['heading']=f'Fill in the blank · {i+1}'
section(c,'exercises','Comprehensive exercises',[dict(heading='Word bank · Questions 1–6',**line('一生　打招呼　丰富　留　弹　优秀','whole life; greet; rich; leave; play; excellent'))]+ex[:6]+[dict(heading='Word bank · Questions 7–12',**line('羡慕　礼貌　律师　数字　继续　口语','envy; courtesy; lawyer; digital; continue; speaking'))]+ex[6:],[14])
opts=lines('''还可以直接给大家放视频|can also play videos for everyone
第一个进教室的人|the first person into the classroom
老师和学生都觉得方便|teachers and students find it convenient
上课时|during class''')
bs=[dict(heading='Choose A–D',**line('现在有了数字教室，上课方式和以前大不相同了。____，只要按下门口的“上课”，灯和空调就会自己打开，不用一个一个去开。____，用到的“黑板”是一块能上网的电子屏幕，老师不仅可以在上面写字，____。数字教室里的桌椅也分成几个小组，小组里的人聚在一起，都能互相看到对方，这样方便大家交流。这些变化让上课方式丰富了不少，____，所以数字教室很受欢迎。','Digital classrooms differ greatly. ____, pressing “class” switches on lights and air conditioning. ____, the board is an internet-enabled screen; teachers can write and ____. Grouped desks help discussion. These changes enrich classes, ____, so they are popular.'))]
bs += [dict(heading=chr(65+i),**o) for i,o in enumerate(opts)]
for i,a in enumerate('BDAC'):bs.append(dict(heading=f'Gap {i+1}',zh=f'第{i+1}空：____',en=f'Gap {i+1}',input=True,solution=a,answers=[dict(opts[ord(a)-65],en=a+' · '+opts[ord(a)-65]['en'])]))
section(c,'cloze','Complete the passage',bs,[14,15])
section(c,'picture-writing','Look & write',[dict(image='4b/c11-exercise.jpg',alt='Three original picture-writing prompts for chapter 11')]+questions('''老年人|Use 老年人 to describe picture 1.|这两位老年人很开心。|These two older people look happy.
准时|Use 准时 to describe picture 2.|飞机准时起飞了。|The plane took off on time.
散步|Use 散步 to describe picture 3.|他们在公园里散步。|They are taking a walk in the park.'''),[15])
bs=questions('''三人一组，请以“网络给我们带来的影响”为题，从好的影响和坏的影响两方面进行讨论。讨论后，填写表格。|In groups of three, discuss positive and negative effects of the internet, then complete the table.|网络让我们查资料和学习更方便。|The internet makes research and learning easier.|我们可以和远方的朋友聊天儿。|We can chat with friends far away.|上网太久会影响休息，所以要注意时间。|Too much time online affects rest, so manage your time.
你喜欢老师怎样上课？请根据你的经历，写一篇短文，说说你喜欢的课堂教学方式，并说明理由，不少于140字。|Describe your preferred teaching style and explain why, based on experience, in at least 140 Chinese characters.|我喜欢老师先介绍今天要学的内容，然后让我们一起练习。遇到不懂的地方，老师可以举一些生活中的例子，这样我更容易听明白。我也喜欢和同学一起讨论，因为大家的想法不一样，我能从他们那里学到很多东西。数字教室很方便，课后我可以再看视频记录，但是我仍然希望有机会在线下和老师交流。对我来说，好的课堂不是老师一直说、学生一直听，而是大家都有机会提问题、练口语。即使开始时说得不好，我也会认真参加。我觉得这样的学习更有意思，也能帮助我养成主动学习的好习惯。|I like teachers to introduce the material and then let us practise. Everyday examples clarify difficult points. Class discussions expose me to different ideas. Digital recordings are convenient, but I still value in-person contact. A good class gives everyone opportunities to ask questions and speak rather than only listening. I participate even when my speaking is imperfect. This approach is engaging and develops active learning habits.''')
bs[0]['heading']='Group discussion';bs[1].update(heading='Writing · at least 140 characters',minChars=140)
bs.insert(1,dict(heading='Discussion table · Positive effects',zh='好的影响',en='Record the positive effects of the internet.',input=True));bs.insert(2,dict(heading='Discussion table · Negative effects',zh='坏的影响',en='Record the negative effects of the internet.',input=True))
section(c,'tasks','Task-based activities',bs,[15])
section(c,'summary','Book self-assessment',[dict(**line(z,e),input=True,heading='No problem / It’s OK / Need to improve') for z,e in [('能使用本课词语谈论终身教育、线上教学等话题。','I can discuss lifelong and online education using this chapter’s words.'),('能理解并运用本课的四个语言点。','I can understand and use the four grammar points.'),('能介绍线上教学等信息。','I can explain online teaching.'),('能表达对终身教育的看法。','I can express views on lifelong learning.')]], [16])
save(c)

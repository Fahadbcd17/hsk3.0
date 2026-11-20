import sys
sys.path.insert(0,'tools')
from book4b_author import *
from PIL import Image
c=chapter(13)
words(c,'''熊|bear|我怎么也没想到这只熊这么大。|I never imagined this bear would be so big.
老虎|tiger|我们等了很久，老虎怎么也不出来。|We waited a long time, but the tiger would not come out.
喊|shout; call|我怎么喊，他都不回答。|However much I call, he does not answer.
级|grade; rank|作为学生，我想知道自己是几级。|As a student, I want to know what level I am.
树林|woods|我怎么也没想到这片树林这么大。|I never imagined these woods would be so large.
景区|scenic area|这个景区一年比一年热闹。|This scenic area gets livelier every year.
区|area; district|这个区的房子一年比一年多。|There are more houses in this district each year.
美|beautiful|这个地方一天比一天美。|This place grows more beautiful every day.
节假日|festivals and holidays|节假日，来这里的人一年比一年多。|More people come here during holidays each year.
千万|be sure to; absolutely|大约八点出门，千万别迟到。|Leave at about eight; be sure not to be late.
开玩笑|joke|作为朋友，我只是跟你开玩笑。|As your friend, I am only joking with you.
月饼|mooncake|这些月饼一个比一个好吃。|Each of these mooncakes is tastier than the last.
葡萄|grape|这些葡萄一颗比一颗大。|Each of these grapes is larger than the last.
香|fragrant|我怎么也没想到这茶这么香。|I never imagined this tea would smell so fragrant.
街道|street|这条街道一年比一年热闹。|This street gets livelier every year.
剧院|theatre|我们大约七点到剧院。|We will reach the theatre at about seven.
演出|perform; performance|演出大约八点开始。|The performance starts at about eight.
赶|happen to coincide with|两个活动都大约八点开始，赶在一起了。|Both activities start at about eight and happen to coincide.
巧|coincidental; opportune|我怎么也没想到会这么巧。|I never imagined there could be such a coincidence.
之中|among; in|作为老师，他是这些人之中最年轻的。|As a teacher, he is the youngest among these people.
铁路|railway|铁路上的车一年比一年多。|There are more trains on the railway each year.
人员|personnel; staff|作为工作人员，我应该帮助大家。|As a staff member, I should help everyone.
反向|reverse; in the opposite direction|作为司机，他知道不能反向开车。|As a driver, he knows he must not drive in the opposite direction.
团圆|reunite|我们大约七点到家，和父母团圆。|We will arrive home at about seven to reunite with our parents.
左右|approximately; or so|我们晚上六点左右吃饭。|We eat at around six in the evening.
大约|approximately|他大约九点回来。|He will return at about nine.
烤|roast; bake|这家店的烤鱼一天比一天好吃。|This restaurant’s roast fish gets tastier every day.
西红柿|tomato|这些西红柿一个比一个大。|Each of these tomatoes is larger than the last.
出现|appear|他大约八点出现在门口。|He appeared at the door at about eight.
作为|as; in the capacity of|作为朋友，我会帮助你。|As your friend, I will help you.
传统|traditional; tradition|作为传统节日，春节很重要。|As a traditional festival, Spring Festival is important.
有着|have; possess|作为老师，她有着丰富的经验。|As a teacher, she has rich experience.
意义|meaning; significance|作为礼物，这本书对我很有意义。|As a gift, this book means a lot to me.
到来|arrive; come|春天到来后，天气一天比一天暖。|After spring arrives, the weather grows warmer each day.
美食|delicious food|这里的美食一年比一年多。|This place has more delicious food every year.
年夜饭|Chinese New Year’s Eve dinner|我们大约六点吃年夜饭。|We have New Year’s Eve dinner at about six.
回忆|recall; remember|我怎么也回忆不起来那天发生了什么。|However hard I try, I cannot recall what happened that day.
童年|childhood|作为父母，我们希望孩子有幸福的童年。|As parents, we hope our children have a happy childhood.
记忆|memory|我怎么也忘不了这段美好的记忆。|I cannot forget this wonderful memory.
已|already|他大约六点来的，现在已回家了。|He came at about six and has already gone home.
中年|middle age|作为一个中年人，我更关心身体了。|As a middle-aged person, I care more about my health.
仍然|still|大约十点了，他仍然在学习。|It is about ten, and he is still studying.
兄弟|brothers|作为兄弟，我们应该互相帮助。|As brothers, we should help one another.''','怎么都／也＋不／没……；一＋量词＋比＋一＋量词；大约／左右；作为')
c['warmup']=lines('''兄弟|brothers
老虎|tiger
树林|woods
葡萄|grapes
月饼|mooncakes
喊|shout''')
im=Image.open(R/'assets/4b/page-029.jpg')
models=lines('''他正在大声喊。|He is shouting loudly.
两个兄弟在一起很高兴。|The two brothers are happy together.
这里有一片树林。|There are woods here.
树上的葡萄很多。|There are many grapes on the vine.
桌上有几个好吃的月饼。|There are several tasty mooncakes on the table.
这只老虎很大。|This tiger is big.''')
for i,(answer,(x,y),s) in enumerate(zip([5,0,2,3,4,1],[(264,877),(510,877),(753,877),(264,1044),(510,1044),(753,1044)],models)):
 path=f'4b/c13-warm-{i}.jpg';im.crop((x,y,x+161,y+146)).save(R/'assets'/path,quality=94);c['pictures'].append(dict(image=path,answer=answer,sentence=s))
c['questions']=questions('''你的国家有哪些重要节日？这些节日到来时人们会吃什么美食？|What important festivals does your country have? What delicious food do people eat then?|春节很重要，我们会吃饺子。|Spring Festival is important; we eat dumplings.|中秋节时，大家会吃月饼。|At Mid-Autumn Festival, people eat mooncakes.|我们过节时会做很多家人爱吃的菜。|During festivals, we cook many dishes our family likes.
你和兄弟姐妹或者好朋友节假日在一起时都会做些什么？|What do you do with siblings or close friends during holidays?|我们一起吃饭、聊天儿。|We eat and chat together.|我们会去公园走走。|We take a walk in the park.|我们喜欢一起看电影。|We like watching films together.''')
listening(c,'''王一雪提醒小明：|What does Wang Yixue remind Xiaoming to do?|别害怕|Do not be afraid|不要吃东西|Do not eat|看看熊和老虎|Look at the bears and tigers|不要总是大喊|Do not keep shouting|D
刘明觉得景区怎么样？|What does Liu Ming think of the scenic area?|游客很多|Many visitors|门票便宜|Cheap tickets|又大又美|Large and beautiful|饭馆很多|Many restaurants|C
王一飞和杨同乐准备了什么？|What have Wang Yifei and Yang Tongle prepared?|月饼、葡萄和苹果|Mooncakes, grapes and apples|葡萄、西瓜和苹果|Grapes, watermelon and apples|月饼、苹果、西瓜和茶|Mooncakes, apples, watermelon and tea|月饼、葡萄、西瓜和茶|Mooncakes, grapes, watermelon and tea|D
李文为什么没来？|Why has Li Wen not come?|在学校学习|Studying at school|去买水果了|Went to buy fruit|要给爷爷过生日|Celebrating his grandfather’s birthday|和同事一起过节|Celebrating with colleagues|C
周力不能回家过中秋节，是因为：|Why can Zhou Li not go home for Mid-Autumn Festival?|不想回家|He does not want to|工作需要|His work requires him to stay|没买到车票|He could not get a ticket|想去外地过节|He wants to celebrate elsewhere|B
中秋节这天，周力的父母为儿子做了什么？|What did Zhou’s parents do for him on Mid-Autumn Festival?|买月饼|Bought mooncakes|打扫卫生|Cleaned|买了一件上衣|Bought a top|做了一桌饭菜|Cooked a tableful of dishes|D
下列哪个节日没有提到？|Which festival is not mentioned?|春节|Spring Festival|元宵节|Lantern Festival|端午节|Dragon Boat Festival|六一儿童节|Children’s Day|D
根据课文，春节到来时，人们会做什么？|According to the text, what do people do when Spring Festival arrives?|准备美食|Prepare delicious food|外出看花|Go out to see flowers|出去旅游|Travel|照顾孩子|Look after children|A''')
text(c,1,'''六一儿童节，刘明、王一雪带刘小明到北京野生动物园看动物，他们先坐车进入猛兽区。|On Children’s Day, Liu Ming and Wang Yixue take Liu Xiaoming to Beijing Wildlife Park. They first ride into the predator area.
刘小明：爸爸、妈妈，快看，熊和老虎都在这儿呢！|Xiaoming: Dad, Mum, look! The bears and tigers are all here!
王一雪：小明，注意安全，不要一直大喊！|Wang: Xiaoming, be careful and stop shouting all the time!
刘明：你们看，那个叫东北虎，是国家一级保护动物。那边树林里还有很多动物呢。|Liu: Look, that is a Siberian tiger, a nationally protected first-class animal. There are many more animals in those woods.
刘小明：咱们都能看到吧？|Xiaoming: We can see all of them, right?
王一雪：对。景区的车每到一个动物区都会停一会儿，让人们能近距离看看这些动物。|Wang: Yes. The park vehicle stops at each animal area so people can see the animals up close.
刘明：真不错，这景区真大、真美！我知道北京野生动物园很大，可怎么也没想到这么大！|Liu: Wonderful! This park is huge and beautiful. I knew Beijing Wildlife Park was large, but I never imagined it was this large!
王一雪：这里有几千只动物呢，能不大吗？现在是节假日，人多。小明，一会儿千万别跑丢了，我可不是开玩笑呢。|Wang: There are thousands of animals here; how could it be small? It is a holiday and crowded. Xiaoming, be sure not to run off and get lost. I am not joking.''','''小明在北京野生动物园里先看到了什么动物？|Which animals did Xiaoming first see at Beijing Wildlife Park?|他先看到了熊和老虎。|He first saw bears and tigers.
北京野生动物园有多少只动物？|How many animals does Beijing Wildlife Park have?|那里有几千只动物。|There are several thousand animals.''',[30,31],dict(pages=[31],prompt=line('六一儿童节，刘明、王一雪带儿子刘小明到北京野生动物园游玩。在动物园里，小明兴奋地喊着：“爸爸、妈妈，快看，……！”王一雪让他注意安全，……。刘明说，他们看到的老虎叫……，是国家……。刘明还说，那边树林里……。小明很想看到那些动物，王一雪告诉他，景区的车……都会停一会儿，让人们能近距离……。北京野生动物园很大，刘明说他怎么也没……。王一雪说，这里有……呢。同时，王一雪也提醒小明，节假日人多，千万……。','On Children’s Day the family visits the wildlife park. Xiaoming shouts, “Look, …!” His mother asks him to be careful and…. His father identifies the tiger as…and nationally…. More animals are…. The vehicle stops…so visitors can…. Liu never imagined…. There are…. During the crowded holiday, Xiaoming must not….'),answer=line('六一儿童节，刘明和王一雪带小明到动物园。小明看到熊和老虎，大声喊了起来。王一雪让他注意安全，不要一直大喊。刘明说那是东北虎，是国家一级保护动物，树林里还有很多动物。景区的车到每个动物区都会停，让大家近距离看动物。这里有几千只动物，又大又美，刘明怎么也没想到这么大。王一雪提醒小明千万别跑丢了。','The family visits the zoo on Children’s Day. Xiaoming shouts when he sees bears and tigers. His mother asks him to be careful and stop shouting. His father identifies the nationally protected Siberian tiger and points out other animals. The vehicle stops at each area for a close look. Thousands of animals live in the unexpectedly large, beautiful park. His mother reminds him not to get lost.')))
text(c,2,'''在王一飞家，王一飞夫妇邀请白家月、安妮和陈天中过中秋节。|At Wang Yifei’s home, she and her husband host Bai Jiayue, Annie and Chen Tianzhong for Mid-Autumn Festival.
王一飞：来，大家快吃月饼，这儿还有葡萄、西瓜。|Wang: Come and have mooncakes, everyone. There are also grapes and watermelon.
杨同乐：这是今年的新茶，你们也尝尝。|Yang: This is this year’s fresh tea. Try some too.
陈天中：好的。这茶闻着真香！|Chen: All right. This tea smells wonderful!
白家月：我还是第一次在中国过中秋节呢。|Bai: This is my first Mid-Autumn Festival in China.
安妮：我在加拿大时和中国朋友一起过过中秋节。我记得那天，外面的街道、剧院有很多演出活动。|Annie: I celebrated it with Chinese friends in Canada. I remember many performances on the streets and in theatres that day.
王一飞：在中国，每年中秋节都会举办很多活动，而且这几年一年比一年热闹。对了，家月，今天是李文爷爷的生日，李文来不了了，你就多吃一块月饼吧。|Wang: China holds many Mid-Autumn events, and they get livelier each year. Jiayue, it is Li Wen’s grandfather’s birthday today, so Li cannot come. Have an extra mooncake!
白家月：谢谢，那我就不客气了。|Bai: Thanks, I will!
杨同乐：中秋节和生日赶在了一块儿，真巧、真好！中秋节多陪陪家人也是应该的。|Yang: The festival and birthday coincide—what a lovely coincidence! It is right to spend more time with family at Mid-Autumn Festival.''','''白家月以前在中国过过中秋节吗？|Has Bai celebrated Mid-Autumn Festival in China before?|没有，这是她第一次在中国过中秋节。|No, this is her first time celebrating it in China.
在加拿大，安妮和中国朋友过中秋节时那里有什么活动？|What activities were held when Annie celebrated with Chinese friends in Canada?|街道、剧院有很多演出活动。|There were many performances in streets and theatres.''',[32,33,34])
text(c,3,'''中秋节的“反向团圆”|The Mid-Autumn “Reverse Reunion”
中秋节时中国人一般都会回家过节。但是有些人由于工作需要，不能回家，只能一个人留在工作的地方过节。周力就是这些人之中的一位。他是一名铁路工作人员，今年中秋假期，要负责铁路安全检查。|Chinese people generally go home for Mid-Autumn Festival. Some must remain where they work because of their duties. Zhou Li is one of them. He is a railway employee responsible for railway safety inspections during this year’s holiday.
周力的父母知道儿子这次不能回家后，就决定来一次“反向团圆”。早上五点左右他们就坐上了高铁，大约七点就来到了儿子工作的城市。在儿子家，他们做了一桌儿子爱吃的饭菜，有烤肉、烤鱼、饺子等等，还有西红柿鸡蛋汤。周力下班回家，看到一桌子饭菜和突然出现的父母，他感觉特别幸福。|When his parents learned he could not come home, they decided on a “reverse reunion.” They boarded a high-speed train at around five in the morning and arrived in his city at about seven. At his home they cooked his favourite roast meat, roast fish, dumplings and tomato-and-egg soup. Returning from work to see the food and his unexpectedly present parents, Zhou felt especially happy.
这个中秋节，地点变了，但爱没变。|This Mid-Autumn Festival, the place changed, but the love did not.''','''“反向团圆”是什么意思？|What does “reverse reunion” mean?|孩子不能回家，父母就去孩子工作的地方团圆。|When children cannot come home, parents visit where they work to reunite.
周力为什么感觉特别幸福？|Why did Zhou feel especially happy?|因为父母来到他家，还做了一桌他爱吃的饭菜。|His parents came to his home and prepared his favourite dishes.''',[35,36],dict(pages=[36],prompt=line('''中秋节时中国人一般都……。但是有些人由于……，不能回家，只能一个人……过节。周力就是……。他是……，今年中秋假期，要负责……。
周力的父母知道周力……后，就决定来一次……。早上五点左右他们就……，大约七点就来到了……。在儿子家，他们做了一桌……，有……等等，还有……。周力下班回家，看到……，他感觉特别幸福。
这个中秋节，地点……，但……。''','At Mid-Autumn Festival Chinese people usually…. Some cannot return because of…and remain…. Zhou is…. He works as…and is responsible for…. His parents learn…and decide…. At around five they…and around seven arrive…. They cook…, including…and…. Seeing…, he feels happy. The place…, but….'),answer=line('中秋节时，中国人一般会回家过节。周力是铁路工作人员，因为要检查铁路安全，不能回家。父母决定去他工作的地方“反向团圆”。他们五点左右坐高铁，大约七点到达，给儿子做了烤肉、烤鱼、饺子和西红柿鸡蛋汤。周力下班回家，看到父母和一桌饭菜，非常幸福。这个中秋节，地点变了，但爱没变。','People usually return home for Mid-Autumn Festival, but railway employee Zhou must inspect railway safety. His parents travel to him for a reverse reunion, taking the train around five and arriving about seven. They cook roast meat, fish, dumplings and tomato-and-egg soup. He feels very happy to find them and the food at home. The place changed, but the love did not.')))
text(c,4,'''节日的美好记忆|Wonderful Memories of Festivals
中国有很多节日，比如春节、元宵节、端午节、中秋节等。|China has many festivals, including Spring Festival, Lantern Festival, Dragon Boat Festival and Mid-Autumn Festival.
作为一年里最重要的传统节日，春节对中国人来说有着特别的意义。春节到来时，人们不管在哪里，都想回家过年。春节前也最忙，既要收拾房子、打扫卫生，又要准备各种美食。除夕这天晚上，一家人一边吃年夜饭，一边看春晚。零点一到，大家互相祝新年快乐，到处都是幸福的笑声。|As the year’s most important traditional festival, Spring Festival has special meaning for Chinese people. Wherever they are, people want to go home. Beforehand they are busy tidying and cleaning their homes and preparing delicious food. On New Year’s Eve, the family eats dinner while watching the Spring Festival Gala. At midnight everyone exchanges New Year greetings amid happy laughter.
每当回忆起童年，我最美好的记忆很多也发生在过年时。虽然现在已人到中年，离开了家，但是春节仍然是我最喜欢的节日，过年时也更想父母、兄弟姐妹。|When I recall childhood, many of my happiest memories are of New Year. Although I am now middle-aged and have left home, Spring Festival remains my favourite festival, when I miss my parents and siblings even more.''','''为什么说春节对中国人来说有着特别的意义？|Why does Spring Festival have special meaning for Chinese people?|因为它是一年里最重要的传统节日，大家都想回家和家人一起过年。|It is the most important traditional festival, when everyone wants to celebrate with family at home.
春节为什么一直是他最喜欢的节日？|Why has Spring Festival always been his favourite festival?|因为他很多美好的童年记忆都发生在过年时。|Many of his happiest childhood memories are of New Year.''',[37,38])
grammar(c,1,'怎么都／也＋不／没…… expresses an unsuccessful result despite all efforts. It can also express surprise at something unexpected.','''我知道北京野生动物园很大，可怎么也没想到这么大！|I knew Beijing Wildlife Park was large, but never imagined it was this large!
她在包里找了半天，怎么都没找到，真奇怪。|She searched her bag for ages but could not find it—how strange.
我们想看那只熊猫，在动物园等了两个多小时，可是它怎么都不出来。|We waited over two hours at the zoo to see the panda, but it simply would not come out.''','''A：我一直想买这种茶，去店里买了几次，____。B：最近天热，买这种茶的人太多了。|I have wanted this tea and visited the shop several times,…. The hot weather has made it popular.|可怎么也没买到|but I still could not buy any
A：我想了半天，____。B：你们好长时间没见了，突然想不起来他叫什么也能理解。|I thought for ages,…. You have not met for a long time; forgetting his name is understandable.|怎么也想不起来他叫什么|but I cannot remember his name
A：这道题太难了，我做了好久，____。B：是吗？我来试试，看能不能做出来。|This problem is hard; I worked for ages,…. Let me try solving it.|怎么也做不出来|but cannot solve it''',[32])
grammar(c,2,'一＋measure word＋比＋一＋measure word＋adjective compares successive things or periods, each showing a greater degree.','''在中国，每年中秋节都会举办很多活动，而且这几年一年比一年热闹。|China holds many Mid-Autumn activities, livelier every year recently.
夏天快到了，天气也一天比一天热。|Summer is approaching and each day is hotter.
这家店里的杯子一个比一个漂亮，我都不知道选哪个了。|Each cup in this shop is prettier than the next; I cannot choose.''','''A：这儿的衣服怎么样？B：很不错，可以说，____漂亮。|How are the clothes here? Very good; you could say each is prettier than the next.|一件比一件|each item compared with the next
A：你那里的天气怎么样？B：现在进入冬天了，____。|How is the weather where you are? Winter has arrived,….|天气一天比一天冷|it is colder every day
A：他们中文学得怎么样？B：不错，感觉____。|How is their Chinese learning? Good; it feels….|一天比一天好|better every day''',[34])
grammar(c,3,'大约 precedes a time expression and 左右 follows it. Both indicate an approximate time.','''早上五点左右他们就坐上了高铁，大约七点就来到了儿子工作的城市。|They boarded the train around five and reached their son’s city about seven.
我中午十二点左右到你们学校，和大家一起去食堂吃饭。|I will reach your school around noon and eat with everyone at the canteen.
昨天飞机晚点，我晚上大约十点半才到家。|The plane was late yesterday, so I only got home at about 10:30 p.m.''','''咱们____门口见吧，然后一起进去看演出。（剧院）|Let’s meet … at the entrance and then watch the performance. (theatre)|大约七点在剧院|at the theatre at about seven
这只老虎____。（出现）|This tiger…. (appear)|每天早上八点左右出现|appears around eight every morning
我们明天晚上____。（千万）|Tomorrow evening we…. (be sure)|大约六点见，千万别迟到|will meet at about six; be sure not to be late''',[36])
grammar(c,4,'作为 introduces a person’s identity or the nature of something. It must combine with the noun phrase that follows it.','''作为一年里最重要的传统节日，春节对中国人来说有着特别的意义。|As the year’s most important traditional festival, Spring Festival has special meaning for Chinese people.
作为新产品，这个手机不仅样子好看，价格也不高。|As a new product, this phone looks good and is affordable.
作为好朋友，我们一直互相关心、互相帮助。|As close friends, we have always cared for and helped each other.''','''作为父母，____。|As parents,….|我们应该关心孩子|we should care for our children
____，我必须请你尝尝北京烤鸭。|…, I must treat you to Beijing roast duck.|作为北京人|As a Beijinger
____，我支持你的决定。|…, I support your decision.|作为你的朋友|As your friend''',[38])
section(c,'objectives','Chapter objectives',lines('''能够听懂并交流节日生活方面的话题。|Understand and discuss festival life.
能够口头或书面表达节日特点、节日活动等内容。|Describe festival characteristics and activities orally and in writing.
了解中国人特别重视传统节日背后的文化内涵。|Understand the cultural significance of traditional Chinese festivals and why they are valued.'''),[29])
ex=questions('''西安也是一座____三千多年历史的城市，欢迎您参观游玩。|Xi’an is also a city … over three thousand years of history. Welcome to visit.|有着|having
他____在中国生活二十年了，生活习惯和我们没什么不同。|He has … lived in China for twenty years and has similar habits to ours.|已|already
有妈妈细心照顾，孩子们每天都生活在幸福____。|With Mum’s careful care, the children live … happiness every day.|之中|in
妈妈终于____在车站出口，孩子们开心极了。|Mum finally … at the station exit, delighting the children.|出现|appeared
虽然遇到了很大困难，他____坚持下来了。|Despite great difficulties, he … persevered.|仍然|still
这是什么咖啡？闻起来真____！|What coffee is this? It smells so…!|香|fragrant
A：你去的那家动物园有____吗？B：有，还有熊、大熊猫等好多种动物呢。|Does that zoo have…? Yes, and bears, pandas and many other animals.|老虎|tigers
A：虽然离开家已四十年，但我还会经常____起小时候在家时的生活。B：我也是，年龄越大越想家。|Though I left home forty years ago, I often … childhood there. Me too; I miss home more as I age.|回忆|recall
A：明天的活动你们一定要来，____别忘了。B：好的，放心吧，我们会来的。|You must come tomorrow; … do not forget. Don’t worry, we will.|千万|be sure
A：我刚才____了你几遍，你都没看我。B：对不起，我戴着耳机呢，没听见。|I … you several times but you did not look. Sorry, I had headphones on.|喊|called
A：没想到咱们在机场遇见了，真是太____了。我去北京，你呢？B：是啊，我也去北京出差。|What a … to meet at the airport! I’m going to Beijing. Me too, on business.|巧|coincidence
A：小雨，你的生日快到了。生日____时，你想要什么礼物？B：我想要一个大蛋糕。|Xiaoyu, when your birthday …, what gift would you like? A big cake.|到来|arrives''')
for i,b in enumerate(ex):b['heading']=f'Fill in the blank · {i+1}'
section(c,'exercises','Comprehensive exercises',[dict(heading='Word bank · Questions 1–6',**line('仍然　已　香　之中　有着　出现','still; already; fragrant; in; have; appear'))]+ex[:6]+[dict(heading='Word bank · Questions 7–12',**line('到来　老虎　喊　回忆　千万　巧','arrive; tiger; call; recall; be sure; coincidental'))]+ex[6:],[38,39])
opts=lines('''兄弟姐妹都离开了家|the siblings all left home
很难见面|it is hard to meet
小时候喜欢过节|as a child he liked festivals
一家人聚在一起|the whole family gathers''')
bs=[line('冬冬从小到大都喜欢过节，特别是春节和元宵节。____，是因为可以吃到很多好吃的。长大后，____，去外地上大学、工作。平时大家很忙，____，但一到重要节日，在外地的兄弟姐妹就都回来了，和父母一起过节。____，特别热闹，也特别开心。','Dongdong has always loved festivals, especially Spring Festival and Lantern Festival. ____, because of all the delicious food. Growing up, ____ to attend university and work elsewhere. Everyone is busy, so ____. At important festivals the siblings return to celebrate with their parents. ____, making it lively and joyful.')]+[dict(heading=chr(65+i),**o)for i,o in enumerate(opts)]
for i,a in enumerate('CABD'):bs.append(dict(heading=f'Gap {i+1}',zh=f'第{i+1}空：____',en=f'Gap {i+1}',input=True,solution=a,answers=[dict(opts[ord(a)-65],en=a+' · '+opts[ord(a)-65]['en'])]))
section(c,'cloze','Complete the passage',bs,[39])
Image.open(R/'assets/4b/page-040.jpg').crop((181,192,1015,438)).save(R/'assets/4b/c13-exercise.jpg',quality=94)
section(c,'picture-writing','Look & write',[dict(image='4b/c13-exercise.jpg',alt='Chapter 13 picture-writing prompts: theatre, scenic area and holidays')]+questions('''剧院|Use 剧院 to describe picture 1.|人们在剧院里看演出。|People watch a performance in the theatre.
景区|Use 景区 to describe picture 2.|这个景区又大又美。|This scenic area is large and beautiful.
节假日|Use 节假日 to describe picture 3.|节假日，一家人一起出去玩。|During the holidays, a family goes out together.'''),[40])
bs=questions('''三至四人一组，每人介绍一个你最喜欢的节日，说说为什么喜欢，过节时你都会做什么，等等。讨论后，每人再向大家介绍小组中另一位同学最喜欢的节日。|In groups of three or four, share your favourite festival, why you like it and what you do. Then introduce another group member’s favourite festival.|我最喜欢春节，因为可以和家人一起吃饭、聊天儿。|I like Spring Festival most because I can eat and chat with my family.|我的朋友最喜欢中秋节。他会和父母一起吃月饼。|My friend likes Mid-Autumn Festival most and eats mooncakes with his parents.|她喜欢春节，因为能回老家，看望父母和兄弟姐妹。|She likes Spring Festival because she can visit her hometown, parents and siblings.
在你的国家，你最喜欢过什么节？请写一篇短文，说说过节时发生的故事，不少于140字。|Which festival in your country do you most enjoy? Write at least 140 Chinese characters telling a story from that festival.|我最喜欢春节，因为过年时一家人能在一起。去年春节，我和父母一起回老家。我们大约下午三点到，爷爷、奶奶已在门口等我们了。我帮奶奶准备年夜饭，父亲打扫房间，母亲和爷爷聊天儿。六点左右，大家坐下来吃饭。我怎么也没想到，奶奶做了这么多我爱吃的菜！饭后，我们一起看电视，说起我童年时的事情，大家都笑了。虽然平时工作很忙，很难见面，但是春节让我们有机会团圆。作为家里的一员，我希望以后每年都能回家，多陪陪父母和爷爷、奶奶。这是我最美好的记忆之一。|Spring Festival is my favourite because the family can reunite. Last year we reached our hometown around three, where my grandparents were waiting. I helped prepare dinner, Dad cleaned, and Mum chatted with Grandpa. At around six we ate; I was amazed by all my favourite dishes. Later we watched television and laughed about my childhood. Although work makes it hard to meet, the festival brings us together. I hope to return every year and spend more time with my family. This is one of my happiest memories.''')
bs[0]['heading']='Group discussion';bs[1].update(heading='Writing · at least 140 characters',minChars=140)
section(c,'tasks','Task-based activities',bs,[40])
section(c,'summary','Book self-assessment',[dict(**line(z,e),input=True,heading='No problem / It’s OK / Need to improve')for z,e in [('能使用本课“景区、节假日、剧院、中秋节、美食、回忆”等词语，谈论关于美好日子的话题。','I can use the chapter vocabulary to discuss wonderful days.'),('能理解并运用“怎么都／也＋不／没……”“一＋量词＋比＋一＋量词”“大约”“左右”“作为”等语言点。','I can understand and use all four grammar points.'),('能介绍一些节日以及节日里发生的有趣的故事。','I can introduce festivals and tell interesting stories about them.')]], [41])
section(c,'proper-nouns','Proper nouns',lines('''东北虎|Siberian tiger
北京野生动物园|Beijing Wildlife Park
中秋节|Mid-Autumn Festival
加拿大|Canada
元宵节|Lantern Festival
端午节|Dragon Boat Festival
除夕|Chinese New Year’s Eve
春晚|Spring Festival Gala'''),[31,33,38])
assert len(c['words'])==43
save(c)

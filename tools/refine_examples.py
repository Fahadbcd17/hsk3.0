from pathlib import Path
p=Path('source/vocabulary.tsv')
fix={
(1,'减轻'):('要是你来帮我，就能减轻我的工作。','If you help me, you can lighten my work.'),
(1,'研究生'):('要是考上研究生，我就去北京学习。','If I get into postgraduate school, I will go to Beijing to study.'),
(1,'成为'):('要是你想成为医生，就要认真学习。','If you want to become a doctor, you need to study seriously.'),
(1,'贸易'):('要是你想做贸易，就先学中文吧。','If you want to work in trade, study Chinese first.'),
(1,'另'):('我一方面想工作，另一方面也想学习。','On one hand I want to work, and on the other I want to study.'),
(2,'毕业'):('我毕业了，不过还想在学校学习。','I have graduated, but still want to study at school.'),
(2,'入住'):('今天可以入住，不过要先给钱。','You can move in today, but you need to pay first.'),
(2,'整个'):('整个房子都很好，不过有点儿贵。','The whole home is good, but a little expensive.'),
(2,'查看'):('我查看了材料，并告诉了老师。','I checked the materials and told the teacher.'),
(2,'同时'):('他学习中文，不过同时也要工作。','He studies Chinese, but also needs to work at the same time.'),
(2,'位置'):('这个位置很好，不过有点儿贵。','This location is good, but a little expensive.'),
(2,'工资'):('工资不高，不过我很喜欢这个工作。','The salary is not high, but I like this job.'),
(2,'感'):('这里很小，不过让我有安全感。','This place is small, but it gives me a sense of security.'),
(3,'下载'):('我想听音乐，于是下载了这首歌。','I wanted to listen to music, so I downloaded this song.'),
(3,'现金'):('我没有现金，于是向朋友借钱。','I had no cash, so I borrowed money from a friend.'),
(3,'改变'):('天气变了，于是我改变了出发时间。','The weather changed, so I changed the departure time.'),
(3,'手指'):('手指疼，于是我不写了。','My finger hurt, so I stopped writing.'),
(3,'个人'):('我不仅写了姓名，还写了其他个人信息。','I wrote my name and also other personal information.'),
(3,'法律'):('我不仅学习中文，还学习中国法律。','I study Chinese and also Chinese law.'),
(3,'手段'):('他不仅有新的手段，还有很多好方法。','He has new means and also many good methods.'),
(3,'保证'):('我不仅保证早点儿来，还会认真准备。','I promise to come early and also prepare carefully.'),
(4,'费'):('这里的费用既不高，服务又好。','The fees here are not high, and the service is good.'),
(4,'出行'):('出行既可以坐车，也可以走路。','You can travel by vehicle or on foot.'),
(4,'电动车'):('电动车既快又方便。','An electric bike is fast and convenient.'),
(4,'充电'):('这里可以充电，再说离家也近。','You can charge here, and besides, it is close to home.'),
(4,'购买'):('来得及的话，我们去购买一些书。','If there is enough time, we will go and buy some books.'),
(5,'随意'):('他说话够随意的。','He speaks very casually.'),
(5,'重视'):('学校至少应该重视学生的问题。','Schools should at least take students’ problems seriously.'),
(6,'性别'):('先写性别，好让老师了解你。','Write your gender first so the teacher can learn about you.'),
(6,'身'):('我偶尔穿一身白色的衣服。','I occasionally wear an all-white outfit.'),
(6,'汗'):('我偶尔跑步跑出汗。','I occasionally run until I sweat.'),
(6,'治疗'):('他偶尔去医院治疗。','He occasionally goes to hospital for treatment.'),
(7,'生意'):('在生意方面，他知道得很多。','He knows a lot about business.'),
(7,'管理'):('在管理方面，他做得很好。','He does well in management.'),
(8,'郊区'):('跟这里相比，郊区更安静。','Compared with here, the suburbs are quieter.'),
(8,'戴'):('不管什么时候，他都戴眼镜。','He wears glasses all the time.'),
(8,'帽子'):('不管去哪儿，他都带着帽子。','Wherever he goes, he takes his hat.'),
(8,'加班'):('别总是加班，否则身体会不好。','Do not always work overtime, otherwise your health will suffer.'),
(8,'失去'):('不管失去什么，都要好好生活。','Whatever you lose, keep living well.'),
(8,'首都'):('跟这里相比，首都大多了。','Compared with here, the capital is much bigger.'),
(8,'实际上'):('不管去哪里，实际上我都很高兴。','Wherever I go, I am actually very happy.'),
(9,'深'):('尽管水不深，但是也要注意安全。','Although the water is not deep, you still need to be careful.'),
(10,'零下'):('天气再次变成零下了。','The temperature has dropped below zero again.'),
(10,'低于'):('今天的价格低于昨天，而东西是一样的。','Today’s price is lower than yesterday’s, while the items are the same.'),
(10,'方言'):('他说方言，而我说中文。','He speaks a dialect, while I speak Chinese.'),
(10,'普通话'):('我说普通话，而他说英语。','I speak standard Mandarin, while he speaks English.')}
a=[];c=0
for s in p.read_text().splitlines():
 if s.startswith('#'):c=int(s[1:]);a.append(s);continue
 w,en,zh,tr=s.split('|')
 if (c,w)in fix:zh,tr=fix[c,w]
 a.append('|'.join([w,en,zh,tr]))
p.write_text('\n'.join(a)+'\n')

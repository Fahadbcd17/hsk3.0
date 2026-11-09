import json,pathlib,re
R=pathlib.Path(__file__).resolve().parent.parent
out={str(i):[] for i in range(1,11)}
def grouped(file):
 d={};c=0
 for row in (R/'source'/file).read_text().splitlines():
  if row.startswith('#'):c=int(row[1:]);d[c]=[]
  elif row:d[c].append(row.split('|'))
 return d
texts=grouped('texts.tsv');gram=grouped('grammar.tsv');comp=grouped('comprehension.tsv');ex=grouped('exercises.tsv');gp=grouped('grammar-practice.tsv')
starts=[11,22,33,45,57,69,81,93,105,117,130]
qpages=[[12,15,16,18],[24,26,27,29],[35,37,39,41],[47,49,50,52],[59,61,63,65],[71,73,74,76],[83,85,86,88],[95,97,98,100],[107,109,111,113],[119,121,123,125]]
textpages=[[12,14,16,18],[23,25,27,29],[34,36,38,40],[46,48,50,52],[58,60,62,64],[70,72,74,76],[82,84,86,88],[94,96,98,100],[106,108,110,112],[118,120,122,125]]
gpages=[[13,15,17,19],[24,26,28,30],[35,37,39,41],[47,49,51,53],[59,61,63,65],[71,73,75,76],[83,85,87,89],[95,97,99,101],[107,109,111,113],[119,121,123,126]]
expages=[[19,20],[30,31],[41,42],[53,54],[65,66],[77,78],[89,90],[101,102],[113,114,115],[126,127]]
for c in range(1,11):
 if (R/'source/listening.json').exists():out[str(c)].append({'id':'listening','title':'Listen / read & choose','intro':'Original listening questions, grouped by Text 1–4. Use your book recordings, or read the corresponding text below. Audio is not included in the supplied PDF. Choose A, B, C or D; hide answers before starting.','blocks':json.loads((R/'source/listening.json').read_text())[str(c)]})
 for i,(num,zh,en) in enumerate(texts[c]):
  zs=zh.split('\\n');es=en.split('\\n');assert len(zs)==len(es),(c,i,len(zs),len(es))
  blocks=[{'zh':z,'en':e} for z,e in zip(zs,es)]
  page=qpages[c-1][i];raw=(R/'source'/f'page-{page:03}.txt').read_text().split('根据课文内容回答问题。')[-1]
  qs=[re.sub(r'^（[12]）','',x) for x in raw.splitlines()[1:5] if re.match(r'（[12]）',x)]
  assert len(qs)==2,(c,i,qs)
  for j,q in enumerate(qs):
   qe,az,ae=comp[c][i*2+j];q=re.sub(r'（zuoyong,effect）','',q)
   blocks.append({'heading':'Read & answer '+str(j+1),'zh':q,'en':qe,'answers':[{'zh':az,'en':ae}],'input':True})
  out[str(c)].append({'id':f'text{i+1}','title':f'Text {i+1}','intro':'Read the original textbook text. The English is a study translation; the responses are model answers.','blocks':blocks,'sourcePages':list(range(textpages[c-1][i],page+1)),'note':'Retell this text in your own words'})
  g,explanation,z1,e1,z2,e2=gram[c][i]
  practice=[{'heading':f'Book practice · {j+1}','zh':v[0],'en':v[1],'answers':[{'zh':v[2],'en':v[3]}],'input':True} for j,v in enumerate(gp[c][i*3:i*3+3])]
  out[str(c)].append({'id':f'grammar{i+1}','title':f'Grammar {i+1} · {g}','intro':explanation,'blocks':[{'zh':z1,'en':e1},{'zh':z2,'en':e2}]+practice,'sourcePages':[gpages[c-1][i]],'note':'My sentence using this grammar'})
 blocks=[]
 for i,(z,e,a) in enumerate(ex[c]):blocks.append({'heading':f'Fill in the blank · {i+1}','zh':z,'en':e,'answers':[{'zh':a,'en':'Answer: '+a}],'input':True,'solution':a})
 out[str(c)].append({'id':'exercises','title':'Comprehensive exercises','intro':'Complete the original book exercises. English translations describe the completed meaning, so hide English before testing yourself.','blocks':blocks,'sourcePages':expages[c-1]})
# Additional cloze passages, picture prompts and task activities are loaded below.
if (R/'source/additional.json').exists():
 for c,ss in json.loads((R/'source/additional.json').read_text()).items():out[c].extend(ss)
(R/'source/sections.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('Built',sum(len(x)for x in out.values()),'sections')

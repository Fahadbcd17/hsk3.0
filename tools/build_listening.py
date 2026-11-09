import json,re,pathlib
R=pathlib.Path(__file__).resolve().parent.parent
all=[]
for p in range(11,130):
 ls=(R/'source'/f'page-{p:03}.txt').read_text().splitlines()
 for i,l in enumerate(ls):
  if not re.match(r'^[（(][12][）)]',l) or not any(re.match('^A',v)for v in ls[i+1:i+4]):continue
  chunk=''
  for v in ls[i+1:]:
   if re.match(r'^[（(][123][）)]',v):break
   chunk+=v
   if 'D' in chunk and len(chunk.split('D')[-1])>0:break
  m=re.match(r'.*?A(.*?)B(.*?)C(.*?)D(.+)',chunk)
  if not m:continue
  q=re.sub(r'^[（(][12][）)]','',l);q=re.sub(r'[（(][）)]?$','',q)
  q=q.replace("（kouwei,one's taste）",'')
  all.append({'page':p,'zh':q,'options':list(m.groups())})
assert len(all)==80,len(all)
(R/'source/listening-candidates.json').write_text(json.dumps(all,ensure_ascii=False,indent=2))
for i,x in enumerate(all):print(i+1,x['page'],x['zh'],' / '.join(x['options']))
translations=(R/'source/listening.tsv').read_text().splitlines()
assert len(translations)==80
out={str(c):[] for c in range(1,11)}
for i,(q,row) in enumerate(zip(all,translations)):
 en,*opts,answer=row.split('|');assert len(opts)==4
 block={'heading':f'Choose the answer · Text {i%8//2+1}, question {i%2+1}','zh':q['zh'],'en':en,'choices':[{'zh':z,'en':e} for z,e in zip(q['options'],opts)],'input':True,'solution':answer,'answers':[{'zh':q['options'][ord(answer)-65],'en':answer+' · '+opts[ord(answer)-65]}]}
 out[str(i//8+1)].append(block)
(R/'source/listening.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))

"""Small authoring helpers for Book 4B; no runtime dependencies."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent.parent
META=json.loads((R/'source/4b/meta.json').read_text())
def line(zh,en):return {'zh':zh,'en':en}
def lines(text):return [line(*r.split('|',1)) for r in text.strip().splitlines() if r.strip()]
def chapter(n):
 c=dict(next(c for c in META if c['id']==n));c.update(book='4B',sourceRange=[c['page'],next((x['page']-1 for x in META if x['id']==n+1),127)],words=[],warmup=[],pictures=[],questions=[],sections=[]);return c
def words(c,text,grammar):
 for r in text.strip().splitlines():
  z,e,s,t=r.split('|');c['words'].append(dict(zh=z,en=e,example=line(s,t),grammar=grammar))
def section(c,id,title,blocks,pages=None,intro=None,**kw):
 s=dict(id=id,title=title,blocks=blocks,**kw)
 if pages:s['sourcePages']=pages
 if intro:s['intro']=intro
 c['sections'].append(s);return s
def questions(text):
 out=[]
 for r in text.strip().splitlines():
  vals=r.split('|');z,e=vals[:2];q=line(z,e);q.update(input=True,answers=[line(vals[i],vals[i+1]) for i in range(2,len(vals),2)]);out.append(q)
 return out
def listening(c,text):
 bs=[]
 for i,r in enumerate(text.strip().splitlines()):
  v=r.split('|');q=line(v[0],v[1]);opts=[line(v[j],v[j+1]) for j in range(2,10,2)];a=v[10];q.update(heading=f'Choose the answer · Text {i//2+1}, question {i%2+1}',choices=opts,input=True,solution=a,answers=[dict(opts[ord(a)-65],en=a+' · '+opts[ord(a)-65]['en'])]);bs.append(q)
 assert len(bs)==8
 section(c,'listening','Listen / read & choose',bs)
def text(c,n,content,qs,pages,retell=None):
 bs=lines(content)
 for i,q in enumerate(questions(qs)):q['heading']=f'Read & answer {i+1}';bs.append(q)
 s=section(c,f'text{n}',f'Text {n}',bs,pages,'Role-play the dialogue.' if n<3 else 'Read the text aloud.',note='Retell this text in your own words')
 if retell:s['retelling']=retell
 return s
def grammar(c,n,explanation,examples,practice,pages):
 bs=lines(examples)
 for i,b in enumerate(questions(practice)):b['heading']=f'Book practice · {i+1}';bs.append(b)
 return section(c,f'grammar{n}',f'Grammar {n} · {c["grammar"][n-1]}',bs,pages,explanation,note='My sentence using this grammar')
def save(c):
 # Keep text / grammar pairs adjacent even when authored in a different order.
 order={'objectives':-2,'listening':-1,**{f'{k}{n}':n*2+(k=='grammar') for n in range(1,5) for k in ['text','grammar']},'tips':10,'exercises':11,'cloze':12,'picture-writing':13,'tasks':14,'bonus':15,'summary':16}
 c['sections'].sort(key=lambda s:order.get(s['id'],17))
 (R/f'source/4b/chapters/{c["id"]}.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')

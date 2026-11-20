"""Validate the root files actually deployed to GitHub Pages."""
import json,re
from pathlib import Path
R=Path(__file__).resolve().parent.parent
D=json.loads((R/'data.js').read_text().split('=',1)[1].strip().rstrip(';'))
cs=D['chapters']
assert [c['id'] for c in cs]==list(range(1,21)), 'Expected chapters 1–20'
assert sum(len(c['words']) for c in cs[:10])==391
assert sum(len(c['pictures']) for c in cs[:10])==58
stats={'chapters':len(cs),'words':0,'warmup pictures':0,'texts':0,'retellings':0,'choice questions':0,'writing models':0}
for c in cs:
 n=c['id'];assert len(c['questions'])==2,n
 assert all(len(q['answers'])==3 for q in c['questions']),n
 assert len(c['grammar'])==4,n
 assert len({s['id'] for s in c['sections']})==len(c['sections']),n
 assert all(w['zh'] in w['example']['zh'] for w in c['words']),n
 assert len(c['pictures'])==(4 if n==5 else 6),n
 assert all(0<=p['answer']<len(c['warmup']) for p in c['pictures']),n
 stats['words']+=len(c['words']);stats['warmup pictures']+=len(c['pictures'])
 sections={s['id']:s for s in c['sections']}
 choices=sections['listening']['blocks'];assert len(choices)==8,n
 assert all(len(b['choices'])==4 and b.get('solution') in 'ABCD' and b.get('answers') for b in choices),n
 stats['choice questions']+=len(choices)
 for k in range(1,5):
  assert f'text{k}' in sections and f'grammar{k}' in sections,n
  stats['texts']+=1
  if k in (1,3):
   retell=sections[f'text{k}']['retelling']
   assert retell['prompt']['zh'] and retell['answer']['zh'] and retell['pages'],n
   assert 'image' not in retell,n
   stats['retellings']+=1
 for s in c['sections']:
  for b in s.get('blocks',[]):
   if b.get('minChars'):
    assert b['minChars']==(140 if n>10 else 120),(n,b['minChars'])
    assert len(re.findall('[\u3400-\u9fff]',b['answers'][0]['zh']))>=b['minChars'],n
    stats['writing models']+=1
 for p in range(c['sourceRange'][0],c['sourceRange'][1]+1):
  asset=f'4b/page-{p:03}.jpg' if n>10 else f'page-{p}.jpg'
  assert (R/'assets'/asset).is_file(),asset

def walk(x):
 if isinstance(x,dict):
  if x.get('zh'):assert x.get('py') and x.get('en'),str(x)[:100]
  if x.get('image'):assert (R/'assets'/x['image']).is_file(),x['image']
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(cs)
assert all(v.get('py') and v.get('en') for v in D['dictionary'].values())
for n in range(1,11):
 for track in (1,3,5,7):
  name=f'HSK 4A TEXTBOOK (HSK 3.0 2026 Edition) - Lesson {n:02}-{track:02}.mp3'
  assert (R/'assets/audio'/name).is_file(),name
for name in ['index.html','app.js','styles.css','data.js','.nojekyll','assets/logo/logo.jpg']:
 assert (R/name).is_file(),name
assert stats['writing models']==20
print('PASS: '+', '.join(f'{v} {k}' for k,v in stats.items())+'. All bilingual lines and local assets present.')

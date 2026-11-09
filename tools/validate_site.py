"""Check course structure, translations and deployable local assets."""
import json,re,pathlib
R=pathlib.Path(__file__).resolve().parent.parent
D=json.loads((R/'source/course.json').read_text());cs=D['chapters']
assert len(cs)==10
assert sum(len(c['words']) for c in cs)==391
assert sum(len(c['pictures']) for c in cs)==58
for c in cs:
 assert len(c['questions'])==2
 assert all(len(q['answers'])==3 for q in c['questions'])
 assert len(c['grammar'])==4
 assert len({s['id'] for s in c['sections']})==len(c['sections'])
 assert all(w['zh'] in w['example']['zh'] for w in c['words'])
 assert sum(len(s['blocks']) for s in c['sections'] if s['id']=='listening')==8
 for s in c['sections']:
  for b in s.get('blocks',[]):
   if b.get('minChars'):
    assert len(re.findall('[\u3400-\u9fff]',b['answers'][0]['zh']))>=b['minChars'],c['id']
 for p in range(c['sourceRange'][0],c['sourceRange'][1]+1):assert (R/'site/assets'/f'page-{p}.jpg').exists()
def walk(x):
 if isinstance(x,dict):
  if x.get('zh'):assert x.get('py') and x.get('en'),str(x)[:100]
  if x.get('image'):assert (R/'site/assets'/x['image']).is_file(),x['image']
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(cs)
assert all(v.get('py') and v.get('en') for v in D['dictionary'].values())
for name in ['index.html','app.js','styles.css','data.js']:assert (R/'site'/name).is_file()
print('PASS: 10 chapters, 391 target examples, 58 picture matches, 80 choice questions, 60 discussion answers, 10 full writing models, all referenced local assets and bilingual lines.')

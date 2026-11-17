"""Update root course data from reviewed retelling prompts and model answers."""
import json,sys
from pathlib import Path
sys.path.insert(0,'/tmp/hsk-retelling-deps')
from pypinyin import lazy_pinyin,Style,load_phrases_dict
R=Path(__file__).resolve().parent.parent
load_phrases_dict({w:[[s] for s in p.split()] for w,p in {'白家月':'bái jiā yuè','陈天中':'chén tiān zhōng','王一雪':'wáng yī xuě','杨同乐':'yáng tóng lè','王一飞':'wáng yī fēi','咳嗽':'ké sou','暖和':'nuǎn huo','还给':'huán gěi','还可以':'hái kě yǐ','还会':'hái huì','还没':'hái méi','还有':'hái yǒu','长城':'cháng chéng','得穿':'děi chuān','觉得':'jué de','认识':'rèn shi','熟悉':'shú xī','不客气':'bú kè qi','不是':'bú shì','不会':'bú huì','一个':'yí gè','一起':'yì qǐ','一点儿':'yì diǎn ér','地方':'dì fang','东西':'dōng xi','主意':'zhǔ yi'}.items()})
def rows(name):
 return {k:(zh,en) for k,zh,en in (row.split('|') for row in (R/'source'/name).read_text().splitlines() if row)}
def line(zh,en):return {'zh':zh,'py':' '.join(lazy_pinyin(zh,style=Style.TONE)).replace(' ，','，').replace(' 。','。'),'en':en}
p=R/'data.js';d=json.loads(p.read_text().removeprefix('window.HSK_DATA = ').rstrip(';\n'))
prompts=rows('retelling-prompts.tsv');answers=rows('retelling-answers.tsv');meta=json.loads((R/'source/retelling.json').read_text())
for c in d['chapters']:
 for s in c['sections']:
  key=f"{c['id']}-{s['id'].removeprefix('text')}"
  if s['id'].startswith('text') and key in prompts:
   if key in answers:answer=line(*answers[key])
   else:
    blocks=[b for b in s['blocks'] if not b.get('heading')]
    answer=line('\n'.join(b['zh'] for b in blocks),'\n'.join(b['en'] for b in blocks))
   meta[key]={'pages':meta[key]['pages'],'prompt':line(*prompts[key]),'answer':answer}
   s['retelling']=meta[key]
assert len(meta)==20 and all(v.get('prompt') and v.get('answer') for v in meta.values())
(R/'source/retelling.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
p.write_text('window.HSK_DATA = '+json.dumps(d,ensure_ascii=False,separators=(',',':'))+';\n')
print('Updated all 20 retelling prompts and bilingual model answers.')

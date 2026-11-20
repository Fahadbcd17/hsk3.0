"""Merge reviewed Book 4B chapters into the deployable data without changing Book 4A.
Requires pypinyin (authoring only); the published site has no Python dependency.
"""
import json, sys
from pathlib import Path
R=Path(__file__).resolve().parent.parent
sys.path.insert(0,'/tmp/hsk4b-deps')
from pypinyin import lazy_pinyin, Style, load_phrases_dict
load_phrases_dict({'家长':[['jiā'],['zhǎng']], '长大':[['zhǎng'],['dà']], '长得':[['zhǎng'],['de']], '得空':[['dé'],['kòng']], '还给':[['huán'],['gěi']], '干活':[['gàn'],['huó']], '弹钢琴':[['tán'],['gāng'],['qín']], '教室':[['jiào'],['shì']], '教授':[['jiào'],['shòu']], '散步':[['sàn'],['bù']], '便宜':[['pián'],['yi']], '暖和':[['nuǎn'],['huo']], '为了':[['wèi'],['le']], '弹得':[['tán'],['de']], '待在':[['dāi'],['zài']], '待了':[['dāi'],['le']], '一卷':[['yī'],['juàn']], '万卷':[['wàn'],['juàn']]})
def read_data():
 return json.loads((R/'data.js').read_text().split('=',1)[1].strip().rstrip(';'))
def enrich(obj):
 if isinstance(obj,dict):
  if obj.get('zh') and not obj.get('py'):
   obj['py']=' '.join(lazy_pinyin(obj['zh'],style=Style.TONE,neutral_tone_with_five=False))
  for v in obj.values():enrich(v)
 elif isinstance(obj,list):
  for v in obj:enrich(v)
def main():
 d=read_data();original=[c for c in d['chapters'] if c['id']<=10]
 assert len(original)==10
 chapters=[json.loads((R/f'source/4b/chapters/{n}.json').read_text()) for n in range(11,21)]
 for c in chapters:
  c['book']='4B'
  for w in c['words']+c['warmup']:
   if w['zh'] in {'弹':'tán','待':'dāi','卷':'juàn','当':'dàng'}:
    w['py']={'弹':'tán','待':'dāi','卷':'juàn','当':'dàng'}[w['zh']]
  enrich(c)
  # Source objectives always precede the texts; retain original section IDs for notes.
  c['sections'].sort(key=lambda s: -2 if s['id']=='objectives' else -1 if s['id']=='listening' else 0)
  for w in c['words']+c['warmup']:
   if w['zh'] not in d['dictionary'] or d['dictionary'][w['zh']].get('chapter',0)>10:
    d['dictionary'][w['zh']]={'py':w['py'],'en':w['en'],'chapter':c['id']}
 d['title']='New HSK Course 4A & 4B';d['chapters']=original+chapters
 (R/'data.js').write_text('window.HSK_DATA = '+json.dumps(d,ensure_ascii=False,separators=(',',':'))+';\n')
 assert read_data()['chapters'][:10]==original
 print(f'Built {len(d["chapters"])} chapters; Book 4A unchanged; {sum(len(c["words"]) for c in chapters)} Book 4B vocabulary entries.')
if __name__=='__main__':main()

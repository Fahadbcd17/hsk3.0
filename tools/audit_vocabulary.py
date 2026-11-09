"""Conservative vocabulary audit. Flags require editorial review, not automatic rejection.
A segment may consist of known morphemes; this cannot prove semantic difficulty.
Original textbook passages and fixed exercise answers are not rewritten by this audit.
"""
import json,pathlib,re
R=pathlib.Path(__file__).resolve().parent.parent
D=json.loads((R/'source/course.json').read_text())
known=set()
for f in ['anki_hsk1/source/syllabus_level1.json','anki_hsk234/source/level2_syllabus.json','anki_hsk234/source/level3_syllabus.json']:
 for w in json.loads((R/f).read_text())['vocabulary']:known.add(re.sub(r'[0-9¹²³]+$','',w['词语']));known.add(re.sub(r'[0-9¹²³]+$','',w['词语']).removesuffix('儿'))
# Inflectional/result complements, common single-character forms and place names.
known.update('儿 吧 了 着 过 的 地 得 们 这 那 哪 都 没 不 是 在 很 也 又 和 还 要 有 会 能 上 下 里 中 外 前 后 最 让 把 被 对 再 才 就 更 到 用 多 少 大 小 好 说 做 看 想 写 买 吃 走 人 钱 给 学 时 每 一 二 三 四 五 六 七 八 九 十 两 零 个 些 位 名 房 网 别 越 完 首 边 饭 花 太 慢 早 点 打 美 话 清 英语 北京 中国'.split())
gram=[{'任何','要是','随着','一方面','另一方面','另','方面'},{'就是','并','不过','由于'},{'不仅','甚至','于是','不过'},{'再说','既','来得及','来不及','不了'},{'至少','够','各','等','不够'},{'厉害','偶尔','好'},{'方面','既然','拿','来说','使'},{'不管','否则','相比','跟'},{'尽管','但是','此','从来'},{'得','而','再次','说什么','也得','有的是'}]
def residual(s,allowed):
 # Dynamic programming finds a segmentation with the fewest unmatched characters.
 cost=[10**6]*(len(s)+1);paths=[[] for _ in cost];cost[0]=0
 for i in range(len(s)):
  penalty=1 if re.match('[\u3400-\u9fff]',s[i]) else 0
  if cost[i]+penalty<cost[i+1]:cost[i+1]=cost[i]+penalty;paths[i+1]=paths[i]+([s[i]] if penalty else [])
  for j in range(i+1,min(len(s),i+12)+1):
   if s[i:j] in allowed and cost[i]<cost[j]:cost[j]=cost[i];paths[j]=paths[i]
 return ''.join(paths[-1])
flags=[];checked=0
for c in D['chapters']:
 for w in c['words']:
  checked+=1;bad=residual(w['example']['zh'],known|gram[c['id']-1]|{w['zh']})
  if bad:flags.append({'chapter':c['id'],'kind':'word example','target':w['zh'],'zh':w['example']['zh'],'unmatched':bad})
 for q in c['questions']:
  for a in q['answers']:
   checked+=1;bad=residual(a['zh'],known)
   if bad:flags.append({'chapter':c['id'],'kind':'discussion answer','zh':a['zh'],'unmatched':bad})
 for p in c['pictures']:
  checked+=1;bad=residual(p['sentence']['zh'],known|{w['zh'] for w in c['warmup']})
  if bad:flags.append({'chapter':c['id'],'kind':'picture example','zh':p['sentence']['zh'],'unmatched':bad})
 known|={w['zh'] for w in c['words']}
report={'checked':checked,'method':'Level 1–3 local syllabus plus earlier chapter words; target and chapter grammar allowed for word examples; warm-up labels allowed for matching. Morpheme segmentation is a screening aid, not a linguistic guarantee.','flags':flags}
(R/'source/vocabulary-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))

import sys,json,pathlib
sys.path.insert(0,'/tmp/hsk-python')
from PIL import Image,ImageDraw
pages=[20,31,42,54,66,78,90,102,114,127];thumbs=[]
for c,p in enumerate(pages,1):
 rows=json.loads(pathlib.Path(f'source/page-{p:03}.json').read_text());start=next(int(r[0][2][1])+5 for r in rows if r[1].startswith('看图'))
 end=next((int(r[0][0][1])-10 for r in rows if r[1].startswith('任务活动') and r[0][0][1]>start),1480)
 im=Image.open(f'/tmp/hsk-scan-{p:03}.jpg').crop((120,start,1040,end));im.save(f'site/assets/c{c}-exercise.jpg',quality=92)
 if c==9:
  im2=Image.open('/tmp/hsk-scan-115.jpg').crop((120,100,1040,460));im2.save('site/assets/c9-exercise-2.jpg',quality=92)
 im.thumbnail((600,300));thumbs.append((c,im.copy()))
 sheet=Image.new('RGB',(1200,1700),'white');draw=ImageDraw.Draw(sheet)
 for i,(n,im)in enumerate(thumbs):x=(i%2)*600;y=(i//2)*340;draw.text((x+10,y+10),str(n),fill='black');sheet.paste(im,(x,y+30))
 sheet.save('/tmp/exercise-sheet.jpg')

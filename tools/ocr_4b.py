"""Extract the scanned second volume without altering Book 4A sources."""
import sys,json
from pathlib import Path
sys.path.insert(0,'/tmp/hsk4b-deps')
from rapidocr_onnxruntime import RapidOCR
root=Path(__file__).resolve().parent.parent
engine=RapidOCR(intra_op_num_threads=2,inter_op_num_threads=2)
for path in sorted((root/'assets/4b').glob('page-*.jpg')):
 n=int(path.stem.split('-')[-1])
 if len(sys.argv)>1 and not int(sys.argv[1])<=n<=int(sys.argv[2]):continue
 out=root/'source/4b'/f'{path.stem}.json'
 if out.exists():continue
 result,_=engine(str(path))
 out.write_text(json.dumps(result,ensure_ascii=False))
 out.with_suffix('.txt').write_text('\n'.join(r[1] for r in result))
 print(path.stem,flush=True)

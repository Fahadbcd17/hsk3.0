import json, pathlib, sys
sys.path.insert(0,'/tmp/hsk-python')
from rapidocr_onnxruntime import RapidOCR
engine=RapidOCR(intra_op_num_threads=2,inter_op_num_threads=2)
for path in sorted(pathlib.Path('/tmp').glob('hsk-scan-*.jpg')):
    n=int(path.stem.split('-')[-1]); out=pathlib.Path('source')/f'page-{n:03}.json'
    if out.exists():continue
    result,_=engine(str(path))
    out.write_text(json.dumps(result,ensure_ascii=False))
    pathlib.Path('source',f'page-{n:03}.txt').write_text('\n'.join(r[1] for r in result))
    print(n,flush=True)

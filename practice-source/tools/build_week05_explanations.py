from pathlib import Path
import json
from code_line_explanations import explain
ROOT=Path(__file__).resolve().parents[1]
code=json.loads((ROOT/'src/code.json').read_text())
notes={key:explain(code[key],'handler' if key=='handler' else 'form',week=5) for key in ['form','handler','final']}
(ROOT/'src/week05-explanations.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
print('Explained every line of Week05 form, C# backend and complete Razor page')

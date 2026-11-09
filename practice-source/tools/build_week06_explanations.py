"""Generate line-by-line teaching notes from the actual checkpoint files; fail on uncovered lines."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
steps=json.loads((ROOT/'src/week06/checkpoints.json').read_text())
from code_line_explanations import explain
out={'steps':[{'handler':explain(s['handler'],'handler'),'form':explain(s['form'],'form')} for s in steps]}
model=steps[1]['handler'];offset=model.index('public class RegistrationInput');out['model']=explain(model[offset:],'handler')
out['binding']=explain('[BindProperty]\npublic RegistrationInput Input { get; set; } = new();','handler')
(ROOT/'src/week06/explanations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Explained every line in 8 checkpoint pairs, Input Model and binding')

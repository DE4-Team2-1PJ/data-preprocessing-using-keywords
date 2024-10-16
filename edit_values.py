import json
from datetime import datetime
from .keyword import Keyword

jobs = []
with open("job_total.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)
       
keyword = Keyword()
for job in jobs:
    job = keyword.edit_values(job) # keyword class로 데이터 변환

# 결과 저장
with open("job_total_edit.json", 'w', encoding='utf-8') as f:
    json.dump(jobs, f, ensure_ascii=False, indent=4)


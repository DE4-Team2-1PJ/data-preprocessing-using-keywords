from datetime import datetime
class Keyword:
    
    ds = ["과학", "scientist", "science", "research", "사이언", "r&d", "연구"]
    da = ["분석", "analy", "애널리", "ml", "ai", "머신", "machine", "인공지능", "deep", "computer vision", "컴퓨터 비전", 'llm']
    de = ["데이터 엔지니어", "데이터엔지니어", "engineer, data", "engineer(data)", "engineer (Data)", "데이터 개발자", "data engineer", "warehouse", "dw", "bi", "etl", "pipeline", "infra", "플랫폼", "platform"]
    
    def edit_values(self, job: dict) -> dict:
        
        # 각 함수에서 값 분류
        job['category_name'] = self.category_name(job['title'])
        keys = ['end_date', 'career','region', 'stack']
        
        for key in keys:
            if key in job.keys():
                job[key] = getattr(self, key, None)(job[key])
            else:
                job[key] = None
                
        return job
        
    def category_name(self, title):
        
        for keyword in self.ds:
            if keyword in title.lower():
                return "데이터 사이언티스트"
            
        for keyword in self.da:
            if keyword in title.lower():
                return "데이터 분석가"
            
        for keyword in self.de:
            if keyword in title.lower():
                return "데이터 엔지니어"
        
        return None # 데이터 관련 직무로 볼 수 없음

    def end_date(self, date):
        words = ['채용', '수시', '상시']
        #yy.mm.dd, 수시채용, yyyy-mm-dd, yyyy.mm.dd, 채용시, 상시채용, N/A, 채용시까지, 상시, mm/dd
        if not date or date == "N/A":
            return None

        for word in words:
            if word in date:
                return "상시채용"
        
        if date.count("-") == 2:
            return date
        elif date.count(".") == 2:
            year, month, day = date.split(".")
        elif date.count("/") == 1: #mm/dd
            month, day = date.split("/")
            if int(month) < datetime.now().month:
                year = str(int(year) + 1)
            else:
                year = datetime.now().year
                
        return f"{year}-{month}-{day}"
    
    def career(self, career):
        junior_senior = ['신입·경력', '무관', '0']
        if career == 'N/A':
            return None

        if "경력(연차무관)" == career:
            return "경력"
        
        for i in junior_senior:
            if i in career:
                return "신입·경력"
        
        if "경력" in career or "년" in career:
            return "경력"
        
        if "신입" in career:
            return "신입"
        
        if "인턴" in career:
            return "인턴"
        
        return None
    
    def region(self, region):
        if region == 'N/A' or region == '지역' or not region:
            return None
        
        if region == "재택근무" or region == "100% 원격근무":
            return "재택근무"
        
        region_len = len(region.split())
        if region_len == 1:
            return region
        elif region_len >= 2:
            return ' '.join(region.split()[:2])
    
    def stack(self, stack):
        if stack == 'N/A' or not stack:
            return ["기술 스택 없음"]
        else:
            return stack

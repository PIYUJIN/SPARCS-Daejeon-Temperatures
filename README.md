# Sparcs 해커톤 데이터분석 미션
[대전 지역 열섬현상 분석 - 기간별, 지역별 온도 시각화](https://sparcs-daejeon-temperatures.streamlit.app/)
<br>
<br>
## 참고 데이터 
기상청 데이터 : 
[기상청 기후변화 표준 시나리오](http://www.climate.go.kr/home/CCS/contents_2021/35_download.php) / 
[기상청 기온분석](https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70)
 <br>
행정동 경계 데이터 : [행정동 경계](https://github.com/vuski/admdongkor)
<br>
<br>
## 데이터 
Daejeon.geojson : 대전지역 행정동 경계 정보 <br>
merged_avg_tamax_by_region.csv : 대전지역 각 행정구역의 일별 최고온도 (2000년 ~ 2019년) <br>
대전광역시_년도별온도_기본_2010-2023 : 대전지역 연도별 평균기온, 최저기온, 최고기온 (2010 ~ 2023년)
<br>
<br>
## 파일 
page_app.py : 앱 실행 파일 <br>
data_preprocessing.py : 데이터 전처리
<br>
<br>
## Quick Start
라이브러리 섩치
```bash
pip install -r requirements.txt
```
streamlit 실행
```bash
streamlit run streamlit_app.py
```

<br><br>
배포 링크
> https://sparcs-daejeon-temperatures.streamlit.app/
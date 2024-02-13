import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

show_pages(
    [
        Page("page/streamlit_linechart.py", "연도별 평균온도", "📈"),
        Page("page/streamlit_map.py", "지역별 평균온도", "🗺️"),
    ]
)

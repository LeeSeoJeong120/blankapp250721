
import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 Streamlit 요소 예시 페이지")  # 페이지 제목

st.header("1. 텍스트 관련 요소")  # 섹션 헤더
st.subheader("서브헤더 예시")  # 서브헤더
st.write("일반 텍스트 출력")  # 일반 텍스트
st.markdown("**마크다운** _지원_ :sparkles:")  # 마크다운 지원
st.code("print('Hello, Streamlit!')", language="python")  # 코드 블록
st.latex(r"E=mc^2")  # LaTeX 수식


st.header("2. 입력 위젯")  # 입력 위젯 섹션
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120, step=1)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])  # 라디오 버튼
hobby = st.multiselect("취미를 선택하세요", ["독서", "운동", "게임", "음악"])  # 다중 선택
color = st.selectbox("좋아하는 색을 선택하세요", ["빨강", "파랑", "초록"])  # 셀렉트 박스
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time = st.time_input("시간을 선택하세요")  # 시간 입력
uploaded_file = st.file_uploader("파일을 업로드하세요")  # 파일 업로더
slider_val = st.slider("값을 선택하세요", 0, 100, 50)  # 슬라이더

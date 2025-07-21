import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# NanumGothic 폰트 경로 지정
font_path = "./fonts/NanumGothic-Regular.ttf"

# 폰트 등록 및 설정
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

st.title("Matplotlib 데이터 시각화 예시")

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label='사인 곡선')
ax.set_title('사인 함수 그래프')  # 한글 제목
ax.set_xlabel('x 값')            # 한글 x축
ax.set_ylabel('y 값')            # 한글 y축
ax.legend()

st.pyplot(fig)  # Streamlit에 그래프 출력
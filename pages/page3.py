import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

# NanumGothic 폰트 경로 지정
font_path = "/workspaces/blankapp250721/fonts/NanumGothic-Regular.ttf"
font_manager.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

st.title("성적 데이터 시각화 및 분석")  # 페이지 제목

# 파일 업로드 위젯
uploaded_file = st.file_uploader("성적 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.subheader("업로드된 성적 데이터 미리보기")
    st.dataframe(df)  # 데이터 미리보기

    # 수치형 컬럼(성적)만 선택
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    if numeric_cols:
        # 학생별 총점 및 평균, 등수 계산
        df['총점'] = df[numeric_cols].sum(axis=1)
        df['평균'] = df[numeric_cols].mean(axis=1)
        df['등수'] = df['총점'].rank(ascending=False, method='min').astype(int)

        st.write("### 학생별 총점, 평균, 등수")
        st.dataframe(df)

        # 학생별 평균 점수만 따로 표시
        st.write("### 학생별 평균 점수")
        avg_df = df[[df.columns[0], '평균']]
        st.dataframe(avg_df)

        # 과목별 점수 분포 시각화
        st.write("### 과목별 점수 분포")
        fig, ax = plt.subplots()
        df[numeric_cols].plot(kind='box', ax=ax)
        ax.set_title("과목별 점수 Boxplot")
        st.pyplot(fig)

        # 학생별 총점 시각화
        st.write("### 학생별 총점 막대그래프")
        fig2, ax2 = plt.subplots()
        df.plot(x=df.columns[0], y='총점', kind='bar', ax=ax2)
        ax2.set_ylabel('총점')
        ax2.set_title('학생별 총점')
        st.pyplot(fig2)
    else:
        st.warning("성적 데이터(수치형 컬럼)가 필요합니다.")
else:
    st.info("CSV 파일을 업로드하면 성적 데이터 분석 결과가 표시됩니다.")
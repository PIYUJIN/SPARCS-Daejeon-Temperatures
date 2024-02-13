import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드 함수


def load_data(filepath):
    data = pd.read_csv(filepath, skiprows=10, header=None)
    data.columns = ['Year', 'Days', 'AverageTemperature',
                    'LowestTemperature', 'HighestTemperature']
    return data

# 데이터 시각화 함수


def plot_temperature(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Year'], data['LowestTemperature'], marker='o',
             linestyle='-', color='blue', label='Average Lowest Temperature')  # 평균 최저 온도
    plt.plot(data['Year'], data['AverageTemperature'], marker='o',
             linestyle='-', color='green', label='Average Temperature')  # 평균 온도
    plt.plot(data['Year'], data['HighestTemperature'], marker='o',
             linestyle='-', color='red', label='Average Highest Temperature')  # 평균 최고 온도
    plt.title('Yearly Temperature Trends in Daejeon (2010 - 2023)')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

# Streamlit 애플리케이션


def main():
    st.title('대전광역시 연도별 평균온도 비교 (2010 - 2023)')
    filepath = './data/대전광역시_년도별온도_기본_2010-2023.csv'
    data = load_data(filepath)
    st.write("대전지역 연도별 평균온도 비교")
    st.dataframe(data.head())

    # 데이터 시각화
    fig = plot_temperature(data)
    st.pyplot(fig)


if __name__ == "__main__":
    main()

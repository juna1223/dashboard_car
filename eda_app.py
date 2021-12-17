import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app() : 
    st.subheader('EDA 화면입니다.')

    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')

    radio_menu = ['데이터프레임','통계치','컬럼정보']
     



     
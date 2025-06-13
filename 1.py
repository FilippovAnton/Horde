import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

@st.cache_data
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    df = pd.read_csv(path, parse_dates=['Date'])  
    return df

def create_plot(df_new, name='bijiy'):
    fig, ax = plt.subplots(figsize=(10, 6))

    for color, time in zip(['black', 'red', 'brown', 'green', 'blue'], [30, 60, 180, 240, 300]):
        df_loc = df_new[(df_new['Name'] == name) & (df_new['Turn'] == 0) & (df_new['Time'] == time)].copy()
        df_loc['SumDif'] = df_loc['RatingDif'].cumsum()
        x = pd.to_datetime(df_loc['Date'])
        y = df_loc['SumDif']
        ax.plot(x, y, color=color, label=str(time))
        if not df_loc.empty:
            ax.text(x.iloc[-1], y.iloc[-1], str(len(df_loc)), color=color,
                    fontsize=12, verticalalignment='bottom', horizontalalignment='left')

    ax.set_xlabel('Время')
    ax.set_ylabel('Изменение рейтинга')
    ax.set_title('Изменение рейтинга в нетурнирных партиях')
    ax.grid(True)
    ax.legend()

    return fig

def main():
    st.title("Graph")
    df = load_data("https://drive.google.com/file/d/17sn61A1ntXtVJmr9aINGB8lOPBVU0H-7/view?usp=sharing")
    name = st.number_input("Enter the player's nickname", value=2)
    if st.button("Get player statistics"):
        fig = create_plot(df, name)
        st.pyplot(fig)  # отображаем график в приложении

if __name__ == "__main__":
    main()

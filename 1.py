import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import gdown

@st.cache_data
def load_data(url):
    output = 'file.csv'
    gdown.download(url, output, quiet=False)
    df = pd.read_csv(output) #, index_col=0, parse_dates=['Date'])
    return df

def create_plot(df_new, name='bijiy'):
    fig, ax = plt.subplots(figsize=(10, 6))
    df_new = df_new[(df_new['Name'] == name) & (df_new['Turn'] == 0)]
    preferred_time = df_new['Time'].value_counts().head(5).index.to_list()

    for color, time in zip(['black', 'red', 'brown', 'green', 'blue'], preferred_time):
        df_loc = df_new[df_new['Time'] == time].copy()
        if df_loc.empty:
            continue
        df_loc['SumDif'] = df_loc['RatingDif'].cumsum()
        x = pd.to_datetime(df_loc['Date'])
        y = df_loc['SumDif']
        ax.plot(x, y, color=color, label=str(time))
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
    url = 'https://drive.google.com/uc?id=1SxWKiFPIYGfHYb4NdPlegQbnIhD9K5hA'
    df = load_data(url) 
    name = st.text_input("Enter the player's nickname", value="bijiy")
    
    if st.button("Get player statistics"):
        fig = create_plot(df, name)
        st.pyplot(fig)

if __name__ == "__main__":
    main()

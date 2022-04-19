import streamlit as st
import os


st.set_page_config(
    page_title="Globetrack Radios",
    page_icon=":radio:",
    layout="wide",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            
            <style>
                #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def main():

    st.markdown(" ")
    st.title("Listen to recordings from RMS radio stations")
    st.markdown("""
    #### Select a station and recorded file from the side menu and start listening.
    """)

    select_station = st.selectbox('Pick a station...', get_available_stations())

    radios_dir = f"{os.sep}".join(os.path.abspath(__file__).split(os.sep)[:-1])
    recordings = os.listdir(f"{radios_dir}/RADIO_RECORDINGS/{select_station.upper().replace(' ', '_')}")

    with st.expander(f"Open to see recordings from {select_station}"):
        for i, recording in enumerate(recordings):
            col_name, col_size, col_open = st.columns((2, 1, 1))

            col_name.write(recording)
            col_size.write("X Kb")
            col_open.button(label="Open", key=recording)
        
        print(select_station)

    


def get_available_stations():

    radios_dir = f"{os.sep}".join(os.path.abspath(__file__).split(os.sep)[:-1])
    stations = [x.replace('_', ' ').title() for x in os.listdir(f"{radios_dir}/RADIO_RECORDINGS")]

    return stations






if __name__ == '__main__':
    main()

import base64

import streamlit as st

from plot import create_heart_pressure_gauge

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode("utf-8")
    return base64_str


if __name__ == "__main__":
    # Streamlit Interface
    st.markdown("""
        <style>
            .centered-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    pressure_path = "pressure.png"
    pressure_base = image_to_base64(pressure_path)
    st.markdown(
        f'<div class="centered-container"><img src="data:image/png;base64,{pressure_base}"><h1>Non candidabile a RDN</h1></div>',
        unsafe_allow_html=True)

    heart_pressure = st.slider("Select Heart Pressure (mmHg)", 100, 170, 135)
    fig = create_heart_pressure_gauge(heart_pressure)
    st.plotly_chart(fig)
    logo_path = "logo-medtronic.png"
    logo_base = image_to_base64(logo_path)
    st.markdown(
        f'<div class="centered-container"><img src="data:image/png;base64,{logo_base}"></div>',
        unsafe_allow_html=True)

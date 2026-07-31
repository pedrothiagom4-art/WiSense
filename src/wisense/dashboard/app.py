import time

import pandas as pd
import plotly.express as px
import streamlit as st

from wisense.simulation import SignalSimulator

st.set_page_config(
    page_title="WiSense",
    layout="wide",
)

st.title("📡 WiSense")

simulator = SignalSimulator()

placeholder = st.empty()

samples = []

while True:

    sample = simulator.generate()

    samples.append(sample)

    df = pd.DataFrame({

        "RSSI":[s.rssi for s in samples]

    })

    with placeholder.container():

        col1, col2 = st.columns(2)

        col1.metric(
            "RSSI Atual",
            f"{sample.rssi:.2f} dBm"
        )

        col2.metric(
            "Status",
            "🚶 Movimento"
            if sample.movement
            else "🟢 Normal"
        )

        fig = px.line(
            df,
            y="RSSI",
            title="RSSI em tempo real"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    time.sleep(0.5)
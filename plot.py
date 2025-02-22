import plotly.graph_objects as go


def create_heart_pressure_gauge(heart_pressure):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=heart_pressure,
        title={'text': "Heart Pressure (mmHg)", 'font': {'size': 24, 'color': 'white'}},
        gauge={
            'axis': {'range': [100, 170], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "white"},
            'bgcolor': "#1010eb",
            'borderwidth': 2,
            'bordercolor': "white",
            'steps': [
                {'range': [100, 130], 'color': 'green'},  # Normal HR
                {'range': [130, 140], 'color': 'orange'},  # High Normal HR
                {'range': [140, 170], 'color': 'red'}  # High HR
            ],
        }
    ))

    fig.update_layout(
        paper_bgcolor="#1010eb",
        plot_bgcolor="#1010eb",
        font={'color': "white", 'family': "Arial"}
    )

    return fig
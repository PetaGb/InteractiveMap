import pandas as pd
import json
import plotly.express as px
import plotly


def map_fig():

    df = pd.read_csv("dataset.csv")
    Western_Europe = df[df['Regional indicator'] == 'Western Europe']
    Central_and_Eastern_Europe = df[df['Regional indicator'] == 'Central and Eastern Europe']
    Europe = pd.concat([Western_Europe, Central_and_Eastern_Europe])

    cols = ['Country name', 'Ladder score', 'Logged GDP per capita', 'Social support',
            'Healthy life expectancy', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']

    fig = px.choropleth(Europe,
                        scope="europe",
                        locations="Country name",
                        locationmode='country names',
                        color='Ladder score',
                        hover_name='Ladder score',
                        hover_data=cols,
                        color_continuous_scale=px.colors.sequential.Blues,
                        )

    fig_final = fig.update_layout(height=800, width=1600, margin={"r": 1, "t": 0, "l": 0, "b": 0})
    return json.dumps(fig_final.show(), cls=plotly.utils.PlotlyJSONEncoder)

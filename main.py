import streamlit as st
import pandas as pd
import plotly.express as px
from pages import home, map, heatmap, epc_rating

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

pathname = '/Users/meghna_mac2/PycharmProjects/WMCA/wmca_app/'  # your pathname

st.markdown(
    """
    <style>
    .main {
        background-color: F5F5F
    }
    </style>
    """,
    unsafe_allow_html = True
)

@st.cache
def get_data(filename):
    data = pd.read_csv(filename)
    return data

with header:
    st.title('WMCA - Pure LeapFrog Demo')
    st.text('')

with dataset:
    st.header('EPC data')
    epc_data = get_data(pathname+'data/numerical_individual_columns_data.csv')
    st.write(epc_data.head())
    constituency = pd.DataFrame(epc_data['constituency'].value_counts())
    st.bar_chart(constituency)

    ####### plotly animation #####

    # epc_data['construction-age-band'] = pd.to_datetime(epc_data['construction-age-band']).dt.strftime('%Y-%m-%d')
    # construction_age_band = epc_data['construction-age-band'].unique().tolist()
    # fig1 = px.scatter(epc_data, x='constituency', y='mean_counsumption', animation_frame='construction-age-band')
    # st.write(fig1)  

######## maps ####
# st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

pages = [
        # {"func": home.app, "title": "Home", "icon": "house"},
        # {"func": heatmap.app, "title": "Heatmap", "icon": "map"}
        {"func": epc_rating.app, "title": "Heatmap", "icon": "map"},
        # {"func": map.app, "title": "Home", "icon": "house"}
]


titles = [app["title"] for app in pages]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in pages]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))


for app in pages:
    app["func"]()
    


# with features:
#     st.header('feature')


# with model_training:            
#     st.header('model')
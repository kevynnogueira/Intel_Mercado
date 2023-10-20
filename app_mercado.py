import streamlit as st
import plotly.express as px
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Calculadora de mercado"
                   #, page_icon=":signal_strength:"
                   , layout="wide")

with st.container():
    st.title(" :signal_strength: Calculadora de mercado")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
    st.write("Desenvolvido por [Kevyn Nogueira](https://www.linkedin.com/in/kevynnogueira/)")
    st.write("-------------------------------------------------------------------------------")

@st.experimental_memo
def carregar_dados():
    df = pd.read_csv("df_completo.csv", encoding="UTF-8")
    return df

df = carregar_dados()

st.sidebar.header("FILTROS:")

# Create for UF
uf=st.sidebar.multiselect("Unidade federativa:", df["UF"].sort_values().unique())
if not uf:
    df2=df.copy()
else:
    df2=df[df["UF"].isin(uf)]

# Create for DESCRICAO_MUNICIPIO
municipio=st.sidebar.multiselect("Município:", df2["DESCRICAO_MUNICIPIO"].sort_values().unique())
if not municipio:
    df3=df2.copy()
else:
    df3=df2[df2["DESCRICAO_MUNICIPIO"].isin(municipio)]

# Create for BAIRRO
bairro=st.sidebar.multiselect("Bairro:", df3["BAIRRO"].sort_values().unique())

if not bairro:
    df4 = df3.copy()
else:
    df4 = df3[df3["BAIRRO"].isin(bairro)]

# Create for PORTE DA EMPRESA
porte_empresa = st.sidebar.multiselect("Porte da empresa:", df4["PORTE DA EMPRESA"].sort_values().unique())

if not porte_empresa:
    df5 = df4.copy()
else:
    df5 = df4[df4["PORTE DA EMPRESA"].isin(porte_empresa)]


# Create for TIPO DE EMPRESA
tipo_empresa = st.sidebar.multiselect("Tipo de empresa:", df5["TIPO DE EMPRESA"].sort_values().unique())

if not tipo_empresa:
    df6 = df5.copy()
else:
    df6 = df5[df5["TIPO DE EMPRESA"].isin(porte_empresa)]

# Filtering the data

if not uf and not municipio and not bairro and not porte_empresa and not tipo_empresa: filtered_df = df6.copy()
elif uf and municipio and bairro and porte_empresa and not tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa)]
elif uf and municipio and bairro and not porte_empresa and tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif uf and municipio and bairro and not porte_empresa and not tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro)]
elif uf and municipio and not bairro and porte_empresa and tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif uf and municipio and not bairro and porte_empresa and not tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['PORTE DA EMPRESA'].isin(porte_empresa)]
elif uf and municipio and not bairro and not porte_empresa and tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif uf and municipio and not bairro and not porte_empresa and not tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio)]
elif uf and not municipio and bairro and porte_empresa and tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif uf and not municipio and bairro and porte_empresa and not tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa)]
elif uf and not municipio and bairro and not porte_empresa and tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['BAIRRO'].isin(bairro) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif uf and not municipio and bairro and not porte_empresa and not tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['BAIRRO'].isin(bairro)]
elif uf and not municipio and not bairro and porte_empresa and tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif uf and not municipio and not bairro and porte_empresa and not tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['PORTE DA EMPRESA'].isin(porte_empresa)]
elif uf and not municipio and not bairro and not porte_empresa and tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif uf and not municipio and not bairro and not porte_empresa and not tipo_empresa: filtered_df = df6[df6['UF'].isin(uf)]
elif not uf and municipio and bairro and porte_empresa and tipo_empresa: filtered_df = df6[df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif not uf and municipio and bairro and porte_empresa and not tipo_empresa: filtered_df = df6[df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa)]
elif not uf and municipio and bairro and not porte_empresa and tipo_empresa: filtered_df = df6[df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif not uf and municipio and bairro and not porte_empresa and not tipo_empresa: filtered_df = df6[df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro)]
elif not uf and municipio and not bairro and porte_empresa and tipo_empresa: filtered_df = df6[df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif not uf and municipio and not bairro and porte_empresa and not tipo_empresa: filtered_df = df6[df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['PORTE DA EMPRESA'].isin(porte_empresa)]
elif not uf and municipio and not bairro and not porte_empresa and tipo_empresa: filtered_df = df6[df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif not uf and municipio and not bairro and not porte_empresa and not tipo_empresa: filtered_df = df6[df6['DESCRICAO_MUNICIPIO'].isin(municipio)]
elif not uf and not municipio and bairro and porte_empresa and tipo_empresa: filtered_df = df6[df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif not uf and not municipio and bairro and porte_empresa and not tipo_empresa: filtered_df = df6[df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa)]
elif not uf and not municipio and bairro and not porte_empresa and tipo_empresa: filtered_df = df6[df6['BAIRRO'].isin(bairro) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif not uf and not municipio and bairro and not porte_empresa and not tipo_empresa: filtered_df = df6[df6['BAIRRO'].isin(bairro)]
elif not uf and not municipio and not bairro and porte_empresa and tipo_empresa: filtered_df = df6[df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
elif not uf and not municipio and not bairro and porte_empresa and not tipo_empresa: filtered_df = df6[df6['PORTE DA EMPRESA'].isin(porte_empresa)]
elif not uf and not municipio and not bairro and not porte_empresa and tipo_empresa: filtered_df = df6[df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
#elif uf and municipio and bairro and porte_empresa and tipo_empresa: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]
else: filtered_df = df6[df6['UF'].isin(uf) & df6['DESCRICAO_MUNICIPIO'].isin(municipio) & df6['BAIRRO'].isin(bairro) & df6['PORTE DA EMPRESA'].isin(porte_empresa) & df6['TIPO DE EMPRESA'].isin(tipo_empresa)]

porte_df=filtered_df.groupby(by=["PORTE DA EMPRESA"], as_index=False)["CNPJ BASICO"].count().sort_values(by =["CNPJ BASICO"])
tipo_cnae_df=filtered_df.groupby(by=["TIPO DE EMPRESA"], as_index=False)["CNPJ BASICO"].count().sort_values(by =["CNPJ BASICO"])
cnae_df=filtered_df.groupby(by=["DESCRICAO CNAE"], as_index=False)["CNPJ BASICO"].count().sort_values(by =["CNPJ BASICO"])
capital_df=filtered_df[['CNPJ BASICO', 'CAPITAL SOCIAL']].drop_duplicates()
#-----------------------------------------------------------------------------------------------
# create columns
kpi1, kpi2, kpi3=st.columns(3)

# fill the column with respect to the KPIs
kpi1.metric("Quantidade total de empresas ativas",filtered_df["CNPJ BASICO"].nunique())

kpi2.metric("Quantidade total de estabelecimentos ativos",filtered_df["CNPJ BASICO"].count())

capital = f"R${capital_df['CAPITAL SOCIAL'].sum():_.2f}"
capital = capital.replace('.', ',').replace('_', '.')
kpi3.metric("Capital social total", capital)

st.subheader("Quantidade de estabelecimentos por porte da empresa")
fig=px.bar(porte_df, x="PORTE DA EMPRESA", y="CNPJ BASICO", text_auto=True,
             template="seaborn")
st.plotly_chart(fig,use_container_width=True, height=200)

st.subheader("Quantidade de estabelecimentos por atividade")
fig=px.bar(tipo_cnae_df, x="TIPO DE EMPRESA", y="CNPJ BASICO", text_auto=True,
             template="seaborn")
st.plotly_chart(fig,use_container_width=True, height=200)

st.subheader("Quantidade de estabelecimentos por CNAE")
fig=px.bar(cnae_df, y="DESCRICAO CNAE", x="CNPJ BASICO", text_auto=True,
             template="seaborn")
st.plotly_chart(fig,use_container_width=True, height=200)

# --------------------------------------

coord_df = filtered_df[['LATITUDE', 'LONGITUDE']].dropna()
coord_df.rename(columns={"LATITUDE": "lat", "LONGITUDE": "lon"},inplace=True)

st.subheader("Geolocalização por CNPJ")
st.map(coord_df)

st.subheader("Quantidade de estabelecimentos por Bairro")
bairro_cnpj_df=filtered_df[['BAIRRO','CNPJ BASICO']].drop_duplicates().groupby(['BAIRRO']).count().reset_index().sort_values(by = 'CNPJ BASICO',ascending=False).reset_index(drop  = True)

fig=px.bar(bairro_cnpj_df, x="BAIRRO", y="CNPJ BASICO", text_auto=True, template="seaborn").update_layout(
    xaxis={
        "range": [bairro_cnpj_df["CNPJ BASICO"].quantile(1), df["CNPJ BASICO"].max()],
        "rangeslider": {"visible": True},
        "autorange": True
    }
)
st.plotly_chart(fig,use_container_width=True, height=200)

st.subheader("Leads")

filtered_table = filtered_df.drop(['RAZAO SOCIAL','LATITUDE','LONGITUDE'], axis = 1).fillna("-").astype(str)

st.dataframe(filtered_table)
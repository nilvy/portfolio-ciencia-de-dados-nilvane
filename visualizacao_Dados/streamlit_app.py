import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Exportações do Brasil", page_icon="📊", layout="wide")
st.title("📊 Exportações do Brasil (2020–2025)")

# Leitura do CSV de exportações
@st.cache_data
def carregar_dados():
    df = pd.read_csv("exportacoes_brasil_2020_2025.csv")
    df["Ano"] = df["Ano"].astype(int)
    df["Valor_US$Bi"] = pd.to_numeric(df["Valor_US$Bi"], errors="coerce")
    df["Participacao_%"] = pd.to_numeric(df["Participacao_%"], errors="coerce")
    return df

df = carregar_dados()

# Filtros
anos = sorted(df["Ano"].unique())
produtos = sorted(df["Produto"].unique())
setores = sorted(df["Setor"].unique())

ano_sel = st.multiselect("Selecione ano(s)", options=anos, default=anos)
setor_sel = st.multiselect("Selecione setor(es)", options=setores, default=setores)
produto_sel_raw = st.multiselect("Selecione produto(s)", options=produtos)

# Se nenhum produto for selecionado, usar todos os produtos do setor selecionado
if not produto_sel_raw:
    produto_sel = df[df["Setor"].isin(setor_sel)]["Produto"].unique().tolist()
else:
    produto_sel = produto_sel_raw


# Aplicar filtros
df_f = df[df["Ano"].isin(ano_sel) & df["Produto"].isin(produto_sel) & df["Setor"].isin(setor_sel)]

# KPIs
col1, col2, col3 = st.columns(3)
if not df_f.empty:
    col1.metric("Total exportado (US$ Bi)", f"{df_f['Valor_US$Bi'].sum():,.2f}")
    col2.metric("Produto líder", df_f.groupby("Produto")["Valor_US$Bi"].sum().idxmax())
    col3.metric("Ano com maior valor", df_f.groupby("Ano")["Valor_US$Bi"].sum().idxmax())
else:
    col1.metric("Total exportado (US$ Bi)", "0.00")
    col2.metric("Produto líder", "—")
    col3.metric("Ano com maior valor", "—")


st.divider()

# Evolução por produto ao longo dos anos
st.subheader("📈 Evolução anual por produto (US$ Bi)")
fig = px.line(
    df_f,
    x="Ano",
    y="Valor_US$Bi",
    color="Produto",
    markers=True,
    title="Exportações por produto ao longo dos anos"
)
fig.update_layout(
    xaxis=dict(tickmode="linear", dtick=1),
    yaxis_title="Valor (US$ Bi)",
    legend_title="Produto",
    title_x=0.5
)
st.plotly_chart(fig, use_container_width=True)

# Comparação por produto em um único ano
st.subheader("📌 Comparação por produto em um ano específico")
ano_unico = st.selectbox("Selecione um ano", options=anos, index=len(anos)-1)
df_unico = df[df["Ano"] == ano_unico]
df_unico = df_unico[df_unico["Produto"].isin(produto_sel) & df_unico["Setor"].isin(setor_sel)]
st.bar_chart(df_unico.set_index("Produto")["Valor_US$Bi"])

st.divider()

# Download dos dados filtrados
st.subheader("📥 Baixar dados filtrados")
csv_bytes = df_f.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", data=csv_bytes, file_name="exportacoes_filtrado.csv", mime="text/csv")

st.divider()

# Tabela detalhada com estilo
st.subheader("📋 Tabela detalhada")
df_formatado = df_f.sort_values(["Ano", "Valor_US$Bi"], ascending=[True, False])
st.dataframe(
    df_formatado.style.format({
        "Valor_US$Bi": "{:.2f}",
        "Participacao_%": "{:.1f}"
    }),
    use_container_width=True
)

st.divider()
st.subheader("🌍 Destinos de exportação por setor (2025)")

# Carregar dataset de destinos
@st.cache_data
def carregar_destinos():
    df_dest = pd.read_csv("destinos_exportacoes_2025.csv")
    df_dest["Valor_US$Bi"] = pd.to_numeric(df_dest["Valor_US$Bi"], errors="coerce")
    return df_dest

df_destinos = carregar_destinos()

# Agrupar por país e setor
df_sel = df_destinos[df_destinos["Produto"].isin(produto_sel) & df_destinos["Setor"].isin(setor_sel)]
df_grouped = df_sel.groupby(["Pais", "Setor"]).agg({
    "Valor_US$Bi": "sum",
    "Produto": lambda x: ", ".join(sorted(set(x)))
}).reset_index()

# Paleta de cores por setor
cores_setor = {
    "Agropecuário": "green",
    "Extrativo": "gray",
    "Manufaturado": "orange"
}

fig_mapa = go.Figure()

for setor in df_grouped["Setor"].unique():
    df_s = df_grouped[df_grouped["Setor"] == setor]
    fig_mapa.add_trace(go.Scattergeo(
        locationmode='country names',
        locations=df_s["Pais"],
        text=df_s.apply(lambda row: f"🌍 {row['Pais']}<br>Setor: {row['Setor']}<br>Produtos: {row['Produto']}<br>Valor total: {row['Valor_US$Bi']:.1f} US$ Bi", axis=1),
        name=setor,
        mode='markers',
        marker=dict(
            size=df_s["Valor_US$Bi"] * 2,
            color=cores_setor.get(setor, "blue"),
            line=dict(width=0.5, color="black")
        )
    ))

fig_mapa.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='natural earth',
        bgcolor="rgba(240,240,240,0.95)"
    ),
    title="🌍 Destinos de exportação por setor (2025)",
    title_x=0.5,
    legend_title="Setor"
)

# Exibir mapa e ranking lado a lado
col_mapa, col_ranking = st.columns([2, 1])

with col_mapa:
    st.plotly_chart(fig_mapa, use_container_width=True, key="mapa_setorial")

with col_ranking:
    st.subheader("📊 Ranking de exportação")
    df_rank = df_f.groupby("Produto")["Valor_US$Bi"].sum().reset_index().sort_values("Valor_US$Bi", ascending=False)
    st.dataframe(df_rank.style.format({"Valor_US$Bi": "{:.2f}"}), use_container_width=True)

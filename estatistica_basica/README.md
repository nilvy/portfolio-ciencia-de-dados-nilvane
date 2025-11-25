# 📊 Estatística Básica com Séries Econômicas (Brasil, 2014–2024)

Este projeto tem como objetivo aplicar conceitos de estatística descritiva utilizando séries temporais públicas e confiáveis, disponibilizadas pelo Banco Central do Brasil via API SGS. A análise é feita diretamente no Google Colab, sem necessidade de download de arquivos ou uso de armazenamento local.

---

## 🎯 Objetivos

- Praticar estatística básica (média, mediana, moda, desvio padrão)
- Visualizar séries temporais econômicas com gráficos interativos
- Trabalhar com dados reais e atualizados via API
- Criar um projeto leve, funcional e replicável

---

## 🧩 Fontes de dados

Utilizamos a [API SGS do Banco Central do Brasil](https://dadosabertos.bcb.gov.br/dataset/series-temporais) para acessar as seguintes séries:

| Indicador        | Código SGS | Frequência | Unidade        |
|------------------|------------|------------|----------------|
| IPCA mensal      | 433        | Mensal     | % no mês       |
| Câmbio USD/BRL   | 1          | Diária     | R$ por US$     |
| Selic Meta       | 432        | Mensal     | % ao ano       |

---

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- **Google Colab**
- `pandas` – manipulação de dados
- `requests` – acesso à API
- `matplotlib` – visualização gráfica

---

## 📈 Etapas da análise

1. **Importação das bibliotecas**
2. **Consulta à API do Banco Central**
   - IPCA: código 433
   - Período: 01/01/2014 a 31/12/2024
3. **Limpeza e transformação dos dados**
   - Conversão de datas e valores
   - Ordenação cronológica
4. **Estatística descritiva**
   - Média, mediana, moda, desvio padrão
5. **Visualização**
   - Gráfico de linha da evolução do IPCA mensal

---

## 📌 Resultados esperados

- Estatísticas claras sobre o comportamento da inflação no Brasil
- Gráfico funcional e informativo
- Base para expandir com câmbio e taxa Selic

## 📈 Resultados

### Estatísticas básicas
- Média, mediana, moda e desvio padrão do IPCA mensal (2014–2024)

### Gráficos gerados
1. **IPCA mensal (linha temporal)**  
   ![IPCA mensal](images/ipca_linha.png)

2. **Boxplot por ano**  
   ![Boxplot IPCA por ano](images/ipca_boxplot_ano.png)

3. **Média móvel 12 meses**  
   ![Média móvel IPCA](images/ipca_media_movel.png)

4. **Picos e quedas identificados**  
   ![Picos e quedas](images/ipca_picos_quedas.png)

5. **Distribuição por mês (sazonalidade)**  
   ![IPCA sazonalidade](images/ipca_sazonalidade.png)

6. **Boxplot por mês**  
   ![Boxplot IPCA por mês](images/ipca_boxplot_mes.png)

7. **Heatmap ano × mês (calendário)**  
   ![Heatmap IPCA](images/ipca_heatmap.png)

---
## 🔍 Principais insights

- **Tendência suavizada:** a média móvel de 12 meses evidencia ciclos de alta e queda, reduzindo o ruído da variação mensal.
- **Meses extremos:** os gráficos de picos e quedas destacam os meses com maior e menor inflação no período, úteis para contextualizar choques.
- **Sazonalidade clara:** a média por mês e o boxplot mensal mostram padrões recorrentes; alguns meses apresentam inflação consistentemente mais alta.
- **Volatilidade anual:** anos com maior desvio padrão sinalizam ambientes macroeconômicos mais instáveis.
- **Mapa de calor ano × mês:** facilita comparar rapidamente períodos quentes (inflação elevada) e frios (inflação baixa) ao longo dos anos.
----

## 🚀 Expansões futuras
- Adicionar câmbio USD/BRL (código SGS 1) com agregação mensal
- Incluir taxa Selic Meta (código SGS 432)
- Criar dashboard interativo com Streamlit
- Comparar inflação × juros × câmbio


---

## 📂 Estrutura sugerida do projeto


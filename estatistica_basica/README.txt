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

---

## 🚀 Expansões futuras

- Adicionar análise do câmbio USD/BRL com agregação mensal
- Incluir série da taxa Selic Meta
- Criar dashboard interativo com Streamlit
- Comparar inflação × juros × câmbio

---

## 📂 Estrutura sugerida do projeto


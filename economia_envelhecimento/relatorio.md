# Relatório de Análise – Envelhecimento Populacional e Gastos Previdenciários no Brasil

**Autora:** Nilvane Oliveira Rocha  
**Projeto:** Ciência de Dados aplicada à economia e demografia  
**Fontes:** IBGE (projeções populacionais) e INSS (gastos anuais)

---

## 🎯 Objetivo

Investigar como o envelhecimento populacional no Brasil impacta os gastos previdenciários, com foco nos dados do INSS entre 2010 e 2025.  
A análise busca identificar correlações, tendências e projeções futuras que possam orientar políticas públicas e planejamento fiscal.

---

## 🧪 Metodologia

- Coleta de dados reais do IBGE e INSS.  
- Construção de DataFrame com anos, percentual de população idosa (60+ e 65+) e gastos previdenciários.  
- Visualizações gráficas com séries temporais, dispersão, normalização e crescimento percentual.  
- Aplicação de regressão linear para prever gastos futuros com base no envelhecimento.  
- Cálculo de correlação estatística e médias de crescimento anual.  

---

## 📊 Resultados

### Evolução populacional e fiscal
- A proporção de idosos (60+) aumentou de **11,3% em 2010** para **17% em 2025**.  
- Os gastos do INSS cresceram de **R$ 450 bilhões** para **R$ 1,007 trilhão** no mesmo período.  

### Correlação estatística
- Coeficiente da regressão: **90.13**  
- Intercepto: **-550.50**  
- Correlação ajustada entre % de idosos e gastos INSS: **0.99**  
👉 Indica relação fortemente positiva.  

### Previsões futuras com base no modelo
- Com **18,5%** de idosos: **R$ 1.116,91 bilhões**  
- Com **20%** de idosos: **R$ 1.252,11 bilhões**  
- Com **22%** de idosos: **R$ 1.432,37 bilhões**  

---

## 📈 Análise complementar

Para uma análise mais precisa da dinâmica entre envelhecimento e gastos, optamos por representar a **taxa de crescimento percentual anual** em vez dos valores absolutos. Essa abordagem destaca descompassos temporais e pressões fiscais não lineares.

- Média de crescimento anual da população idosa (60+): **5,28%**  
- Média de crescimento anual dos gastos do INSS: **10,83%**  

> Isso revela que os gastos previdenciários aumentam em ritmo superior ao envelhecimento populacional, sugerindo que fatores adicionais — como reajustes de benefícios, judicializações, mudanças legislativas e aumento da expectativa de vida — contribuem significativamente para a pressão fiscal.  
> Essa discrepância reforça a necessidade de **planejamento previdenciário sustentável**, especialmente diante das projeções de envelhecimento acelerado até 2040.  

---

## ✅ Conclusão

O envelhecimento populacional representa um desafio fiscal significativo para o Brasil.  
Projetos como este ajudam a visualizar tendências e apoiar decisões estratégicas em políticas públicas, previdência social e planejamento econômico de longo prazo.  

---

## 🔗 Referências

- IBGE – Projeções populacionais  
- INSS – Painéis estatísticos de gastos  
- Python (pandas, matplotlib, scikit-learn)  
- Google Colab e GitHub  

---

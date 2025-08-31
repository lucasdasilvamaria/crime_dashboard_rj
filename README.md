# Crime Dashboard - Rio de Janeiro

Este projeto é um **dashboard interativo** que visualiza estatísticas de crimes no estado do Rio de Janeiro. Os dados utilizados vêm de uma base histórica mensal por município, desde 2003, disponibilizada pelo governo. O objetivo do dashboard é permitir que o usuário explore os crimes ao longo do tempo, filtrando por faixa de anos e tipos de crimes.

> **Fonte dos dados:** os dados foram retirados do [dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/isp-estatisticas-de-seguranca-publica) e podem ser baixados livremente em CSV.

---

## 📊 Funcionalidades

- Filtragem por **faixa de anos**.
- Seleção de múltiplos tipos de crimes.
- Visualização dinâmica:
  - **Tabela interativa** com os dados filtrados.
  - **Gráficos de linha** mostrando a tendência dos crimes selecionados.
- Dashboard responsivo, executável em navegador via **Streamlit**.

---

## 📁 Estrutura do Projeto

```

crime\_dashboard\_rj/
│
├─ data/
│   └─ BaseEstadoTaxaMes.csv       # CSV com os dados de crimes
│
├─ src/
│   └─ dashboard.py                # Código do dashboard
│
├─ assets/                         # Imagens para README
│   ├─ 1.png
│   ├─ 2.png
│   └─ 3.png
│
├─ requirements.txt                # Bibliotecas necessárias
├─ README.md                        # Este arquivo
└─ .gitignore

````

---

## 🛠️ Instalação e Configuração

1. **Clone o repositório:**

```bash
git clone https://github.com/lucasdasilvamaria/crime_dashboard_rj.git
cd crime_dashboard_rj
````

2. **Crie um ambiente virtual** (opcional, mas recomendado):

```bash
python -m venv .venv
```

3. **Ative o ambiente virtual:**

* Windows:

```bash
.venv\Scripts\activate
```

* Linux / MacOS:

```bash
source .venv/bin/activate
```

4. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

5. **Verifique se o CSV `BaseEstadoTaxaMes.csv` está na pasta `data/`.**
   Caso queira, você pode baixar o CSV diretamente do [dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/isp-estatisticas-de-seguranca-publica).

---

## 🚀 Como Executar

No terminal, dentro da pasta do projeto:

```bash
streamlit run src/dashboard.py
```

Isso abrirá o dashboard no navegador padrão.

---

## ⚙️ Uso

* **Faixa de anos:** Use o slider na barra lateral para escolher o período que deseja analisar.
* **Seleção de crimes:** Marque os crimes que deseja visualizar no gráfico e na tabela.
* **Tabela de dados:** Mostra todos os crimes selecionados para os anos filtrados.
* **Gráfico de linha:** Mostra a tendência dos crimes selecionados ao longo do tempo.

---

## 🖼️ Exemplos de Visualização

**Dashboard Principal:**

![Dashboard](assets/1.png)

**Tabela filtrada por anos e crimes:**

![Tabela filtrada](assets/2.png)

**Gráfico de tendência de crimes:**

![Gráfico de crimes](assets/3.png)

---

## 📊 Bibliotecas Utilizadas

* `pandas` - manipulação de dados
* `numpy` - operações numéricas
* `plotly` - visualização interativa
* `streamlit` - construção do dashboard web
* `openpyxl` - (caso queira exportar para Excel)

---

## 💡 Possíveis Melhorias

* Adicionar **mapa interativo** por município usando `folium`.
* Incluir **estatísticas agregadas**, como média e variação percentual.
* Exportação de gráficos e tabelas em **PDF/Excel**.
* Melhorar layout e estilo do dashboard com `streamlit` ou `dash`.

---

## ⚖️ Licença

Este projeto é open-source e está disponível para **uso educacional e profissional**.

---

## 📌 Observações

* O dashboard utiliza dados oficiais de crimes, mas algumas informações podem estar incompletas ou ausentes em determinados meses.
* Sempre verifique a qualidade dos dados antes de tomar decisões baseadas neles.

```
```

# Week 2: Exploratory Data Analysis (EDA) and Visualization Framework Design

## TelePulse AI — Universal EDA & Visual Analytics Blueprint

### Project Overview
This deliverable presents a comprehensive, universal Exploratory Data Analysis (EDA) and Visualization Framework designed to diagnose, audit, and extract actionable statistical intelligence from complex tabular datasets using Python. The framework is adaptable to any dataset and follows a structured 6-stage diagnostic methodology.

### Deliverable Contents
- **EDA Strategic Philosophy** — Why rigorous exploratory analysis is the foundation of reliable data science
- **Data Type Taxonomy** — Continuous, discrete, nominal, ordinal, temporal, and binary classification with handling protocols
- **Univariate Analysis** — Distribution moments, KDE histograms, categorical frequency profiling
- **Bivariate Analysis** — Pearson/Spearman correlations, ANOVA, Chi-Square tests, comparative visualizations
- **Multivariate Analysis** — Correlation matrices, PCA/t-SNE projections, higher-order feature interactions
- **Missing Data Protocols** — MCAR/MAR/MNAR taxonomy, KNNImputer, IterativeImputer, missingness indicators
- **Outlier Detection** — Z-Score, IQR fencing, Isolation Forest, Winsorization treatment
- **Visualization Grammar** — Chart selection matrix following Tufte's data-ink principles
- **Python Tooling** — Pandas, Matplotlib, Seaborn, Plotly, Missingno, Statsmodels, YData-Profiling
- **Reporting Architecture** — 4-tier documentation hierarchy from technical audit to executive brief

### Strategic Diagrams (Embedded in Report)
| Figure | Description |
|--------|-------------|
| `figures/w2_fig1_eda_framework.png` | 6-Stage Universal EDA Diagnostic Architecture |
| `figures/w2_fig2_data_profiling.png` | Multi-Panel EDA Statistical Diagnostic Suite |
| `figures/w2_fig3_cleaning_flow.png` | Missing Value & Outlier Treatment Decision Tree |

### Tools & Technologies
Python 3.13 · Pandas · NumPy · Matplotlib · Seaborn · Plotly · Statsmodels · Missingno · YData-Profiling

### How to Regenerate
```bash
pip install python-docx matplotlib seaborn numpy
python generate_week2_doc.py
```

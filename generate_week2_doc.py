import os
from docx.shared import Inches, Pt, RGBColor
from doc_builder import (
    create_base_document, add_header_banner, add_heading_1, add_heading_2,
    add_heading_3, add_paragraph, add_bullet, add_callout, add_styled_table, add_figure
)

def build_week2_document():
    doc = create_base_document()
    
    # Header Banner
    add_header_banner(
        doc,
        title="Exploratory Data Analysis (EDA) & Visualization Framework Design",
        subtitle="Universal Diagnostic Architecture, Statistical Exploration Protocols, and Visual Analytics Blueprint",
        task_badge="Week 2 Deliverable | Technical Framework Guide"
    )

    # 1. Introduction to EDA & Strategic Philosophy
    add_heading_1(doc, "1. Executive Introduction & Strategic Philosophy of EDA")
    
    add_paragraph(doc,
        "Exploratory Data Analysis (EDA) represents the bedrock of disciplined data science practice. First formalized by statistician John Tukey, EDA is not merely a collection of preliminary statistical summaries; it is an investigative mindset and iterative diagnostic philosophy. In enterprise data systems, jumping directly into predictive machine learning without exhaustive exploratory interrogation is the single leading cause of model failure, data leakage, and algorithmic bias in production environments.",
        bold_prefix="Conceptual Overview: "
    )
    
    add_paragraph(doc,
        "A robust EDA framework fulfills four foundational functions: (1) revealing underlying distributional geometries and latent structures, (2) diagnosing severe data quality defects including missingness mechanisms, anomalies, and schema corruptions, (3) validating or invalidating core business hypotheses prior to model training, and (4) guiding optimal feature engineering and selection transformations. This deliverable outlines an end-to-end, adaptable EDA and visual analytics framework designed to scale across diverse tabular and multi-relational datasets.",
        bold_prefix="Core Mission: "
    )

    add_callout(
        doc,
        "The primary purpose of an architectural EDA framework is to convert raw, unstructured observations into actionable statistical intelligence, de-risking downstream model development and accelerating time-to-value across the data science lifecycle.",
        title="Core Architectural Principle"
    )

    add_figure(doc, "figures/w2_fig1_eda_framework.png", "Comprehensive 6-Stage Universal Exploratory Data Analysis & Diagnostic Architecture", width=Inches(6.5))

    # 2. Comprehensive Taxonomy of Data Types
    add_heading_1(doc, "2. Comprehensive Taxonomy of Data Types & Exploration Protocols")
    add_paragraph(doc,
        "An effective exploratory strategy begins with classifying variables into their fundamental statistical taxonomies, as each archetype requires distinct transformation pipelines, distance metrics, and visual encodings.")

    data_types_headers = ["Data Category", "Archetype / Sub-Type", "Characteristics & Examples", "Analytical Pitfalls & Handling Protocols"]
    data_types_rows = [
        ["Numerical (Quantitative)", "Continuous (Ratio)", "Unbounded real numbers with true zero (e.g., MonthlyCharges, TotalCharges, BandwidthGB)", "Susceptible to extreme skewness; requires log/Box-Cox transform or RobustScaler; check for zero/negative anomalies."],
        ["Numerical (Quantitative)", "Discrete (Interval / Count)", "Non-negative integer counts (e.g., TechSupportTickets, DeviceCount, TenureMonths)", "High zero-inflation; assess Poisson/Negative Binomial distributions; evaluate threshold discretization."],
        ["Categorical (Qualitative)", "Nominal", "Unordered distinct categories (e.g., PaymentMethod, InternetService, ContractType)", "High-cardinality hazard causing sparse matrices; apply One-Hot Encoding for low cardinality or Target Encoding with smoothing."],
        ["Categorical (Qualitative)", "Ordinal", "Rank-ordered discrete levels (e.g., SatisfactionRating: Poor < Fair < Good < Excellent)", "Preserve inherent order via integer ordinal encoding (e.g., 1 to 4); do not treat as nominal to avoid losing relational order."],
        ["Temporal / Sequential", "Date / Timestamp", "Time of event generation (e.g., SignupDate, LastLoginTimestamp, InvoiceDue)", "Cannot enter ML models directly; must engineer rolling aggregates, recency, tenure velocity, and seasonal cyclic encodings."],
        ["Binary / Indicator", "Boolean / Dichotomous", "Two mutually exclusive states (e.g., SeniorCitizen [0/1], ChurnFlag [True/False])", "Evaluate severe class imbalance ratios; ensure boolean conversion to uint8/int to minimize memory consumption."]
    ]
    add_styled_table(doc, data_types_headers, data_types_rows, [Inches(1.3), Inches(1.4), Inches(2.2), Inches(1.8)])

    # 3. Methodical Data Exploration Techniques
    add_heading_1(doc, "3. Methodical Data Exploration Techniques")
    add_paragraph(doc,
        "The diagnostic methodology systematically scales from isolated variable distributions to complex multi-dimensional feature interactions, ensuring no statistical artifact escapes detection.")

    add_heading_2(doc, "3.1 Univariate Analysis: Structural & Distributional Auditing")
    add_bullet(doc, "Computation of location (mean, median, trimmed mean), dispersion (variance, standard deviation, interquartile range [IQR]), and shape metrics (Fisher-Pearson skewness coefficient and kurtosis). A skewness > |1.0| indicates heavy tails requiring power transformations.", bold_prefix="Moments of Distribution: ")
    add_bullet(doc, "Simultaneous inspection via Freedman-Diaconis rule histograms and Gaussian Kernel Density Estimation (KDE) to detect multimodality, zero-inflation clusters, or artificial value truncation.", bold_prefix="Continuous Density Mapping: ")
    add_bullet(doc, "Frequency tabulations, absolute counts, percentage shares, and Pareto distribution cumulative plots to detect dominant majority classes and extreme rare levels.", bold_prefix="Categorical Frequency Profiling: ")

    add_heading_2(doc, "3.2 Bivariate Analysis: Relational & Target-Conditioned Diagnostics")
    add_bullet(doc, "Pearson linear correlation coefficient (r) for linear continuous relationships; Spearman rank correlation (rho) for non-linear monotonic trends; and Kendall's tau for robust small-sample assessments.", bold_prefix="Continuous vs. Continuous: ")
    add_bullet(doc, "Comparative box plots, violin plots, and one-way Analysis of Variance (ANOVA) F-tests to assess whether target classes (e.g., Churned vs Retained) exhibit statistically significant distribution shifts.", bold_prefix="Continuous vs. Categorical: ")
    add_bullet(doc, "Two-way contingency cross-tabulations, normalized stacked bar charts, and Chi-Square Tests of Independence (χ²) with Cramer's V effect size to quantify association strength between categorical features and target labels.", bold_prefix="Categorical vs. Categorical: ")

    add_heading_2(doc, "3.3 Multivariate Analysis: Interactions & Manifold Discovery")
    add_bullet(doc, "Full pairwise correlation heatmaps with hierarchical dendrogram clustering to reveal feature collinearity clusters and prevent redundant information feeding into linear/tree models.", bold_prefix="Correlation Matrices & Collinearity: ")
    add_bullet(doc, "Principal Component Analysis (PCA) and t-Distributed Stochastic Neighbor Embedding (t-SNE) / UMAP projections to visualize high-dimensional customer separability in 2D/3D latent space.", bold_prefix="Dimensionality Reduction: ")
    add_bullet(doc, "Ternary and faceted sub-cohort conditioning (e.g., examining Monthly Charges vs Tenure conditioned simultaneously on Contract Type and Payment Method) to uncover Simpson's Paradox phenomena.", bold_prefix="Higher-Order Feature Interactions: ")

    add_figure(doc, "figures/w2_fig2_data_profiling.png", "Exploratory Data Analysis Diagnostic Suite: Distributional Patterns, Class Differences, and Correlation Matrix", width=Inches(6.5))

    # 4. Data Cleaning Protocols: Missingness & Anomaly Management
    add_heading_1(doc, "4. Data Cleaning Protocols: Missingness & Anomaly Management")
    add_paragraph(doc,
        "Data hygiene constitutes over 60% of real-world exploratory effort. Handling corruptions requires disciplined mathematical taxonomy rather than naive ad-hoc imputation.")

    add_heading_2(doc, "4.1 Missing Data Mechanism Taxonomy & Resolution Strategy")
    add_paragraph(doc,
        "Donald Rubin's missing data framework categorizes missingness into three distinct mechanisms:")
    add_bullet(doc, "Missingness is completely unrelated to observed or unobserved data (e.g., occasional network packet drop during transmission). Action: If < 3% of total records, simple listwise deletion or median/mode imputation is statistically benign.", bold_prefix="Missing Completely at Random (MCAR): ")
    add_bullet(doc, "Missingness probability depends systematically on other observed variables (e.g., senior citizens omitting online streaming logs). Action: Use advanced multi-variable imputation such as K-Nearest Neighbors (KNNImputer) or Iterative Multivariate Imputation (MICE / IterativeImputer).", bold_prefix="Missing at Random (MAR): ")
    add_bullet(doc, "Missingness is directly related to the unobserved value itself (e.g., customers with highest churn sentiment refusing to answer exit surveys). Action: Do not impute blindly; create an explicit binary missingness indicator column (`feature_is_missing`) to preserve predictive signal.", bold_prefix="Missing Not at Random (MNAR): ")

    add_heading_2(doc, "4.2 Outlier Detection & Treatment Decision Architecture")
    add_paragraph(doc,
        "Outliers should never be mechanically purged, as extreme values often house the most vital business signals (such as fraudulent transaction spikes or premium VIP subscriber accounts).")
    add_bullet(doc, "Effective for normally distributed metrics. Observations exceeding Z = ±3.0 standard deviations are flagged for inspection.", bold_prefix="Parametric Z-Score Method: ")
    add_bullet(doc, "Robust to heavy tails. Data points falling beyond [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR] are categorized as mild outliers; points beyond 3.0 * IQR are extreme outliers.", bold_prefix="Non-Parametric Interquartile Range (IQR): ")
    add_bullet(doc, "Unsupervised anomaly detection algorithm that constructs random tree isolation splits; points requiring few splits are flagged as multi-dimensional anomalies.", bold_prefix="Algorithmic Isolation Forest: ")
    add_bullet(doc, "Three-tiered treatment protocol: (1) Data entry error -> Correct or drop; (2) Genuine extreme skewness -> Winsorization (capping at 1st and 99th percentiles) or Log1p transformation; (3) Distinct subpopulation -> Segment into dedicated modeling cohort.", bold_prefix="Treatment Protocol: ")

    add_figure(doc, "figures/w2_fig3_cleaning_flow.png", "Systematic Decision Tree Workflow for Missing Value Imputation and Outlier Treatment", width=Inches(6.4))

    # 5. Visualization Strategies & Chart Selection Matrix
    add_heading_1(doc, "5. Visualization Strategies & Visual Grammar Framework")
    add_paragraph(doc,
        "Visual storytelling is governed by Edward Tufte's principles of graphical excellence: maximizing the data-ink ratio, avoiding visual clutter (chart-junk), and utilizing perceptually uniform color scales.")

    viz_headers = ["Exploratory Objective", "Recommended Chart Type", "Visual Encodings (X, Y, Color, Size)", "Design Justification & Interpretation Guide"]
    viz_rows = [
        ["Single Continuous Distribution", "KDE Histogram + Boxplot Margin", "X: Continuous Value, Y: Density / Count", "Reveals multi-modality, skewness, outliers, and boundary truncations simultaneously."],
        ["Single Categorical Frequency", "Horizontal Sorted Bar Chart", "Y: Category Name, X: Frequency Count / %", "Facilitates rapid reading of lengthy category labels without awkward text rotation."],
        ["Two Continuous Variables", "Scatter Plot + Lowess Trendline", "X: Feature 1, Y: Feature 2, Color: Target", "Displays bivariate non-linear correlation, heteroscedasticity, and class cluster clustering."],
        ["Categorical vs. Target Rate", "Stacked 100% Normalized Bar", "X: Category Level, Y: Ratio, Color: Target", "Normalizes sample size disparities across categories to directly compare relative risk rates."],
        ["Full Feature Pairwise Matrix", "Annotated Correlation Heatmap", "X & Y: Feature Labels, Color: Diverging Map", "Instantly highlights severe collinearity (r > 0.80) requiring feature pruning or ridge penalties."],
        ["Multi-cohort Distribution Shift", "Violin / Ridgeline Plots", "X: Feature Value, Y: Cohort Group, Color: Group", "Provides richer density visualization than boxplots alone when comparing multiple segments."]
    ]
    add_styled_table(doc, viz_headers, viz_rows, [Inches(1.4), Inches(1.5), Inches(1.8), Inches(2.0)])

    # 6. Tooling & Python Ecosystem Specialization
    add_heading_1(doc, "6. Python Library Ecosystem & Functional Specialization")
    add_paragraph(doc,
        "A scalable EDA framework orchestrates a multi-tiered Python toolchain, leveraging each library for its specific analytical strength:")

    tool_headers = ["Library Name", "Primary Specialty", "Key Functions / Modules Employed", "Strategic Role in EDA Workflow"]
    tool_rows = [
        ["Pandas", "Tabular Ingestion & Wrangling", "`.info()`, `.describe()`, `.groupby()`, `.pivot_table()`, `.query()`", "Serves as the central data manipulation engine for aggregations, slicing, and schema audits."],
        ["Matplotlib", "Foundational Visual Canvas", "`plt.subplots()`, `ax.text()`, `patches`, `plt.savefig()`", "Low-level fine-grained formatting, custom figure layouts, and publication-ready static exports."],
        ["Seaborn", "Statistical Graphics", "`sns.kdeplot()`, `sns.boxplot()`, `sns.heatmap()`, `sns.pairplot()`", "High-level statistical abstractions with automated hue grouping and aesthetic default palettes."],
        ["Plotly", "Interactive Drill-down Visuals", "`px.scatter()`, `px.sunburst()`, `dcc.Graph()`, `go.Figure()`", "Browser-based interactive zooming, tooltips, and dynamic filtering for executive presentations."],
        ["Missingno", "Missing Data Visualization", "`msno.matrix()`, `msno.bar()`, `msno.heatmap()`, `msno.dendrogram()`", "Visual pattern mapping of missingness mechanisms and inter-feature missingness correlations."],
        ["Statsmodels", "Rigorous Statistical Tests", "`sm.stats.diagnostic`, `sm.OLS()`, `sm.stats.anova_lm()`", "Hypothesis testing, VIF collinearity calculation, normality tests, and p-value validation."],
        ["YData-Profiling", "Automated Profiling Reports", "`ProfileReport(df, minimal=True).to_file()`", "Rapid initial baseline auditing producing 100+ automated summary metrics in HTML format."]
    ]
    add_styled_table(doc, tool_headers, tool_rows, [Inches(1.3), Inches(1.5), Inches(2.1), Inches(1.8)])

    # 7. Documentation & Reporting Architecture
    add_heading_1(doc, "7. Reporting Architecture & Stakeholder Communication Plan")
    add_paragraph(doc,
        "The culmination of exploratory work is the structured dissemination of insights. The framework establishes a 4-tier documentation hierarchy:")
    add_bullet(doc, "Automated HTML output containing complete distributions, zero-counts, correlations, and memory warnings generated during Phase 1.", bold_prefix="Tier 1: Technical Data Audit Log: ")
    add_bullet(doc, "Executable Jupyter notebooks containing clean, commented Python code following PEP-8 standards, organized into logical markdown sections with interactive widgets.", bold_prefix="Tier 2: Reproducible Analytical Notebook: ")
    add_bullet(doc, "A standalone data dictionary specifying each variable's business definition, historical min/max, imputation methodology, and downstream usage constraints.", bold_prefix="Tier 3: Feature Catalog & Data Dictionary: ")
    add_bullet(doc, "A non-technical slide deck and executive summary translating statistical findings into business language, highlighting key customer churn risk factors and projected financial impacts.", bold_prefix="Tier 4: Executive Insights Brief: ")

    add_callout(
        doc,
        "By systematizing the EDA process into reproducible statistical phases, data science teams eliminate blind spots, protect model integrity against covariate shift, and establish an unassailable foundation for predictive modeling.",
        title="Framework Conclusion"
    )

    # Save document
    out_path = "deliverables/Week_2_EDA_and_Visualization_Framework_Design.docx"
    doc.save(out_path)
    print(f"Successfully generated: {out_path}")

if __name__ == '__main__':
    build_week2_document()

# Olist Retail Operations Master Dashboard

This project is being developed as part of our core analytics initiative to optimize e-commerce operations.

## 🎯 Objectives
* Analyze Brazilian e-commerce retail sales performance.
* Identify top-performing product categories and regional sales concentrations.
* Track revenue and order trends over time.
* Build an interactive, centralized Power BI dashboard for executive decision-making.
* Ensure data integrity through robust Portuguese-to-English category translation and relational modeling.

## 🛠️ Technologies Used
| Technology | Purpose |
| :--- | :--- |
| **SQL Server (SSMS)** | Database hosting, bulk data import, and relational mapping |
| **SQL** | Data cleaning, deduping, and query extraction |
| **Power BI** | Data modeling, DAX measures, and interactive visualizations |
| **Power Query** | Automated null-value filtering and data transformation |
| **Git & GitHub** | Version control, branching strategies, and team collaboration |

## 📁 Project Structure
```text
RETAIL-SALES-INVENTORY-ANALYTICS-DASHBOARD/
├── .venv/
├── .gitignore
├── pyvenv.cfg
├── Dashboard Architecture_Week 3/ PowerBI/
│   └── Olist_Retail_Operations_Master_Dashboard.pbix
├── Data Collection & Foundation_Week 1/
│   ├── .ipynb_checkpoints/
│   │   └── 01_load_data-checkpoint.ipynb
│   ├── Brazilian E-Commerce Public Dataset by Olist/
│   ├── venv/
│   └── 01_load_data.ipynb
├── README.md
├── Insights & Final Delivery_Week 4/
│   └── .gitkeep
├── Presentation/
└── SQL Development & Metrics_Week 2/
    ├── 01_Schema_Setup.sql
    ├── 02_Data_Ingestion.sql
    ├── 03_audit_report.md
    ├── 03_Master_Views.sql
    └── README_Team_Instructions.md

📅 Project Timeline & Task Distribution
Week 1: Foundation & Database Setup
      - Acquired Olist Brazilian E-Commerce dataset.
      - Configured local SQL Server environment.
      - Performed bulk import of raw flat files into the relational database structure.
      - Analyzed underlying schema and table interactions.

Week 2: Version Control & Data Profiling
      - Ran initial SQL queries to validate data and identify translation/duplication inconsistencies.
      - Established project version control using Git and GitHub.
      - Defined branching strategy (e.g., dev-data-cleaning) and set up collaborative repository for the team.

Week 3: Power BI Data Modeling & Master Visuals
     - Resolved critical memory and duplicate blank row errors in the translation table via SSMS and Power Query.
     - Established clean One-to-Many relationships and semantic models in Power BI.
     - Built core DAX measures: Total Revenue, Total Orders, and Average Order Value (AOV).
     - Designed the Page 1 Executive Overview with a grouped, layered Master Filter Panel (synced across all pages).
     - Delegated specific visual builds to team members (Kasak, Ahmad, Swetha).

Week 4: Final Assembly & Insights (Upcoming)
     - Integrate delegated charts (Time-series, Category Bar, Geospatial Heatmap) into the master layout.
     - Implement advanced UX features like a master show/hide slicer panel using bookmarks.
     - Insight generation and final executive documentation.
     - Project submission and stakeholder presentation.

📈 Expected Insights
     - Temporal Trends: 12-month revenue trajectory and seasonality.
     - Category Performance: Identification of top-selling English product categories.
     - Geospatial Concentration: Heatmap of regional sales density across Brazilian states.
     - Executive KPIs: Global visibility into overall Revenue, Volume, and AOV.
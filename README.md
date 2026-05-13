**Title: Retail-Sales-Inventory-Analytics**

**Project Description: Omnichannel Retail Sales and Inventory Analytics**

**Executive Problem Statement**

As multi-location retailers scale, they often struggle with fragmented data across multiple sales channels, leading to systemic bottlenecks. The lack of centralized data prevents businesses from effectively tracking overall sales trends, forecasting inventory needs, and identifying top-performing products. This project addresses these challenges by developing an interactive Business Intelligence (BI) dashboard that provides a unified view of physical and digital retail operations.

**Core Objectives**

**Data Unification:** Process raw sales transactions to create a single source of truth for both online and offline data.

**Operational Intelligence:** Identify seasonal revenue patterns and peak purchasing periods to optimize inventory turnover.

**Performance Metrics:** Calculate and track essential Key Performance Indicators (KPIs) such as Total Sales, Average Revenue per Order, and year-over-year (YoY) growth.

**Actionable Insights:** Enable data-driven decision-making for Store Managers, Inventory Planners, and Regional Sales Directors through dynamic filtering by timeframe, location, and product category.

**Technical Architecture**

The project utilizes a professional-grade technology stack to ensure scalability and efficiency:

**Data Preparation:** Leveraging Microsoft Excel for initial exploration and Python (Pandas) for automated, large-scale cleaning and manipulation.

**Database Management:** Utilizing SQL (MySQL or PostgreSQL) for efficient data aggregation and complex metric extraction using advanced joins and window functions.

**Visualization:** Developing interactive dashboards in Power BI or Tableau featuring time-series trends, product performance bar charts, and peak-hour heatmaps.




**Getting Started**

**Project Roadmap & Sprint Progress**

This project was developed over a strict four-week engineering sprint as part of the Infotact Technical Internship Program:

**Week 1: Data Collection & Infrastructure –** Initiated GitHub repository, established environment, and performed initial data cleaning (handling NULLs, duplicates, and standardizing formats).
**Week 2: Relational Database Design –** Migrated cleaned data to a SQL database. Developed complex queries for metric extraction, including revenue aggregations and geographic distribution.
**Week 3: Dashboard Architecture –** Connected Power BI/Tableau to the SQL database. Created interactive visualizations, heatmaps, and dynamic filters for drill-down analysis.
**Week 4: Insights & Reporting –** Analyzed visualizations to extract strategic findings and finalized documentation.


**Installation and Setup**

To replicate this analytics pipeline, follow the steps below:

**1. Prerequisites**
Ensure you have the following tools installed:

**Python 3.x** (with Pandas library)
**SQL Database** (MySQL or PostgreSQL)
**Business Intelligence Tool** (Power BI Desktop or Tableau)
**Git** for version control

**2. Environment Setup**
Clone the repository and set up your local environment:
git clone [your-repository-link]
cd omnichannel-retail-analytics
3. Data Cleaning (Python/Pandas)
Navigate to the notebooks/ directory and run the cleaning script to process raw CSV logs:
Standardizes date/time formats.
Validates data types.
Handles missing values via mean/median imputation where applicable.1
4. Database Configuration (SQL)
Import the cleaned dataset into your SQL environment. Execute the scripts in the sql/ folder to build the necessary aggregations:
schema_setup.sql: Defines table structures.
analytical_queries.sql: Contains the logic for KPI calculations like YoY growth and peak purchasing periods.1
5. Dashboard Connection
Open Power BI or Tableau.
Connect to your local SQL database.
Load the pre-configured .pbix or .twb file from the dashboards/ directory to view the interactive visualizations.1
Mandatory Protocol Note: Per project requirements, this repository maintains a granular commit history (3-5 commits per day) to reflect the iterative development lifecycle.


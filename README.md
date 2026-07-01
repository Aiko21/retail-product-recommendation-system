# 🛒 Retail Product Recommendation System

A machine learning-based recommendation system designed to optimize cross-selling opportunities in online retail businesses.

---

# 📌 Project Overview

Online retail businesses often offer thousands of products. Customers may struggle to discover relevant products, resulting in missed sales opportunities and lower customer engagement.

This project develops an Item-Based Collaborative Filtering recommendation engine to provide personalized product recommendations and improve business performance.

---

# 🎯 Business Problem

The company currently does not provide personalized product recommendations.

Consequences:

- Lost cross-selling opportunities.
- Lower Average Order Value (AOV).
- Reduced customer engagement.
- Potential revenue loss.

---

# 👥 Stakeholders

- Marketing Team
- Product Team
- Sales Team
- Management
- Customers

---

# 📈 Business KPIs

- Average Order Value (AOV)
- Revenue
- Cross-Selling Revenue
- Customer Engagement
- Recommendation Coverage

---

# 🧠 Machine Learning Framing

This problem is framed as a:

## Recommendation System

Approach:

- Baseline Model:
  - Popularity-Based Recommender

- Advanced Model:
  - Item-Based Collaborative Filtering

---

# 📂 Dataset

Dataset: UCI Online Retail Dataset

Characteristics:

- 541,909 transactions
- 4,338 customers
- 4,070 products
- 38 countries

---

# 🔬 Project Workflow

1. Business Understanding
2. Dataset Audit
3. Data Understanding
4. Data Cleaning
5. Exploratory Data Analysis
6. Feature Engineering
7. Baseline Modeling
8. Advanced Modeling
9. Hyperparameter Tuning
10. Recommendation Explainability
11. Business Impact Analysis
12. Model Export
13. Streamlit Deployment
14. Docker Deployment

---

# 📊 Exploratory Findings

- Missing CustomerID: 24.93%
- Duplicate Rows: 5,225
- Cancelled Transactions: 8,872
- Final Clean Dataset: 392,692 rows

---

# ⚙️ Feature Engineering

Features created:

- Customer Product Interaction Matrix
- Interaction Strength
- Customer Activity
- Product Popularity

---

# 🤖 Models

## Baseline

Popularity-Based Recommender

Coverage:

0.27%

Diversity:

100%

---

## Advanced Model

Item-Based Collaborative Filtering

Coverage:

100%

Diversity:

90.91%

Best Hyperparameter:

K = 5

Precision@5:

0.0193

Recall@5:

0.0141

MAP@5:

0.0107

---

# 💰 Business Impact

Current Revenue:

£8,887,208.89

Additional Revenue:

£44,436.04

Cross-Selling Revenue:

£266,616.27

Projected Revenue:

£8,931,644.93

Estimated ROI:

6121%

---

# 🖥️ Streamlit Dashboard

Features:

- Product Recommendation
- Similarity Visualization
- Recommendation Download
- Recommendation Explainability
- Business Insights

---

# 🐳 Docker Deployment

Build image:

```bash
docker build -f docker/Dockerfile -t retail-recommendation .
```

Run container:

```bash
docker run -p 8501:8501 retail-recommendation
```

---

# 📁 Project Structure

```text
├── app
├── assets
├── config
├── data
├── docker
├── models
├── notebooks
├── src
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Docker
- Matplotlib

---

# 👨‍💻 Author

Soko Diraharja

---

# 📚 References

1. Sarwar et al. (2001). Item-Based Collaborative Filtering Recommendation Algorithms.
2. UCI Machine Learning Repository.
3. Ricci et al. Recommender Systems Handbook.

---

# Notes
Due to GitHub file size limitations, the item similarity matrix is not included in the repository.

Please regenerate it by executing:

07_model_advanced.ipynb

or

## 🚀 Live Demo

Streamlit Application:

http://52.2.29.141:8501

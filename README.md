# Waridi ML – Property Intelligence & Conversational AI

**Project:** Waridi Real Estate Super App  
**Service:** Machine Learning & Conversational Intelligence  
**Technology:** Python, FastAPI, PostgreSQL, Scikit-learn, CatBoost and OpenAI API  
**Status:** Initial Development  
**Version:** 1.0.0

---

## 1. Project Overview

Waridi ML is the machine learning and artificial intelligence service powering the intelligence capabilities of the Waridi Real Estate Super App.

The platform is designed to transform Waridi's property data into actionable insights through machine learning, predictive analytics, intelligent property recommendations and natural language conversations.

Users will be able to interact with Waridi using simple conversational statements and questions instead of having to understand complex search filters.

For example:

- "I'm looking for a two-bedroom apartment in Kilimani."
- "What can I get with a budget of KSh 5 million?"
- "How much does a three-bedroom house cost in Ruiru?"
- "Which areas near Westlands are more affordable?"
- "Is Ruaka a good location for property investment?"
- "Show me properties with good rental income potential."
- "Compare property prices in Kilimani and Kileleshwa."

The system will analyse the user's intent, retrieve relevant property information, invoke appropriate machine learning models and generate understandable responses.

### Primary Objective

Build a property intelligence system powered by Waridi's own property data, with the ability to understand natural language, predict property prices, analyse locations, recommend properties and provide investment insights.

---

## 2. Core Capabilities

### 2.1 Conversational Property Intelligence

Provide a conversational interface that allows users to interact naturally with the Waridi platform.

Capabilities:

- Understand natural language questions and statements.
- Identify property search requirements.
- Extract location, budget, property type and other preferences.
- Maintain conversation context.
- Handle incomplete questions by asking relevant follow-up questions.
- Retrieve matching properties from PostgreSQL.
- Explain property recommendations and market insights.
- Convert ML predictions into understandable responses.

Example conversation:

**User:** I'm looking for a house around Kilimani.

**Waridi AI:** Are you looking to rent or buy?

**User:** Rent, preferably a two-bedroom.

**Waridi AI:** Great! What's your approximate monthly budget?

**User:** Around KSh 80,000.

**Waridi AI:** I'll look for two-bedroom rental properties around Kilimani within your budget.

### 2.2 Property Price Prediction

Develop machine learning models to estimate property prices using historical property data.

Potential features:

- Location.
- Property type.
- Number of bedrooms.
- Number of bathrooms.
- Property size.
- Land size.
- Property amenities.
- Listing type.
- Other relevant property characteristics.

Algorithm:

- CatBoost Regression.
- Random Forest Regression.
- Gradient Boosting Regression.
- Other algorithms where experimentation demonstrates an improvement.

Evaluation metrics:

- Mean Absolute Error (MAE).
- Root Mean Squared Error (RMSE).
- R-squared (R²).

Sale and rental prices must be modelled separately, with consistent currency and pricing periods.

### 2.3 Location Intelligence

Analyse geographical and property market patterns to identify attractive locations.

Capabilities:

- Location-based property analysis.
- Average and median property prices.
- Price per square metre.
- Rental price comparisons.
- Location clustering.
- Nearby location discovery.
- Comparison of property markets across locations.

Potential algorithms:

- K-Means Clustering.
- DBSCAN.
- HDBSCAN.
- Geographic distance-based analysis.

### 2.4 Property Recommendations

Develop an intelligent recommendation engine that identifies relevant properties based on user preferences.

Initial recommendation approach:

- Content-based filtering.
- K-Nearest Neighbours.
- Similarity scoring.
- Weighted property ranking.

Future improvements:

- User behaviour analysis.
- Property views.
- Saved properties.
- Enquiries.
- Shortlists.
- Completed transactions.
- Personalised recommendations.

### 2.5 Investment Intelligence

Provide property investment insights using available property and rental data.

Initial capabilities:

- Gross rental yield.
- Estimated net rental yield.
- Annual rental income.
- Property price comparisons.
- Investment opportunity comparisons.

Formula:

Gross Rental Yield:

Annual Rental Income / Property Purchase Price × 100

Net Rental Yield:

(Annual Rental Income − Annual Operating Expenses) / Property Purchase Price × 100

Future capabilities may include rental price prediction, vacancy estimation and investment forecasting when sufficient historical data is available.

---

## 3. System Architecture

The system will operate as an independent Python service integrated with the existing Waridi backend.

### High-Level Architecture

```text
                  WARIDI USERS
                       |
                       |
              WARIDI MOBILE / WEB
                       |
                       |
               NODE.JS BACKEND
                       |
             REST API / INTERNAL API
                       |
                       |
               WARIDI ML SERVICE
                   FASTAPI
                       |
          +------------+-------------+
          |            |             |
          |            |             |
     AI AGENT      ML MODELS     DATA SERVICES
          |            |             |
          |            |             |
     LLM API       CATBOOST       POSTGRESQL
          |        CLUSTERING          |
          |        RECOMMENDER         |
          |        INVESTMENT          |
          |            |               |
          +------------+---------------+
                       |
                INTELLIGENT RESPONSE
                       |
                 NODE.JS BACKEND
                       |
                  WARIDI USERS
```

### Component Responsibilities

| Component | Responsibility |
|---|---|
| Node.js Backend | Main application backend, authentication, users and business operations |
| FastAPI | Exposes ML and AI capabilities |
| Conversational Agent | Understands natural language and manages conversations |
| LLM API | Language understanding and response generation |
| CatBoost | Property price prediction |
| Scikit-learn | Clustering, similarity and recommendation experiments |
| PostgreSQL | Property and location data source |
| Pandas | Data extraction, processing and analysis |
| JupyterLab | Data exploration and experimentation |

**Important:** The LLM is responsible for understanding and orchestrating conversations. The machine learning models are responsible for predictions and analytical tasks. Property availability and prices must come from Waridi's actual database, not be invented by the language model.

---

## 4. Technology Stack

### Programming Language

- Python 3.11 / 3.12

### Machine Learning

- Pandas
- NumPy
- Scikit-learn
- CatBoost

### Conversational AI

- OpenAI API
- Python-based agent and tool orchestration.

### Backend API

- FastAPI
- Uvicorn
- Pydantic

### Database

- PostgreSQL
- SQLAlchemy
- Psycopg2
- PostGIS (optional, recommended for geographical queries).

### Experimentation and Visualisation

- JupyterLab
- Matplotlib
- Seaborn

### Model Management

- Joblib
- MLflow (future integration).

### Testing

- Pytest

---

## 5. Project Structure

```text
waridi-ml/
│
├── notebooks/
│   ├── 01_database_exploration.ipynb
│   ├── 02_property_analysis.ipynb
│   ├── 03_price_prediction.ipynb
│   └── 04_model_evaluation.ipynb
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── price_prediction/
│   ├── location_clustering/
│   ├── recommendations/
│   └── investment/
│
├── src/
│   │
│   ├── api/
│   │   └── main.py
│   │
│   ├── agent/
│   │   ├── conversation.py
│   │   ├── tools.py
│   │   └── prompts.py
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   ├── data/
│   │   ├── extraction.py
│   │   ├── preprocessing.py
│   │   └── validation.py
│   │
│   ├── features/
│   │   └── engineering.py
│   │
│   ├── training/
│   │   ├── train_price.py
│   │   ├── train_location.py
│   │   └── train_recommendations.py
│   │
│   ├── evaluation/
│   │   └── evaluate.py
│   │
│   └── services/
│       └── property_service.py
│
├── scripts/
│   └── inspect_database.py
│
├── tests/
│   ├── __init__.py
│   └── test_database.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### Directory Responsibilities

**notebooks/**

Used for exploratory data analysis, feature experiments, model prototyping and visualisation.

**data/**

Stores extracted and processed datasets. Raw production data must be protected and excluded from Git.

**models/**

Stores trained machine learning models and associated metadata.

**src/agent/**

Contains the conversational intelligence, system instructions, context handling and tools available to the AI agent.

**src/database/**

Contains PostgreSQL connectivity and database configuration.

**src/data/**

Responsible for extracting, cleaning and validating property data.

**src/features/**

Contains reusable feature engineering logic.

**src/training/**

Contains machine learning model training pipelines.

**src/evaluation/**

Evaluates model performance and determines whether a trained model meets deployment criteria.

**src/services/**

Contains reusable property intelligence and business logic consumed by the API and agent.

**src/api/**

Contains FastAPI application routes and API configuration.

**tests/**

Contains automated tests for the data pipeline, ML services and API.

---

## 6. Environment Setup

### Prerequisites

Install:

- Python 3.11 or later.
- PostgreSQL access.
- Visual Studio Code or another Python IDE.
- Git.
- JupyterLab.

Docker is optional during initial development.

### Clone the Repository

```bash
git clone <WARIDI_ML_REPOSITORY_URL>
cd waridi-ml
```

### Create a Virtual Environment

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Register Jupyter Kernel

```bash
python -m ipykernel install --user \
  --name waridi-ml \
  --display-name "Waridi ML Python"
```

### Start JupyterLab

```bash
jupyter lab
```

Select the `Waridi ML Python` kernel when creating notebooks.

---

## 7. Environment Variables

Create a `.env` file in the project root.

```env
# PostgreSQL
DB_HOST=localhost
DB_PORT=5432
DB_NAME=waridi
DB_USER=waridi_ml_readonly
DB_PASSWORD=your_database_password

# API
API_HOST=0.0.0.0
API_PORT=8001

# Model storage
MODEL_DIR=./models

# Conversational AI
OPENAI_API_KEY=your_openai_api_key
```

The database configuration must be updated to match the actual Waridi PostgreSQL environment.

Use a dedicated read-only database account for ML data extraction.

Never commit `.env` or expose database credentials and API keys.

---

## 8. Database Integration

PostgreSQL is the primary source of truth for Waridi property information.

The ML service will initially connect to the existing database through SQLAlchemy.

### Data Discovery

Before implementing extraction queries, inspect the existing database schema.

List available tables:

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE'
ORDER BY table_name;
```

Inspect property and location columns:

```sql
SELECT
    table_name,
    column_name,
    data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND (
      table_name ILIKE '%propert%'
      OR table_name ILIKE '%location%'
      OR table_name ILIKE '%amenit%'
  )
ORDER BY table_name, ordinal_position;
```

### Expected Data Categories

The actual table and column names will be established from the existing Sequelize models and PostgreSQL schema.

| Data Category | Potential Information |
|---|---|
| Property | Price, bedrooms, bathrooms, size, property type |
| Location | County, town, neighbourhood, coordinates |
| Listing | Sale/rent, listing status, dates |
| Amenities | Parking, swimming pool, security, furnishing |
| Images | Property images and descriptions |
| Rental | Monthly rent, rental terms, historical rental prices |
| User Behaviour | Views, enquiries, saved properties and transactions |

### Data Quality Requirements

The extraction and validation pipeline must account for:

- Missing values.
- Duplicate listings.
- Incorrect or inconsistent property prices.
- Currency differences.
- Sale and rental listing separation.
- Different rental pricing periods.
- Invalid coordinates.
- Outliers.
- Inactive or unavailable properties.
- Inconsistent location names.

The system must not assume that an asking price is equivalent to a completed transaction price.

---

## 9. Machine Learning Development Workflow

### Phase 1: Data Exploration

Use JupyterLab to:

1. Connect to PostgreSQL.
2. Inspect the property schema.
3. Extract property records.
4. Analyse missing values.
5. Examine price distributions.
6. Compare prices across locations.
7. Identify data inconsistencies.
8. Determine which features are suitable for training.

### Phase 2: Data Preparation

Implement reusable preprocessing logic in `src/data/`.

Tasks include:

- Data cleaning.
- Duplicate detection.
- Currency normalisation.
- Categorical feature standardisation.
- Missing value handling.
- Outlier investigation.
- Sale/rental separation.
- Feature preparation.

### Phase 3: Feature Engineering

Create meaningful features such as:

- Price per square metre.
- Location-based price indicators.
- Bedroom and bathroom ratios.
- Property size categories.
- Property type encoding.
- Rental yield indicators.
- Geographical distance features.

Features must be calculated using information that would actually be available at prediction time to avoid data leakage.

### Phase 4: Model Training

Train and evaluate the initial models.

| Model | Algorithm | Objective |
|---|---|---|
| Price Prediction | CatBoost Regressor | Estimate property prices |
| Location Analysis | K-Means / DBSCAN | Identify location clusters |
| Property Recommendations | Content-based ranking / KNN | Recommend similar properties |
| Investment Analysis | Financial calculations | Estimate investment returns |

### Phase 5: Model Evaluation

Price prediction:

- MAE.
- RMSE.
- R².
- Performance by location.
- Performance by property type.
- Performance by sale/rental category.

Recommendation engine:

- Precision@K.
- Recall@K.
- NDCG@K when suitable relevance labels are available.

Location clustering:

- Silhouette score where applicable.
- Cluster distribution.
- Geographic coherence.
- Business interpretability.

Models must be compared against simple baselines before deployment.

### Phase 6: Model Deployment

Save trained models using Joblib or their appropriate native serialization format.

Include model metadata:

- Model version.
- Training date.
- Training dataset size.
- Feature definitions.
- Evaluation metrics.
- Model artifact location.

A new model should only replace the currently deployed model after passing quality checks.

---

## 10. Conversational AI Architecture

The conversational agent is responsible for translating natural language into property intelligence operations.

### Conversation Processing

The agent should:

1. Receive a user message.
2. Understand the user's intent.
3. Extract relevant entities and preferences.
4. Retrieve relevant conversation context.
5. Determine which tool or model to invoke.
6. Execute the required operation.
7. Interpret the results.
8. Generate a natural language response.

### Example Intents

| User Statement | Intent |
|---|---|
| Find me a two-bedroom in Kilimani | Property Search |
| What is the average price in Ruaka? | Price Analysis |
| Can I afford a house with KSh 5M? | Budget-Based Search |
| Compare Kilimani and Kileleshwa | Location Comparison |
| Is this property a good investment? | Investment Analysis |
| Show me similar properties | Property Recommendation |

### Agent Tools

The agent will eventually have access to controlled functions such as:

- `search_properties()`
- `predict_property_price()`
- `get_location_statistics()`
- `compare_locations()`
- `recommend_properties()`
- `calculate_rental_yield()`
- `analyse_investment()`

The LLM should call these tools instead of independently inventing property prices, locations or availability.

Conversation context should be maintained using conversation/session identifiers, with appropriate privacy and retention controls.

---

## 11. FastAPI Endpoints

The Python service will expose internal APIs consumed by the Waridi Node.js backend.

Planned endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Service information |
| GET | `/health` | Health check |
| POST | `/agent/chat` | Conversational property intelligence |
| POST | `/predict-price` | Predict property price |
| POST | `/recommend-properties` | Recommend properties |
| GET | `/locations/clusters` | Retrieve location cluster information |
| POST | `/compare-locations` | Compare locations |
| POST | `/investment-analysis` | Analyse investment potential |

API endpoints will be implemented incrementally as the underlying services become available.

### Start the API

```bash
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8001
```

### API Documentation

Once running:

```text
http://localhost:8001/docs
```

---

## 12. Integration with Waridi Node.js Backend

The existing Waridi Node.js backend remains the primary application backend.

The Python ML service will operate independently and communicate through internal HTTP requests.

Example integration:

```text
Waridi Frontend
      |
      v
Node.js Backend
      |
      v
Python FastAPI
      |
      +---- Conversational Agent
      |
      +---- Property Prediction
      |
      +---- Property Recommendations
      |
      +---- Location Intelligence
      |
      +---- PostgreSQL
```

The Node.js backend should:

- Authenticate users.
- Validate requests.
- Manage conversation identifiers.
- Forward permitted requests to the Python service.
- Return the AI response to the frontend.
- Enforce access control and rate limits.

The Python service should not bypass application authorisation when returning user-specific or restricted property information.

---

## 13. Testing

Run automated tests:

```bash
pytest
```

Test categories:

- Database connectivity.
- Data extraction.
- Data validation.
- Feature engineering.
- Model predictions.
- Recommendation ranking.
- API endpoints.
- Conversational agent tool execution.

Include tests for missing data, invalid inputs, unusual property values and failed database connections.

---

## 14. Model Monitoring and Retraining

Model quality should be reviewed regularly.

Monitoring should include:

- Prediction accuracy.
- Changes in property price distributions.
- Data quality degradation.
- Feature distribution drift.
- Recommendation relevance.
- Model execution errors.
- Prediction latency.

Retraining should be based on data availability and model quality rather than automatically replacing models on a fixed schedule.

Every training run should produce an evaluation report.

A model should only be promoted when it meets the agreed evaluation criteria.

---

## 15. Development Roadmap

| Phase | Deliverable | Status |
|---|---|---|
| 1 | Python environment and project bootstrap | Initial setup |
| 2 | PostgreSQL schema discovery | Pending |
| 3 | Property data extraction pipeline | Pending |
| 4 | Data exploration and quality analysis | Pending |
| 5 | Property price prediction | Pending |
| 6 | Location intelligence and clustering | Pending |
| 7 | Property recommendation engine | Pending |
| 8 | Investment analysis | Pending |
| 9 | Conversational AI agent | Pending |
| 10 | FastAPI integration | Pending |
| 11 | Node.js backend integration | Pending |
| 12 | Testing and model evaluation | Pending |
| 13 | Production deployment and monitoring | Pending |

---

## 16. Initial Development Priorities

The initial development should focus on establishing a reliable data foundation.

Recommended order:

1. Bootstrap the Python environment.
2. Connect to Waridi PostgreSQL.
3. Inspect existing Sequelize models and database tables.
4. Establish the property data extraction pipeline.
5. Explore the available property data using JupyterLab.
6. Identify suitable features for machine learning.
7. Build the first property price prediction model.
8. Implement location analysis and recommendations.
9. Develop the conversational agent.
10. Integrate the Python service with Waridi Node.js.

The first milestone is to establish a reliable connection to the actual Waridi database and understand the quality and structure of the available property records.

---

## 17. Security Considerations

- Use dedicated database credentials.
- Apply least-privilege database permissions.
- Store secrets in environment variables or a secrets manager.
- Do not expose the ML service publicly without authentication.
- Restrict internal service communication.
- Validate all incoming API requests.
- Apply rate limiting to AI endpoints.
- Avoid logging passwords, API keys or sensitive conversation data.
- Do not expose private user or property information through model responses.
- Validate LLM tool calls against server-side permissions.

---

## 18. Future Enhancements

Potential future capabilities include:

- Property price trend forecasting.
- Rental demand forecasting.
- Automated property valuation.
- Personalised property discovery.
- Natural language property comparisons.
- Geographic market heatmaps.
- Neighbourhood insights.
- Investment opportunity scoring.
- Property description intelligence.
- Multilingual conversations.
- Voice-based property search.
- Automated market reports.

These capabilities will be prioritised based on data availability, user demand and measurable model performance.

---

## 19. Project Principles

The Waridi ML project follows these principles:

1. **Data-driven:** Predictions must be based on actual Waridi data.
2. **Conversational:** Users should interact naturally without needing technical search syntax.
3. **Explainable:** AI-generated recommendations and predictions should have understandable supporting reasons.
4. **Modular:** ML models, agent logic, APIs and database services should remain independently maintainable.
5. **Scalable:** The service should support future growth in properties, users and AI capabilities.
6. **Measurable:** Model performance must be evaluated before production deployment.
7. **Secure:** User data and production database access must be protected.

---

## 20. Project Vision

Waridi ML aims to make property discovery, valuation and investment analysis more intelligent and accessible.

Rather than simply allowing users to search through property listings, Waridi will understand what users are looking for, analyse available market information and help them make better property decisions through conversational artificial intelligence and machine learning.

**Waridi – Intelligent Real Estate Discovery.**


# API-Autism Screening System (AutCare) for Toddlers

## Overview
This project provides a **Flask-based API** for predicting Autism Spectrum Disorder (ASD) in children based on a set of input features. The API uses **machine learning models** (Logistic Regression, Decision Tree, and K-Nearest Neighbors) to make predictions. The data is stored in **MongoDB**, and the API allows users to input data and receive predictions in real-time.

## Features
### Machine Learning Models
The API uses three different machine learning models for prediction:
- **Logistic Regression**
- **Decision Tree Classifier**
- **K-Nearest Neighbors (KNN) Classifier**

### MongoDB Integration
- The input data is stored in a **MongoDB** database for future reference.

### RESTful API
- The API provides endpoints for making predictions and storing data.

## Installation

### Prerequisites
- Python 3.7 or higher
- MongoDB (either local or remote)
- Required Python packages (listed in `requirements.txt`)

### Steps

1. **Clone the repository**:
   ```sh
   git clone https://github.com/asaavi30/API-Autism_Screening_System.git
   cd your-repo-name
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**:
   - Ensure MongoDB is running locally or provide the connection string for a remote MongoDB instance.
   - Update the MongoDB connection string in `app.py`:
     ```python
     client = pymongo.MongoClient("mongodb+srv://root:root@asddatasystem.wjqngms.mongodb.net/test")
     ```

5. **Run the Flask application**:
   ```sh
   python app.py
   ```
   - The API will be available at **http://127.0.0.1:5000/**.

## Usage

### API Endpoints

#### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a simple "Hello, World!" message.
- **Example Response**:
  ```json
  {
    "message": "Hello, World!"
  }
  ```

#### 2. Prediction Endpoint
- **URL**: `/api/algo/<int:algo>/data/<string:arr>`
- **Method**: `GET`
- **Description**: Accepts a comma-separated string of input features and returns a prediction based on the selected algorithm.
- **Parameters**:
  - `algo`: The algorithm to use for prediction (`1`: Logistic Regression, `2`: Decision Tree, `3`: KNN).
  - `arr`: A comma-separated string of **15 input features** (`A1_Score` to `A10_Score`, `age`, `sex`, `ethnicity`, `child_jaundice`, `family_jaundice`).

- **Example Request**:
  ```
  /api/algo/1/data/1,0,1,0,1,0,1,0,1,0,30,1,2,1,0
  ```
- **Example Response**:
  ```json
  {
    "prediction": "1",
    "message": "The child may have autism"
  }
  ```

## Example Input Data
The input data should be a **comma-separated string** with the following features in order:

| Feature           | Description                              | Values         |
|------------------|--------------------------------------|---------------|
| **A1_Score**    | Score for question A1                | `0` or `1`    |
| **A2_Score**    | Score for question A2                | `0` or `1`    |
| **A3_Score**    | Score for question A3                | `0` or `1`    |
| **A4_Score**    | Score for question A4                | `0` or `1`    |
| **A5_Score**    | Score for question A5                | `0` or `1`    |
| **A6_Score**    | Score for question A6                | `0` or `1`    |
| **A7_Score**    | Score for question A7                | `0` or `1`    |
| **A8_Score**    | Score for question A8                | `0` or `1`    |
| **A9_Score**    | Score for question A9                | `0` or `1`    |
| **A10_Score**   | Score for question A10               | `0` or `1`    |
| **age**         | Age of the child in months           | Integer       |
| **sex**         | Sex of the child                     | `0: Female`, `1: Male` |
| **ethnicity**   | Ethnicity of the child (encoded)     | Integer       |
| **child_jaundice** | Whether the child had jaundice at birth | `0: No, 1: Yes` |
| **family_jaundice** | Whether a family member has jaundice | `0: No, 1: Yes` |

## Dataset
The dataset used for training the models is provided in **`dataset.csv`**. It contains the following columns:

| Column Name                 | Description |
|-----------------------------|-------------|
| **Case_No**                 | Unique identifier for each case. |
| **A1 to A10**               | Scores for the 10 questions in the ASD screening tool. |
| **Age_Mons**                | Age of the child in months. |
| **Qchat-10-Score**          | Total score from the Qchat-10 screening tool. |
| **Sex**                     | Sex of the child (`M` or `F`). |
| **Ethnicity**               | Ethnicity of the child. |
| **Jaundice**                | Whether the child had jaundice at birth (`Yes` or `No`). |
| **Family_mem_with_ASD**      | Whether a family member has ASD (`Yes` or `No`). |
| **Who_completed_the_test**   | Who completed the test (e.g., family member, health care professional). |
| **ClassASD_Traits**         | Whether the child has ASD traits (`Yes` or `No`). |

---

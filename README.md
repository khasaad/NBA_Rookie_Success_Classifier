<!-- Start of HTML content -->
<div style="font-family: Arial, sans-serif; max-width: 800px; margin: auto;">

<!-- Stubborn -->
<h3 style="color: #2c3e50;">khasaad, 11 february 2025</h3>
<h1>NBA project</h1>
<p>
    <strong>Author</strong>: SAAD Khaled<br>
    Data Scientist<br>
</p>
<hr>

<!-- Section Context -->
<h2>1 – Context & Data</h2>
<p>
    Dataset : <code>nba_logreg.csv</code><br>
    Goal : The goal is to provide a classifier to predict whether a player is worth investing in because he will last more than 5 years in the NBA based on his sports statistics. This model aims to advise investors looking to capitalize on future NBA talents.
</p>

<table border="1" style="border-collapse: collapse; width: 100%;">
  <tr>
    <th>Column>
    <th>Description</th>
  </tr>
  <tr><td>Name</td><td>Player Name</td></tr>
  <tr><td>GP</td><td>Games Played</td></tr>
  <tr><td>MIN</td><td>Minutes Played</td></tr>
  <tr><td>PTS</td><td>Points Per Game</td></tr>
  <tr><td>FGM</td><td>Field Goals Made</td></tr>
  <tr><td>FGA</td><td>Field Goal Attempts</td></tr>
  <tr><td>FG%</td><td>Field Goal Percent</td></tr>
  <tr><td>3P Made</td><td>3 Point Made</td></tr>
  <tr><td>3PA</td><td>3 Point Attempts</td></tr>
  <tr><td>3P%</td><td>3 Point Percentage</td></tr>
  <tr><td>FTM</td><td>Free Throw Made</td></tr>
  <tr><td>FTA</td><td>Free Throw Attempts</td></tr>
  <tr><td>FT%</td><td>Free Throw Percent</td></tr>
  <tr><td>OREB</td><td>Offensive Rebounds</td></tr>
  <tr><td>DREB</td><td>Defensive Rebounds</td></tr>
  <tr><td>REB</td><td>Rebounds</td></tr>
  <tr><td>AST</td><td>Assists</td></tr>
  <tr><td>STL</td><td>Steals</td></tr>
  <tr><td>BLK</td><td>Blocks</td></tr>
  <tr><td>TOV</td><td>Turnovers</td></tr>
  <tr><td>TARGET_5Yrs</td><td>1 si career length ≥5 ans, 0 if not</td></tr>
</table>

<!-- Questions Section -->
<h2>2 – Questions</h2>

<h3>Question 1 : Training</h3>

<p>Your goal will be to propose, train and validate a classifier that best meets the investors' objective.</p>

<h3>Question 2 : Integration</h3>
<p>Deploy the model as REST API using flask.</p>

<!-- Pied de page -->
<hr>

# Project Report: Predictive Ranking for NBA Talent Investment Based on Rookie Player Statistics

## 1. Context and Objective  
The project aims to develop a classifier capable of predicting whether an NBA rookie will last more than 5 years in the league. The primary goal is to help investors identify future NBA talents to invest in. The dataset used, `nba_logreg.csv`, contains sports statistics of these players.

## 2. Project Structure  
The project is divided into four main parts:  

1. **Folder `Classifier_evaluator`**  
   - File **`classifier.py`**: Refactored version of `test.py` using object-oriented programming (OOP) for flexible use with Jupyter Notebook. This file contains essential functions to read, preprocess data, and train models.  

2. **File `nba_logreg.ipynb`**  
   - *Data Exploration and Preparation*: Python libraries were used to explore and prepare the data. Visualizations were generated for better understanding.  
   - *Model Training and Validation*: Multiple classification methods were tested. Trained models are stored in the `Models` folder for later use.  
   - *Conclusion*: Results and best classifier (based on performance metrics) are discussed. Key features influencing the model were identified.  

3. **File `app.py`**  
   - *REST API with Flask*: Defines a web service using Flask to predict a player’s career length via API requests.  
   - *Postman Testing*: API tested and demonstrated using Postman for development and debugging.  

4. **Folder `Test`**  
   - **`test_score_classifier.py`**: Unit tests for `classifier.py` using pytest.  
   - **`test_app.py`**: Unit tests to verify the Flask API’s integrity.  

## 3. Development Environment  
- **Language and Version**: Python 3.12  
- **Libraries**:  
  - Flask for the web API  
  - Pandas and Scikit-Learn for data analysis and model training  
  - Matplotlib and Seaborn for data visualization  
  - Pytest for unit testing  

- **Dependency Installation**:  
  - Create a virtual environment (Windows example):  
    ```bash
    py -m venv <name_of_venv>
    <name_of_venv>\Scripts\activate
    ```  
  - Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```
    
## 4. Model Development and Validation  
### a. Data Exploration  
- Visualized distributions and correlations between player statistics.  
- Preprocessed data to handle missing values.  

### b. Model Training  
- Tested classification algorithms (Random Forest, Logistic Regression, Support Vector Classifier).  
- Used hyperparameter tuning (GridSearchCV, RandomizedSearchCV).  
- Selected the best model based on **recall** to prioritize identifying promising players.  

### c. Performance Evaluation  
- Analyzed metrics: precision, recall, F1-score.  
- Identified key features influencing predictions. 

## 5. Model Integration into a Web Service  
- **REST API Implementation**:  
  - Defined `/predict` endpoint to receive player stats and return predictions.  
  - Integrated the trained model for real-time predictions.  

- **Testing and Deployment**:  
  - Validated API with Postman test cases.  
  - Automated unit tests with pytest to ensure application robustness.

## 6. Conclusion  
This project demonstrates a systematic approach to developing and deploying a predictive classifier to advise investors on future NBA talents. The solution includes thorough data exploration, model training/validation, and a practical REST API. Results show the classifier effectively identifies players with high potential for long-term success in the NBA, offering valuable insights for investors. 

</div>
<!-- End of HTML content -->
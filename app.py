import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the models
lr_model = joblib.load('nba_lr_model.pkl')
GBoost_model = joblib.load('nba_GBoost_model.pkl')
RF_model = joblib.load('nba_rf_model.pkl')

# Load the data required for predictions
nba_elo = pd.read_csv('data/nba_elo_latest.csv')

# Function to preprocess input data for predictions
def preprocess_input(team1, team2, table2):
    table2['date'] = pd.to_datetime(table2['date'])
    df2 = table2[table2['season'] == 2023]
    
    # Determine game results (1 if team1 wins, 0 if team2 wins)
    df2['game_result'] = (df2['score1'] > df2['score2']).astype(int)

    # Drop insignificant columns
    cols_to_drop = ['date', 'season', 'playoff', 'team1', 'team2', 'elo1_post', 'elo2_post', 'neutral', 
                    'carm-elo1_pre', 'carm-elo2_pre', 'carm-elo_prob1', 'carm-elo_prob2', 
                    'carm-elo1_post', 'carm-elo2_post', 'importance', 'total_rating', 'score1', 'score2']
    df2.drop(columns=cols_to_drop, inplace=True)

    df2.reset_index(drop=True, inplace=True)
    
    return df2

# Streamlit UI
st.title('NBA Game Outcome Predictor')

# User input for teams
team1 = st.selectbox('Select Team 1', options=nba_elo['team'].unique())
team2 = st.selectbox('Select Team 2', options=nba_elo['team'].unique())

# Prediction button
if st.button('Predict Outcome'):
    # Preprocess the input data
    input_data = preprocess_input(team1, team2, nba_elo)
    
    # Make predictions with all models
    lr_prediction = lr_model.predict(input_data)[0]
    gboost_prediction = GBoost_model.predict(input_data)[0]
    rf_prediction = RF_model.predict(input_data)[0]

    # Convert predictions to readable format
    result_mapping = {1: f'{team1} Wins', 0: f'{team2} Wins'}
    st.write("Predictions:")
    st.write(f"Logistic Regression: {result_mapping[lr_prediction]}")
    st.write(f"Gradient Boosting: {result_mapping[gboost_prediction]}")
    st.write(f"Random Forest: {result_mapping[rf_prediction]}")

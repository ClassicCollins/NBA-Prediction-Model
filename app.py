import streamlit as st
import pandas as pd
import joblib

# Load your pre-trained models
lr_model = joblib.load('nba_lr_model.pkl')
GBoost_model = joblib.load('nba_GBoost_model.pkl')
RF_model = joblib.load('nba_rf_model.pkl')

st.title('NBA Playoff Predictions')

# User input for team selection
team1 = st.text_input('Enter Home Team (e.g., BOS):')
team2 = st.text_input('Enter Away Team (e.g., PHI):')

# Load and preprocess data
@st.cache
def load_data():
    table1 = pd.read_csv("data/nba_elo.csv")
    table2 = pd.read_csv("data/nba_elo_latest.csv")
    return table1, table2

table1, table2 = load_data()

def preprocess_data(table2):
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

test = preprocess_data(table2)

def predict_outcome(team1, team2, model):
    test_sample = test[(test['team1'] == team1) & (test['team2'] == team2)]
    if test_sample.empty:
        return None
    test_sample = test_sample.drop(columns=['game_result'])
    prediction = model.predict(test_sample)
    return prediction[0]

# Predict button
if st.button('Predict Outcome'):
    if team1 and team2:
        prediction_lr = predict_outcome(team1, team2, lr_model)
        prediction_gb = predict_outcome(team1, team2, GBoost_model)
        prediction_rf = predict_outcome(team1, team2, RF_model)

        if prediction_lr is None or prediction_gb is None or prediction_rf is None:
            st.write(f"No data found for the game between {team1} and {team2}")
        else:
            st.write(f"Logistic Regression Model Prediction: Team {team1 if prediction_lr == 1 else team2} wins")
            st.write(f"Gradient Boosting Model Prediction: Team {team1 if prediction_gb == 1 else team2} wins")
            st.write(f"Random Forest Model Prediction: Team {team1 if prediction_rf == 1 else team2} wins")
    else:
        st.write("Please enter both Team 1 and Team 2.")

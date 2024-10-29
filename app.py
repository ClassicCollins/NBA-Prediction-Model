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
@st.cache_data
def load_data():
    table1 = pd.read_csv("data/nba_elo.csv")
    table2 = pd.read_csv("data/nba_elo_latest.csv")
    return table1, table2

table1, table2 = load_data()

def preprocess_data(table2):
    table2['date'] = pd.to_datetime(table2['date'])
    df2 = table2[table2['season'] == 2023]

    # Drop insignificant columns
    cols_to_drop = ['date', 'season', 'playoff', 'elo1_post', 'elo2_post', 'neutral', 
                    'importance', 'total_rating', 'score1', 'score2']
    df2.drop(columns=cols_to_drop, inplace=True)
    df2.reset_index(drop=True, inplace=True)

    return df2

# Prepare the test data
test = preprocess_data(table2)

def create_test_sample(teamA, teamB, test):
    # Create a test sample for the input teams
    if teamA not in test['team'].values or teamB not in test['team'].values:
        return None

    # Extract features for the teams
    elo1_pre = test.loc[test['team'] == teamA, 'elo'].values[0]
    elo2_pre = test.loc[test['team'] == teamB, 'elo'].values[0]
    raptor1_pre = test.loc[test['team'] == teamA, 'raptor1_pre'].values[0]  # Adjust according to your actual column name
    raptor2_pre = test.loc[test['team'] == teamB, 'raptor2_pre'].values[0]  # Adjust according to your actual column name
    elo_prob1 = test.loc[test['team'] == teamA, 'elo_prob1'].values[0]  # Adjust according to your actual column name
    elo_prob2 = test.loc[test['team'] == teamB, 'elo_prob2'].values[0]  # Adjust according to your actual column name
    raptor_prob1 = test.loc[test['team'] == teamA, 'raptor_prob1'].values[0]  # Adjust according to your actual column name
    raptor_prob2 = test.loc[test['team'] == teamB, 'raptor_prob2'].values[0]  # Adjust according to your actual column name
    quality = test.loc[test['team'] == teamA, 'quality'].values[0]  # Adjust according to your actual column name

    test_sample = pd.DataFrame({
        'team1': [teamA],
        'team2': [teamB],
        'elo1_pre': [elo1_pre],
        'elo2_pre': [elo2_pre],
        'elo_prob1': [elo_prob1],
        'elo_prob2': [elo_prob2],
        'raptor1_pre': [raptor1_pre],
        'raptor2_pre': [raptor2_pre],
        'raptor_prob1': [raptor_prob1],
        'raptor_prob2': [raptor_prob2],
        'quality': [quality],
        'game_result': [None]  # Placeholder for game_result if needed
    })
    return test_sample

def predict_outcome(teamA, teamB, model):
    test_sample = create_test_sample(teamA, teamB, test)
    if test_sample is None:
        return None
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

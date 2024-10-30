import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('trained_models/nba_lr_model.pkl')

# Load the preprocessed Elo ratings data
elo_processed_data = pd.read_csv('data/elo_processed_data.csv')  # Adjust this as needed to load your data

# Streamlit App
st.title("NBA Game Outcome Predictor")

# Prediction function
def predict_outcome(team1, team2, date, data):
    new_game = data[(data['team1'] == team1) & 
                    (data['team2'] == team2) & 
                    (data['date'] < date)].sort_values(by='date', ascending=False).head(1)
    
    if new_game.empty:
        return None, None

    features = data.drop(['score1', 'score2', 'date', 'team1', 'team2'], axis=1)
    new_game = new_game[features.columns].dropna()
    
    if new_game.empty:
        return None, None

    prediction1 = model.predict(new_game)
    prediction = model.predict_proba(new_game)[0][1]
    return prediction1[0], prediction
    
# Team Selection
team1 = st.selectbox("Select Home Team", elo_processed_data['team1'].unique())
team2 = st.selectbox("Select Away Team", elo_processed_data['team2'].unique())

# Date Input
date = st.date_input("Select Game Date", pd.to_datetime('today'))
# Prediction Button
if st.button("Predict Outcome"):
    prediction1, prediction = predict_outcome(team1, team2, date.strftime('%Y-%m-%d'), elo_processed_data)

    if prediction1 is None:
        st.error(f"No previous data found for teams {team1} and {team2} before {date}")
    elif prediction1 == 1:
        st.success(f"The predicted outcome of the game between {team1} and {team2} on {date} is {team1} wins with {prediction * 100:.1f}% probability")
    elif prediction1 == 0:
        st.warning(f"The predicted outcome of the game between {team1} and {team2} on {date} is {team1} loses with {prediction * 100:.1f}% probability")
    else:
        st.info(f"The predicted outcome of the game between {team1} and {team2} on {date} is uncertain")


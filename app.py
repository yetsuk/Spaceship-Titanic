# --- Application Streamlit - Spaceship Titanic ---#

# Import des modules
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

st.set_page_config(
    page_title = 'Spaceship Titanic analysis model'
)

st.title(':milky_way: Spaceship Titanic prédictions de survie')

st.write('''SpaceShip Titanic est une base de donnée Kaggle comportant les données de 13000 passagers du vol interstellaire Titanic
         ayant décolé en 2912. En passant, aux alentours d'Alpha Centauri le vol a eu une collision avec une anomalie spatiale camouflée
         dans un nuage de poussière cosmique. Au cours de l'accident de nombreux passagers se sont envolés vers une autre dimension.
         L'objectif de ce modéle est de prédire si un individu aurait disparu au cours de cette incident sur la base de ses caractéristiques.
''')

# Chargement du model de prédiction
artefact = joblib.load("model_complete.pkl")

model = artefact['model']


st.header(':bust_in_silhouette: Profil du passager')
st.write('Veuillez remplir les informations suivantes pour pouvoir prédire votre destinté à bord du Spaceship Titanic.')


# Formulaire pour extraire les informations des différentes variables
st.subheader('Information Relative au passager')

Age = st.slider('Quelle age avez-vous ?', min_value = 0, max_value = 105)

HomePlanet = st.radio('Quelle était votre planet de départ ?', ['Europa', 'Earth', 'Mars'], horizontal = True)

CryoSleep = st.radio("Avez-vous bénéficiez du système d'endormissement cryogénique?", ['Oui', 'Non'], horizontal = True)

Destination = st.radio("Quelle était votre planet d'arrivé ?", ['PSO J318.5-22','TRAPPIST-1e', '55 Cancri e'], horizontal = True)

col1, col2 = st.columns(2)

with col1:

    Vip = st.selectbox('Aviez-vous des billets VIP pour monter à bord du vaisseau ?', ['Oui', 'Non']) 

    Deck = st.selectbox('A quel niveau du vaisseau vous trouviez-vous ?', ['A', 'B', 'C', 'D', 'E', 'F'])

with col2:
    Side = st.selectbox('De quel côté du vaisseau votre place se situé ?', ['S', 'P'])

    Cabin_Num = st.number_input('Numéro de cabine', min_value = 1, max_value = 1894)

st.divider()
st.subheader('Dépense lors du voyage')

col3, col4 = st.columns(2)

with col3:
    RoomService = st.number_input("Combien d'euros avez vous dépensé au Room Service ?", min_value = 0, max_value = 100000)

    FoodCourt = st.number_input("Combien d'euros avez vous dépensé au Food Court ?", min_value = 0, max_value = 100000)

with col4:
    Spa = st.number_input("Combien d'euros avez vous dépensé au Spa ?", min_value = 0, max_value = 10000)

    VRDeck = st.number_input("Combien d'euros avez vous dépensé au VRDeck ?", min_value = 0, max_value = 10000)


# Création du profil et prédiction de survie
button = st.button('Validez vos informations et commencer la prédiction')

# Début du programme
if button:

    # Ajout des variables prédictive
    HomePlanet_Europa = HomePlanet == 'Europa'
    HomePlanet_Mars = HomePlanet == 'Mars'
    CryoSleep_True = CryoSleep == 'Oui'
    Destination_TRAPPIST = Destination == 'TRAPPIST-1e'
    VIP_True = Vip == 'Oui'
    Cabin_Deck_B = Deck == "B"
    Cabin_Deck_C = Deck == "C"
    Cabin_Deck_D = Deck == "D"
    Cabin_Deck_E = Deck == "E"
    Cabin_Deck_F = Deck == "F"
    Cabin_Side_S = Side == "S"

    # Création du profil individu
    Individu = [[Age,
    RoomService,
    FoodCourt,
    Spa,
    VRDeck,
    Cabin_Num,
    HomePlanet_Europa,
    HomePlanet_Mars,
    CryoSleep_True,
    Destination_TRAPPIST,
    VIP_True,
    Cabin_Deck_B,
    Cabin_Deck_C,
    Cabin_Deck_D,
    Cabin_Deck_E,
    Cabin_Deck_F,
    Cabin_Side_S]]

    prediction = model.predict(Individu)

    if prediction == True:
        st.subheader(':fog: Vous avez était transporté dans une autre dimension !!!')

    else:
        st.subheader(":smiley: Vous n'avez pas était transporté dans une autre dimension !!!")
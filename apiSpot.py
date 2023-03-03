import streamlit as st
import pandas as pd
import numpy as np
import pickle

from api import *


pickle_in = open('xg_reg.pkl', 'rb') 
modelSpot = pickle.load(pickle_in)



titre = "Prediction popularité de la chanson en 2022"
original_title = '<p style="font-family:Courier; color:Blue; font-size: 42px;">{} </p>'.format(titre)
st.markdown(original_title, unsafe_allow_html=True)

columns_model = ['duration_ms', 'danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']



carac = pd.DataFrame()
artist = pd.DataFrame()


titre_chanson  = st.text_input(label="Quels est le titre de votre chanson ?  :", key="title")

carac = get_audio_features(titre_chanson)
carac = carac.to_dict()
carac = list(carac.values())
valeurs = [value for d in carac for value in d.values()]
print(valeurs)

artist = get_audio_artist(titre_chanson)
artist = artist.to_dict()
artist = list(artist.values())
artist_value = [value for d in artist for value in d.values()]

if(st.button("Valider")):
   
    predic_Spoty = int(modelSpot.predict(pd.DataFrame(np.array(valeurs).reshape(1, -1),columns=columns_model)))
    


    st.markdown("<h1 style='text-align: center;'>Votre prediction</h1>", unsafe_allow_html=True)

    new_title = '<p style="font-family:sans-serif; color:Green;width:100%;text-align:center; font-size: 36px;">{} / 100 </p>'.format(predic_Spoty)
    st.write("le nom de l'artiste est : ",artist_value[0])
    st.markdown(new_title, unsafe_allow_html=True)

   
   
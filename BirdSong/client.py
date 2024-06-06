import requests
from flask import Flask, jsonify, request
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import librosa
import pathlib

def main():
    # Ask the user for the path to the audio file
    audio_file_path = input("Please enter the full path to the audio file: ")
    
    # URL of the REST API server that returns bird information
    info_url = "http://192.168.0.55:5000/bird"

    # Load the model                                                                          
    try:
        model = load_model('model.h5')
        print("Model loaded successfully.")
    except Exception as e:
        app.logger.error("Failed to load model: %s", e)
        raise e

    def get_spectrogram(file_path):
        data_dir = pathlib.Path(file_path)
        #audio = tf.keras.utils.audio_dataset_from_directory(directory=data_dir)
        audio, sr = librosa.load(file_path, sr=16000)
        spectrogram = tf.signal.stft(
            audio, frame_length=256, frame_step=128)
        # Obtain the magnitude of the STFT.
        spectrogram = tf.abs(spectrogram)
        # Add a `channels` dimension so that the Spectrogram can be used
        spectrogram = spectrogram[..., tf.newaxis]
        spectrogram = spectrogram[None, ...]
        #assert spectrogram.shape[1:] == (124, 129, 1), f"Unexpected shape: {spectrogram.shape}"
        return spectrogram
    
    def load_and_convert_to_spectrogram(file_path, target_shape=(124, 129)):
        # Load audio file with librosa, default sr=22050                                      
        audio, sr = librosa.load(file_path, sr=16000)
            
        # Parameters for STFT                                                                 
        n_fft = 2048  # Number of STFT components 
        hop_length = int(sr / target_shape[1])  # Calculate hop_length to achieve ~129 columns

        # Compute the Short-Time Fourier Transform (STFT)                                     
        stft = librosa.stft(audio, n_fft=n_fft, hop_length=hop_length)

        # Convert to magnitude spectrogram                                                    
        spectrogram = np.abs(stft)

        # Apply logarithmic scaling                                                           
        spectrogram = librosa.amplitude_to_db(spectrogram, ref=np.max)
         
        return spectrogram

    def decode_prediction(prediction):
        # Assuming you have a function to decode predictions
        classes = {0 : "Black-crowned night heron",
                   1 : "Bushtit",
                   2 : "Common raven",
                   3 : "House sparrow",
                   4 : "Northern Cardinal",
                   5 : "Nuttall's woodpecker",
                   6 : "Peregrine falcon",
                   7 : "Red-tailed hawk",
                   8 : "Rock pigeon",
                   9 : "Western bluebird"}
        #predicted_class = np.argmax(prediction, axis=1)
        probs = prediction[0]
        max_index = 0
        max_element = 0;
        for i in range (1,len(probs)): #iterate over array
            if probs[i] > max_element: #to check max value
                max_element = probs[i]
                ind = i
                predicted_class = classes[ind]
        return predicted_class


    #identify audio
    audio = get_spectrogram(audio_file_path)
    prediction = model.predict(audio)
    bird_name = decode_prediction(prediction)
    print(f"Identified bird: {bird_name}")
    
    # Send the bird name to the information REST API server
    info_response = requests.get(f"{info_url}?bird_name={bird_name}")
    
    # Check if the info request was successful
    response = requests.get(f"{info_url}?name={bird_name}")
    if response.status_code == 200:
        bird_info = response.json()
        print("Bird Information:")
        print(f"Name: {bird_name}")
        print(f"Description: {bird_info['Description']}")
        print(f"Habitat: {bird_info['Habitat']}")
        print(f"Depiction: {bird_info['Depiction']}")
    else:
        print("Failed to retrieve bird information. Server responded with an error.")

if __name__ == "__main__":
    main()

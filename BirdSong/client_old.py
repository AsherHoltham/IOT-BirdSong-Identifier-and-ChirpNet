import requests

def main():
    # Ask the user for the path to the audio file
    audio_file_path = input("Please enter the full path to the audio file: ")

    # URL of the ML server that processes the audio file and returns a bird name
    ml_url = "http://example-ml.com/api/identify_bird"

    # URL of the REST API server that returns bird information
    info_url = "http://example-info.com/api/bird_info"

    # Ensure the file exists and is accessible before sending
    try:
        with open(audio_file_path, 'rb') as f:
            files = {'audio': (audio_file_path, f)}
            # Send the audio file via POST request to the ML server
            ml_response = requests.post(ml_url, files=files)

            # Check if the ML request was successful
            if ml_response.status_code == 200:
                bird_name = ml_response.json().get('bird_name', 'Unknown')
                print(f"Identified bird: {bird_name}")

                # Send the bird name to the information REST API server
                info_response = requests.get(f"{info_url}?bird_name={bird_name}")

                # Check if the info request was successful
                if info_response.status_code == 200:
                    bird_info = info_response.json()
                    print("Bird Information:")
                    # Example of parsing JSON data (assuming structure is known)
                    print(f"Name: {bird_info.get('name', 'N/A')}")
                    print(f"Description: {bird_info.get('description', 'N/A')}")
                    print(f"Habitat: {bird_info.get('habitat', 'N/A')}")
                else:
                    print("Failed to retrieve bird information. Server responded with an error.")
            else:
                print("Failed to identify bird. ML Server responded with an error.")
    except FileNotFoundError:
        print("Error: The file was not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
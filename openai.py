import requests

def open_ai(music_name, open_ai_key, open_ai_model):
    # Set your OpenAI API key

    # Define the endpoint and headers for the OpenAI API request
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {open_ai_key}',
        'Content-Type': 'application/json'
    }

    # Define the system prompt and user prompt
    user_content = f"""From the following list of Genre options please choose the most appropriate genre for the music name provided. 
    
    Genre List ::
    1. Classical
    2. Jazz
    3. Rock
    4. Pop
    5. Hip-Hop/Rap
    6. Electronic
    7. Country
    8. R&B/Soul
    9. Reggae
    10. Blues
    11. Folk
    12. World Music
    13. Latin
    14. New Age
    15. Alternative
    
    Music Name :: {music_name}
    
    MAKE SURE TO ADD A SPOTIFY REFERENCE LINK IF FOUND. MAKE SURE YOU ONLY ADD THE REFERENCE LINK. If you do not find a Reference link just say UNAVAILABLE
    Make sure the output looks something like this = "Genre Name :: Music Name. Spotify Link : --------"
    Example = "Jazz :: What a wonderful world. Spotify Link : https://open.spotify.com/track/29U7stRjqHU6rMiS8BfaI9"
    """
    messages = [
        {"role": "system", "content": "You are a professional Music Genre Identifier."},
        {"role": "user", "content": user_content}
    ]

    # Define the request payload
    data = {
        'model': open_ai_model,
        'messages': messages
    }

    # Send the request to the OpenAI API
    response = requests.post(url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code}, Error Text : {response.text}"

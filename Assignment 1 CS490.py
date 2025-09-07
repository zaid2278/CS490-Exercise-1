import requests
import json

def main():
    # API endpoint
    url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

    # Your required information
    data = {
        "UCID": "zh34",  
        "first_name": "Zaid",
        "last_name": "Hasan",
        "github_username": "zaid2278",   # change if your GitHub username is different
        "discord_username": "zaid_2278",  # update with your actual Discord tag
        "favorite_cartoon": "Spongebob",
        "favorite_language": "Python",
        "movie_or_game_or_book": "EAFC",
        "section": "103"
    }

    try:
        # Send POST request
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data)
        )

        # Print results
        print("Status Code:", response.status_code)
        print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        print("Error while connecting:", e)


if __name__ == "__main__":
    main()

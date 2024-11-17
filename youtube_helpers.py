import requests

API_KEY = "XXXX"

def get_youtube_transcript_with_searchapi(video_id):
    """
    Retrieves the transcript of a YouTube video using the searchapi.io API and returns it as a single string with sentences.

    Returns:
        str: A single string containing the transcript with sentences.

    Raises:
        ValueError: If the YouTube URL is invalid.
        Exception: If an error occurs while fetching the transcript.
    """

    # API endpoint and parameters
    api_url = "https://searchapi.io/api/v1/search"
    params = {
        "api_key": API_KEY,
        "engine": "youtube_transcripts",
        "video_id": video_id
    }

    try:
        # Make the API request
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the JSON response
        data = response.json()

        # Check if transcript is available
        if "transcripts" not in data or not data["transcripts"]:
            raise Exception("Transcript not available for this video")

        # Join sentences with a space, adding a period at the end of each sentence if needed
        transcript_text = " ".join(
            [line["text"].strip() + "." if not line["text"].strip().endswith('.') else line["text"].strip()
             for line in data["transcripts"]]
        )

        return transcript_text

    except requests.RequestException as e:
        raise Exception(f"An error occurred while fetching the video transcript: {e}")
    except KeyError as e:
        raise Exception(f"Unexpected API response format: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ''
        for transcript in transcript_list:
            transcript_text += transcript['text'] + ' '
        return transcript_text
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Replace 'VIDEO_ID' with the ID of the YouTube video you want to extract the transcript from
video_id = 'p5ItkPxCSRY'
transcript = get_transcript(video_id)

if transcript:
    print(transcript)
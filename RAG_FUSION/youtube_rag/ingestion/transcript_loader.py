from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled,NoTranscriptFound
from utils.logger import get_logger

logger = get_logger(__name__)


def load_transcript(video_id :str)->str:
    
    logger.info(f"Fetching transcript for video: {video_id}")
    
    try:
        api = YouTubeTranscriptApi()

        transcript_list = api.fetch(
            video_id,
            languages=["en", "hi"]
        )

        transcript = " ".join(
            chunk.text for chunk in transcript_list
        )

        logger.info("Transcript fetched successfully.")
        logger.info(f"Transcript Length: {len(transcript)} characters")

        return transcript
    
    except TranscriptsDisabled:
        logger.error("Transcripts are disabled for this video.")
        raise
    except Exception as e:
        logger.exception(f"Unexcepeted Error: {e}")
        
        raise
    
if __name__ == "__main__":

    VIDEO_ID = "90lLQVZe2Nc"

    transcript = load_transcript(VIDEO_ID)

    print(transcript[:1000])
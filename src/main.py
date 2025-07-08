from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware # Import CORS middleware

from src.resources.ws_stream import generate_frames

app = FastAPI()

# --- CORS Configuration ---
# If you have multiple domains, you can add them to the list.
# For development, you might temporarily use ["*"] but NEVER do this in production.
origins = [
    "https://steveseelan.com",
    "https://raspi.steveseelan.com",
    "http://localhost:3000", # For local development
    # Add other domains if necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # List of origins that are allowed to make requests
    allow_credentials=True,      # Allow cookies to be included in cross-origin requests
    allow_methods=["GET"],       # Only allow GET requests for the video stream
    allow_headers=["*"],         # Allow all headers
)
# --- End CORS Configuration ---

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/video-feed")
async def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

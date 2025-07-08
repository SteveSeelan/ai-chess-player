from picamera2 import Picamera2
import cv2
import asyncio

picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"format": "RGB888", "size": (640, 480)}))
picam2.start()

async def generate_frames():
    while True:
        frame = picam2.capture_array() # capture frame with pi camera
        ret, buffer = cv2.imencode('.jpg', frame) # Encode Frame to JPEG
        if not ret:
            continue # skip if encoding failed

        frame_bytes = buffer.tobytes() # Get JPEG Bytes
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n') # Yield MJPEG Multipart Segment
       
        await asyncio.sleep(0.06)  # ~30 FPS cap

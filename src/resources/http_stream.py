import io

from picamera2 import Picamera2
from fastapi import FastAPI, Response

app = FastAPI()

@app.get('/image' , methods=['GET'])
def get_image():
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
    data = io.BytesIO()
    picam2.start()
    picam2.capture_file(data, "test.jpg")
    picam2.stop()
    picam2.close()
    return Response(content=data.get_value(), media_type='image/jpeg')

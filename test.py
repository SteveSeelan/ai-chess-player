from picamera2 import Picamera2, Preview
from flask import Flask, Response

app = Flask(__name__)
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
picam2.start()
# picam2.start_preview(Preview.NULL)
# picam2.start()
# time.sleep(2)
# picam2.capture_file("test.jpg")

picam2.start_and_record_video("test_vid.mp4", duration=5)

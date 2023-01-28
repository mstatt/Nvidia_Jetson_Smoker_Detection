import cv2
import asyncio
import os


class VideoGrabber:
    def __init__(self, n, save_dir=None):
        self.n = n
        self.save_dir = save_dir
        self.video = cv2.VideoCapture(0)
        self.frame_count = 0

    async def grab_frames(self):
        while True:
            success, frame = self.video.read()
            if success:
                self.frame_count += 1
                if self.save_dir and self.frame_count % self.n == 0:
                    cv2.imwrite(
                        os.path.join(self.save_dir, f"frame{self.frame_count}.jpg"),
                        frame,
                    )
                yield frame
            else:
                break
        self.video.release()

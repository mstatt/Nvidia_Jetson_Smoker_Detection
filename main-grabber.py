import cv2
from grabber import VideoGrabber
import asyncio


async def main():
    save_dir = "./grabbed"
    grabber = VideoGrabber(n=30, save_dir=save_dir)
    async for frame in grabber.grab_frames():
        # do something with the frame
        cv2.imshow("frame", frame)
        cv2.waitKey(1)


asyncio.run(main())

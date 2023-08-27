# Question
# Given a short video, (use your own > 60 second video), use OpenCV to clip a 5 second clip from the 00:30 mark to the 00:35 mark and draw a red 100 x 100 pixel sized box in the middle of the video.
import argparse
import platform
from os import mkdir
from pathlib import Path

import cv2

MACOS, LINUX, WINDOWS = (
    platform.system() == x for x in ["Darwin", "Linux", "Windows"]
)


def check_source_and_output_paths(source_path, output_folder):
    # Check if source path exists
    if not Path(source_path).exists():
        raise FileNotFoundError(f"Source video {source_path} does not exist")

    # Create output path if it does not exist
    Path(output_folder).mkdir(exist_ok=True)

    # return video name and output path
    return Path(source_path).stem, source_path, output_folder


def check_video_length_start_end(start_time, end_time, total_frames, fps):
    # Check if start and end times are valid
    if start_time > end_time:
        raise ValueError("Start time cannot be greater than end time")

    # Check if start and end times are valid
    if start_time > total_frames / fps:
        raise ValueError("Start time cannot be greater than video length")

    # Check if start and end times are valid
    if end_time > total_frames / fps:
        raise ValueError("End time cannot be greater than video length")


def setup_writer(output_dir, source_name, width, height, fps=30):
    # Set the output path
    suffix = ".mp4" if MACOS else ".avi" if WINDOWS else ".avi"
    fourcc = "avc1" if MACOS else "WMV2" if WINDOWS else "MJPG"
    out_fps = 30
    save_path = str((Path(output_dir) / source_name).with_suffix(suffix))

    # Set video writer to save the output
    writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*fourcc), fps,
                             (int(width), int(height)))
    return writer


def process_video(video_path, start_time, end_time, output_dir='output', full_video=False, box_size=100):
    # Check if source and output paths are valid
    source_name, source_path, output_dir = check_source_and_output_paths(
        video_path, output_dir)

    # Load the video
    cap = cv2.VideoCapture(video_path)

    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Check if start and end times are valid
    check_video_length_start_end(start_time, end_time, total_frames, fps)

    # Get the width and height of frame
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # Get the start and end frame
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    writer = setup_writer(output_dir, source_name, width, height, fps)
    if not full_video:
        # Skip to the start frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame-1)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        # Exit if not full video and current frame is greater than end frame
        if not full_video and current_frame > end_frame:
            break

        if current_frame >= start_frame and current_frame <= end_frame:
            # Draw the red box in the middle
            box_size = 100
            frame_height, frame_width, _ = frame.shape
            box_x = int((frame_width - box_size) / 2)
            box_y = int((frame_height - box_size) / 2)
            cv2.rectangle(frame, (box_x, box_y),
                          (box_x + box_size, box_y + box_size), (0, 0, 255), 2)

        # Write the frame to the output
        writer.write(frame)

    # Release the capture and output objects
    cap.release()
    writer.release()
    cv2.destroyAllWindows()
    print(f"Saved video to {output_dir}")


if __name__ == "__main__":

    # arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--video_path', type=str, required=True)
    # parser.add_argument('--start_time', type=int, required=True)
    # parser.add_argument('--end_time', type=int, required=True)
    # parser.add_argument('--box_size', type=int, required=True)
    # parser.add_argument('--output_dir', type=str, default='output')
    # parser.add_argument('--full_video', type=bool, default=False)
    # args = parser.parse_args()

    video_path = 'data/Google Please Hire Me - Nick White.mp4'
    start_time = 30  # in secondss
    end_time = 35  # in seconds

    process_video(video_path, start_time, end_time,
                  output_dir='output', full_video=True)

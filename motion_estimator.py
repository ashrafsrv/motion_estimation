from extract_frames import extract_frames
from extract_video import extract_video
import numpy as np
import cv2

# Path to the video file to be processed
video = './monkey.avi'

# Extracting frames from the video
length, frame_height, frame_width, fps = extract_frames(video)




# MOTION ESTIMATION CODE
# def calculate_SSD(block1, block2):
#     subtracted = block1 - block2
#     return np.sqrt(np.sum(np.square(subtracted)))
#
#
# frame1 = cv2.imread('./frames/frame1.tif')
#
# frame2 = cv2.imread('./frames/frame3.tif')
# print(frame1.shape)
#
# N = 25
#
# height = frame1.shape[0]
# width = frame1.shape[1]
#
# count = 1
#
# while(count < length):
#     for x in range((N - 1) // 2, width, N):
#         ssd = np.zeros((height//2, width//2))
#         curr_frame = cv2.imread('./frames/frame%d.tif' % count)
#         ref_frame = cv2.imread('./frames/frame%d.tif' % (count + 1))
#
#         for y in range((N - 1) // 2, height, N):
#             curr_block = curr_frame[x-((N-1)//2):x+((N-1)//2)][y-((N-1)//2):y+((N-1)//2)][:]
#
#             for j in range(x + ((N-1)//2),width,N):
#                 for i in range(y + ((N-1)//2), height, N):
#
#
#                     ref_block = ref_frame[i-((N-1)//2):i+((N-1)//2)][j-((N-1)//2):j+((N-1)//2)][:]
#
#                     ssd = np.append(ssd, calculate_SSD(curr_block, ref_block))








#Extracting video from the new frames
extract_video(length, frame_height, frame_width, fps)
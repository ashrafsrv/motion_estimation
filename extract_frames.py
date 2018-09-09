import cv2
import sys
from create_directory import create_dir

frame_save_path = './frames'

def extract_frames(video):
	cap = cv2.VideoCapture(video)

	if not cap.isOpened():
		print('Failed to open {}'.format(video))
		sys.exit(1)

	create_dir(frame_save_path)

	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
	frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
	fps = cap.get(cv2.CAP_PROP_FPS)

	count = 0

	while(True):
		ret, frame = cap.read()

		if not ret:
			print('The video has finished')
			break

		cv2.imwrite('frames/frame%d.tif' % count, frame)
		cv2.putText(img=frame, text='phase 1: %d%%' % int(100*count/length), org=(int(0), int(frame.shape[1] / 2)), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.7, color=(0, 255, 0))
		cv2.imshow('Video', frame)
		count += 1
		if cv2.waitKey(30) & 0xff == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()

	return length, frame_height, frame_width, fps
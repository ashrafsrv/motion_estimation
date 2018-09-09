import cv2


def extract_video(length, frame_height, frame_width, fps):
    count = 0
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (int(frame_width), int(frame_height)))
    while(1):
        img = cv2.imread('frames/frame%d.tif' % count)
        if img is None:
            break;
        print('phase 3: saving video %d%%' % int(100*count/length))
        out.write(img)
        count += 1
    out.release()
    cv2.destroyAllWindows()
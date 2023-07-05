import os
import cv2
from ultralytics import YOLO


def pred_video(in_video_name: str, out_video_name: str, model_path: str, threshold: float):
    video_path = os.path.join('videos', in_video_name)
    video_path_out = os.path.join('videos', out_video_name)  # будет хранится уже задетектированное видео

    video = cv2.VideoCapture(video_path)
    ret, frame = video.read()
    H, W, _ = frame.shape
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Создаем объект выходного видео, указав его путь, формат видео, фпс и размер кадра
    out_video = cv2.VideoWriter(filename=video_path_out,
                                fourcc=cv2.VideoWriter_fourcc(*'MP4V'),
                                fps=fps,
                                frameSize=(W,
                                           H))

    model = YOLO(model_path)

    while ret:
        pred = model(frame)[0]

        for result in pred.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0),
                              5)  # рисуем предсказанные рамки
                cv2.putText(frame, pred.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

        out_video.write(frame)
        ret, frame = video.read()

    video.release()
    out_video.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    return


threshold = 0.7
in_video_name = 'my_turtle_1'

pred_video(in_video_name=f'{in_video_name}.mp4',
           out_video_name=f'{in_video_name}_out_threshold_{threshold}.mp4',
           model_path='runs/detect/train4/weights/last.pt',
           threshold=threshold)

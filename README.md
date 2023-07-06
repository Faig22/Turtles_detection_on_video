# Детекция красноухих черепах на видео с помощью YOLOv8
![image](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/c2101970-db9e-478d-82eb-52062a9b9a3b)

## Структура проекта
### Парсинг фотографий (get_images.py)
1. Фотографии были взяты с открытого источника (https://phonoteka.org/44628-krasnouhaja-cherepaha-oboi.html)
2. С помощью библиотек ***urllib***, ***BeautifulSoup*** все фотографии были успешно скачаны и сохранились в папку ***images***

### Разметка фотографий
1. С помощью сайта cvat.ai (https://www.cvat.ai/) были прорисованы боксы для каждого изображения,
2. Также получены координаты боксов в формате YOLO (***class_id, x, y, h, w***), где ***class_id*** - это номер класса объекта, ***x*** и ***y*** координаты центра объекта, а ***h*** и ***w*** высота и ширина объекта 
   ![image](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/e2eaa1a4-1dc1-4988-9686-12feea4f8bee)

### Разбиение данных на тренировочный и валидационный набор (train_val_images.py)
1. Были созданы пути *train/images*, *train/labels*, *val/images*, *val/labels*
2. Часть данных было отправлено в тренировочный набор, часть в валидационный

### Обучение модели (train.py)
1. Была выбрана модель YOLOv8 (https://docs.ultralytics.com/)
![image](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/fbb4c460-db35-4a63-9928-4401d5b90106)
Ссылка на источник, где была взята картинка (https://blog.roboflow.com/whats-new-in-yolov8/)

2. В пакете ultralytics/YOLO есть пять моделей для обнаружения, сегментации и классификации. ***YOLOv8n*** - самый быстрый и маленький, в то время как ***YOLOv8 Extra Large*** (***YOLOv8x***) - самый точный, но самый медленный среди них. 
![image](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/64a59a79-3345-4134-be06-a89a23834a13)
3. Была выбрана модель ***YOLOv8n*** с коробки
4. Обучили на 100 эпохах вместе со встроенной аугментацией
5. Результаты обучения сохранились в *runs/detect/train/*
   
Ниже представлены размеченные фотографии из валидационного набора

![image](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/159f2716-46ae-4c60-b940-e554ddd31b8d)

Далее представлены результаты модели на валидации

![image](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/fef80cb5-68f7-4d44-a216-3b7184d036fc)




### Детекция на видео (predict_video.py)

Составлена функция, которая на вход принимает несколько параметров:
-    ***in_video_name*** - название видео, которая подается в модель
-    ***out_video_name*** - название видео, которая быдет на выходе модели
-    ***model_path*** - путь до весов нашей модели
-    ***threshold*** - порог, необходимый для отрисовки боксов на видео

Далее представлены видео с задетектированными черепахами с различными значениями ***threshold*** 

threshold = 0.7

![ezgif com-video-to-gif (1)](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/006514d8-b8b7-4fd1-a10b-c6e5af57f7b9)

threshold = 0.5

![ezgif com-video-to-gif (2)](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/b44afc74-6d04-4036-ab9d-c1afdd735453)

threshold = 0.7

![ezgif com-video-to-gif (4)](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/c6141012-d84d-40c2-b7ab-bb41a29cac97)

threshold = 0.5
  
![ezgif com-video-to-gif (3)](https://github.com/Faig22/Turtles_detection_on_video/assets/95417164/efeae139-aa21-4bb0-a94b-1a492002787b)



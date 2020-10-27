# Fine-tuning of YOLOv3

This repository is based on https://github.com/eriklindernoren/PyTorch-YOLOv3 and fine-tuned on [Open Images dataset](https://storage.googleapis.com/openimages/web/index.html).

For downloading the Open Images dataset please refer to https://github.com/WyattAutomation/Train-YOLOv3-with-OpenImagesV4

After adding the images and labels into the /data/custom/ folder, run create_path.py to create txt documents of image path and label path, which will be further used in the training.

## YOLOv3:

You only look once (YOLO) is a state-of-the-art, real-time object detection system. On a Pascal Titan X it processes images at 30 FPS and has a mAP of 57.9% on COCO test-dev. YOLOv3 uses a few tricks to improve training and increase performance, including: multi-scale predictions, a better backbone classifier, and more. The full details are in https://pjreddie.com/media/files/papers/YOLOv3.pdf.

![yolo](https://github.com/tian-cthit/Fine-tuning-YOLOv3-Pytorch/blob/main/Screen_Shot_2018-03-24_at_10.48.42_PM.png)

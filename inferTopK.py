from paddleocr import PaddleOCR, draw_ocr
import os
from PIL import Image

# lang `ch`, `en`, `chinese_cht`
ocr = PaddleOCR(lang='ch')

in_root_path = r'E:\Desktop\test\in'
out_root_path = r'E:\Desktop\test\out'
if not os.path.isdir(out_root_path):
    os.makedirs(out_root_path)

img_path_list = os.listdir(in_root_path)

for i in range(0, len(img_path_list)):
    img_path = os.path.join(in_root_path, img_path_list[i])
    img_out_path = os.path.join(out_root_path, img_path_list[i])
    result = ocr.ocr(img_path, cls=False, det=False)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)

    # 显示结果
    # 如果本地没有simfang.ttf，可以在doc/fonts目录下下载
    # result = result[0]
    # image = Image.open(img_path).convert('RGB')
    # boxes = [line[0] for line in result]
    # txts = [line[1][0] for line in result]
    # scores = [line[1][1] for line in result]
    # im_show = draw_ocr(image, boxes, txts, scores, font_path='doc/fonts/simfang.ttf')
    # im_show = Image.fromarray(im_show)
    # im_show.save(os.path.join(img_out_path))
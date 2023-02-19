Update:

- modify `rec_postprocess.py`

  - 输出topK的预测结果。
  https://github.com/haoxia1/PaddleOCR/blob/e52c8f07928f85065ff471fe8ac1a8665f62a3e6/ppocr/postprocess/rec_postprocess.py#L143-L163
  
  - 官方代码中默认只获取第一个重复项，没考虑重复项置信度是不一样的，导致识别是正确的，但有时置信度却异常低（为了保证效率）。本文修改为返回正确值的最高的置信度（任务所需）。
  https://github.com/haoxia1/PaddleOCR/blob/e52c8f07928f85065ff471fe8ac1a8665f62a3e6/ppocr/postprocess/rec_postprocess.py#L77-L102
  
- add `inferTopK.py`

from ultralytics import YOLO

# 加载模型
model = YOLO("yolov8n.pt")

# 识别图片
results = model("my_test.jpg")

# 关键！把画好框的图，存成当前文件夹的 test_result.jpg
results[0].save("test_result.jpg")
print("图片已保存！去左边找！")
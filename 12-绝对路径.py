# 图片显示程序
# 
# 使用OpenCV库读取并显示图片
# 主要功能：读取指定路径的图片并在窗口中显示
# 
# 输入参数：
#   img_path: 图片的绝对路径
# 输出：
#   显示图片窗口

import cv2

# 定义图片路径
img_path = "C:\Opencv\sun.jpg"

# 读取图片
img = cv2.imread(img_path)

# 检查图片是否成功读取
if img is None:
    print("错误：无法读取图片，请检查图片路径是否正确")
else:
    # 显示图片
    cv2.imshow('image', img)
    # 等待按键，按任意键关闭窗口
    cv2.waitKey(0)
    # 关闭所有窗口
    cv2.destroyAllWindows()

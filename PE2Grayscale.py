import cv2
import os
import numpy as np
from math import sqrt,ceil

current_dir = os.getcwd()
files_in_dir = os.listdir(current_dir)

for input_file_name in files_in_dir:

# input_file_name = 'rufus-4.4.exe'
# mở file ở chế độ nhị phân
    with open(input_file_name,'rb') as binary_file:
        data = binary_file.read()
    data_len = len(data)
    # Chuyển dữ liệu nhị phân thành một mảng các số nguyên không dấu 8 bit
    d = np.frombuffer(data,dtype=np.uint8)
    sqrt_len = int(ceil(sqrt(data_len)))
    new_len = sqrt_len*sqrt_len
    pad_len = new_len - data_len
    # Thêm các giá trị 0 vào cuối mảng dữ liệu để làm đầy kích thước
    padded_d = np.hstack((d, np.zeros(pad_len, np.uint8)))
    # Định hình lại mảng dữ liệu đã được thêm giá trị 0 thành ma trận 2 chiều
    im = np.reshape(padded_d, (sqrt_len, sqrt_len))
    im = cv2.resize(im,(256,256),interpolation= cv2.INTER_AREA )
    cv2.imwrite('D:/UIT/Nam2/security/DOAN/sample/'+input_file_name +'.png',im)
print('The file is saved.')
# cv2.imshow('im',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

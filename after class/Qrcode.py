""" import qrcode
img = qrcode.make("Vanakkam thamizha")
img.save("swetha.jpg")
 """
import qrcode
img = qrcode.make("printer than make")
img.save("python.jpg")
""" 
#pip install opencv-python
import cv2
qr_img = cv2.imread("123.jpg")
qr_det = cv2.QRCodeDetector()
val, pts, st_code = qr_det.detectAndDecode(qr_img)
print("Information:", val)
 """
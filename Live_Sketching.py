import cv2
import tkinter as tk
from PIL import Image, ImageTk

def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_kernel_size_value = blur_kernel_size.get()
    if blur_kernel_size_value % 2 == 0:  # Ensure odd kernel size
        blur_kernel_size_value += 1
    img_gray_blur = cv2.GaussianBlur(img_gray, (blur_kernel_size_value, blur_kernel_size_value), 0)
    canny_edges = cv2.Canny(img_gray_blur, canny_threshold1.get(), canny_threshold2.get())
    ret, mask = cv2.threshold(canny_edges, threshold_value.get(), 255, cv2.THRESH_BINARY_INV)
    return mask

def update_frame():
    ret, frame = cap.read()
    sketch_image = cv2.cvtColor(sketch(frame), cv2.COLOR_GRAY2RGB)
    img = Image.fromarray(sketch_image)
    imgtk = ImageTk.PhotoImage(image=img)
    label_img.imgtk = imgtk
    label_img.configure(image=imgtk)
    label_img.after(10, update_frame)

cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("ScorpionTaj - Sketching Application")

blur_kernel_size = tk.IntVar(value=5)
canny_threshold1 = tk.IntVar(value=10)
canny_threshold2 = tk.IntVar(value=70)
threshold_value = tk.IntVar(value=70)

frame_controls = tk.Frame(root)
frame_controls.pack(side=tk.BOTTOM)

tk.Label(frame_controls, text="Blur Kernel Size").pack(side=tk.LEFT)
tk.Scale(frame_controls, variable=blur_kernel_size, from_=1, to=15, orient=tk.HORIZONTAL).pack(side=tk.LEFT)

tk.Label(frame_controls, text="Canny Threshold 1").pack(side=tk.LEFT)
tk.Scale(frame_controls, variable=canny_threshold1, from_=1, to=200, orient=tk.HORIZONTAL).pack(side=tk.LEFT)

tk.Label(frame_controls, text="Canny Threshold 2").pack(side=tk.LEFT)
tk.Scale(frame_controls, variable=canny_threshold2, from_=1, to=200, orient=tk.HORIZONTAL).pack(side=tk.LEFT)

tk.Label(frame_controls, text="Threshold Value").pack(side=tk.LEFT)
tk.Scale(frame_controls, variable=threshold_value, from_=1, to=255, orient=tk.HORIZONTAL).pack(side=tk.LEFT)

label_img = tk.Label(root)
label_img.pack()

update_frame()

root.mainloop()

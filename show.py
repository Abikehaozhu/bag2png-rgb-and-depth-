"""通过观察图像证明了彩色图像与深度图像配准"""
import cv2 as cv

if __name__ == '__main__':
    for i in range(2400):
        img = cv.imread(f"rgb\\{i}.png")
        depth = cv.imread(f"depth\\{i}.png")
        cv.imshow("rgb", img)
        cv.imshow("depth", depth)
        if cv.waitKey(30) == 27:
            break

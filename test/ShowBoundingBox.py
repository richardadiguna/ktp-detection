import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def face_coord(faces):
    return faces[:1][0]


def ktp_coord(ktps):
    if len(ktps) > 1:
        ktp = np.mean(ktps, axis=0, dtype=int)
        return ktp
    else:
        return ktps[0]


def define_position(ktp_position, face_position):
    kx, ky, kw, kh = ktp_position
    fx, fy, fw, fh = face_position

    c_x = (fx + (fx + fw)) / 2
    c_y = (fy + (fy + fh)) / 2

    br_x = fx+fw
    br_y = fy+fh

    tr_x = fx+fw
    tr_y = fy

    bl_x = fx
    bl_y = fy+fh

    if kx < c_x:
        if ky < c_y:
            if kx >= fx:
                return "Top"
            else:
                return "Left"
        else:
            if kx >= bl_x:
                return "Bottom"
            else:
                return "Left"
    else:
        if ky < c_y:
            if kx <= tr_x:
                return "Top"
            else:
                return "Right"
        else:
            if kx <= br_x:
                return "Bottom"
            else:
                return "Right"


def plot_image(image, ktp_position,
               face_position, position_desc):
    font = cv2.FONT_HERSHEY_SIMPLEX
    kx, ky, kw, kh = ktp_position
    fx, fy, fw, fh = face_position
    cv2.rectangle(
        image,
        (kx, ky),
        (kx + kw, ky + kh),
        (255, 0, 0), 2)
    cv2.rectangle(
        image,
        (fx, fy),
        (fx + fw, fy + fh),
        (0, 255, 0), 2)
    cv2.putText(
        image,
        position_desc,
        (kx - 5, ky - 5),
        font, 0.7,
        (255, 255, 0), 2,
        cv2.LINE_AA)
    return image


def classify_object_in(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ktpCascade = cv2.CascadeClassifier('trainedclassifier/ktpcascade.xml')
    faceCascade = cv2.CascadeClassifier('trainedclassifier/facecascade.xml')

    faces = faceCascade.detectMultiScale(gray, 1.1, 5)
    ktps = ktpCascade.detectMultiScale(gray, 1.1, 5)

    ktp_position = ktp_coord(ktps)
    face_position = face_coord(faces)

    position = define_position(
        ktp_position,
        face_position)
    new_image = plot_image(
        image,
        ktp_position,
        face_position,
        position)

    return new_image


def classify_all_test_images():
    for image in os.listdir('test/images'):
        im = cv2.imread('test/images/' + image)
        new_image = classify_object_in(im)
        plt.imshow(new_image)
        plt.show()


if __name__ == '__main__':
    classify_all_test_images()

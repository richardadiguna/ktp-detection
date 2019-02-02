#!/bin/sh
opencv_createsamples -img haardataset/transformed/positive/1.jpg -bg haardataset/transformed/bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 600
opencv_createsamples -info info/info.lst -num 600 -w 20 -h 20 -vec vector/positives.vec
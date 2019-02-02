#!/bin/sh
opencv_traincascade -data trainedclassifier -vec vector/positives.vec -bg bg.txt -numPos 500 -numNeg 250 -numStages 10 -w 20 -h 20


# Some good source of parameter description:
# - http://answers.opencv.org/question/84852/traincascades-error-required-leaf-false-alarm-rate-achieved-branch-training-terminated/
import numpy
import cv2 as cv
videoHandler = cv.VideoCapture("STATIC.mov")
succeed, inputImage=videoHandler.read()
retina = cv.bioinspired_Retina.create((inputImage.shape[1], 
inputImage.shape[0]))
retina.write('retinaParams.xml')
stillProcess=True
while stillProcess is True:
    stillProcess, inputImage=videoHandler.read()
    retina.run(inputImage)
    retinaOut_magno=retina.getMagno()
    ret1,th1 = cv.threshold(retinaOut_magno,150,255,cv.THRESH_BINARY)
    
    cv.imshow('retina magno out', th1)

    cnts = cv.findContours(th1.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[1]
    for c in cnts:

            rect = cv.minAreaRect(c)
            box = cv.boxPoints(rect)
            box = numpy.int0(box)
            center = (int(rect[0][0]),int(rect[0][1]))
            cv.drawContours(inputImage,[box],0,(0,0,255),5)

            cv.imshow("MEOW",inputImage)
    cv.waitKey(1)


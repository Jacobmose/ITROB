#!/usr/bin/env python
import cv2
import urllib
import numpy as np

class Recognition:
		""" Used for recognising the bricks """
				
		def fetch_image_from_webcam(self):
			"""
			Fetches an image from the webcam
			"""
			print "try fetch from webcam..."
			stream=urllib.urlopen('http://192.168.0.20/image/jpeg.cgi')
			bytes=''
			bytes+=stream.read(64500)
			a = bytes.find('\xff\xd8')
			b = bytes.find('\xff\xd9')
		
			if a != -1 and b != -1:
				jpg = bytes[a:b+2]
				bytes= bytes[b+2:]
				i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
				return i
			else:
				print "did not receive image, try increasing the buffer size in line 13:" 
				
		def get_from_file(self,filename):
			"""
			Loads image from file
			"""
			print "loading from file..."
			return cv2.imread(filename)
						
		def extract_single_color_mean(self,image,hsv,lower,upper):
			
			mask = cv2.inRange(hsv, lower, upper)
									
			mean = cv2.mean(image, mask = mask)
			
			return mean

		def show_bricks(self,image,bricks,color):
			for b in bricks:
				cv2.drawContours(image,[b],0,color,2)
		
		def detect_brick_center(self, cnt):
			M = cv2.moments(cnt)
			center_x = int(M['m10']/M['m00'])
			center_y = int(M['m01']/M['m00'])
			return center_x,center_y
			
		
		def detect_brick(self, image, lower, upper, debug = False):
		
			crop_img = image[40:387, 6:612]
			
			blurimg = cv2.medianBlur(crop_img,5)
			
			grayimg = cv2.cvtColor(blurimg, cv2.COLOR_BGR2GRAY)
			
			edges = cv2.Canny(grayimg, 40, 100, grayimg)
			if debug: cv2.imshow('edges',grayimg)
			
			ret,th1 = cv2.threshold(grayimg,40,255,cv2.THRESH_BINARY)
			resdi = cv2.dilate(th1,np.ones((3,3),np.uint8))
			if debug: cv2.imshow('threshold',th1)
			closing = cv2.morphologyEx(resdi, cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
			
			if debug: cv2.imshow('closing',closing)
			
			contours,hierachy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
					
			returnbrick = ()
			bricks = []
						
			for cnt in contours:				
				epsilon = 0.1*cv2.arcLength(cnt,True)
				approx = cv2.approxPolyDP(cnt,epsilon,True)
				rect = cv2.minAreaRect(approx)								
				area = cv2.contourArea(approx)				
				box = cv2.cv.BoxPoints(rect)
				box = box = np.int0(box)
				if area > 700 and area < 1800:					
					x,y = self.detect_brick_center(cnt)
					x_bound,y_bound,w,h = cv2.boundingRect(cnt)
					cropimg = crop_img[y_bound:y_bound+h,x_bound:x_bound+w]										
					hsv = cv2.cvtColor(cropimg, cv2.COLOR_BGR2HSV)
					color = self.extract_single_color_mean(cropimg, hsv, lower, upper)					
					colorarray = np.asarray(color, np.uint8)
					colorarray = np.delete(colorarray, len(colorarray)-1)
					bricks.append(box)
					if np.count_nonzero(colorarray) > 0:
						if debug: cv2.imshow('single brick', cropimg)					
						returnbrick = (x,y,colorarray)
			
			if debug: print(returnbrick)
			
			return returnbrick
		
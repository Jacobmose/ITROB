#!/usr/bin/env python

from qrtools import QR

class QRfuncs:
        
        def create_qr_image(self, brickcolor, debug = False):
            qr_creator = QR(data=u"pattern" + brickcolor + "", pixel_size=10)
            qr_creator.encode("pattern" + brickcolor + ".png")
            if debug: print(qr_creator.filename)
            
            return qr_creator.filename
            
        def decode_qr_code(self):
            qr_reader = QR()
            qr_reader.decode_webcam(None, "http://192.168.0.20/video.cgi")

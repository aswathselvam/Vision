import cv2
import numpy as np

class MeanShift:
    def __init__(self,image):
        self.h = image.shape[0]
        self.w = image.shape[1]
        self.image = image
        self.windowSize = 2
        self.THRESHOLD = 10
        pass
    
    def classify(self):
        classes = {}

        for pixel_i in range(self.h):
            for pixel_j in range(self.w):
                window_center_i = pixel_i
                window_center_j = pixel_j
                prev_mean= float('inf')
                mean = 0
                while(abs(prev_mean-mean)>self.THRESHOLD):
                    prev_mean = mean
                    x,dx= window_center_i, self.windowSize
                    y,dy= window_center_j, self.windowSize
                    feature = self.image[x:x+dx, y:y+dy]
                    # print(feature)
                    feature = feature - mean
                    # print("Relative featre:\n ",feature)
                    norm = np.linalg.norm(feature,axis=2)
                    # norm = feature.sum(axis=2)
                    # norm = feature/norm[:,np.newaxis]
                    # print("Norm:\n",norm)
                    x_range = np.arange(x,x+dx, 1, dtype=int)
                    y_range = np.arange(y,y+dy, 1, dtype=int)
                    total_norm = np.linalg.norm(norm)*5
                    weighted_distance_x = x_range * norm/total_norm
                    weighted_distance_y = y_range *norm/total_norm
                    # print("weignted distance:\n",weighted_distance_x)

                    window_center_i =  int(np.mean(weighted_distance_x))
                    window_center_j =  int(np.mean(weighted_distance_y))
                    # print(window_center_i)
                    input(prev_mean-mean)
                
                prev_dist = float('inf')
                for mode,_ in classes.items():
                    dist = np.linalg(mean-mode)
                    if dist < prev_dist:
                        mean = mode
                classes[mean].append([pixel_i,pixel_j]) 
                
        pass



image = cv2.imread('./road_intersection.jpg')
image = cv2.resize(image,(500,500))

meanShift = MeanShift(image)
meanShift.classify()

cv2.imshow("image",image)
cv2.waitKey(0)
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
                prev_mean= np.array([float('inf'),float('inf')])
                mean =  np.array([0,0])
                while(any(abs(prev_mean-mean)>self.THRESHOLD)):
                    prev_mean = mean
                    x,dx= window_center_i, self.windowSize
                    y,dy= window_center_j, self.windowSize
                    feature = self.image[x:x+dx, y:y+dy]
                    # print(feature)
                    center_feature =  self.image[x, y]
                    feature = feature - center_feature
                    # print("Relative featre:\n ",feature)
                    norm = np.linalg.norm(feature,axis=2)
                    # norm = feature.sum(axis=2)
                    # norm = feature/norm[:,np.newaxis]
                    # print("Norm:\n",norm)
                    x_range = np.arange(x,x+dx, 1, dtype=int)
                    y_range = np.arange(y,y+dy, 1, dtype=int)
                    total_norm = np.linalg.norm(norm)/4
                    weighted_distance_x = x_range * norm/total_norm
                    weighted_distance_y = y_range *norm/total_norm
                    print("weignted distance:\n",weighted_distance_x)
                    print("weignted distance:\n",weighted_distance_y)

                    window_center_i =  int(np.mean(weighted_distance_x))
                    window_center_j =  int(np.mean(weighted_distance_y))
                    # print(window_center_i)
                    mean = np.array([window_center_i,window_center_j])
                    input(prev_mean-mean)
                
                prev_dist = float('inf')
                for mode,_ in classes.items():
                    if mode:
                        dist = np.linalg(mean-np.array(mode))
                        if dist < self.THRESHOLD:
                            prev_dist = mode
                if prev_dist == float('inf'):
                    classes[(mean[0],mean[1])] = [pixel_i,pixel_j]
                else:    
                    classes[(mean[0],mean[1])].append([pixel_i,pixel_j]) 
            
            print("Classes:\n",classes)

        pass



image = cv2.imread('./road_intersection.jpg')
image = cv2.resize(image,(500,500))

meanShift = MeanShift(image)
meanShift.classify()

cv2.imshow("image",image)
cv2.waitKey(0)
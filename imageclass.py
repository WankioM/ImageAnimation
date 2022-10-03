from turtle import ycor
import numpy as np
import png
import cv2

class Image:
    def __init__(self, x_pixels=0, y_pixels=0, filename=''):
        # you need to input either filename OR x_pixels, y_pixels, and num_channels
        self.input_path = 'pyphotoshop-main\input/'
        self.output_path = 'pyphotoshop-main\output/'
       
        self.x_pixels = x_pixels
        self.y_pixels = y_pixels
            
        self.array = np.zeros((x_pixels, y_pixels))


#Read original image          
im=cv2.imread(r"Animate\images\flag (1).png")
print(f"cv2 image is of type {type(im)} and size: {np.shape(im)} ")

#Change to 2D array and canny_edges
canny_edges=cv2.Canny(image=im, threshold1=100, threshold2=200)
print(f"cannied image is of type {type(canny_edges)} and size: {np.shape(canny_edges)} ")
print(f"Canny edges: {canny_edges}")


#pic=Image(canny_edges)
#print(type(pic))

manys=np.random.randint(255, size=(5,5))
ones=np.array([[0, 255, 0, 255,0],[ 255, 0,  0, 255,  255],[0,  255,  0,  255, 0],[255, 255,  0,  255, 0],[ 255, 0, 255, 0, 255]])
print(ones)

print(f"ones image is of type {type(ones)} and shape: {np.shape(ones)} ")

cv2.imwrite("ones.png",ones)

#Try loop through elements in the image matrice:


print("/n Next")

# find neighbouring pixel:
def get_neighbours(image, x_pixels, y_pixels, kernel=0):
    for x in range(x_pixels-1):
        for y in range(y_pixels-1):
            neighbour_coords=[[max(0, (x-1)),max(0,(y-1))],
            [max(0, (x-1)),y],
            [max(0, (x-1)), min((y_pixels-1),(y+2))]] # to finish array kernel....
            neighbour_coords=np.array(neighbour_coords)
            print(f"Image pixel is : {image[x,y]} at {x,y} and neighbour co-ords : {neighbour_coords}")
            return neighbour_coords

#find value at neighbour
def value_at_neighbour(image):
    x_pixels, y_pixels=np.shape(image)
    for x in range(x_pixels-1):
        for y in range(y_pixels-1):
            neighbour_coords=get_neighbours(image, x_pixels, y_pixels,kernel=0)
            neighbour_values=np.array(image[x,y])#empty array with shape of nighbour-co-ords array
            for z in neighbour_coords:
                neighbour_value = image[neighbour_coords[z]]
                #neighbour_values =np.append(neighbour_values, neighbour_value, axis=0)
        
            print(f"\n Neighbour values are: {neighbour_values}")

            



print("/n Next neighbours")
value_at_neighbour(ones)



# i think I may ned to remove the for in for in neighbour co-ords
"""empty=np.array([])
empty=np.append(empty,[2,3,5],axis=0)
empty=np.append(empty,[2,"gh",5],axis=0)


print(empty)
empty=np.array([3,4,5])

empty=np.append(empty,[[2,"gh",5],[2,7,8]],axis=0)
print(np.shape(empty), "Empty :", empty)"""

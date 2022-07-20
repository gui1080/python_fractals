import numpy as np
import matplotlib.pyplot as plt

from examples.mandel import mandelbrot

    
if __name__ == '__main__':
    
    print("Começo do script")
    
    output = mandelbrot(1000,1000,150)   
    
    print(output)
    plt.imshow(output.T, cmap = "hot")
    plt.axis("off")
    plt.show()
    
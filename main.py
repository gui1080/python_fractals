import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import yfinance as yahooFinance
from datetime import datetime, timedelta

from examples.mandel import mandelbrot

    
if __name__ == '__main__':
    
    print("Começo do script")
    
    hoje = datetime.today().strftime('%Y-%m-%d')
    ontem = datetime.today() - timedelta(days=1)
    
    ontem = ontem.strftime('%Y-%m-%d')
    
    #ibov = yf.Ticker("^BVSP")
    ibovespa = yahooFinance.Ticker("EWZ")
    
    print(ibovespa.history(start=ontem, end=hoje))
    
    output = mandelbrot(1000,1000,150)   
    
    #print(output)
    plt.imshow(output.T, cmap = "hot")
    plt.axis("off")
    plt.savefig("mandelbrot.png")
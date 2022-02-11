import numpy as np
import pandas as pd
import yfinance as yf

class Base_Data(object):



    def __init__(self, symbol, start, end , verbose=True):
            self.symbol = symbol
            self.start = start
            self.end = end
            self.position = 0
            self.verbose = verbose
            self.get_data()
    
    """def obtener_token(usuario, contraseña):
        
        
        
        return token"""

    def get_data(self):
        ''' Retrieves and prepares the data.
        '''
        raw = yf.download(f"{self.symbol}").dropna()
        raw = raw.loc[self.start:self.end]
        self.data = raw

if __name__ == '__main__':
    bb = Base_Data('AAPL', '2010-1-1', '2019-12-31', 10000)
import numpy as np
def float_range (start ,stop , step):
      """bilindiği üzere range fonksiyonunda step değeri tam sayı olmalı fakat
      numpy modülünün arange metodunda step değeri kesirli sayı olabilir """
      return np.arange(start,stop,step)
# deneyelim
print(float_range(7,77,5.5))
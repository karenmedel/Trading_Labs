import pandas as pd
import numpy as np
import datetime
a = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)), columns=['a', 'b', 'c', 'd', 'e'])
a.to_csv('/Users/pablomendoza/Documents/ITESO/Trading/Lab_1/ITESO/MYST_LABs/cos' + str(datetime.datetime.now()) + '.csv')

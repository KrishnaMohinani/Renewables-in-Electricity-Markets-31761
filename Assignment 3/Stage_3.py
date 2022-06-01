## Data preparation
import numpy
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('Stage_3.xlsx', 'Power-Previous' )

data_2015 = data [0:672]
data_2016 = data [672:1368]
data_2017 = data [1368:2040]

## 2015 polynomial regression of order 2
x_2015 =(data_2015['WS100'][0:673])
y_2015 =(data_2015['Power'][0:673])

poly_2015 = numpy.poly1d(numpy.polyfit(x_2015, y_2015, 6))

polyline_2015 = numpy.linspace(0.616165, 21.1732, 100)

plt.scatter(x_2015, y_2015,color='pink')
plt.plot(polyline_2015, poly_2015(polyline_2015),color='red')
plt.show() 
print(poly_2015)

## 2016 polynomial regression of order 2
x_2016 =(data_2016['WS100'][0:1368])
y_2016 =(data_2016['Power'][0:1368])

poly_2016 = numpy.poly1d(numpy.polyfit(x_2016, y_2016, 6))

polyline_2016 = numpy.linspace(0.234608, 23.8686, 100)

plt.scatter(x_2016, y_2016, color='pink')
plt.plot(polyline_2016, poly_2016(polyline_2016),color='red')
plt.show() 
print(poly_2016)

## 2017 polynomial regression of order 2
x_2017 =(data_2017['WS100'][0:2040])
y_2017 =(data_2017['Power'][0:2040])
x_new_2017 = x_2017[1:672]
y_new_2017 = y_2017[1:672]

poly_2017 = numpy.poly1d(numpy.polyfit(x_new_2017, y_new_2017, 6))

polyline_2017 = numpy.linspace(2.1, 22.9, 40)

plt.scatter(x_new_2017, y_new_2017,color='pink')
plt.plot(polyline_2017, poly_2017(polyline_2017),color='red')
plt.show() 
print(poly_2017)





                        



## Data preparation
import numpy
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('stage_2.xlsx', 'Trendline' )

data_2015 = data [0:664]
data_2016 = data [664:1384]
data_2017 = data [1384:2103]

## 2015 polynomial regression of order 2
x_2015 =(data_2015['WS100'][0:664])
y_2015 =(data_2015['POWER'][0:664])

poly_2015 = numpy.poly1d(numpy.polyfit(x_2015, y_2015, 2))

polyline_2015 = numpy.linspace(1, 26.9805, 100)

plt.scatter(x_2015, y_2015,color='pink')
plt.plot(polyline_2015, poly_2015(polyline_2015),color='red')
plt.show() 
print(poly_2015)

## 2016 polynomial regression of order 2
x_2016 =(data_2016['WS100'][0:1384])
y_2016 =(data_2016['POWER'][0:1384])

poly_2016 = numpy.poly1d(numpy.polyfit(x_2016, y_2016, 2))

polyline_2016 = numpy.linspace(1, 20, 100)

plt.scatter(x_2016, y_2016, color='pink')
plt.plot(polyline_2016, poly_2016(polyline_2016),color='red')
plt.show() 
print(poly_2016)

## 2017 polynomial regression of order 2
x_2017 =(data_2017['WS100'][0:2103])
y_2017 =(data_2017['POWER'][0:2103])

poly_2017 = numpy.poly1d(numpy.polyfit(x_2017, y_2017, 2))

polyline_2017 = numpy.linspace(1, 24.8179, 100)

plt.scatter(x_2017, y_2017,color='pink')
plt.plot(polyline_2017, poly_2017(polyline_2017),color='red')
plt.show() 
print(poly_2017)



#Improved forecast (wind speed of WS70. 2016 - Poly 3 and 2017 - Poly 2)

### Data preparation
#import numpy
#import pandas as pd
#import matplotlib.pyplot as plt
#data = pd.read_excel('stage_2.xlsx', 'Trendline' )
#
#data_2015 = data [0:664]
#data_2016 = data [664:1384]
#data_2017 = data [1384:2103]
#
### 2015 polynomial regression of order 2
#x_2015 =(data_2015['WS70'][0:664])
#y_2015 =(data_2015['POWER'][0:664])
#
#poly_2015 = numpy.poly1d(numpy.polyfit(x_2015, y_2015, 2))
#
#polyline_2015 = numpy.linspace(1, 26.9805, 100)
#
#plt.scatter(x_2015, y_2015,color='pink')
#plt.plot(polyline_2015, poly_2015(polyline_2015),color='red')
#plt.show() 
#print(poly_2015)
#
### 2016 polynomial regression of order 3
#x_2016 =(data_2016['WS70'][0:1384])
#y_2016 =(data_2016['POWER'][0:1384])
#
#poly_2016 = numpy.poly1d(numpy.polyfit(x_2016, y_2016, 3))
#
#polyline_2016 = numpy.linspace(1, 20, 100)
#
#plt.scatter(x_2016, y_2016, color='pink')
#plt.plot(polyline_2016, poly_2016(polyline_2016),color='red')
#plt.show() 
#print(poly_2016)
#
### 2017 polynomial regression of order 2
#x_2017 =(data_2017['WS70'][0:2103])
#y_2017 =(data_2017['POWER'][0:2103])
#
#poly_2017 = numpy.poly1d(numpy.polyfit(x_2017, y_2017, 2))
#
#polyline_2017 = numpy.linspace(1, 24.8179, 100)
#
#plt.scatter(x_2017, y_2017,color='pink')
#plt.plot(polyline_2017, poly_2017(polyline_2017),color='red')
#plt.show() 
#print(poly_2017)






                        



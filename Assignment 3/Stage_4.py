## Data preparation
import numpy
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('Stage_4.xlsx', 'Trendline' )

data_2015 = data [0:744]
data_2016 = data [744:1488]
data_2017 = data [1488:2232]

## 2015 polynomial regression of order 2
x_2015 =(data_2015['WS 70'][0:744])
y_2015 =(data_2015['POWER'][0:744])

#poly_2015 = numpy.poly1d(numpy.polyfit(x_2015, y_2015, 3))
#
#polyline_2015 = numpy.linspace(0.116165, 17, 100)
#
#plt.scatter(x_2015, y_2015,color='pink')
#plt.plot(polyline_2015, poly_2015(polyline_2015),color='red')
#plt.show() 
#print(poly_2015)

## 2016 polynomial regression of order 2
x_2016 =(data_2016['WS 70'][0:1488])
y_2016 =(data_2016['POWER'][0:1488])

#poly_2016 = numpy.poly1d(numpy.polyfit(x_2016, y_2016, 3))
#
#polyline_2016 = numpy.linspace(0.234608, 20 , 100)
#
#plt.scatter(x_2016, y_2016, color='pink')
#plt.plot(polyline_2016, poly_2016(polyline_2016),color='red')
#plt.show() 
#print(poly_2016)

## 2017 polynomial regression of order 2
x_2017 =(data_2017['WS 70'][0:2232])
y_2017 =(data_2017['POWER'][0:2232])

#poly_2017 = numpy.poly1d(numpy.polyfit(x_2017, y_2017, 3))
#
#polyline_2017 = numpy.linspace(0.5, 16, 100)
#
#plt.scatter(x_2017, y_2017,color='pink')
#plt.plot(polyline_2017, poly_2017(polyline_2017),color='red')
#plt.show() 
#print(poly_2017)


## DAY 1 
x_day1 = x_2017[0:24]
y_day1 = y_2017[0:24]

poly_day1 = numpy.poly1d(numpy.polyfit(x_day1, y_day1, 2))

polyline_day1 = numpy.linspace(6, 16.5, 100)

#plt.scatter(x_day1, y_day1,color='pink')
#plt.plot(polyline_day1, poly_day1(polyline_day1),color='red')
#plt.show() 
print(poly_day1)

## DAY 2 
x_day2 = x_2015[24:48]
y_day2 = y_2015[24:48]

poly_day2 = numpy.poly1d(numpy.polyfit(x_day2, y_day2, 2))

polyline_day2 = numpy.linspace(6, 12.5, 100)

#plt.scatter(x_day2, y_day2 ,color='pink')
#plt.plot(polyline_day2, poly_day2(polyline_day2),color='red')
#plt.show() 
print(poly_day2)

## DAY 3 
x_day3 = x_2015[48:72]
y_day3 = y_2015[48:72]

poly_day3 = numpy.poly1d(numpy.polyfit(x_day3, y_day3, 2))

polyline_day3 = numpy.linspace(5.8, 12.5, 100)

#plt.scatter(x_day3, y_day3 ,color='pink')
#plt.plot(polyline_day3, poly_day3(polyline_day3),color='red')
#plt.show() 
print(poly_day3)
                        
## DAY 4 
x_day4 = x_2017[72:96]
y_day4 = y_2017[72:96]

poly_day4 = numpy.poly1d(numpy.polyfit(x_day4, y_day4, 2))

polyline_day4 = numpy.linspace(5, 10.7, 100)

#plt.scatter(x_day4, y_day4 ,color='pink')
#plt.plot(polyline_day4, poly_day4(polyline_day4),color='red')
#plt.show() 
print(poly_day4)

## DAY 5 
x_day5 = x_2017[96:120]
y_day5 = y_2017[96:120]

poly_day5 = numpy.poly1d(numpy.polyfit(x_day5, y_day5, 2))

polyline_day5 = numpy.linspace(4.8, 10.1, 100)

#plt.scatter(x_day5, y_day5 ,color='pink')
#plt.plot(polyline_day5, poly_day5(polyline_day5),color='red')
#plt.show() 
print(poly_day5)

## DAY 6 
x_day6 = x_2016[120:144]
y_day6 = y_2016[120:144]

poly_day6 = numpy.poly1d(numpy.polyfit(x_day6, y_day6, 2))

polyline_day6 = numpy.linspace(0, 4.7, 100)

#plt.scatter(x_day6, y_day6 ,color='pink')
#plt.plot(polyline_day6, poly_day6(polyline_day6),color='red')
#plt.show() 
print(poly_day6)

## DAY 7 
x_day7 = x_2017[144:168]
y_day7 = y_2017[144:168]

poly_day7 = numpy.poly1d(numpy.polyfit(x_day7, y_day7, 2))

polyline_day7 = numpy.linspace(2, 8.5, 100)

#plt.scatter(x_day7, y_day7 ,color='pink')
#plt.plot(polyline_day7, poly_day7(polyline_day7),color='red')
#plt.show() 
print(poly_day7)

## DAY 8 
x_day8 = x_2016[168:192]
y_day8 = y_2016[168:192]

poly_day8 = numpy.poly1d(numpy.polyfit(x_day8, y_day8, 2))

polyline_day8 = numpy.linspace(1.6, 7, 100)

#plt.scatter(x_day8, y_day8 ,color='pink')
#plt.plot(polyline_day8, poly_day8(polyline_day8),color='red')
#plt.show() 
print(poly_day8)

## DAY 9 
x_day9 = x_2016[192:216]
y_day9 = y_2016[192:216]

poly_day9 = numpy.poly1d(numpy.polyfit(x_day9, y_day9, 2))

polyline_day9 = numpy.linspace(4.8, 10.1, 100)

#plt.scatter(x_day9, y_day9 ,color='pink')
#plt.plot(polyline_day9, poly_day9(polyline_day9),color='red')
#plt.show() 
print(poly_day9)

## DAY 10 
x_day10 = x_2015[216:240]
y_day10 = y_2015[216:240]

poly_day10 = numpy.poly1d(numpy.polyfit(x_day10, y_day10, 2))

polyline_day10 = numpy.linspace(9.9, 12.2 , 100)

#plt.scatter(x_day10, y_day10 ,color='pink')
#plt.plot(polyline_day10, poly_day10(polyline_day10),color='red')
#plt.show() 
print(poly_day10)

## DAY 11 
x_day11 = x_2017[240:264]
y_day11 = y_2017[240:264]

poly_day11 = numpy.poly1d(numpy.polyfit(x_day11, y_day11, 2))

polyline_day11 = numpy.linspace(4, 9.5 , 100)

#plt.scatter(x_day11, y_day11 ,color='pink')
#plt.plot(polyline_day11, poly_day11(polyline_day11),color='red')
#plt.show() 
print(poly_day11)

## DAY 12 
x_day12 = x_2016[264:288]
y_day12 = y_2016[264:288]

poly_day12 = numpy.poly1d(numpy.polyfit(x_day12, y_day12, 2))

polyline_day12 = numpy.linspace(0, 6 , 100)

#plt.scatter(x_day12, y_day12 ,color='pink')
#plt.plot(polyline_day12, poly_day12(polyline_day12),color='red')
#plt.show() 
print(poly_day12)

## DAY 13 
x_day13 = x_2015[288:312]
y_day13 = y_2015[288:312]

poly_day13 = numpy.poly1d(numpy.polyfit(x_day13, y_day13, 2))

polyline_day13 = numpy.linspace(6, 8.5 , 100)

#plt.scatter(x_day13, y_day13 ,color='pink')
#plt.plot(polyline_day13, poly_day13(polyline_day13),color='red')
#plt.show() 
print(poly_day13)

## DAY 14 
x_day14 = x_2016[312:336]
y_day14 = y_2016[312:336]

poly_day14 = numpy.poly1d(numpy.polyfit(x_day14, y_day14, 2))

polyline_day14 = numpy.linspace(3.5, 7.1, 100)

#plt.scatter(x_day14, y_day14 ,color='pink')
#plt.plot(polyline_day14, poly_day14(polyline_day14),color='red')
#plt.show() 
print(poly_day14)

## DAY 15 
x_day15 = x_2017[336:360]
y_day15 = y_2017[336:360]

poly_day15 = numpy.poly1d(numpy.polyfit(x_day15, y_day15, 2))

polyline_day15 = numpy.linspace(14, 8.5, 100)

#plt.scatter(x_day15, y_day15 ,color='pink')
#plt.plot(polyline_day15, poly_day15(polyline_day15),color='red')
#plt.show() 
print(poly_day15)

## DAY 16 
x_day16 = x_2015[360:384]
y_day16 = y_2015[360:384]

poly_day16 = numpy.poly1d(numpy.polyfit(x_day16, y_day16, 3))

polyline_day16 = numpy.linspace(8.75, 10.3, 100)

#plt.scatter(x_day16, y_day16 ,color='pink')
#plt.plot(polyline_day16, poly_day16(polyline_day16),color='red')
#plt.show() 
print(poly_day16)

## DAY 17 
x_day17 = x_2017[384:408]
y_day17 = y_2017[384:408]

poly_day17 = numpy.poly1d(numpy.polyfit(x_day17, y_day17, 2))

polyline_day17 = numpy.linspace(4, 14, 100)

#plt.scatter(x_day17, y_day17 ,color='pink')
#plt.plot(polyline_day17, poly_day17(polyline_day17),color='red')
#plt.show() 
print(poly_day17)

## DAY 18 
x_day18 = x_2016[408:432]
y_day18 = y_2016[408:432]

poly_day18 = numpy.poly1d(numpy.polyfit(x_day18, y_day18, 2))

polyline_day18 = numpy.linspace(4, 12, 100)

#plt.scatter(x_day18, y_day18 ,color='pink')
#plt.plot(polyline_day18, poly_day18(polyline_day18),color='red')
#plt.show() 
print(poly_day18)

## DAY 19 
x_day19 = x_2016[432:456]
y_day19 = y_2016[432:456]

poly_day19 = numpy.poly1d(numpy.polyfit(x_day19, y_day19, 2))

polyline_day19 = numpy.linspace(3.5, 14.1, 100)

#plt.scatter(x_day19, y_day19 ,color='pink')
#plt.plot(polyline_day19, poly_day19(polyline_day19),color='red')
#plt.show() 
print(poly_day19)

## DAY 20 
x_day20 = x_2015[456:480]
y_day20 = y_2015[456:480]

poly_day20 = numpy.poly1d(numpy.polyfit(x_day20, y_day20, 2))

polyline_day20 = numpy.linspace(4, 9, 100)

#plt.scatter(x_day20, y_day20 ,color='pink')
#plt.plot(polyline_day20, poly_day20(polyline_day20),color='red')
#plt.show() 
print(poly_day20)

## DAY 21 
x_day21 = x_2015[480:504]
y_day21 = y_2015[480:504]

poly_day21 = numpy.poly1d(numpy.polyfit(x_day21, y_day21, 2))

polyline_day21 = numpy.linspace(3, 13.1, 100)

#plt.scatter(x_day21, y_day21 ,color='pink')
#plt.plot(polyline_day21, poly_day21(polyline_day21),color='red')
#plt.show() 
print(poly_day21)

## DAY 22 
x_day22 = x_2017[504:528]
y_day22 = y_2017[504:528]

poly_day22 = numpy.poly1d(numpy.polyfit(x_day22, y_day22, 2))

polyline_day22 = numpy.linspace(0, 13.5, 100)

#plt.scatter(x_day22, y_day22 ,color='pink')
#plt.plot(polyline_day22, poly_day22(polyline_day22),color='red')
#plt.show() 
print(poly_day22)

## DAY 23 
x_day23 = x_2017[528:552]
y_day23 = y_2017[528:552]

poly_day23 = numpy.poly1d(numpy.polyfit(x_day23, y_day23, 2))

polyline_day23 = numpy.linspace(3, 9, 100)

#plt.scatter(x_day23, y_day23 ,color='pink')
#plt.plot(polyline_day23, poly_day23(polyline_day23),color='red')
#plt.show() 
print(poly_day23)

## DAY 24 
x_day24 = x_2017[552:576]
y_day24 = y_2017[552:576]

poly_day24 = numpy.poly1d(numpy.polyfit(x_day24, y_day24, 2))

polyline_day24 = numpy.linspace(2, 8, 100)

#plt.scatter(x_day24, y_day24 ,color='pink')
#plt.plot(polyline_day24, poly_day24(polyline_day24),color='red')
#plt.show() 
print(poly_day24)

## DAY 25
x_day25 = x_2015[576:600]
y_day25 = y_2015[576:600]

poly_day25 = numpy.poly1d(numpy.polyfit(x_day25, y_day25, 2))

polyline_day25 = numpy.linspace(1, 10, 100)

#plt.scatter(x_day25, y_day25 ,color='pink')
#plt.plot(polyline_day25, poly_day25(polyline_day25),color='red')
#plt.show() 
print(poly_day25)

## DAY 26
x_day26 = x_2015[600:624]
y_day26 = y_2015[600:624]

poly_day26 = numpy.poly1d(numpy.polyfit(x_day26, y_day26, 2))

polyline_day26 = numpy.linspace(3.7, 8, 100)

#plt.scatter(x_day26, y_day26 ,color='pink')
#plt.plot(polyline_day26, poly_day26(polyline_day26),color='red')
#plt.show() 
print(poly_day26)

## DAY 27
x_day27 = x_2017[624:648]
y_day27 = y_2017[624:648]

poly_day27 = numpy.poly1d(numpy.polyfit(x_day27, y_day27, 2))

polyline_day27 = numpy.linspace(3.7, 6.1, 100)

#plt.scatter(x_day27, y_day27 ,color='pink')
#plt.plot(polyline_day27, poly_day27(polyline_day27),color='red')
#plt.show() 
print(poly_day27)

## DAY 28
x_day28 = x_2016[648:672]
y_day28 = y_2016[648:672]

poly_day28 = numpy.poly1d(numpy.polyfit(x_day28, y_day28, 2))

polyline_day28 = numpy.linspace(11, 19, 100)

#plt.scatter(x_day28, y_day28 ,color='pink')
#plt.plot(polyline_day28, poly_day28(polyline_day28),color='red')
#plt.show() 
print(poly_day28)

## DAY 29
x_day29 = x_2015[672:696]
y_day29 = y_2015[672:696]

poly_day29 = numpy.poly1d(numpy.polyfit(x_day29, y_day29, 2))

polyline_day29 = numpy.linspace(6, 10, 100)

#plt.scatter(x_day29, y_day29 ,color='pink')
#plt.plot(polyline_day29, poly_day29(polyline_day29),color='red')
#plt.show() 
print(poly_day29)

## DAY 30
x_day30 = x_2016[696:720]
y_day30 = y_2016[696:720]

poly_day30 = numpy.poly1d(numpy.polyfit(x_day30, y_day30, 2))

polyline_day30 = numpy.linspace(4, 11, 100)

#plt.scatter(x_day30, y_day30 ,color='pink')
#plt.plot(polyline_day30, poly_day30(polyline_day30),color='red')
#plt.show() 
print(poly_day30)

## DAY 31
x_day31 = x_2016[720:744]
y_day31 = y_2016[720:744]

poly_day31 = numpy.poly1d(numpy.polyfit(x_day31, y_day31, 2))

polyline_day31 = numpy.linspace(6, 9, 100)

#plt.scatter(x_day31, y_day31 ,color='pink')
#plt.plot(polyline_day31, poly_day31(polyline_day31),color='red')
#plt.show() 
print(poly_day31)











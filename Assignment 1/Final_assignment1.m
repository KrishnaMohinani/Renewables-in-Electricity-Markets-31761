T1 = readtable('Directory.xlsx');  %reading the excel file Directory.xlsx
A = eye(22); 
f = [24 62 72 80 87 150 260 0 -17 17 44 40 37 32 5 12 235 -500 -12 0 261 236];  
Aeq = -[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0; 0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,-1,0,1]; % A equivalent
lb =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-600,0,0]; % lower bounds of all generators,transmission and load shedding
P=zeros(2,1464);
U=zeros(22,1464);

for j = 1:1:1464
WW1 = T1.WW1;
ww1 = WW1(j);
WW2 = T1.WW2;
ww2 = WW2(j);
NN = T1.Nuke_west;
nuke_west = NN(j);
EW1 = T1.EW1;
ew1 = EW1(j);
EW2 = T1.EW2;
ew2 = EW2(j);
NN_East = T1.Nuke_east;
nuke_east = NN_East(j);
b=[nuke_west,350,380,370,480,320,1200,ww1,ww2,nuke_east,300,380,360,320,750,600,860,ew1,ew2,600,T1.Demand_1(j),T1.Demand_2(j)];
beq = -[ T1.Demand_1(j); T1.Demand_2(j)]; 
[units,obj,z,w,price] = linprog(f,A,b,Aeq,beq,lb)

U(:,j)=units;  %units scheduled for each generators in a form of a table
Prices = price.eqlin;
P(:,j)=Prices;  %making a market clearing price table for DK1 and DK2 
end





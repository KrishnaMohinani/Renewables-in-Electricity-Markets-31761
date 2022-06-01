clear
close all
%% reading all the input values %%
Data = xlsread('Data.xlsx');

%% Calculating revenues (Perfect market)

DA_prices = Data(:,30);               %day ahead price
up_price = Data (:,31);               %up price
down_price = Data(:,32);              %down price

Actual_power = Data(:,4)/1000;        %actual power
justbalancing_deterministic=zeros(8760,1) ; 
deter_prices=zeros(8760,1);
Perfect_revenues=zeros(8760,1);

for i = 1:1:8760
Perfect_revenues(i) = Actual_power(i)*DA_prices(i);
end
R = sum(Perfect_revenues);
%% Calculating revenues for base values (Nominal)

Nominal_prices=zeros(8760,1);
Justbalancing_nominal=zeros(8760,1);

for i = 1:1:8760
Nominal_prices(i) = 160.*DA_prices(i);
Justbalancing_nominal(i) = (Actual_power(i)-160).*up_price(i);
end
Total_Nominal_prices = sum(Nominal_prices);
Total_Justbalancing_nominal = sum(Justbalancing_nominal);
%% Calculating revenues (Probablistic)

Optimal_quantile = Data(:,26)/1000;   %probabilistic quantity
Prob_prices= zeros(8760,1);
justbalancing_prob=zeros(8760,1);

for i = 1:1:8760
    Prob_prices(i)= Optimal_quantile(i)*DA_prices(i);
if Actual_power(i) > Optimal_quantile(i)
    justbalancing_prob(i) = (Actual_power(i) - Optimal_quantile(i)).*down_price(i);
else
    justbalancing_prob(i) = (Actual_power(i) - Optimal_quantile(i)).*up_price(i);
end
end
Total_Prob_prices = sum(Prob_prices);
Total_justbalancing_prob = sum(justbalancing_prob);

%% Calculating revenues (Deterministic)
D_q =Data(:,5)/1000;                  %deterministic quantity
justbalancing_deterministic=zeros(8760,1);
deter_prices= zeros(8760,1);

for i = 1:1:8760
deter_prices(i) = D_q(i).*DA_prices(i);

if Actual_power(i) > D_q(i)
    justbalancing_deterministic(i) = down_price(i).*(Actual_power(i) - D_q(i));  
else
     justbalancing_deterministic(i) = up_price(i).*(Actual_power(i) - D_q(i));
end
     
end
    totalDA_deter = sum(deter_prices);
totalbal_deterministic = sum(justbalancing_deterministic);

%% Calculating revenue (Base - Average forecast)

Average_base = Data(:,27);     % base avergae prognosis strategy (quantity)
justbalancing_averagebase = zeros(8760,1);
AverageBase_prices = zeros(8760,1);
for i = 1:1:8760
    AverageBase_prices(i) = Average_base(i).*DA_prices(i);
if Actual_power(i) > Average_base(i)
    justbalancing_averagebase(i) = (Actual_power(i) - Average_base(i)).*down_price(i);
else
    justbalancing_averagebase(i) = (Actual_power(i) - Average_base(i)).*up_price(i);
end 
end
Total_AverageBase_prices = sum(AverageBase_prices);
Total_justbalancing_averagebase = sum(justbalancing_averagebase);

%% Calculating revenues for base values (Capacity factor)

Cf_prices = zeros(8760,1);  
justbalancing_capacitybase = zeros(8760,1);

for i = 1:1:8760
    Cf_prices(i) = 105.45.*DA_prices(i);
if Actual_power(i) > 105.45
    justbalancing_capacitybase(i) = (Actual_power(i) - 105.45).*down_price(i);
else
    justbalancing_capacitybase(i) = (Actual_power(i) - 105.45).*up_price(i);
end 
end
Total_Cf_prices = sum(Cf_prices);
Total_justbalancing_capacitybase = sum(justbalancing_capacitybase);
%% Calculating revenues for base values (Correction) 

Average_basecorrection = Data(:,29); %correction staregy (quantity)
Correction_price = zeros(8760,1);
justbalancing_correctionbase = zeros(8760,1);

for i = 1:1:8760
    Correction_price(i) = Average_basecorrection(i).*DA_prices(i);
if Actual_power(i) > Average_basecorrection(i) 
    justbalancing_correctionbase(i) = (Actual_power(i) - Average_basecorrection(i)).*down_price(i);
else
    justbalancing_correctionbase(i) = (Actual_power(i) - Average_basecorrection(i)).*up_price(i);
end 
end
Total_Correction_price = sum(Correction_price);
Total_justbalancing_correctionbase = sum(justbalancing_correctionbase);
















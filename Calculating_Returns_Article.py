#! /usr/bin/python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib



Returns_low = [1.08,1.08,0.97,1.08,1.08,0.97,1.08,1.08,0.97,1.08,1.08,0.97,1.08,1.08,0.97,1.08,1.08,0.97,1.08,1.08,0.97,]
Returns = [1.15,1.15,1.15,1.15,0.5,1.15,1.15,1.15,0.5,1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15,1.15,0.5]

def result_of_return_series(returns,initial_account = 10000):
    im_account = [initial_account]
    for i,number in enumerate(returns):
        im_account.append(im_account[i]*number)
    return im_account

result_low = result_of_return_series(Returns_low)
result_high = result_of_return_series(Returns)

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 30}

matplotlib.rc('font', **font)

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(result_low,label = "Kontstante niedrige Renditen")
ax1.plot(result_high, label = "Hohe volatile Renditen")
ax1.set_title("Verlgeich zwischen Depots mit Hoher und niedriger Volatilität - Auswirkung unterschiedlicher Renditen",fontweight = "bold")
plt.ylabel("Depotstand",rotation = "vertical")
plt.xlabel("Anzahl Jahre")
leged_settings = {'weight':'normal'}
plt.legend(prop=leged_settings)

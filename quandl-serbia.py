# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 10:00:01 2016

@author: nemanjar
"""

import Quandl
import matplotlib.pyplot as plt


end_year = '2016-12-31'
EUR = 120.0

rs_gdp_const = Quandl.get('ODA/SRB_NGDP_R')
rs_gov_rev = Quandl.get('ODA/SRB_GGR')
rs_gov_balance = Quandl.get('ODA/SRB_GGSB')
rs_unemp = Quandl.get('ODA/SRB_LUR')
rs_debt_gross = Quandl.get('ODA/SRB_GGXWDG')
rs_debt_net = Quandl.get('ODA/SRB_GGXWDN')
debt_vs_gdp = rs_debt_gross.join(rs_gdp_const, lsuffix='_Balance', rsuffix='_GDP')

plt.figure(1)
plt.plot(rs_gdp_const.iloc[rs_gdp_const.index < end_year]/EUR)
plt.title('Bruto domaći proizvod u milijardama EUR'.decode('utf-8'))
plt.ylabel('Milijardi EUR')

plt.figure(2)
plt.plot(rs_gov_rev.iloc[rs_gov_rev.index < end_year]/EUR)
plt.title('Ukupni prihodi države u milijardama EUR'.decode('utf-8'))
plt.ylabel('Miliona USD')

plt.figure(3)
plt.plot(rs_gov_balance.iloc[rs_gov_balance.index < end_year]/EUR)
plt.title('Deficit vlade u milijardama EUR'.decode('utf-8'))
plt.ylabel('Miliona USD')

plt.figure(4)
plt.plot(rs_unemp.iloc[rs_unemp.index < end_year])
plt.title('Stopa nezaposlenosti u Srbiji (zvanični podaci)'.decode('utf-8'))
plt.ylabel('%')

plt.figure(5)
plt.plot(rs_debt_gross.iloc[rs_debt_gross.index < end_year]/EUR)
plt.title('BRUTO javni dug Srbije u milijarda evra')
plt.ylabel('Miliona USD')

plt.figure(6)
plt.plot(rs_debt_net.iloc[rs_debt_net.index < end_year]/EUR)
plt.title('Neto javni dug Srbije u milijarda evra')
plt.ylabel('Miliona USD')

plt.figure(7)
plt.plot(debt_vs_gdp.iloc[debt_vs_gdp.index < end_year]/EUR)
plt.legend(['Javni dug','bruto domaći proizvod'.decode('utf-8')], loc = 'best')
plt.title('Rast bruto domaćeg proizvoda i javnog duga Srbije'.decode('utf-8'))
plt.ylabel('Milijardi EUR')
plt.annotate('@baskervilski', xy=(0.95, 0.05), xycoords='axes fraction',
             fontsize=16, alpha = 0.6,
             horizontalalignment='right', verticalalignment='bottom')
plt.show()
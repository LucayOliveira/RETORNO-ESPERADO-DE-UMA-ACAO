# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:46:59 2022

@author: lucas

ESTUDO DE CASO, REGRESSÃO LINEAR, PLOT, MERCADO FINANCEIRO, IBOVESPA, AÇÕES

"""



#BLIBLIOTECAS UTILIZADAS
from pandas_datareader import data as pdr
import datetime as dt
from scipy import stats
import matplotlib.pyplot as plt
import os
import yfinance as yf

#DIRECTORIO DE TRABALHO
os.chdir('C:\\Users\lucas\OneDrive\Área de Trabalho\PROGRAMAS PYTHON\TRABALHO 3 RETORNO ESPERADO  DE UMA AÇÃO')


#AÇÕES QUE SERÃO ANALISADAS
acoes = ['TAEE11.SA',
         'TRPL4.SA']

#CRIANDO DATA FRAME DAS COTAÇÕES
DiasCalc = dt.timedelta(796)
fim = dt.date(2023, 3, 4) #(aa/mm/dd)
inicio = fim - DiasCalc

#COTAÇÃO DE FECHAMENTO PARA OS ÚLTIMOS 18 MESES!
print('!!Espaço de tempo necessário para fazer o calculo uma amostra de 540 dias!!')

yf.pdr_override()

#VARIÁVEL IDEPENDENTE INDICE IBOVESPA  'X'
acao1 = ['^BVSP']
df1 = pdr.get_data_yahoo(acao1,inicio,fim, interval = '1d')


#VARIÁVEL DEPENDENTE AÇÕES 'Y'
for i in range(len(acoes)):
    acao2 = acoes[i]
    df2 = pdr.get_data_yahoo(acao2,inicio,fim, interval = '1d')
        
    #CALCULANDO O RETORNO DO IBOVESPA
    #OBS: .iloc[539] É NECESSÁRIO PARA CALCULAR NO ESPAÇO DA DATAFRAME
        
    df3 = df1['Close']
    df4 = df2['Close']
    retorno_ibovespa = (df3.iloc[539]-df3.iloc[0]) / df3.iloc[0]
    
    #REGRESSÃO LINEAR
    beta,beta0,r_value,p_value,std_err = stats.linregress(df3,df4)
    
    #CALCULANDO A RETA
    yLin = beta*df3+beta0
    
    #CRIANDO O GRÁFICO DA REGRESSÂO
    plt.plot(df3,yLin,'-k',df3,df4,'ok')
    plt.xlabel('IBOVESPA')
    plt.ylabel(acao2)
    plt.show()
    
    
    #CALCULO DO RETORNO ESPERADO PARA AÇÃO
    #ARBITRAGE PRICING THEORY (STEPHEN ROSS)
    #MODELO DE MERCADO
    
    retorno_esperado = (beta0+(beta*retorno_ibovespa))*100
    print('Beta: ',beta)
    print('beta0: ',beta0)
    print('r_value: ',r_value)
    print('p_value: ',p_value)
    print('std_err: ',std_err)
    print('Retorno esperado da ação ',acao2,': ',retorno_esperado,'%')

    
print('Retorno do Ibovespa no período: ',retorno_ibovespa)

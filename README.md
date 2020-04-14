# MinorGreeks

Minor Greeks: Lambda and Python Visualization __(Derivation at the bottom)__

I want to shed some light onto less popular greeks that can provide additional insights into any sort of option analysis.

__Lambda__ - "leverage factor" - essential for traders to understand how much more leverage they carry as they enter options trade. It shows how the leverage changes as price of the underlying asset changes by 1% and calculated as a ratio of underlying asset and option price multiplied by delta.

__Example__: Assume that a share of stock trades at 100$ and that the call option with strike price of 100$ trades at 2.5$ with a delta of 0.62. Lambda of this call option is (100/2.5)*0.62=24.8%. 

This means that a 1% increase in the stock value would lead to 24.8% increase in the value invested in the option position. 

Compare a position where you invested 1000$ into 10 stocks and the same 1000$ invested in call options (4 contracts with the size of 100 each at a price of 2.5$). If the stock price changes by 1% your position in stocks will become 1.01*1000=1010$. 
The option price will change from 2.5$ to 3.12$ according to the delta. Then your position in options will become 3.12$*100*4=1248$ , which is 24.8% increase in value.



I included some graphs that I coded in #python. They show how the leverage that traders carry can be affected by change in Volatility, Risk free rate and Time decay. 

![alt text](https://github.com/rustemshinkaruk/MinorGreeks/blob/master/lambda.png)
 

Lambda Formula:

<img src="https://render.githubusercontent.com/render/math?math=\lambda =  \frac{ \frac{dC}{c} }{ \frac{dS}{S} } = \frac{S}{c}* \frac{dC}{dS}  =\frac{S}{c}* \Delta">




We want to find  <img src="https://render.githubusercontent.com/render/math?math=\frac{d \lambda }{d \sigma } , \frac{d \lambda}{dr} ,\frac{d \lambda}{dt}">


Chain rule
<img src="https://render.githubusercontent.com/render/math?math=\frac{d \lambda }{d \sigma } = \frac{d \lambda }{dC  } * \frac{dC}{d \sigma }">


<img src="https://render.githubusercontent.com/render/math?math=\frac{d \lambda }{dC  } = \frac{S* \Delta }{-c^2}">


<img src="https://render.githubusercontent.com/render/math?math=\frac{dC}{d \sigma } = vega">


<img src="https://render.githubusercontent.com/render/math?math=\frac{d \lambda }{d \sigma } = \frac{S* \Delta }{-c^2} * vega">


Using chain rule in the same way as outlined above we can compute  <img src="https://render.githubusercontent.com/render/math?math=\frac{d \lambda}{dr} , \frac{d \lambda}{dt}">


Use explicit formulas for Vega, Rho and Theta in your calculations:

![alt text](https://github.com/rustemshinkaruk/MinorGreeks/blob/master/greeks.gif)


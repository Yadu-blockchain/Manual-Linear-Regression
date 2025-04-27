# Manual-Linear-Regression
A simple project to predict student marks(y) based on hours studied (x) — coding everything manually, including gradient descent optimization! 🧠
A walk through how to build a simple linear regression model to predict student marks based on hours studied, using Gradient Descent — from scratch!

The Math Behind Linear Regression
At its core, Linear Regression is a way to model the relationship between a dependent variable (y) and one or more independent variables (x). In this case:

y = Marks Obtained

x = Hours Studied

The formula for a straight line is:

y=mx+b

Where:

m = Slope of the line (how much marks change per hour studied)
b = Intercept (marks when no hours are studied)

To make our model as accurate as possible, we need to minimize the error between our predicted values (y_pred) and the actual values (y_actual). This error is captured using Mean Squared Error (MSE):

ypredicted=mx=b, where both m and 0 are set to 0 initially.

MSE=1/n∑(yactual−ypredicted)^2
*************************************************************
Gradient Descent: The Optimization Method**
Now, to minimize this error, we use Gradient Descent. It’s an optimization algorithm that adjusts the values of m and b to reduce the error:

Calculate the gradients (slopes) of the error with respect to both m and b.

Update the parameters (m and b) in the direction that reduces the error.

The update rules are:
L(Learning rate) =0.01

(partial derivate m)∂m∂L=-2/n(i=1 to n∑xi(yi−(m⋅xi+b)))
(partial derivate b)∂b∂L=-2/n(i=1 to n∑(yi−(m⋅xi+b)))

m new = m current -L*∂m∂L
b new= b curent-L*∂b∂L

calculate Mean square error with m new and b new, calcualte the partial derivative with m and b and with the latest m and b again calculate Mean Square error, repeat this until, you get the least Mean Square Error, this is the optimal m and b points.



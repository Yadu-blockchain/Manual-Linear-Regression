import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("C:\\Users\\user\\Desktop\\Jupyter\\Hoursstudied.csv")

# Define the loss function
def loss_function(m, b, points):
    totalerror = 0
    for i in range(len(points)):
        x = points.loc[i].HoursStudied
        y = points.loc[i].MarksObtained
        totalerror += (y - (m * x + b)) ** 2
    return totalerror / float(len(points))

# Define the gradient descent function
def gradientdescent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0
    n = len(points)
    
    for i in range(n):
        x = points.iloc[i].HoursStudied
        y = points.iloc[i].MarksObtained
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))
        
    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

# Initialize parameters
m = 0
b = 0
L = 0.01
epochs = 5000

# Create a dictionary to store errors
error_dict = {}

# Run the training loop
for i in range(epochs):
    if i % 50 == 0:
        print(f"Epochs: {i}")
    
    m, b = gradientdescent(m, b, data, L)
    error = loss_function(m, b, data)
    
    # Store error in dictionary with (m, b) as key
    error_dict[(m, b)] = error

    print(f"m: {m}, b: {b}, error: {error}")

# Find the (m, b) pair with error closest to 0
best_m_b = min(error_dict, key=lambda k: abs(error_dict[k]))
best_error = error_dict[best_m_b]

# Unpack m and b
best_m, best_b = best_m_b

print(f"Best m: {best_m}")
print(f"Best b: {best_b}")
print(f"Error closest to 0: {best_error}")

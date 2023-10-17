import numpy as np
import matplotlib.pyplot as plt

# Load data from CSV files
x_sequence = np.loadtxt("x_sequence.csv")
y_sequence = np.loadtxt("y_sequence.csv")
x_TrainPart = np.loadtxt("x_TrainPart.csv")
y_prediction_Train = np.loadtxt("y_prediction_Train.csv")
x_TestPart = np.loadtxt("x_TestPart.csv")
y_prediction_Test = np.loadtxt("y_prediction.csv")

# Plot the first curve (x_sequence vs y_sequence)
plt.figure(figsize=(10, 6))
plt.plot(x_sequence, y_sequence, label='y = cos(x)', color='b')
plt.xlabel('x_sequence')
plt.ylabel('y_sequence')
plt.legend()
plt.title('Plot of y = cos(x)')
plt.grid(True)
plt.show()

# Plot the second curve with Train and Test predictions
plt.figure(figsize=(10, 6))
plt.plot(x_TrainPart, y_prediction_Train, 'ro', label='Train predictions')
plt.plot(x_TestPart, y_prediction_Test, 'go', label='Test predictions')
plt.plot(x_sequence, y_sequence, label='y = cos(x)', color='b')
plt.xlabel('x_sequence')
plt.ylabel('y_prediction')
plt.legend()
plt.title('Train and Test Predictions')
plt.grid(True)
plt.show()





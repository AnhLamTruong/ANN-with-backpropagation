import numpy as np

# seed random numbers to make calculation
# np.random.seed(1)

# sigmoid function
def nonlin (x, deriv=False):
  if (deriv==False):
    return 1/(1 + np.exp(-x))
  return x * (1 - x)


#Input datasets
inputs = np.array([[0,0,1],
                   [0,1,1],
                   [1,0,1],
                   [1,1,1]])
# output dataset 
expected_output = np.array([[0,1,1,0]]).T



#Use two neurons in the input layer, 
#two neurons in the hidden layer, 
#and one neuron in the output layer.
inputLayer = 3
hiddenLayer = 2
outputLayer = 1 


#initialize weights randomly with mean 0
hidden_weights = np.random.uniform(size=(inputLayer,hiddenLayer))
hidden_bias =np.random.uniform(size=(1,hiddenLayer))
output_weights = np.random.uniform(size=(hiddenLayer,outputLayer))
output_bias = np.random.uniform(size=(1,outputLayer))

print("Initial hidden weights: ",end='')
print(*hidden_weights)
print("Initial hidden biases: ",end='')
print(*hidden_bias)
print("Initial output weights: ",end='')
print(*output_weights)
print("Initial output biases: ",end='')
print(*output_bias)

#Training algorithm
for iter in range(100000):

  #Forward Propagation
  hidden_layer = np.dot(inputs,hidden_weights)
  hidden_layer+= hidden_bias
  hidden_layer_output = nonlin(hidden_layer)
  output_layer= np.dot(hidden_layer_output,output_weights)
  output_layer += output_bias
  predicted_output = nonlin(output_layer)

  #Backpropagation using Gradient Descent Algorithm
   # how much did we miss?
  error = expected_output - predicted_output
  
  # multiply how much we missed by the 
  # slope of the sigmoid at the values in predicted_output
  delta_predicted= error * nonlin(predicted_output,True)
  error_hidden_layer = delta_predicted.dot(output_weights.T)
  delta_hidden_layer = error_hidden_layer * nonlin(hidden_layer_output,True)
  
  #Updating Weights and Biases
  #Getting closer to expected_output
  output_weights += hidden_layer_output.T.dot(delta_predicted) * 0.1
  output_bias += np.sum(delta_predicted,axis=0,keepdims=True) * 0.1
  hidden_weights += inputs.T.dot(delta_hidden_layer) * 0.1
  hidden_bias += np.sum(delta_hidden_layer,axis=0,keepdims=True) * 0.1



print("Final hidden weights: ",end='')
print(*hidden_weights)
print("Final hidden bias: ",end='')
print(*hidden_bias)
print("Final output weights: ",end='')
print(*output_weights)
print("Final output bias: ",end='')
print(*output_bias)
print("\nOutput from NN after 100,000 trains: ",end='')
print(*predicted_output)

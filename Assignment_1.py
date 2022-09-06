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


#Use three neurons in the input layer, 
#two neurons in the hidden layer, 
#and one neuron in the output layer.
inputLayer = 3
hiddenLayer = 2
outputLayer = 1 


#initialize weights randomly with mean 0
hid_weights = np.random.uniform(size=(inputLayer,hiddenLayer))
hid_bias =np.random.uniform(size=(1,hiddenLayer))
out_weights = np.random.uniform(size=(hiddenLayer,outputLayer))
out_bias = np.random.uniform(size=(1,outputLayer))

print("Initial hidden weights: ",end='')
print(*hid_weights)
print("Initial hidden biases: ",end='')
print(*hid_bias)
print("Initial output weights: ",end='')
print(*out_weights)
print("Initial output biases: ",end='')
print(*out_bias)

#Training algorithm
for iter in range(100000):

  #Forward Propagation
  hid_layer = np.dot(inputs,hid_weights)
  hid_layer+= hid_bias
  hid_layer_output = nonlin(hid_layer)
  out_layer= np.dot(hid_layer_output,out_weights)
  out_layer += out_bias
  predicted_output = nonlin(out_layer)

  #Backpropagation using Gradient Descent Algorithm
   # how much did we miss?
  error = expected_output - predicted_output
  
  # multiply how much we missed by the 
  # slope of the sigmoid at the values in predicted_output
  delta_predicted= error * nonlin(predicted_output,True)
  error_hidden_layer = delta_predicted.dot(out_weights.T)
  delta_hidden_layer = error_hidden_layer * nonlin(hid_layer_output,True)
  
  #Updating Weights and Biases
  #Getting closer to expected_output
  out_weights += hid_layer_output.T.dot(delta_predicted) * 0.1
  out_bias += np.sum(delta_predicted,axis=0,keepdims=True) * 0.1
  hid_weights += inputs.T.dot(delta_hidden_layer) * 0.1
  hid_bias += np.sum(delta_hidden_layer,axis=0,keepdims=True) * 0.1



print("Last prediction hidden weights: ",end='')
print(*hid_weights)
print("Last prediction hidden bias: ",end='')
print(*hid_bias)
print("Last prediction output weights: ",end='')
print(*out_weights)
print("Last prediction output bias: ",end='')
print(*out_bias)
print("\nOutput from ANN after 100,000 trains: ",end='')
print(*predicted_output)

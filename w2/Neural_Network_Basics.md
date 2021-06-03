### 1. What does a neuron compute?

- A neuron computes the mean of all features before applying the output to an activation function
- :white_check_mark: A neuron computes a linear function (z = Wx + b) followed by an activation function
- A neuron computes an activation function followed by a linear function (z = Wx + b)
- A neuron computes a function g that scales the input x linearly (Wx + b)

### 2. Which of these is the "Logistic Loss"?

<img width="435" alt="Screenshot 2021-06-03 at 20 13 15" src="https://user-images.githubusercontent.com/38349049/120693164-f8a45080-c4a8-11eb-9d02-08cf09f8c5f4.png">

### 3. Suppose img is a (32,32,3) array, representing a 32x32 image with 3 color channels red, green and blue. How do you reshape this into a column vector?


- x = img.reshape((1,32*32,*3))
- x = img.reshape((32*32,3))
- :white_check_mark: x = img.reshape((32*32*3,1))
- x = img.reshape((3,32*32))

### 4. Consider the two following random arrays "a" and "b": <br> a = np.random.randn(2, 3) # a.shape = (2, 3)b = np.random.randn(2, 1) # b.shape = (2, 1)c = a + b <br> What will be the shape of "c"?

- c.shape = (3, 2)
- The computation cannot happen because the sizes don't match. It's going to be "Error"!
- c.shape = (2, 1)
- :white_check_mark: c.shape = (2, 3)

### 5. Consider the two following random arrays "a" and "b": <br>  a = np.random.randn(4, 3) # a.shape = (4, 3)b = np.random.randn(3, 2) # b.shape = (3, 2)c = a*b <br> What will be the shape of "c"?

- c.shape = (4,2)
- c.shape = (3, 3)
- :white_check_mark: The computation cannot happen because the sizes don't match. It's going to be "Error"!
- c.shape = (4, 3)
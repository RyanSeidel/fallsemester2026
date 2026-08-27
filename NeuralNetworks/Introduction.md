Accuracy -> Maximize
Error -> Minimize

All values must be labeled

In order to do the model it must go through a test set

 Test Dataset

 There is no labels in Unsupervised Learning

 Supervised Learning has labels


Source: https://www.deeplearningbook.org/contents/ml.html

 One way to eﬃciently deﬁne such a large set of functions is tolearn a probability distribution over all the relevant variables, then solve theclassiﬁcation task by marginalizing out the missing variables. Withninputvariables, we can now obtain all 2ndiﬀerent classiﬁcation functions neededfor each possible set of missing inputs, but the computer program needsto learn only a single function describing the joint probability distribution.


FUN joint probability distribution

Types of tasks:
Regression
Transcription
Machine Translation
Structure Output
Anomaly Detection
Synthesis and Sampling
Imputation of missing values
Denoising
Density estimation or probability mass function estimation

Accuracy is just the proportion of examples for which the model produces the correct output.

We therefore evaluate these performance measures using a testset of data that is separate from the data used for training the machinelearning system.

Classification vs Regression

I think the first assignment will be creating a neuron using Linear Regression 
and be able to fully explain the code.

Classification is not continous 


Articifial Neuron
what is the basis? nucleus

There are 
bo -->

w1x1 -->   Sum of wx+b -> A(z) = y
                ^
w2x2 -->        | Single layer (z)

it better to use to a real example to understand why 

** it is not the number of neurons, it is the number of layers **

Activation function is different between each layer 

input layer     | hidden layer | output layer
b + w1 + x1         /\
    |    |          \/------>       _________
    |    |          /\             /         \
    |    |          \/------>      |         | y= Z(f)
    |    |          /\             \_________/
    wn   xn         \/------>       


input layer     | hidden layer | hidden layer 2 | output layer
b + w1 + x1         /\
    |    |          \/------>        /\              _________
    |    |          /\               \/   -->       /         \
    |    |          \/------>        /\   -->       |         | y= Z(f)
    |    |          /\               \/             \_________/
    wn   xn         \/------>       

Why would I have to change a layer / increase more layers? 
To improve more accurary and help increase the understanding of complex patterns


Talks about the types of Neural Networks
like (FNN) (RNN) (CNN) (RBFN)

Weight determines least important to most important feature


# Single Layer Neuron
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, Dropdown, VBox, HBox, Layout


# Define different activation functions
def identity(net):
    return net

def hardlimit(net):
  return np.where(net >= 0, 1, 0)
def sigmoid(net):
    return 1 / (1 + np.exp(-net))

def tanh(net):
    return np.tanh(net)

def relu(net):
    return np.maximum(0, net)

def leaky_relu(net, alpha=0.1):
    return np.where(net >= 0, net, alpha*net)
def sign(net):
    return np.where(net > 0, 1, np.where(net == 0, 0.5, 0))

ACTS = {
    "identity": identity,
    "hardlimit": hardlimit,
    "sigmoid": sigmoid,
    "tanh": tanh,
    "ReLU": relu,
    "leaky ReLU": leaky_relu,
    "sign":sign
}

def neuron_demo(
    x1=0.5, x2=0.5, x3=0.5,
    w1=1.0, w2=1.0, w3=1.0,
    b=0.0,
    activation="sigmoid",
    alpha=0.1
):
    # Forward pass
    x = np.array([x1, x2, x3], dtype=float)
    w = np.array([w1, w2, w3], dtype=float)
    net = float(np.dot(w, x) + b)

    f = ACTS[activation]
    if activation == "leaky ReLU":
        a = float(f(net, alpha=alpha))
    else:
        a = float(f(net))

    # Printing
    print("Single Neuron Forward Pass")
    print("-" * 40)
    print(f"x = [{x1:.3f}, {x2:.3f}, {x3:.3f}]")
    print(f"w = [{w1:.3f}, {w2:.3f}, {w3:.3f}]")
    print(f"b = {b:.3f}")
    print(f"net = w·x + b = {net:.6f}")
    print(f"a = f(z) with {activation} = {a:.6f}")

    # Plot activation curve and current point
    zmin, zmax = -10, 10
    zs = np.linspace(zmin, zmax, 1000)

    if activation == "leaky ReLU":
        ys = f(zs, alpha=alpha)
    else:
        ys = f(zs)

    plt.figure(figsize=(8, 4))
    plt.plot(zs, ys)
    plt.axvline(0, linestyle="--")
    plt.scatter([net], [a], s=80)
    plt.title(f"Activation: {activation}   (Current net={net:.3f}, a={a:.3f})")
    plt.xlabel("net")
    plt.ylabel("a = f(net)")
    plt.grid(True)
    plt.show()

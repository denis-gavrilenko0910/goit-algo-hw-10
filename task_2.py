import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Integration limits
a, b = 0, 2
num_samples = 100000

# Function to integrate
def f(x):
    return x ** 2

def visualize_results(x_random, y_random):
    # Create x range for plotting the function
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    _, ax = plt.subplots()

    # Plot the function curve
    ax.plot(x, y, "r", linewidth=2)

    # Plot the random points
    ax.scatter(x_random, y_random, color = "red")

    # Fill the area under the curve
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Set plot limits and labels
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Add integration limits and title
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Integration plot of f(x) from {a} to {b}")
    
    plt.grid()
    plt.show()

def monte_carlo(a, b, num_samples):
    # Monte Carlo integration

    # Generate random points (x_random inside [a, b], y_random inside [0, f(b)])
    x_random = np.random.uniform(a, b, num_samples)
    y_random = np.random.uniform(0, f(b), num_samples)

    # Count number of points under the curve
    under_curve = np.sum(y_random < f(x_random))

    # Estimate area under the curve (integral)
    area_under_curve = (b - a) * f(b) * under_curve / num_samples

    # Compute exact integral using scipy quad
    result, error = spi.quad(f, a, b)

    print('Monte Carlo area:', area_under_curve, 'Quad area:', result)

    # Visualize results
    visualize_results(x_random, y_random)

if __name__ == "__main__":
    # Run integration for different number of samples
    for density in [100, 1000, 10000, 100000]:
        print(f"\n\tResults for points amount: {density}")
        monte_carlo(a, b, density)



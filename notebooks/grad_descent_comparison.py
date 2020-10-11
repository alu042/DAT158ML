np.random.seed(42)

theta_path_bgd = []
theta_path_sgd = []
theta_path_mgd = []

eta = 0.1 # learning rate

n_epochs_bgd = 1000
n_epochs_sgd = 20
n_iterations = 20


# Batch gradient descent:

theta = np.random.randn(2,1) # Random initalization of the parameters

for epoch in range(n_epochs_bgd):
    gradients = evaluate_gradient(X_b, theta, y)
    theta = theta - eta*gradients
    theta_path_bgd.append(theta)
    
# Stochastic gradient descent:
theta = np.random.randn(2,1)

for epoch in range(n_epochs_sgd):
    for i in range(len(X_b)):
        random_index = np.random.randint(len(X_b)) # Need this to fetch both an x and corresponding y
        xi = X_b[random_index:random_index+1]
        yi = y[random_index]
        eta = lr_schedule(alpha, i)
        gradients = evaluate_gradient(xi, theta, yi)
        theta = theta - eta*gradients
        theta_path_sgd.append(theta)

# Mini-batch gradient descent:
theta = np.random.randn(2,1)
eta = 0.1

for epoch in range(n_iterations):
    shuffled_indices = np.random.permutation(len(X_b))
    X_b_shuffled = X_b[shuffled_indices]
    y_shuffled = y[shuffled_indices]
    for i in range(0, len(X_b), minibatch_size):
        xi = X_b_shuffled[i:i+minibatch_size]
        yi = y_shuffled[i:i+minibatch_size]
        gradients = evaluate_gradient(xi, theta, yi)
        eta = lr_schedule(alpha, i)
        theta = theta - eta * gradients
        theta_path_mgd.append(theta)


theta_path_bgd = np.array(theta_path_bgd)
theta_path_sgd = np.array(theta_path_sgd)
theta_path_mgd = np.array(theta_path_mgd)

# Plot the results:
plt.figure(figsize=(14,10))
plt.plot(theta_path_sgd[:, 0], theta_path_sgd[:, 1], "r-s", linewidth=1, label="Stochastic")
plt.plot(theta_path_mgd[:, 0], theta_path_mgd[:, 1], "g-+", linewidth=2, label="Mini-batch")
plt.plot(theta_path_bgd[:, 0], theta_path_bgd[:, 1], "b-o", linewidth=3, label="Batch")
plt.legend(loc="upper left")
plt.xlabel(r"$\theta_0$")
plt.ylabel(r"$\theta_1$ ", rotation=0)
plt.axis([2.5, 4.5, 2.3, 3.9])
plt.show()
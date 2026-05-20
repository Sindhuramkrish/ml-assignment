from flask import Flask, render_template, jsonify
import numpy as np
import pandas as pd
import random

app = Flask(__name__)

# LOAD DATASET
data = pd.read_csv("data.csv")

k = len(data)
means = data["mean"].values
stds = data["std"].values

# PARAMETERS
epsilon = 0.2

# INIT
Q = np.zeros(k)
N = np.zeros(k)
rewards_history = []

# Pull arm using dataset
def pull_arm(action):
    global Q, N
    
    # Generate reward using dataset distribution
    reward = np.random.normal(means[action], stds[action])
    
    N[action] += 1
    
    # Incremental update rule
    Q[action] = Q[action] + (1 / N[action]) * (reward - Q[action])
    
    rewards_history.append(reward)
    
    return reward

# Step API
@app.route("/step")
def step():
    if random.random() < epsilon:
        action = random.randint(0, k-1)
    else:
        action = int(np.argmax(Q))
    
    reward = pull_arm(action)
    
    avg_reward = sum(rewards_history) / len(rewards_history)
    
    return jsonify({
        "action": action,
        "reward": float(round(reward, 2)),
        "avg_reward": float(round(avg_reward, 2))
    })

# Reset (🔥 useful for demo)
@app.route("/reset")
def reset():
    global Q, N, rewards_history
    
    Q = np.zeros(k)
    N = np.zeros(k)
    rewards_history = []
    
    return jsonify({"message": "Reset successful"})

# Home page
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

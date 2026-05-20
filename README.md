🎰 Epsilon-Greedy Multi-Armed Bandit (Flask)

A simple Flask project that demonstrates the Epsilon-Greedy Reinforcement Learning algorithm using a Multi-Armed Bandit problem.

The app learns which action gives better rewards over time by balancing:

Exploration → trying random actions
Exploitation → choosing the best known action
🚀 Technologies Used
Python
Flask
NumPy
Pandas
📂 Project Structure
project/
│
├── app.py
├── data.csv
└── templates/
    └── index.html
📊 Dataset Format
mean,std
5,1
8,2
3,1
mean → average reward
std → reward variation

Each row represents one bandit arm.

⚡ Algorithm

The project uses:

epsilon = 0.2

Meaning:

20% → random action (exploration)
80% → best action (exploitation)
🧠 Core Logic
Initialize Values
Q = np.zeros(k)
N = np.zeros(k)
Q → estimated reward of each arm
N → number of times each arm selected
Generate Reward
reward = np.random.normal(means[action], stds[action])

Reward is sampled from a normal distribution.

Update Rule
Q[action] = Q[action] + (1 / N[action]) * (reward - Q[action])

Updates the estimated reward incrementally.

Q
n+1
	​

=Q
n
	​

+
N
n
	​

1
	​

(R
n
	​

−Q
n
	​

)

🌐 API Routes
/step

Performs one learning step.

Returns:

{
  "action": 1,
  "reward": 7.42,
  "avg_reward": 5.81
}
/reset

Resets learning values.

/

Loads the frontend page.

▶️ Run the Project

Install dependencies:

pip install flask numpy pandas

Run:

python app.py

Open:

http://127.0.0.1:5000
📌 Features

✅ Epsilon-Greedy Learning
✅ Reward Simulation
✅ Incremental Mean Update
✅ Flask APIs
✅ Reset Functionality

📚 Concepts Learned
Reinforcement Learning
Multi-Armed Bandit
Exploration vs Exploitation
Online Learning
Flask Backend APIs

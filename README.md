# 🎰 Epsilon-Greedy Multi-Armed Bandit (Flask)

A simple Flask project that demonstrates the **Epsilon-Greedy Reinforcement Learning algorithm** using a **Multi-Armed Bandit problem**.

The app learns which action gives better rewards over time by balancing:
- **Exploration** → trying random actions
- **Exploitation** → choosing the best known action

# 🚀 Technologies Used

- Python
- Flask
- NumPy
- Pandas

# 📂 Project Structure

```plaintext
project/
│
├── app.py
├── data.csv
└── templates/
    └── index.html
```

# 📊 Dataset Format

```csv
mean,std
5,1
8,2
3,1
```

- `mean` → average reward
- `std` → reward variation

Each row represents one bandit arm.

# ⚡ Algorithm

```python
epsilon = 0.2
```

Meaning:
- 20% → random action (exploration)
- 80% → best action (exploitation)

# 🧠 Core Logic

## Initialize Values

```python
Q = np.zeros(k)
N = np.zeros(k)
```

- `Q` → estimated reward of each arm
- `N` → number of times each arm selected

## Generate Reward

```python
reward = np.random.normal(means[action], stds[action])
```

Reward is sampled from a normal distribution.

## Update Rule

```python
Q[action] = Q[action] + (1 / N[action]) * (reward - Q[action])
```

Formula:

```text
Q(n+1) = Q(n) + (1 / N(n)) × (R(n) - Q(n))
```

Where:
- `Q(n)` → current estimate
- `R(n)` → current reward
- `N(n)` → number of selections

# 🌐 API Routes

## `/step`

Performs one learning step.

```json
{
  "action": 1,
  "reward": 7.42,
  "avg_reward": 5.81
}
```

## `/reset`

Resets all learning values.

## `/`

Loads the frontend page.

# ▶️ Run the Project

Install dependencies:

```bash
pip install flask numpy pandas
```

Run the app:

```bash
python app.py
```

Open browser:

```plaintext
http://127.0.0.1:5000
```

# 📌 Features

- ✅ Epsilon-Greedy Learning
- ✅ Reward Simulation
- ✅ Incremental Mean Update
- ✅ Flask APIs
- ✅ Reset Functionality

# 📚 Concepts Learned

- Reinforcement Learning
- Multi-Armed Bandit
- Exploration vs Exploitation
- Online Learning
- Flask Backend APIs

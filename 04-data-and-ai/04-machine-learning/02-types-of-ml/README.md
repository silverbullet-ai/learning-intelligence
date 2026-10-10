# Types of Machine Learning

## Overview

Machine Learning can be divided into three core types:

1. **Supervised Learning**
2. **Unsupervised Learning**
3. **Reinforcement Learning**

Each type differs in how a model learns from data or feedback.

---

## 1. Supervised Learning

**Defining characteristic:** The dataset contains a known output, also called the *target feature* or *dependent variable*.

The model learns the relationship between input features and their corresponding target values.

### Example: House Price Prediction

| Size | Rooms | Price |
|---|---:|---:|
| 5,000 ft² | 5 | $450K |
| 6,000 ft² | 6 | $500K |

Here:

- **Independent features / Input features:** Size and Rooms
- **Dependent feature / Output feature / Target:** Price

The model learns from these examples to predict prices for new houses.

### Two Major Problem Types

```text
Supervised Learning
├── Regression
│   └── Continuous numerical output
└── Classification
    └── Categorical output
```

### 1.1 Regression

Regression predicts a continuous numerical value.

**Examples:**
- House price → ₹50 lakh
- Salary → ₹8.5 lakh
- Temperature → 32.7°C

**Algorithms:**
- Linear Regression
- Ridge Regression
- Lasso Regression
- Elastic Net

### 1.2 Classification

Classification predicts a category or class.

**Example:** Study Hours + Play Hours → Pass/Fail.

Types of classification:

- **Binary Classification:** Two possible classes, such as Pass/Fail.
- **Multiclass Classification:** More than two possible classes.

**Algorithms:**
- Logistic Regression
- Decision Tree
- Random Forest
- AdaBoost
- XGBoost
- CatBoost

**Note:** Decision Tree, Random Forest, AdaBoost, XGBoost, and CatBoost have variants for regression and classification. Logistic Regression is commonly used for classification despite its name.

---

## 2. Unsupervised Learning

**Defining characteristic:** There is no known target/output feature supplied for the learning task.

Instead of predicting a known target, the algorithm attempts to discover patterns, similarities, or groups in the data.

### Example: Customer Segmentation

| Salary | Spending Score |
|---:|---:|
| ₹20,000 | 9 |
| ₹45,000 | 2 |
| ... | ... |

There is no target column specifying which group each customer belongs to. The algorithm discovers groups based on similarities in the available features.

Possible groups:

- High salary + High spending
- High salary + Low spending
- Low salary + Low spending
- Medium salary + High spending

This process is called **clustering**.

### Algorithms

- K-Means
- Hierarchical Clustering
- DBSCAN

---

## 3. Reinforcement Learning

Reinforcement Learning differs from both supervised and unsupervised learning.

**Central idea:** An agent learns through actions and rewards or penalties received from an environment.

The lecture uses a baby learning to walk as an analogy: the baby tries actions, experiences outcomes, and gradually learns better behavior.

### Basic Learning Cycle

```text
      Environment
           │
           ▼
         Agent
           │
         Action
           │
           ▼
      Environment
           │
     Reward / Penalty
           │
           ▼
        Learning
```

### Core Concepts

- **Agent:** The learner or decision-maker.
- **Environment:** The world in which the agent operates.
- **Action:** A choice made by the agent.
- **Reward/Penalty:** Feedback received after an action.

The detailed Reinforcement Learning module will be covered later in the course.

---

## 4. Comparison of the Three Types

| Aspect | Supervised | Unsupervised | Reinforcement |
|---|---|---|---|
| Learning signal | Labeled examples | Data without a supplied target | Rewards and penalties |
| Main idea | Learn to predict known outputs | Discover patterns or groups | Learn through actions and feedback |
| Typical task | Prediction | Clustering | Sequential decision-making |
| Example | House price prediction | Customer segmentation | Learning effective actions |
| Key concepts | Regression, Classification | Clustering | Agent, Environment, Action, Reward |

---

## 5. One-Line Memory Tricks

- **Supervised:** "I know the answer; learn to predict it."
- **Unsupervised:** "I don't know the groups; find them."
- **Reinforcement:** "Try actions; learn from rewards."

---

## 6. What's Next?

The next topic is **Simple Linear Regression**, the first supervised learning algorithm in the course sequence.

## Key Takeaway

**Supervised Learning** learns from labeled examples. **Unsupervised Learning** discovers patterns without a supplied target. **Reinforcement Learning** learns through actions and rewards.

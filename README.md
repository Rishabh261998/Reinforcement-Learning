# What is Reinforcement-Learning?

Reinforcement learning is a category of machine learning and it is best understood as If we have an **agent** that interacts with an **environment** such that it can observe the environment **state** and perform **actions**. Upon doing actions, the environment state changes into a new state and the agent recieves a **reward** (or penalty). Reinforcement learning aims at making this agent learn from his experience of interactions with environment so that it chooses the best actions that maximizes the sum of rewards it receives from the environment.
Reinforcement Learning is one of the major parts of **Machine-Learning** alongside **Supervised** and **Unsupervised Learning**.


## Markov Decision Process

Firstly let us talk about the **Markov Property**.
The Markov Property states that `"Once the future is known then the past is irrelevant"`, in mathematical words
a state **_S_**_t_ has the  _Markov_ property, if and only if;

**_P_**[**S**_t+1_ **_|_** **S**_t_] _=_ **_P_**[**S**_t+1_ **_|_** **S**_1_, ….. , **_S_**_t_].

For a _Markov_ state **S** and successor state **S′**, the state transition probability function is defined by,
![](https://miro.medium.com/max/285/1*MttGDZm6XvBMDbJsrDzSIA.png)
**MDP** is basically used to describe the agent and environment interaction in a formal way.

## Value Iteration

Value iteration computes the optimal state value function by iteratively improving the estimate of **V(s)**. The algorithm initialize **V(s)** to arbitrary random values. It repeatedly updates the **Q(s, a)** and **V(s)** values until they converges. Value iteration is guaranteed to converge to the optimal values. This algorithm is shown in the following pseudo-code:
![](https://miro.medium.com/max/700/1*MsD6og8hCReDO24T8iZfNw.png)
## Policy Iteration 

While value-iteration algorithm keeps improving the value function at each iteration until the value-function converges. Since the agent only cares about the finding the optimal policy, sometimes the optimal policy will converge before the value function. Therefore, another algorithm called policy-iteration instead of repeated improving the value-function estimate, it will re-define the policy at each step and compute the value according to this new policy until the policy converges. Policy iteration is also guaranteed to converge to the optimal policy and it often takes less iterations to converge than the value-iteration algorithm.

The pseudo code for Policy Iteration is shown below.
![](https://miro.medium.com/max/700/1*WwOaLxFvDDgY0Uk92FO6Rw.png) `Used Value-Iteration and Policy-Iteration to train a environment(Frozen-Lake8x8) available on gym`

## Q-Learning
**Q-Learning** is an example of model-free learning algorithm. It does not assume that agent knows anything about the state-transition and reward models. However, the agent will discover what are the good and bad actions by trial and error.

The basic idea of Q-Learning is to approximate the state-action pairs Q-function from the samples of Q(s, a) that we observe during interaction with the enviornment. This approach is known as **Time-Difference Learning.**

![](https://miro.medium.com/max/700/1*yoEaeSssoS7tx-8H24yQQQ.png)
where 𝛂 is the learning rate. The `Q(s,a)`table is initialized randomly. Then the agent starts to interact with the environment, and upon each interaction the agent will observe the reward of its action `r(s,a)`and the state transition (new state `s'`). The agent compute the observed Q-value Q_obs(s, a) and then use the above equation to update its own estimate of `Q(s,a)` .
` Used the Q-learning algorithm to train the mountain-car environment on OpenAI Gym.`

## Mountain-Car v0:

Trained the mountain-car environment on openai gym using q-learning.
## Background

OpenAI offers a toolkit for practicing and implementing Deep Q-Learning algorithms. ([http://gym.openai.com/](http://gym.openai.com/)) This is my implementation of the MountainCar-v0 environment. This environment has a small cart stuck in a trench. The cart needs to get to the flag on top of the crest to gain points and the faster it learns to do this, it gains more points. The cart can go left and right, with any variation of speed. Once the cart performs an action, the environment provides it a reward and tells it where the cart is at this point.

` Similarly used Value-Iteration and Policy-Iteration to train and test the frozen-lake environment on openai gym`

## Conclusion:
This was my first project on Reinforcement Learning. I am very thankful to my mentor- "Pawan Agarwal" who helped me throughout the course of my project and cleared my doubts.
The MountainCar showed me how a complex learning algorithm in a continuous space could be developed through Deep Q Learning instead of arduous man hours by developers.

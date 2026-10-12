# -*- coding: utf-8 -*-
"""
Module 4: Advanced Topics & Systems (A01 - A08)
8 complete lessons with all 15 sections, LaTeX mathematics, hyperparameters, and 3-question quizzes.
"""

def get_advanced():
    return [
        {
            "id": "A01",
            "title": "Reinforcement Learning Fundamentals",
            "module": "advanced",
            "level": "intermediate",
            "prerequisites": ["F01", "F04"],
            "estimatedMinutes": 25,
            "tags": ["rl", "mdp", "bellman-equation", "q-learning", "tabular-rl"],
            "shortDesc": "Markov Decision Processes, the Bellman Optimality Equation, Exploration vs Exploitation, and Tabular Q-Learning.",
            "sections": {
                "whatItIs": "Reinforcement Learning (RL) is a computational framework where an agent learns through trial-and-error interaction with a dynamic environment. The problem is mathematically formalized as a <strong>Markov Decision Process (MDP)</strong>, and solved by finding an optimal policy $\\pi^*(a|s)$ that maximizes expected cumulative discounted future reward.",
                "problemItSolves": "Solves sequential decision-making challenges where immediate actions have delayed consequences, there is no static supervisor providing ground-truth labels, and the agent must balance exploring new strategies against exploiting known payoffs.",
                "intuition": "Imagine training a puppy to fetch a ball. You do not explain the physics of canine kinematics. Instead, when the puppy runs toward the ball and brings it back, you give it a treat (positive reward). When it chews your shoe instead, you give no treat (penalty). Over repeated trials, the puppy links sequential actions to treats.",
                "howItWorks": "1. <strong>MDP Tuple:</strong> Defined by states $\\mathcal{S}$, actions $\\mathcal{A}$, transition dynamics $\\mathcal{P}(s'|s,a)$, reward function $\\mathcal{R}(s,a)$, and discount factor $\\gamma$.<br>2. <strong>Markov Property:</strong> The future is conditionally independent of the past given the present state: $P(s_{t+1}|s_t, a_t, \\dots, s_0) = P(s_{t+1}|s_t, a_t)$.<br>3. <strong>Value Function $V(s)$ & Action-Value $Q(s, a)$:</strong> Estimate long-term expected returns.<br>4. <strong>Tabular Q-Learning:</strong> Update lookup table $Q(s, a)$ iteratively using the temporal difference Bellman error.<br>5. <strong>Exploration Strategy:</strong> $\\epsilon$-greedy: take a random exploratory action with probability $\\epsilon$, else pick $\\arg\\max_a Q(s, a)$.",
                "mathematics": "Bellman Optimality Equation for $Q^*(s, a)$:<br>$$Q^*(s, a) = \\mathcal{R}(s, a) + \\gamma \\sum_{s' \\in \\mathcal{S}} \\mathcal{P}(s' \\mid s, a) \\max_{a' \\in \\mathcal{A}} Q^*(s', a')$$<br>Temporal Difference (TD) Q-Learning Update Rule:<br>$$Q(s_t, a_t) \\leftarrow Q(s_t, a_t) + \\alpha \\underbrace{\\left[ r_{t+1} + \\gamma \\max_{a'} Q(s_{t+1}, a') - Q(s_t, a_t) \\right]}_{\\text{TD Error } \\delta_t}$$<br>Optimal Policy Extraction:<br>$$\\pi^*(s) = \\arg\\max_{a \\in \\mathcal{A}} Q^*(s, a)$$",
                "dataRequirements": "Interactive simulator or Markovian environment providing step transitions: `next_state, reward, terminated, truncated, info = env.step(action)`.",
                "hyperparameters": [
                    {"name": "Discount Factor (\\gamma)", "description": "Future reward discount rate (e.g. 0.9 to 0.99).", "effect": "Higher $\\gamma$ values encourage long-range strategic sacrifice."},
                    {"name": "Learning Rate (\\alpha)", "description": "Step magnitude for temporal difference updates.", "effect": "Balances new empirical transition experiences against established Q-estimates."},
                    {"name": "Epsilon Decay (\\epsilon)", "description": "Decaying probability of random exploration.", "effect": "Starts high (e.g. 1.0) for broad exploration; decays to 0.05 for greedy exploitation."}
                ],
                "strengths": [
                    "Requires zero labeled demonstrations: discovers novel emergent strategies from scratch.",
                    "Principled mathematical foundation rooted in Bellman dynamic programming.",
                    "Naturally solves multi-step planning, inventory routing, and sequential optimization."
                ],
                "limitations": [
                    "Tabular Q-learning suffers from the curse of dimensionality: state-action table $|\mathcal{S}| \times |\mathcal{A}|$ becomes intractable for continuous or large states.",
                    "Sample inefficient: requires millions of trials.",
                    "Delayed sparse rewards make credit assignment extremely difficult."
                ],
                "evaluation": "Evaluated using Mean Cumulative Return per episode and Convergence Rate across episodes.",
                "workedExample": "A 4x4 Gridworld maze: Agent starts at (0,0); goal is at (3,3) with reward +1; pit traps have reward -1. Q-learning starts with all $Q(s, a) = 0$. After exploring and falling into pits, negative values backpropagate. Once the agent stumbles into the goal, the $+1$ reward propagates backward along adjacent tiles, carving an optimal path around all pit traps.",
                "whenToUse": "Use for games, routing optimization, robotic planning, traffic light control, and financial algorithmic order execution.",
                "commonMistakes": [
                    "Setting discount factor $\\gamma = 1.0$ in continuing, non-terminating tasks (causes value estimates to diverge to infinity).",
                    "Failing to decay $\\epsilon$, causing the agent to make random clumsy mistakes forever during evaluation."
                ],
                "furtherLearning": [
                    {"title": "Sutton & Barto: Reinforcement Learning: An Introduction (2nd Edition)", "url": "http://incompleteideas.net/book/the-book-2nd.html"},
                    {"title": "David Silver's RL Course (DeepMind / UCL)", "url": "https://www.youtube.com/playlist?list=PLzuuYNsE1EZAXYR4FJQDghguE3WZTtxUo"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the core assumption of the 'Markov Property' in Reinforcement Learning?",
                    "options": [
                        "All rewards must be positive.",
                        "The future state transition depends only on the current state and action, and is conditionally independent of all preceding historical states.",
                        "The agent never makes mistakes.",
                        "There are only two possible actions."
                    ],
                    "correct": 1,
                    "explanation": "A state possesses the Markov property if it encapsulates all relevant historical context, so that future transitions depend solely on $(s_t, a_t)$ and not the prior path."
                },
                {
                    "question": "What does the Temporal Difference (TD) error $\\delta_t = r_{t+1} + \\gamma \\max_{a'} Q(s', a') - Q(s, a)$ represent?",
                    "options": [
                        "The time elapsed in seconds.",
                        "The discrepancy between the current Q-value estimate and a new estimate formed by the immediate reward plus discounted future value (bootstrapping).",
                        "The error of the neural network compiler.",
                        "The difference between training and test loss."
                    ],
                    "correct": 1,
                    "explanation": "TD error measures the surprise: the difference between what the agent expected the state-action pair to be worth and the reality observed after taking the step."
                },
                {
                    "question": "Why is pure greedy action selection (always picking $\\arg\\max Q$) problematic early in training?",
                    "options": [
                        "It crashes the simulation.",
                        "The agent becomes trapped in the first mildly positive reward it discovers, never exploring alternative paths that could yield vastly superior long-term rewards (Exploration vs Exploitation dilemma).",
                        "It causes memory overflow.",
                        "Greedy selection produces infinite loops."
                    ],
                    "correct": 1,
                    "explanation": "Without exploration ($\\epsilon > 0$), the agent exploits imperfect early guesses and never discovers superior hidden strategies."
                }
            ]
        },
        {
            "id": "A02",
            "title": "Recommender Systems",
            "module": "advanced",
            "level": "intermediate",
            "prerequisites": ["F01", "S01", "U05", "D12"],
            "estimatedMinutes": 25,
            "tags": ["recsys", "collaborative-filtering", "matrix-factorization", "two-tower", "cosine-similarity"],
            "shortDesc": "Drive user engagement through Collaborative Filtering, SVD Matrix Factorization, and Deep Two-Tower Retrieval models.",
            "sections": {
                "whatItIs": "Recommender Systems predict user preferences and retrieve personalized items from catalogs containing millions of options. They power Netflix movie suggestions, Amazon product recommendations, and TikTok/YouTube feeds, primarily leveraging **Collaborative Filtering** (patterns of crowd behavior) and **Two-Tower Neural Retrieval**.",
                "problemItSolves": "Information overload. Users cannot manually browse a catalog of 100 million songs or products. Recommender systems filter the vast catalog to surface relevant, personalized items in milliseconds.",
                "intuition": "Collaborative filtering is like asking your movie-buff friend for a movie recommendation: 'You and I have identical taste—we both loved Interstellar and Inception. What movie did you love that I haven't seen yet?' You rely on peer taste overlap rather than reading movie script summaries.",
                "howItWorks": "1. <strong>User-Item Interaction Matrix:</strong> Sparse matrix $\\mathbf{R} \\in \\mathbb{R}^{M \\times N}$ with explicit ratings or implicit clicks.<br>2. <strong>Matrix Factorization (SVD / ALS):</strong> Decompose sparse rating matrix into low-rank user embeddings $\\mathbf{P}$ and item embeddings $\\mathbf{Q}$: $\\mathbf{R} \\approx \\mathbf{P} \\mathbf{Q}^T$.<br>3. <strong>Two-Tower Neural Retrieval:</strong> Deep Query Tower embeds user features; Deep Candidate Tower embeds item features. Dot product measures affinity.<br>4. <strong>Two-Stage Architecture:</strong> Fast Retrieval stage (HNSW vector search narrows 10M items to 500) $\\to$ Heavy Ranking stage (XGBoost/Deep model scores top 500 to pick top 10).",
                "mathematics": "Matrix Factorization Objective with Regularization:<br>$$\\min_{\\mathbf{P}, \\mathbf{Q}} \\sum_{(u, i) \\in \\mathcal{K}} \\left( r_{ui} - \\mathbf{p}_u^T \\mathbf{q}_i \\right)^2 + \\lambda \\left( \\|\\mathbf{p}_u\\|^2 + \\|\\mathbf{q}_i\\|^2 \\right)$$<br>Two-Tower Cosine Logits with In-Batch Negative Sampling:<br>$$s(u, i) = \\frac{\\mathbf{f}_{\\text{user}}(u) \\cdot \\mathbf{g}_{\\text{item}}(i)}{\\|\\mathbf{f}_{\\text{user}}(u)\\| \\|\\mathbf{g}_{\\text{item}}(i)\\|}$$<br>$$\\mathcal{L} = -\\sum_{u} \\log \\frac{\\exp(s(u, i_u) / \\tau)}{\\sum_{j \\in \\text{Batch}} \\exp(s(u, j) / \\tau)}$$",
                "dataRequirements": "User interaction logs (clicks, watch time, purchases, ratings). Extreme sparsity: typically $>99.5\\%$ of user-item pairs are unobserved.",
                "hyperparameters": [
                    {"name": "Latent Embedding Dimension (k)", "description": "Number of latent factors (e.g. 32 to 128).", "effect": "Higher $k$ captures nuanced sub-genres; risks overfitting on inactive users."},
                    {"name": "Regularization (\\lambda)", "description": "L2 penalty on user and item embedding vectors.", "effect": "Prevents popular items from dominating all recommendations."},
                    {"name": "Temperature (\\tau)", "description": "Softmax temperature in two-tower loss.", "effect": "Tunes hardness of negative samples."}
                ],
                "strengths": [
                    "Directly drives corporate revenue and platform user retention.",
                    "Discovers unexpected cross-domain affinities (serendipity).",
                    "Two-tower architectures scale to hundreds of millions of candidates via sub-millisecond vector indexing (FAISS)."
                ],
                "limitations": [
                    "<strong>Cold Start Problem:</strong> Cannot recommend brand-new items or make personalized suggestions to new users with zero history.",
                    "Popularity bias: tends to disproportionately recommend blockbuster items, ignoring the long tail.",
                    "Feedback loops: users only click what is shown, reinforcing narrow filter bubbles."
                ],
                "evaluation": "Evaluated using **Hit Rate@K**, **NDCG@K** (Normalized Discounted Cumulative Gain), Precision@K, Mean Reciprocal Rank (MRR), and online A/B testing (Click-Through Rate / Conversion).",
                "workedExample": "Netflix movie recommendation. User Alice's latent vector: `[Action: 0.9, SciFi: 0.8, Romance: 0.1]`. Movie 'Dune' latent vector: `[Action: 0.8, SciFi: 0.9, Romance: 0.1]`. Dot product: $(0.9 \\times 0.8) + (0.8 \\times 0.9) + (0.1 \\times 0.1) = 0.72 + 0.72 + 0.01 = 1.45$. High score ranks 'Dune' in Alice's top recommendations carousel.",
                "whenToUse": "Use for e-commerce product feeds, streaming media queues, personalized newsletters, and social network friend suggestions.",
                "commonMistakes": [
                    "Confusing the Retrieval stage (candidate generation) with the Ranking stage (scoring precision).",
                    "Ignoring the Cold Start problem for newly published items."
                ],
                "furtherLearning": [
                    {"title": "Koren, Bell, Volinsky: Matrix Factorization Techniques for Recommender Systems (Netflix Prize 2009)", "url": "https://ieeexplore.ieee.org/document/5197422"},
                    {"title": "Covington, Adams, Sargin: Deep Neural Networks for YouTube Recommendations (2016)", "url": "https://research.google/pubs/pub45530/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the 'Cold Start' problem in Recommender Systems?",
                    "options": [
                        "When servers take too long to boot up in winter.",
                        "The challenge of accurately recommending items to brand-new users who have zero interaction history, or recommending brand-new items that have never been rated or clicked.",
                        "When all recommendations are identical.",
                        "When user ratings are all 5 stars."
                    ],
                    "correct": 1,
                    "explanation": "Collaborative filtering relies on past interaction history. When a new user or item arrives with zero interactions, the system has no historical data to compute affinities."
                },
                {
                    "question": "Why do modern industrial recommender systems (like YouTube and Pinterest) use a Two-Stage (Retrieval + Ranking) pipeline?",
                    "options": [
                        "Because one model is not allowed by software licenses.",
                        "Retrieving 100 items from 100 million using fast approximate vector search takes milliseconds; a heavy, complex deep ranking model can then precisely rank only those top 100 candidates.",
                        "To train on two different computers.",
                        "Because ranking models cannot process numbers."
                    ],
                    "correct": 1,
                    "explanation": "Scoring 100 million items with a heavy deep learning model in real-time is impossible ($>500$ ms). Fast vector retrieval filters millions to a few hundred candidates, which the heavy ranker sorts with sub-50ms latency."
                },
                {
                    "question": "What evaluation metric evaluates not just whether relevant items were recommended, but whether they appeared near the top of the recommendation list?",
                    "options": [
                        "Mean Squared Error",
                        "Normalized Discounted Cumulative Gain (NDCG@K)",
                        "Accuracy",
                        "Silhouette Score"
                    ],
                    "correct": 1,
                    "explanation": "NDCG incorporates position discounting: discovering a relevant item at Rank 1 yields significantly higher score than discovering it at Rank 20."
                }
            ]
        },
        {
            "id": "A03",
            "title": "Time-Series Forecasting",
            "module": "advanced",
            "level": "intermediate",
            "prerequisites": ["F01", "F03", "S01"],
            "estimatedMinutes": 25,
            "tags": ["time-series", "forecasting", "arima", "prophet", "stationarity", "temporal"],
            "shortDesc": "Forecast chronological sequences: trends, seasonality, stationarity, ARIMA models, and temporal deep learning.",
            "sections": {
                "whatItIs": "Time-Series Forecasting is the prediction of future values of a variable based on its historically observed chronological sequence. It models underlying temporal components: **Trend** (long-term progression), **Seasonality** (periodic cyclical patterns), and **Residuals** (stochastic noise), using classical statistical models (ARIMA, Exponential Smoothing) or modern architectures (Prophet, PatchTST).",
                "problemItSolves": "Enables forward-looking operational planning: electricity grid demand forecasting, retail inventory stockout prevention, financial revenue projection, and server capacity provisioning.",
                "intuition": "Imagine forecasting ice cream sales. You notice three patterns: First, sales grow 5% year-over-year as the town population grows (Trend). Second, sales skyrocket every July and plummet every December (Seasonality). Third, an unexpected 3-day heatwave in May creates a sudden spike (Stochastic Shock). Time series decomposition isolates each pattern to predict next July accurately.",
                "howItWorks": "1. <strong>Stationarity Check:</strong> Check if mean and variance are constant over time using the Augmented Dickey-Fuller (ADF) test.<br>2. <strong>Differencing ($d$):</strong> If non-stationary, difference the series: $\\Delta y_t = y_t - y_{t-1}$ until stationary.<br>3. <strong>Autoregressive ($p$) & Moving Average ($q$):</strong> Fit $\\text{ARIMA}(p, d, q)$ using Autocorrelation (ACF) and Partial Autocorrelation (PACF) plots.<br>4. <strong>Seasonality ($P, D, Q)_s$:</strong> Model periodic seasonal lags (SARIMA).<br>5. <strong>Modern Deep Learning:</strong> Process raw sequence patches with Temporal Fusion Transformers or PatchTST.",
                "mathematics": "ARIMA($p, d, q$) Equation for differenced series $y_t'$:<br>$$y_t' = c + \\sum_{i=1}^p \\phi_i y_{t-i}' + \\sum_{j=1}^q \\theta_j \\epsilon_{t-j} + \\epsilon_t$$<br>where $\\phi_i$ are Autoregressive terms, $\\theta_j$ are Moving Average shock terms, and $\\epsilon_t \\sim \\text{WN}(0, \\sigma^2)$.<br>Additive Decomposition Model:<br>$$y_t = \\text{Trend}_t + \\text{Seasonality}_t + \\text{Residual}_t$$<br>Walk-Forward Validation (Expanding Window):<br>$$\\text{Train on } [1 \\dots t], \\quad \\text{Evaluate on } [t+1 \\dots t+H]$$",
                "dataRequirements": "Chronologically ordered observations at uniform time intervals (hourly, daily, monthly). Zero temporal shuffling permitted.",
                "hyperparameters": [
                    {"name": "p, d, q Parameters", "description": "Orders of Autoregression, Differencing, and Moving Average.", "effect": "Selected via AIC minimization or auto_arima."},
                    {"name": "Seasonal Period (s)", "description": "Cycle duration (e.g. $s=7$ for daily data with weekly patterns; $s=12$ for monthly).", "effect": "Captures recurring seasonal swings."},
                    {"name": "Forecast Horizon (H)", "description": "Number of future time steps to predict.", "effect": "Uncertainty intervals widen rapidly as $H$ increases."}
                ],
                "strengths": [
                    "ARIMA/SARIMA provides mathematically rigorous prediction intervals and statistical interpretability.",
                    "Facebook Prophet handles missing data, holidays, and trend changepoints out-of-the-box.",
                    "Essential for physical supply chain and industrial operational capacity planning."
                ],
                "limitations": [
                    "Extreme sensitivity to regime changes and structural breaks (e.g. sudden pandemic demand shocks).",
                    "Error accumulation: recursive multi-step forecasting compounds errors over time.",
                    "Cannot foresee black swan events unrepresented in historical records."
                ],
                "evaluation": "Evaluated using Mean Absolute Scaled Error (MASE), Mean Absolute Percentage Error (MAPE), and RMSE using Walk-Forward Temporal Splits.",
                "workedExample": "Forecasting retail store customer traffic. Historical data shows an upward linear trend and weekly seasonality (peaks on Saturday, dips on Tuesday). Using SARIMA($1,1,1)(1,1,1)_7$ captures both the weekly rhythm and the underlying growth, predicting next week's staffing requirements within 4% of actual footfall.",
                "whenToUse": "Use for inventory management, energy load forecasting, macroeconomic planning, and call center staffing.",
                "commonMistakes": [
                    "Randomly shuffling time-series data into train/test sets (causes catastrophic lookahead data leakage).",
                    "Applying linear regression without removing trends and seasonality first (spurious correlation).",
                    "Using percentage error (MAPE) on data containing zeros (causes division by zero)."
                ],
                "furtherLearning": [
                    {"title": "Hyndman & Athanasopoulos: Forecasting: Principles and Practice (Free Online Textbook)", "url": "https://otexts.com/fpp3/"},
                    {"title": "Taylor & Letham: Forecasting at Scale (Prophet Paper 2017)", "url": "https://peerj.com/preprints/3190/"}
                ]
            },
            "quiz": [
                {
                    "question": "Why is random train/test shuffling strictly forbidden when evaluating time-series forecasting models?",
                    "options": [
                        "It crashes Python libraries.",
                        "It leaks future information into the training set (lookahead bias), allowing the model to 'cheat' by predicting the past from future data points.",
                        "It turns all values negative.",
                        "It deletes seasonality."
                    ],
                    "correct": 1,
                    "explanation": "Time-series data has temporal causality. Training on Tuesday and testing on Monday leaks future context that does not exist in real-world deployment."
                },
                {
                    "question": "What is 'Stationarity' in a time series?",
                    "options": [
                        "When the series does not move at all (all values zero).",
                        "A statistical property where the mean, variance, and autocorrelation structure remain constant over time, without time-dependent trends or seasonal variance changes.",
                        "When the model runs on a stationary desktop computer.",
                        "When errors are 100% predictable."
                    ],
                    "correct": 1,
                    "explanation": "A stationary process has time-invariant statistical properties (constant mean and variance). Differencing and log transforms are used to achieve stationarity before fitting ARIMA."
                },
                {
                    "question": "What does the 'd' parameter represent in an ARIMA(p, d, q) model?",
                    "options": [
                        "The number of days in a year.",
                        "The degree of differencing applied to remove non-stationary trends and stabilize the mean.",
                        "The dropout rate.",
                        "The number of decimal places."
                    ],
                    "correct": 1,
                    "explanation": "$d$ specifies the number of times consecutive observations are subtracted ($y_t - y_{t-1}$) to eliminate trends and achieve stationarity."
                }
            ]
        },
        {
            "id": "A04",
            "title": "Ensembles & Stacking",
            "module": "advanced",
            "level": "intermediate",
            "prerequisites": ["F06", "S06", "S09"],
            "estimatedMinutes": 20,
            "tags": ["stacking", "ensembles", "blending", "meta-learner", "out-of-fold"],
            "shortDesc": "Combine diverse model families using Out-of-Fold meta-learners to achieve maximum predictive performance.",
            "sections": {
                "whatItIs": "Stacking (Stacked Generalization / Super Learner) is a meta-ensembling technique that combines predictions from multiple diverse base models (e.g., LightGBM, Random Forest, Neural Network, Ridge Regression) using a meta-learner (typically a regularized linear model or shallow tree).",
                "problemItSolves": "No single algorithm dominates across all data patterns: trees excel at tabular thresholds, neural networks capture non-linear embeddings, and linear models extrapolate smoothly. Stacking learns an optimal non-linear weighting that exploits the complementary strengths of each model family.",
                "intuition": "Imagine a courtroom trial with three expert witnesses: an accountant, an engineer, and a psychologist. Each analyzes the evidence through their specialized lens. The judge (the Meta-Learner) listens to all three opinions and learns when to trust the accountant on numbers, the engineer on structural facts, and the psychologist on motives, rendering a superior verdict.",
                "howItWorks": "1. <strong>Base Models:</strong> Select diverse algorithms (e.g. XGBoost, CatBoost, MLP, SVM).<br>2. <strong>Out-of-Fold (OOF) Predictions:</strong> Using K-Fold CV, train base models on $K-1$ folds and generate out-of-sample predictions on the held-out fold, preventing data leakage.<br>3. <strong>Meta-Dataset:</strong> Stack the OOF prediction vectors from all base models into a new feature matrix $\\mathbf{X}_{\\text{meta}}$.<br>4. <strong>Train Meta-Learner:</strong> Fit the meta-learner on $\\mathbf{X}_{\\text{meta}}$ to predict true target $y$.<br>5. <strong>Inference:</strong> Pass new samples through all base models; feed their predictions into the meta-learner.",
                "mathematics": "Meta-Learner Prediction Function:<br>$$\\hat{y} = g\\left( f_1(\\mathbf{x}), f_2(\\mathbf{x}), \\dots, f_M(\\mathbf{x}); \\mathbf{w}_{\\text{meta}} \\right)$$<br>Out-of-Fold Generation for fold $k$:<br>$$z_{i, m} = f_m^{(-k)}(\\mathbf{x}_i) \\quad \\text{for } i \\in \\text{Fold}_k$$<br>Meta-model minimizes regularized loss on OOF matrix $\\mathbf{Z}$:<br>$$\\mathbf{w}^* = \\arg\\min_{\\mathbf{w}} \\sum_{i=1}^N \\mathcal{L}\\left( g(\\mathbf{z}_i; \\mathbf{w}), y_i \\right) + \\lambda \\|\\mathbf{w}\\|^2$$",
                "dataRequirements": "Tabular or multi-modal datasets. Requires clean K-fold cross-validation partitioning to generate OOF meta-features.",
                "hyperparameters": [
                    {"name": "Meta-Learner Family", "description": "Logistic Regression, Ridge, or LightGBM.", "effect": "Simple regularized linear meta-learners prevent meta-overfitting."},
                    {"name": "Number of Folds (K)", "description": "Folds used to generate OOF predictions (typically 5 or 10).", "effect": "Ensures clean, leak-free training data for the meta-learner."}
                ],
                "strengths": [
                    "The single most reliable strategy for winning competitive data science tournaments (Kaggle).",
                    "Extracts maximum possible performance by blending heterogeneous model inductive biases.",
                    "Can combine predictions across modalities (e.g. vision model predictions + tabular text features)."
                ],
                "limitations": [
                    "High operational complexity and compute overhead: requires maintaining and serving $M \\times K$ models in production.",
                    "High inference latency: cannot output a prediction until the slowest base model completes its forward pass.",
                    "Prone to subtle data leakage if Out-of-Fold partitioning is implemented incorrectly."
                ],
                "evaluation": "Evaluated via cross-validation log-loss, ROC-AUC, or RMSE compared against individual standalone base models.",
                "workedExample": "A Kaggle tabular challenge: Standalone LightGBM achieves 0.885 AUC; CatBoost achieves 0.884 AUC; a Deep MLP achieves 0.871 AUC. Stacking all three with a Ridge regression meta-learner achieves 0.894 AUC, capturing the top of the competition leaderboard.",
                "whenToUse": "Use when predictive accuracy is paramount (Kaggle competitions, high-value algorithmic trading, offline customer risk scoring).",
                "commonMistakes": [
                    "Generating meta-features using in-sample training predictions instead of Out-of-Fold predictions (causes catastrophic meta-overfitting).",
                    "Ensembling nearly identical models (e.g. 5 Random Forests with different seeds); diversity across model families is required for stacking gains."
                ],
                "furtherLearning": [
                    {"title": "Wolpert: Stacked Generalization (Neural Networks 1992)", "url": "https://www.sciencedirect.com/science/article/pii/S0893608005800231"},
                    {"title": "Van der Laan et al.: Super Learner (2007)", "url": "https://biostats.bepress.com/ucbbiostat/paper222/"}
                ]
            },
            "quiz": [
                {
                    "question": "Why MUST meta-features for training the meta-learner be generated using Out-of-Fold (OOF) cross-validation rather than standard training predictions?",
                    "options": [
                        "To make the code run faster.",
                        "Because base models have overly optimistic in-sample training accuracy; training the meta-learner on in-sample predictions causes it to overfit heavily to whichever base model memorized the training data most.",
                        "Because Python lists require folding.",
                        "To reduce the number of features."
                    ],
                    "correct": 1,
                    "explanation": "If a base model overfits its training data (e.g. achieves 100% training accuracy), a meta-learner trained on in-sample predictions will naively give that model 100% weight, collapsing completely on test data."
                },
                {
                    "question": "What type of diversity is most critical to achieve meaningful accuracy gains in a stacked ensemble?",
                    "options": [
                        "Diversity of programming languages.",
                        "Algorithmic diversity: combining different model families (e.g. Boosted Trees + Neural Networks + Linear Models) that make errors on different subsets of samples.",
                        "Using different fonts for plotting.",
                        "Diversity of monitor resolutions."
                    ],
                    "correct": 1,
                    "explanation": "If two models make the exact same errors on the exact same samples, averaging them provides zero benefit. Stacking thrives when models have orthogonal, uncorrelated error distributions."
                },
                {
                    "question": "What is the primary drawback of deploying a 20-model stacked ensemble into live production microservices?",
                    "options": [
                        "Stacked models cannot output JSON.",
                        "Severe inference latency and maintenance overhead: every query must be processed by all 20 base models before the meta-learner can respond.",
                        "Accuracy drops to zero.",
                        "It requires analog hardware."
                    ],
                    "correct": 1,
                    "explanation": "Production systems must maintain pipelines and dependencies for every single base model, and response latency is bounded by the slowest model in the ensemble."
                }
            ]
        },
        {
            "id": "A05",
            "title": "Transfer Learning & Fine-Tuning",
            "module": "advanced",
            "level": "intermediate",
            "prerequisites": ["D01", "D06", "D11", "D13"],
            "estimatedMinutes": 25,
            "tags": ["transfer-learning", "fine-tuning", "lora", "peft", "foundation-models"],
            "shortDesc": "Repurpose massive pre-trained foundation models for downstream tasks using feature extraction, full fine-tuning, and LoRA.",
            "sections": {
                "whatItIs": "Transfer Learning is the paradigm where a model pre-trained on a massive, general dataset (e.g. ImageNet, Common Crawl) is adapted to a specific downstream target task. Techniques range from <strong>Feature Extraction</strong> (freezing the backbone and training a new classification head) to <strong>Full Fine-Tuning</strong> and <strong>Parameter-Efficient Fine-Tuning (PEFT / LoRA)</strong>.",
                "problemItSolves": "Training modern vision backbones or LLMs from scratch requires thousands of GPUs and millions of dollars. Transfer learning allows practitioners to adapt multi-billion parameter foundation models to specialized domain tasks using a single GPU and a few hundred labeled examples.",
                "intuition": "Imagine hiring a master classical violinist to learn an Irish folk fiddle tune. You do not need to teach them how to hold a bow, read sheet music, or train finger dexterity from scratch—they already have 20 years of foundational mastery. They simply need a few afternoon practice sessions (fine-tuning) to learn the folk style.",
                "howItWorks": "1. <strong>Pre-trained Foundation:</strong> Start with weights trained on internet-scale self-supervised data.<br>2. <strong>Freeze Backbone:</strong> Freeze early representation layers that encode general features (edges, textures, grammar).<br>3. <strong>Replace Head:</strong> Replace final projection layer with task-specific head (e.g. 5-class medical diagnostic output).<br>4. <strong>LoRA (Low-Rank Adaptation):</strong> Freeze base weights $\\mathbf{W}_0$ and inject trainable rank-decomposition matrices: $\\mathbf{W} = \\mathbf{W}_0 + \\frac{\\alpha}{r} \\mathbf{B}\\mathbf{A}$, where $r \\ll d$.<br>5. <strong>Fine-Tuning:</strong> Train with small learning rates to prevent <strong>Catastrophic Forgetting</strong>.",
                "mathematics": "Low-Rank Adaptation (LoRA) Weight Decomposition:<br>$$\\mathbf{h} = \\mathbf{W}_0 \\mathbf{x} + \\Delta \\mathbf{W} \\mathbf{x} = \\mathbf{W}_0 \\mathbf{x} + \\frac{\\alpha}{r} \\mathbf{B} \\mathbf{A} \\mathbf{x}$$<br>where $\\mathbf{W}_0 \\in \\mathbb{R}^{d \\times k}$ is frozen, $\\mathbf{B} \\in \\mathbb{R}^{d \\times r}$, $\\mathbf{A} \\in \\mathbb{R}^{r \\times k}$, and rank $r \\ll \\min(d, k)$.<br>Parameter Reduction Ratio:<br>$$\\frac{2 r d}{d^2} = \\frac{2r}{d} \\quad (\\text{e.g. if } d=4096, r=8 \\implies 99.6\\% \\text{ fewer trainable parameters!})$$",
                "dataRequirements": "Small-to-moderate target task dataset (e.g. 500 to 50,000 labeled examples).",
                "hyperparameters": [
                    {"name": "LoRA Rank (r)", "description": "Rank of adaptation matrices (typically $r = 8, 16, \\text{or } 32$).", "effect": "Higher $r$ increases expressive capacity at a slight VRAM cost."},
                    {"name": "Learning Rate", "description": "Must be set significantly lower than pretraining (e.g. 1e-5 to 5e-5).", "effect": "Prevents catastrophic forgetting of foundational capabilities."},
                    {"name": "Layer Freezing Depth", "description": "Number of early backbone layers kept frozen.", "effect": "Preserves core feature extractors."}
                ],
                "strengths": [
                    "Drastically reduces training time, compute costs, and required labeled sample sizes.",
                    "Delivers state-of-the-art accuracy on specialized niche tasks with minimal data.",
                    "LoRA enables multi-tenant serving: one shared base model with tiny plug-and-play adapter weights."
                ],
                "limitations": [
                    "<strong>Catastrophic Forgetting:</strong> Model can lose general reasoning or prior knowledge when fine-tuned aggressively on narrow data.",
                    "Negative Transfer: If the source domain is completely disparate from the target domain, pre-trained weights can hinder performance."
                ],
                "evaluation": "Evaluated using downstream task metrics (Accuracy, F1, BLEU) while monitoring general benchmark retention to check for catastrophic forgetting.",
                "workedExample": "Fine-tuning LLaMA-3-8B for legal contract analysis. Base model has 8 billion parameters. Using LoRA with rank $r=16$ on attention matrices introduces only 20 million trainable parameters (0.25% of the model). It trains in 2 hours on a single consumer GPU, matching full fine-tuning accuracy without altering the base model weights.",
                "whenToUse": "The universal default in modern applied AI: adapting vision models and LLMs to proprietary business workflows.",
                "commonMistakes": [
                    "Using high pretraining learning rates (e.g. 1e-3) during fine-tuning, instantly destroying pre-trained weights.",
                    "Full fine-tuning of massive models when LoRA/QLoRA achieves identical accuracy with a fraction of the VRAM."
                ],
                "furtherLearning": [
                    {"title": "Hu et al.: LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022)", "url": "https://arxiv.org/abs/2106.09685"},
                    {"title": "Dettmers et al.: QLoRA: Efficient Finetuning of Quantized LLMs (2023)", "url": "https://arxiv.org/abs/2305.14314"}
                ]
            },
            "quiz": [
                {
                    "question": "What is 'Catastrophic Forgetting' in transfer learning and fine-tuning?",
                    "options": [
                        "When the computer hard drive corrupts.",
                        "When a pre-trained model fine-tuned on a new narrow task completely loses its previously learned general knowledge and capabilities.",
                        "When the learning rate decays to zero.",
                        "When the model refuses to train."
                    ],
                    "correct": 1,
                    "explanation": "Catastrophic forgetting occurs when updates on a new specialized dataset overwrite the delicate weight patterns that encoded general world knowledge and reasoning."
                },
                {
                    "question": "How does LoRA (Low-Rank Adaptation) drastically reduce VRAM usage during fine-tuning?",
                    "options": [
                        "It deletes 90% of the layers.",
                        "It freezes the original model weights and injects small low-rank trainable decomposition matrices ($B \\times A$), reducing the number of trainable parameters by up to 99%.",
                        "It only trains on CPU.",
                        "It eliminates backpropagation."
                    ],
                    "correct": 1,
                    "explanation": "LoRA freezes the billion-parameter base weight matrix $\\mathbf{W}_0$ and only tracks optimizer states and gradients for two tiny low-rank matrices $\\mathbf{A}$ and $\\mathbf{B}$."
                },
                {
                    "question": "Why should the learning rate used during fine-tuning typically be 10x to 100x smaller than the original pretraining learning rate?",
                    "options": [
                        "To prevent fine-tuning updates from wildly wrecking the carefully pre-trained representation manifolds.",
                        "Because small learning rates make the model file smaller.",
                        "Because fine-tuning datasets are always smaller than 10 rows.",
                        "To avoid GPU overheating."
                    ],
                    "correct": 0,
                    "explanation": "The base model already has excellent representations. Small learning rates make gentle, surgical parameter adjustments rather than aggressive exploratory leaps."
                }
            ]
        },
        {
            "id": "A06",
            "title": "Explainability & Interpretability",
            "module": "advanced",
            "level": "intermediate",
            "prerequisites": ["F01", "S01", "S05", "S06"],
            "estimatedMinutes": 25,
            "tags": ["xai", "shap", "lime", "feature-importance", "interpretability", "shapley-values"],
            "shortDesc": "Unpack black-box models using cooperative game theory (SHAP), local surrogate models (LIME), and permutation feature importance.",
            "sections": {
                "whatItIs": "Explainable AI (XAI) encompasses tools and mathematical methods that reveal why complex, non-linear machine learning models make specific predictions. Key approaches include **SHAP (SHapley Additive exPlanations)** (grounded in cooperative game theory) and **LIME (Local Interpretable Model-agnostic Explanations)** (fitting local linear surrogates).",
                "problemItSolves": "Deep neural networks and boosted ensembles are 'black boxes.' In regulated domains (banking, healthcare, criminal justice), regulators and clinicians require transparent causal explanations: Why was this mortgage denied? Why is this patient flagged for high cardiac risk?",
                "intuition": "Imagine a championship basketball team wins a game by 10 points. How much credit does each player deserve? The star point guard scored 25 points, but the center set 15 screens and grabbed 18 rebounds. Shapley values mathematically compute every player's exact marginal contribution to the final margin by evaluating team outcomes across every possible combination of players on the court.",
                "howItWorks": "1. <strong>Global vs Local:</strong> Global explains overall feature influence across the entire dataset; Local explains a single specific sample prediction.<br>2. <strong>Shapley Values:</strong> Measure the average marginal contribution of feature $j$ across all possible feature coalitions $S \\subseteq F \\setminus \\{j\\}$.<br>3. <strong>SHAP TreeExplainer:</strong> Fast exact algorithm for tree ensembles (XGBoost/Random Forest).<br>4. <strong>LIME:</strong> Perturb the input sample slightly $\\to$ query black-box predictions $\\to$ weight perturbed points by distance $\\to$ fit an interpretable sparse linear model locally.<br>5. <strong>Permutation Importance:</strong> Shuffle feature values in the test set and observe the drop in performance.",
                "mathematics": "Exact Shapley Value for feature $i$ (Cooperative Game Theory):<br>$$\\phi_i(v) = \\sum_{S \\subseteq F \\setminus \\{i\\}} \\frac{|S|! (|F| - |S| - 1)!}{|F|!} \\left[ v(S \\cup \\{i\\}) - v(S) \\right]$$<br>Additive Feature Attribution Property:<br>$$f(\\mathbf{x}) = \\phi_0 + \\sum_{i=1}^M \\phi_i$$<br>where $\\phi_0 = \\mathbb{E}[f(\\mathbf{x})]$ is the base value (dataset expected prediction) and $\\phi_i$ is the positive or negative contribution of feature $i$.",
                "dataRequirements": "Trained model and a background reference dataset (typically 100-500 representative samples) used to simulate missing features.",
                "hyperparameters": [
                    {"name": "Background Dataset Size", "description": "Number of reference samples in KernelSHAP.", "effect": "More samples increase Shapley approximation precision at the expense of compute time."},
                    {"name": "LIME Kernel Width", "description": "Width of the exponential distance weighting kernel.", "effect": "Defines what qualifies as 'local' neighborhood around the query."}
                ],
                "strengths": [
                    "SHAP is the only framework that satisfies four foundational game-theoretic axioms: Efficiency, Symmetry, Dummy, and Additivity.",
                    "Enables regulatory compliance: outputs individualized adverse action notices for credit denials.",
                    "Detects hidden data leakage and bugs (e.g. model relying on hospital watermark logos rather than lung pathology)."
                ],
                "limitations": [
                    "KernelSHAP is computationally expensive: scales exponentially with feature count without tree-specific optimizations.",
                    "LIME is unstable: different random perturbations can produce conflicting explanations for the same sample.",
                    "Correlation pitfalls: Shapley values evaluate unrealistic feature combinations when variables are strongly correlated."
                ],
                "evaluation": "Evaluated using Fidelity (how well the explanation reflects true model behavior), Robustness, and Human Comprehension user studies.",
                "workedExample": "A model predicts a patient has an 82% risk of diabetes (base rate = 15%). TreeSHAP decomposes the +67% deviation: Fasting Blood Glucose $= +35\\%$, Family History $= +20\\%$, Age $58 = +15\\%$, Regular Exercise $= -3\\%$. The sum of base rate + all Shapley values equals exactly 82%.",
                "whenToUse": "Mandatory in credit risk underwriting, healthcare diagnostics, fraud investigations, and debugging unexpected model errors.",
                "commonMistakes": [
                    "Confusing feature importance (global) with local instance explanations (a feature can have low global importance but be the deciding factor for one specific user).",
                    "Using default Mean Decrease in Impurity (MDI) from scikit-learn random forests (MDI heavily biases toward high-cardinality features; use Permutation or SHAP instead)."
                ],
                "furtherLearning": [
                    {"title": "Lundberg & Lee: A Unified Approach to Interpreting Model Predictions (SHAP 2017)", "url": "https://arxiv.org/abs/1705.07874"},
                    {"title": "Ribeiro, Singh, Guestrin: 'Why Should I Trust You?': Explaining the Predictions of Any Classifier (LIME 2016)", "url": "https://arxiv.org/abs/1602.04938"},
                    {"title": "Christoph Molnar: Interpretable Machine Learning (Free Online Book)", "url": "https://christophm.github.io/interpretable-ml-book/"}
                ]
            },
            "quiz": [
                {
                    "question": "What unique mathematical guarantee distinguishes SHAP (Shapley values) from all other feature attribution methods?",
                    "options": [
                        "It is the only method that runs in $\\mathcal{O}(1)$ time.",
                        "It is the only attribution method that simultaneously satisfies the four foundational axioms of cooperative game theory: Efficiency, Symmetry, Dummy player, and Additivity.",
                        "It guarantees 100% test accuracy.",
                        "It eliminates all correlation between features."
                    ],
                    "correct": 1,
                    "explanation": "Lloyd Shapley proved in 1953 that Shapley values are the unique allocation method satisfying efficiency (attributions sum to the total prediction minus base value), symmetry, dummy, and additivity."
                },
                {
                    "question": "Why is the default Mean Decrease in Impurity (Gini importance) in Random Forests often misleading?",
                    "options": [
                        "It cannot handle trees deeper than 3.",
                        "It heavily biases toward continuous features and categorical variables with high cardinality (many unique levels), artificially inflating their importance.",
                        "It only works on binary classification.",
                        "It always outputs negative values."
                    ],
                    "correct": 1,
                    "explanation": "MDI evaluates impurity drop at splits. Features with many unique categories (like IDs or dates) offer more candidate splits, artificially inflating their Gini score even if purely noise."
                },
                {
                    "question": "How does Permutation Feature Importance measure the significance of a feature $X_j$?",
                    "options": [
                        "By deleting the feature column entirely and retraining the model from scratch.",
                        "By randomly shuffling the values of $X_j$ in the test set to break its relationship with the target, and observing how much the model's evaluation score drops.",
                        "By setting all values of $X_j$ to 0.",
                        "By plotting a histogram."
                    ],
                    "correct": 1,
                    "explanation": "Permuting a column destroys its predictive correlation with the target while maintaining the baseline data distribution. A large drop in test accuracy signifies high feature importance."
                }
            ]
        },
        {
            "id": "A07",
            "title": "Responsible ML, Bias & Fairness",
            "module": "advanced",
            "level": "intermediate",
            "prerequisites": ["F01", "F03", "A06"],
            "estimatedMinutes": 25,
            "tags": ["fairness", "responsible-ai", "demographic-parity", "equalized-odds", "ethics"],
            "shortDesc": "Audit algorithmic bias, navigate fairness criteria tradeoffs, and mitigate systemic disparities in ML systems.",
            "sections": {
                "whatItIs": "Responsible Machine Learning is the discipline of auditing, measuring, and mitigating algorithmic unfairness, socio-demographic bias, and unintended harms. It operationalizes formal mathematical definitions of fairness—such as **Demographic Parity**, **Equal Opportunity**, and **Equalized Odds**—across sensitive protected attributes (race, gender, age).",
                "problemItSolves": "Machine learning models trained on historical data inevitably reflect and amplify historical societal discrimination, redlining, and sampling disparities. Unchecked models can systematically deny loans or healthcare to marginalized demographic groups.",
                "intuition": "Imagine evaluating applicants for university admissions. If historical admissions data was biased against students from rural schools, an ML model will learn that rural school addresses predict lower graduation rates, perpetuating the exclusion. Algorithmic fairness audits inspect the model's error distributions to guarantee equitable opportunities.",
                "howItWorks": "1. <strong>Define Protected Attributes:</strong> Identify sensitive features $A$ (e.g. gender, ethnicity).<br>2. <strong>Audit for Disparity:</strong> Compare positive outcome rates and error rates across demographic subgroups.<br>3. <strong>Mathematical Impossibility Theorem (Kleinberg et al., 2016):</strong> Prove that mutually competing fairness criteria (e.g. Calibration within groups and Equalized Odds) cannot be satisfied simultaneously unless base rates are identical.<br>4. <strong>Mitigation Strategies:</strong> Pre-processing (re-weighting data), In-processing (adversarial debiasing, fairness constraints), or Post-processing (group-specific decision threshold adjustment).",
                "mathematics": "Demographic (Statistical) Parity:<br>$$P(\\hat{Y} = 1 \\mid A = 0) = P(\\hat{Y} = 1 \\mid A = 1)$$<br>Equal Opportunity (True Positive Rate parity):<br>$$P(\\hat{Y} = 1 \\mid A = 0, Y = 1) = P(\\hat{Y} = 1 \\mid A = 1, Y = 1)$$<br>Equalized Odds (Both TPR and FPR parity):<br>$$P(\\hat{Y} = 1 \\mid A = a, Y = y) = P(\\hat{Y} = 1 \\mid A = b, Y = y) \\quad \\forall y \\in \\{0, 1\\}, \\; a, b \\in \\mathcal{A}$$<br>Disparate Impact Ratio (80% Rule in US employment law):<br>$$\\text{DIR} = \\frac{P(\\hat{Y} = 1 \\mid A = \\text{unprivileged})}{P(\\hat{Y} = 1 \\mid A = \\text{privileged})} \\ge 0.80$$",
                "dataRequirements": "Demographic metadata or proxy attributes collected for ethical auditing purposes. Strict privacy governance (differential privacy) required when handling sensitive personal attributes.",
                "hyperparameters": [
                    {"name": "Fairness Penalty (\\lambda)", "description": "Lagrange multiplier penalizing disparate impact in the objective loss.", "effect": "Enforces fairness constraints at a minor cost to global accuracy."},
                    {"name": "Subgroup Thresholds", "description": "Independent classification cutoff thresholds tuned per demographic group.", "effect": "Equalizes True Positive or False Positive rates post-training."}
                ],
                "strengths": [
                    "Guarantees ethical compliance with civil rights laws (EEOC, Fair Housing Act, EU AI Act).",
                    "Improves model robustness across underrepresented user segments.",
                    "Protects organizations from reputational, legal, and regulatory sanctions."
                ],
                "limitations": [
                    "Kleinberg's Impossibility Theorem: you cannot satisfy all fairness definitions simultaneously when ground-truth base rates differ.",
                    "'Fairness through Unawareness' fails: simply dropping protected attributes (like race) does not eliminate bias because proxy features (zip code, browsing habits) reconstruct it.",
                    "Post-processing threshold adjustments can face legal challenges in certain jurisdictions."
                ],
                "evaluation": "Evaluated using Disparate Impact Ratio, Equalized Odds Difference, Calibration curves per subgroup, and Fairlearn/AIF360 audit suites.",
                "workedExample": "A recidivism prediction model (e.g. COMPAS). An audit reveals that while the model has equal overall accuracy across racial groups, its False Positive Rate for Black defendants (predicted high-risk but did not re-offend) is twice as high as for White defendants (44% vs 23%). Tuning decision thresholds to satisfy Equalized Odds eliminates this disparity.",
                "whenToUse": "Mandatory in credit underwriting, criminal justice, employment hiring algorithms, medical triage, and public welfare allocation.",
                "commonMistakes": [
                    "Assuming that deleting the 'Gender' or 'Race' column makes a model unbiased ('Fairness through Unawareness' is completely ineffective due to proxy variables).",
                    "Optimizing purely for overall accuracy while ignoring catastrophic error rate disparities on minority subgroups."
                ],
                "furtherLearning": [
                    {"title": "Kleinberg, Mullainathan, Raghavan: Inherent Trade-Offs in the Fair Determination of Risk Scores (2016)", "url": "https://arxiv.org/abs/1609.05807"},
                    {"title": "Barocas, Hardt, Narayanan: Fairness and Machine Learning Book (Free Online)", "url": "https://fairmlbook.org/"},
                    {"title": "Microsoft Fairlearn Toolkit", "url": "https://fairlearn.org/"}
                ]
            },
            "quiz": [
                {
                    "question": "Why does 'Fairness through Unawareness' (simply removing sensitive columns like race or gender from the training data) fail to prevent algorithmic bias?",
                    "options": [
                        "Because machine learning models crash without demographic data.",
                        "Because other correlated features (e.g. zip code, school attended, purchase history, income) act as strong proxies that allow the model to reconstruct the protected attribute.",
                        "Because gender and race are always required by compilers.",
                        "It does not fail; it is the most effective fairness method."
                    ],
                    "correct": 1,
                    "explanation": "High-dimensional feature spaces contain rich proxy variables. In the US, geographical postal codes are heavily correlated with race due to historical housing patterns, allowing models to reconstruct protected attributes easily."
                },
                {
                    "question": "What is the central finding of Kleinberg's Impossibility Theorem regarding algorithmic fairness?",
                    "options": [
                        "Machine learning algorithms can never be trained ethically.",
                        "Except in trivial cases or when base rates are identical, it is mathematically impossible for a risk score to satisfy Calibration, Demographic Parity, and Equalized Odds simultaneously.",
                        "Fairness algorithms require quantum computers.",
                        "Accuracy is always zero when fairness is introduced."
                    ],
                    "correct": 1,
                    "explanation": "Kleinberg et al. mathematically proved that three fundamental fairness definitions—calibration within groups, equal false positives, and equal false negatives—are mutually incompatible whenever groups have differing base rates."
                },
                {
                    "question": "What is the US legal standard known as the '80% Rule' (Four-Fifths Rule) for measuring Disparate Impact in hiring or credit?",
                    "options": [
                        "80% of applicants must be accepted.",
                        "The selection rate for an unprivileged protected group must be at least 80% (four-fifths) of the selection rate for the highest privileged group.",
                        "Models must achieve at least 80% accuracy.",
                        "80% of data must be training data."
                    ],
                    "correct": 1,
                    "explanation": "The EEOC Four-Fifths rule states that if the selection rate for a protected demographic is less than 80% of the selection rate for the group with the highest rate, it constitutes prima facie evidence of disparate impact."
                }
            ]
        },
        {
            "id": "A08",
            "title": "Production MLOps & Deployment",
            "module": "advanced",
            "level": "intermediate",
            "prerequisites": ["F01", "F07", "A06"],
            "estimatedMinutes": 25,
            "tags": ["mlops", "deployment", "concept-drift", "data-drift", "monitoring", "model-serving"],
            "shortDesc": "Bridge the gap from prototype to production: low-latency model serving, Data Drift, Concept Drift, and monitoring pipelines.",
            "sections": {
                "whatItIs": "Machine Learning Operations (MLOps) is the engineering discipline that bridges prototype model training and continuous production deployment. It encompasses model packaging (ONNX, TensorRT), low-latency serving (FastAPI, Triton, vLLM), continuous CI/CD evaluation, telemetry tracking, and automated detection of **Data Drift** and **Concept Drift**.",
                "problemItSolves": "Over 80% of enterprise ML prototypes never make it into production, and those that do inevitably degrade over time as real-world distributions shift, consumer behaviors evolve, or upstream data pipelines alter schema formats.",
                "intuition": "Training a machine learning model in a Jupyter Notebook is like baking a single delicious soufflé in your home kitchen. MLOps is designing and running a chain of 500 commercial bakeries that must bake 50,000 identical soufflés every hour, monitor oven temperatures automatically, switch flour suppliers without changing taste, and trigger emergency alarms if a batch begins to spoil.",
                "howItWorks": "1. <strong>Model Serialization & Optimization:</strong> Export model graph to format-agnostic runtimes (ONNX, TorchScript); apply 8-bit/4-bit quantization and pruning.<br>2. <strong>Serving Architecture:</strong> Deploy via high-throughput model servers (Triton, vLLM) with dynamic batching and horizontal autoscaling.<br>3. <strong>Data Drift Monitoring:</strong> Track distribution shift in input features $P(X)$ using statistical tests (Kolmogorov-Smirnov, Population Stability Index / PSI).<br>4. <strong>Concept Drift Monitoring:</strong> Track shifts in the relationship between features and target $P(Y|X)$.<br>5. <strong>Automated Retraining:</strong> Trigger CI/CD retraining pipelines when drift metrics exceed warning thresholds.",
                "mathematics": "Population Stability Index (PSI) for feature $j$ across reference $R$ and production $P$ across $B$ bins:<br>$$\\text{PSI} = \\sum_{b=1}^B \\left( \\% P_b - \\% R_b \\right) \\times \\ln\\left( \\frac{\\% P_b}{\\% R_b} \\right)$$<br>Interpretation: $\\text{PSI} < 0.1$ (no significant shift); $0.1 \\le \\text{PSI} < 0.2$ (moderate shift); $\\text{PSI} \\ge 0.2$ (significant drift $\\to$ trigger alert/retrain).<br>Covariate Shift vs Concept Drift decomposition:<br>$$P(X, Y) = \\underbrace{P(X)}_{\\text{Covariate / Data Drift}} \\times \\underbrace{P(Y \\mid X)}_{\\text{Concept Drift}}$$",
                "dataRequirements": "Production telemetry logs (inference request payloads and output predictions stored in object storage like S3/GCS). Ground-truth target feedback loops (immediate for ad clicks; delayed for loan defaults).",
                "hyperparameters": [
                    {"name": "PSI Alert Threshold", "description": "Threshold trigger for automated alerts (standard: 0.2).", "effect": "Governs sensitivity to feature distribution shifts."},
                    {"name": "Quantization Precision", "description": "FP32 vs FP16 vs INT8 vs INT4 (AWQ/GPTQ).", "effect": "INT8 reduces memory by 4x and accelerates inference by 2x-3x with negligible accuracy loss."},
                    {"name": "Max Dynamic Batch Window", "description": "Time in milliseconds to buffer incoming queries to form a mini-batch.", "effect": "Trades off single-request latency against hardware GPU throughput."}
                ],
                "strengths": [
                    "Ensures production reliability, high availability (99.99%), and sub-50ms latency SLAs.",
                    "Provides automated safety guardrails: canary rollouts, blue-green deployments, and shadow testing.",
                    "Maintains model predictive performance over years despite shifting macro-economic environments."
                ],
                "limitations": [
                    "Requires substantial DevOps, cloud infrastructure, and distributed systems engineering expertise.",
                    "Delayed ground truth: in domains like credit risk, you do not know if a loan defaulted until 12 months later, making real-time accuracy monitoring impossible.",
                    "High infrastructure costs for dedicated GPU clusters."
                ],
                "evaluation": "Evaluated using operational metrics (P99 Latency, Requests Per Second / RPS, GPU Utilization, Error Rate) and statistical drift metrics (PSI, KS-statistic, Wasserstein distance).",
                "workedExample": "An e-commerce fraud model deployed in production. In November (Black Friday), incoming transaction volumes and average basket sizes jump 400%. The MLOps monitoring pipeline computes a PSI of 0.28 on the 'Basket Amount' feature, firing an alert. Shadow testing confirms the model is over-flagging legitimate holiday shoppers as fraudsters. The pipeline triggers an automated retraining job incorporating seasonal weights, restoring normal approval rates.",
                "whenToUse": "Mandatory whenever any machine learning model is deployed to serve real-world customer queries or business operations.",
                "commonMistakes": [
                    "Monitoring only server health (CPU/RAM/HTTP 200s) without monitoring statistical data drift (a model can return HTTP 200 OK while outputting complete garbage predictions).",
                    "Retraining blindly on uncurated, corrupted production data without automated regression integration tests.",
                    "Serving unquantized FP32 models on expensive GPUs when INT8 quantization would deliver identical accuracy at 1/4 the cost."
                ],
                "furtherLearning": [
                    {"title": "Sculley et al.: Hidden Technical Debt in Machine Learning Systems (Google NIPS 2015)", "url": "https://research.google/pubs/pub43146/"},
                    {"title": "Chip Huyen: Designing Machine Learning Systems (O'Reilly Book)", "url": "https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/"},
                    {"title": "Evidently AI: Open-Source ML Monitoring Guide", "url": "https://docs.evidentlyai.com/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the difference between 'Data Drift' (Covariate Shift) and 'Concept Drift'?",
                    "options": [
                        "Data drift is when the server crashes; concept drift is when the database runs out of space.",
                        "Data drift is a shift in the distribution of input features $P(X)$; Concept drift is a change in the statistical relationship between features and the target label $P(Y|X)$.",
                        "Data drift only happens in Python; concept drift only happens in C++.",
                        "They are identical terms with no difference."
                    ],
                    "correct": 1,
                    "explanation": "Data drift means input values change (e.g. users become younger). Concept drift means the fundamental mapping changes (e.g. what qualified as normal spending behavior during 2019 became fraudulent behavior during 2020 lockdowns)."
                },
                {
                    "question": "Why is HTTP 200 OK monitoring insufficient for monitoring machine learning models in production?",
                    "options": [
                        "Because HTTP status codes are obsolete.",
                        "A model server can return HTTP 200 OK responses with low latency while silently outputting completely nonsensical predictions due to silent data drift or upstream feature pipeline corruption.",
                        "Because HTTP 200 means there was an error.",
                        "Because models only communicate via WebSockets."
                    ],
                    "correct": 1,
                    "explanation": "Standard web metrics only verify that the server is alive. They cannot detect whether an upstream pipeline sent nulls, shifted categorical IDs, or caused the model to predict 100% false positives."
                },
                {
                    "question": "What deployment strategy routes live production traffic to a new candidate model to log its predictions alongside the existing legacy model WITHOUT returning the candidate's output to the user?",
                    "options": [
                        "Shadow (Dark) Deployment",
                        "Blue-Green Deployment",
                        "Canary Release",
                        "Hard Cutover"
                    ],
                    "correct": 0,
                    "explanation": "In Shadow deployment, production queries are duplicated and sent to the new candidate model in the background. Its predictions and latencies are recorded and compared without risking live user impact."
                }
            ]
        }
    ]
print("Advanced module defined: 8 lessons")

/* ============================================================
   FREE MIND ML — glossary.js
   Comprehensive Glossary: 114 Essential ML/DL Terms
   ============================================================ */
window.FML = window.FML || {};
window.FML.glossaryTerms = [
  {
    "term": "Activation Function",
    "category": "Deep Learning",
    "definition": "A mathematical non-linear function applied to a neuron's pre-activation (weighted sum + bias) that introduces curvature and non-linear expressive capacity into neural networks.",
    "lessonId": "D01"
  },
  {
    "term": "Adaptive Learning Rate",
    "category": "Optimization",
    "definition": "An optimization technique (e.g. RMSProp, Adam) that scales individual parameter updates inversely proportional to historical gradient magnitudes.",
    "lessonId": "D03"
  },
  {
    "term": "Agglomerative Clustering",
    "category": "Unsupervised",
    "definition": "A bottom-up hierarchical clustering method where each data point starts as an isolated cluster and pairs of closest clusters are recursively merged.",
    "lessonId": "U02"
  },
  {
    "term": "Algorithm vs Model",
    "category": "Foundations",
    "definition": "An algorithm is the learning procedure (e.g. Backpropagation), an architecture is the structural blueprint (e.g. ResNet), and a model is the trained artifact populated with learned weights.",
    "lessonId": "F07"
  },
  {
    "term": "Anomaly Detection",
    "category": "Unsupervised",
    "definition": "The unsupervised or semi-supervised identification of rare items, events, or observations that deviate significantly from the baseline distribution.",
    "lessonId": "U08"
  },
  {
    "term": "Apriori Principle",
    "category": "Unsupervised",
    "definition": "The anti-monotonicity rule in association rule learning: all non-empty subsets of a frequent itemset must also be frequent.",
    "lessonId": "U07"
  },
  {
    "term": "Attention Mechanism",
    "category": "Deep Learning",
    "definition": "A mathematical formulation (Scaled Dot-Product) enabling sequence elements to dynamically weight and aggregate representations from all other elements in parallel.",
    "lessonId": "D11"
  },
  {
    "term": "Autoregressive Model",
    "category": "Deep Learning",
    "definition": "A sequence model that predicts future tokens conditioned strictly on previously observed historical tokens.",
    "lessonId": "D13"
  },
  {
    "term": "Backpropagation",
    "category": "Deep Learning",
    "definition": "Reverse-mode automatic differentiation applying the multivariate calculus chain rule to compute the exact analytical gradient of loss with respect to all network parameters.",
    "lessonId": "D02"
  },
  {
    "term": "Bagging (Bootstrap Aggregating)",
    "category": "Supervised",
    "definition": "An ensemble technique that trains independent base learners in parallel on random bootstrap samples with replacement to reduce variance.",
    "lessonId": "S06"
  },
  {
    "term": "Batch Normalization",
    "category": "Deep Learning",
    "definition": "A layer technique that normalizes neuron activations across the mini-batch dimension to zero mean and unit variance, stabilizing deep training dynamics.",
    "lessonId": "D04"
  },
  {
    "term": "Batch Size",
    "category": "Foundations",
    "definition": "The number of training observations processed simultaneously in a single forward/backward optimization pass.",
    "lessonId": "F02"
  },
  {
    "term": "Bayes' Theorem",
    "category": "Foundations",
    "definition": "A foundational probability law calculating posterior probability: $P(A|B) = P(B|A)P(A) / P(B)$.",
    "lessonId": "S04"
  },
  {
    "term": "Bellman Equation",
    "category": "Advanced",
    "definition": "A dynamic programming equation decomposing the value of a state or state-action pair into immediate expected reward plus discounted future value.",
    "lessonId": "A01"
  },
  {
    "term": "Bias (Inductive)",
    "category": "Foundations",
    "definition": "The set of structural assumptions a machine learning algorithm makes to generalize beyond training observations (e.g. linearity in linear regression).",
    "lessonId": "F06"
  },
  {
    "term": "Bias-Variance Tradeoff",
    "category": "Foundations",
    "definition": "The fundamental tension between error from erroneous model assumptions (high bias / underfitting) and error from sensitivity to training noise fluctuations (high variance / overfitting).",
    "lessonId": "F06"
  },
  {
    "term": "Boosting",
    "category": "Supervised",
    "definition": "A sequential ensemble methodology where weak base learners are iteratively fit to the residuals or errors of prior models to reduce bias.",
    "lessonId": "S08"
  },
  {
    "term": "CatBoost",
    "category": "Supervised",
    "definition": "A high-performance gradient boosting library optimized for native handling of high-cardinality categorical variables via ordered target statistics.",
    "lessonId": "S10"
  },
  {
    "term": "Catastrophic Forgetting",
    "category": "Advanced",
    "definition": "The tendency of pre-trained neural networks to completely overwrite and lose prior knowledge when fine-tuned aggressively on a narrow new distribution.",
    "lessonId": "A05"
  },
  {
    "term": "Classifier-Free Guidance (CFG)",
    "category": "Deep Learning",
    "definition": "A sampling technique in diffusion models that interpolates between unconditional and conditional predictions to amplify prompt adherence.",
    "lessonId": "D14"
  },
  {
    "term": "Cold Start Problem",
    "category": "Advanced",
    "definition": "The inability of collaborative filtering recommender systems to draw meaningful inferences about brand-new users or catalog items lacking historical interactions.",
    "lessonId": "A02"
  },
  {
    "term": "Collaborative Filtering",
    "category": "Advanced",
    "definition": "Recommender system algorithm predicting user preferences by identifying taste similarities and overlapping interaction patterns across a community of users.",
    "lessonId": "A02"
  },
  {
    "term": "Concept Drift",
    "category": "Advanced",
    "definition": "A shift in the underlying statistical relationship between input features and target outputs ($P(Y|X)$) over time in production environments.",
    "lessonId": "A08"
  },
  {
    "term": "Confusion Matrix",
    "category": "Foundations",
    "definition": "A contingency table detailing True Positives, False Positives, True Negatives, and False Negatives produced by a classification model.",
    "lessonId": "F05"
  },
  {
    "term": "Convolutional Layer (CNN)",
    "category": "Deep Learning",
    "definition": "A neural layer that applies learnable spatial filter kernels across grid tensors to enforce translation equivariance and local receptive fields.",
    "lessonId": "D06"
  },
  {
    "term": "Cosine Similarity",
    "category": "Deep Learning",
    "definition": "The cosine of the angle between two non-zero vectors in an inner product space: $\\cos(\\theta) = (u \\cdot v) / (||u|| ||v||)$.",
    "lessonId": "D12"
  },
  {
    "term": "Cost Function",
    "category": "Foundations",
    "definition": "A scalar objective function measuring average prediction error over an entire batch or dataset (contrast with Loss, computed per sample).",
    "lessonId": "F02"
  },
  {
    "term": "Cross-Validation (K-Fold)",
    "category": "Foundations",
    "definition": "A statistical re-sampling technique partitioning data into $K$ equal subsets to iteratively train on $K-1$ and evaluate on the remaining fold.",
    "lessonId": "F03"
  },
  {
    "term": "Data Drift (Covariate Shift)",
    "category": "Advanced",
    "definition": "A shift in the distribution of input features ($P(X)$) between training data and live production inference streams.",
    "lessonId": "A08"
  },
  {
    "term": "Data Leakage",
    "category": "Foundations",
    "definition": "A fatal pipeline flaw where information from outside the training partition (such as test labels or future timestamps) contaminates the model during training.",
    "lessonId": "F03"
  },
  {
    "term": "DBSCAN",
    "category": "Unsupervised",
    "definition": "A density-based clustering algorithm that groups core points in high-density regions and explicitly labels sparse points as noise (-1).",
    "lessonId": "U03"
  },
  {
    "term": "Decision Boundary",
    "category": "Supervised",
    "definition": "The mathematical geometric hypersurface in feature space where a model's predicted class probability is equal across competing categories.",
    "lessonId": "S02"
  },
  {
    "term": "Decision Tree",
    "category": "Supervised",
    "definition": "A non-parametric model that recursively partitions feature space using orthogonal axis-aligned threshold splits to maximize information gain.",
    "lessonId": "S05"
  },
  {
    "term": "Dendrogram",
    "category": "Unsupervised",
    "definition": "A branching tree diagram displaying the complete hierarchical merger history and linkage distances of agglomerative clustering.",
    "lessonId": "U02"
  },
  {
    "term": "Diffusion Model (DDPM)",
    "category": "Deep Learning",
    "definition": "A generative model that creates samples by learning to iteratively reverse a forward Gaussian noise corruption process.",
    "lessonId": "D14"
  },
  {
    "term": "Disparate Impact",
    "category": "Advanced",
    "definition": "A metric measuring algorithmic discrimination when an apparently neutral decision rule results in significantly worse outcomes for a protected demographic.",
    "lessonId": "A07"
  },
  {
    "term": "Dropout",
    "category": "Deep Learning",
    "definition": "A stochastic regularization technique that randomly zeroes a fraction $p$ of hidden neuron activations during training to break co-adaptations.",
    "lessonId": "D04"
  },
  {
    "term": "Elbow Method",
    "category": "Unsupervised",
    "definition": "A heuristic used to select the optimal number of clusters $k$ by identifying the inflection point where within-cluster inertia reduction flattens.",
    "lessonId": "U01"
  },
  {
    "term": "Embedding",
    "category": "Deep Learning",
    "definition": "A learned continuous vector representation mapping discrete entities (words, products, users) into low-dimensional semantic space.",
    "lessonId": "D12"
  },
  {
    "term": "Epoch",
    "category": "Foundations",
    "definition": "One complete training pass of the optimization algorithm over all training samples in the dataset.",
    "lessonId": "F02"
  },
  {
    "term": "Equalized Odds",
    "category": "Advanced",
    "definition": "A fairness definition requiring a classification model to achieve equal True Positive Rates and equal False Positive Rates across all demographic subgroups.",
    "lessonId": "A07"
  },
  {
    "term": "Evidence Lower Bound (ELBO)",
    "category": "Deep Learning",
    "definition": "The variational objective function maximized in VAEs, combining reconstruction fidelity with a KL divergence latent penalty.",
    "lessonId": "D09"
  },
  {
    "term": "Experience Replay",
    "category": "Deep Learning",
    "definition": "A buffer technique in Deep Q-Networks that stores past environment transitions and samples them randomly to break temporal correlations.",
    "lessonId": "D16"
  },
  {
    "term": "Explainable AI (XAI)",
    "category": "Advanced",
    "definition": "Methods and tools that explain the internal decisions, feature attributions, and reasoning of black-box machine learning models.",
    "lessonId": "A06"
  },
  {
    "term": "Extra Trees",
    "category": "Supervised",
    "definition": "Extremely Randomized Trees: an ensemble that draws split cut-points uniformly at random rather than calculating optimal thresholds.",
    "lessonId": "S07"
  },
  {
    "term": "F1-Score",
    "category": "Foundations",
    "definition": "The harmonic mean of Precision and Recall: $2 \\cdot (P \\cdot R) / (P + R)$, ideal for imbalanced classification.",
    "lessonId": "F05"
  },
  {
    "term": "Feature",
    "category": "Foundations",
    "definition": "An individual measurable variable, attribute, or column describing an observed data entity.",
    "lessonId": "F02"
  },
  {
    "term": "Focal Loss",
    "category": "Deep Learning",
    "definition": "A cross-entropy loss variant that dynamically down-weights easy, well-classified examples to focus gradients on rare, hard samples.",
    "lessonId": "D04"
  },
  {
    "term": "Gaussian Mixture Model (GMM)",
    "category": "Unsupervised",
    "definition": "A soft-clustering probabilistic model representing the data distribution as a weighted combination of multiple multivariate Gaussians.",
    "lessonId": "U04"
  },
  {
    "term": "GELU (Gaussian Error Linear Unit)",
    "category": "Deep Learning",
    "definition": "A smooth activation function weighting inputs by their cumulative Gaussian probability: $x \\cdot \\Phi(x)$, standard in modern Transformers.",
    "lessonId": "D01"
  },
  {
    "term": "Gini Impurity",
    "category": "Supervised",
    "definition": "A measure of node statistical impurity in CART decision trees: $1 - \\sum p_k^2$, indicating the probability of incorrect labeling.",
    "lessonId": "S05"
  },
  {
    "term": "Gradient Boosting (GBM)",
    "category": "Supervised",
    "definition": "An additive ensemble framework where base decision trees are sequentially fit to the negative gradients (pseudo-residuals) of a loss function.",
    "lessonId": "S09"
  },
  {
    "term": "Gradient Descent",
    "category": "Optimization",
    "definition": "A first-order iterative optimization algorithm that updates parameters in the direction of the steepest negative gradient: $\\theta \\leftarrow \\theta - \\alpha \\nabla J$.",
    "lessonId": "D03"
  },
  {
    "term": "Graph Neural Network (GNN)",
    "category": "Deep Learning",
    "definition": "A neural architecture that processes non-Euclidean graphs by iteratively passing and aggregating feature messages along structural edges.",
    "lessonId": "D15"
  },
  {
    "term": "Hallucination",
    "category": "Deep Learning",
    "definition": "The phenomenon where a Large Language Model produces factually incorrect, ungrounded assertions with high linguistic fluency.",
    "lessonId": "D13"
  },
  {
    "term": "He / Kaiming Initialization",
    "category": "Deep Learning",
    "definition": "A weight initialization distribution with variance $2 / n_{in}$, mathematically tailored to prevent vanishing signal variance in ReLU layers.",
    "lessonId": "D01"
  },
  {
    "term": "Hyperparameter",
    "category": "Foundations",
    "definition": "A configuration variable set by the engineer before training begins (e.g. learning rate, tree depth, batch size) that cannot be updated directly by the optimizer.",
    "lessonId": "F02"
  },
  {
    "term": "In-Context Learning",
    "category": "Deep Learning",
    "definition": "The emergent ability of foundation LLMs to perform new tasks simply by reading examples provided inside the input prompt without parameter updates.",
    "lessonId": "D13"
  },
  {
    "term": "Inertia",
    "category": "Unsupervised",
    "definition": "The within-cluster sum of squared Euclidean distances from each data point to its assigned cluster centroid in k-Means.",
    "lessonId": "U01"
  },
  {
    "term": "Isolation Forest",
    "category": "Unsupervised",
    "definition": "An anomaly detection ensemble that isolates outliers via random orthogonal feature partitions, exploiting the fact that anomalies have short tree path lengths.",
    "lessonId": "U08"
  },
  {
    "term": "k-Nearest Neighbors (KNN)",
    "category": "Supervised",
    "definition": "An instance-based supervised model classifying query points via the majority label of their $k$ closest neighbors in feature space.",
    "lessonId": "S03"
  },
  {
    "term": "Kernel Trick",
    "category": "Supervised",
    "definition": "A mathematical technique computing dot products in high-dimensional feature spaces implicitly via kernel functions without transforming coordinates.",
    "lessonId": "S11"
  },
  {
    "term": "Kullback-Leibler (KL) Divergence",
    "category": "Deep Learning",
    "definition": "A non-symmetric statistical measure of relative entropy quantifying the information lost when approximating probability distribution $P$ with $Q$.",
    "lessonId": "D09"
  },
  {
    "term": "Layer Normalization",
    "category": "Deep Learning",
    "definition": "A normalization layer that standardizes activations across the feature dimension for each individual sequence token independently of the batch size.",
    "lessonId": "D04"
  },
  {
    "term": "Learning Rate",
    "category": "Optimization",
    "definition": "The hyperparameter step magnitude scaling parameter updates along the gradient descent trajectory.",
    "lessonId": "D03"
  },
  {
    "term": "Lift",
    "category": "Unsupervised",
    "definition": "In association rules, the ratio of observed co-occurrence of itemset $X$ and $Y$ to their expected co-occurrence under complete statistical independence.",
    "lessonId": "U07"
  },
  {
    "term": "LightGBM",
    "category": "Supervised",
    "definition": "A fast gradient boosting framework using histogram-based feature binning, leaf-wise tree growth, and exclusive feature bundling.",
    "lessonId": "S10"
  },
  {
    "term": "Linear Regression",
    "category": "Supervised",
    "definition": "A classical supervised regression model estimating continuous targets by fitting a linear hyperplane that minimizes sum of squared residuals.",
    "lessonId": "S01"
  },
  {
    "term": "Local Outlier Factor (LOF)",
    "category": "Unsupervised",
    "definition": "An anomaly detection algorithm that compares the local density of an observation to the densities of its $k$-nearest neighbors.",
    "lessonId": "U08"
  },
  {
    "term": "Logistic Regression",
    "category": "Supervised",
    "definition": "A linear classification model that transforms a linear combination of features through the Sigmoid activation to estimate class probabilities.",
    "lessonId": "S02"
  },
  {
    "term": "Long Short-Term Memory (LSTM)",
    "category": "Deep Learning",
    "definition": "A gated recurrent neural network architecture featuring an additive cell state and input, forget, and output gates to solve vanishing gradients.",
    "lessonId": "D08"
  },
  {
    "term": "Low-Rank Adaptation (LoRA)",
    "category": "Advanced",
    "definition": "A parameter-efficient fine-tuning (PEFT) method freezing pre-trained weights and training small low-rank decomposition matrices ($B \\times A$).",
    "lessonId": "A05"
  },
  {
    "term": "Markov Decision Process (MDP)",
    "category": "Advanced",
    "definition": "A mathematical framework for modeling decision making where outcomes are partly random and partly under the control of a decision-making agent.",
    "lessonId": "A01"
  },
  {
    "term": "Matrix Factorization",
    "category": "Advanced",
    "definition": "Decomposing a large sparse user-item interaction matrix into the product of two lower-rank dense matrices capturing latent user and item factors.",
    "lessonId": "A02"
  },
  {
    "term": "Maximum Margin Hyperplane",
    "category": "Supervised",
    "definition": "The unique separating decision boundary found by an SVM that maximizes the geometric distance to the closest training points.",
    "lessonId": "S11"
  },
  {
    "term": "Mean Squared Error (MSE)",
    "category": "Foundations",
    "definition": "The average of the squared differences between predicted values and ground truth targets: $\\frac{1}{N} \\sum (y_i - \\hat{y}_i)^2$.",
    "lessonId": "S01"
  },
  {
    "term": "Message Passing",
    "category": "Deep Learning",
    "definition": "The computational framework of Graph Neural Networks wherein nodes generate messages, aggregate neighbor messages, and update their states.",
    "lessonId": "D15"
  },
  {
    "term": "MLOps",
    "category": "Advanced",
    "definition": "Machine Learning Operations: the set of practices and tooling unifying ML system development, automated CI/CD, testing, serving, and monitoring.",
    "lessonId": "A08"
  },
  {
    "term": "Multilayer Perceptron (MLP)",
    "category": "Supervised",
    "definition": "A feedforward neural network comprising multiple dense layers interleaved with non-linear activation functions.",
    "lessonId": "S13"
  },
  {
    "term": "Naive Bayes",
    "category": "Supervised",
    "definition": "A fast probabilistic classifier based on Bayes' theorem under the assumption that all features are mutually independent given the class label.",
    "lessonId": "S04"
  },
  {
    "term": "One-Class SVM",
    "category": "Unsupervised",
    "definition": "An unsupervised algorithm that fits a tight hypersphere or boundary around normal training data in feature space to identify novel outliers.",
    "lessonId": "U08"
  },
  {
    "term": "Ordinary Least Squares (OLS)",
    "category": "Supervised",
    "definition": "The analytical closed-form method for estimating linear regression coefficients by minimizing the sum of squared vertical residuals.",
    "lessonId": "S01"
  },
  {
    "term": "Out-of-Bag (OOB) Error",
    "category": "Supervised",
    "definition": "The mean prediction error in a Random Forest evaluated on training samples excluded from individual tree bootstrap partitions.",
    "lessonId": "S06"
  },
  {
    "term": "Overfitting",
    "category": "Foundations",
    "definition": "When a model memorizes idiosyncrasies, random noise, and spurious correlations in the training set, causing validation and test accuracy to degrade.",
    "lessonId": "F06"
  },
  {
    "term": "Perceptron",
    "category": "Supervised",
    "definition": "The earliest artificial neuron model (Rosenblatt, 1958) that passes a linear combination of inputs through a hard binary threshold step function.",
    "lessonId": "S12"
  },
  {
    "term": "Permutation Feature Importance",
    "category": "Advanced",
    "definition": "A model-agnostic metric that measures the drop in model evaluation score when values of a specific feature column are randomly shuffled.",
    "lessonId": "A06"
  },
  {
    "term": "Precision and Recall",
    "category": "Foundations",
    "definition": "Precision is the ratio of true positive predictions to total predicted positives; Recall is the ratio of true positives to total actual positives.",
    "lessonId": "F05"
  },
  {
    "term": "Principal Component Analysis (PCA)",
    "category": "Unsupervised",
    "definition": "A linear dimensionality reduction algorithm that projects data onto orthogonal axes that sequentially maximize statistical variance.",
    "lessonId": "U05"
  },
  {
    "term": "Proximal Policy Optimization (PPO)",
    "category": "Deep Learning",
    "definition": "An actor-critic deep reinforcement learning algorithm that clips policy probability updates within $[1-\\epsilon, 1+\\epsilon]$ to prevent catastrophic divergence.",
    "lessonId": "D16"
  },
  {
    "term": "Q-Learning",
    "category": "Advanced",
    "definition": "A model-free, off-policy reinforcement learning algorithm that learns the optimal action-value function $Q(s, a)$ via temporal difference updates.",
    "lessonId": "A01"
  },
  {
    "term": "R-Squared ($R^2$)",
    "category": "Supervised",
    "definition": "The coefficient of determination measuring the proportion of target variance explained by explanatory features relative to a naive mean baseline.",
    "lessonId": "S01"
  },
  {
    "term": "Random Forest",
    "category": "Supervised",
    "definition": "An ensemble of decorrelated decision trees trained on bootstrap samples with random feature subsampling at each split.",
    "lessonId": "S06"
  },
  {
    "term": "Regularization (L1 & L2)",
    "category": "Supervised",
    "definition": "Penalties added to the objective loss ($L_1$ Lasso absolute sum, $L_2$ Ridge squared sum) that constrain parameter weights to prevent overfitting.",
    "lessonId": "F06"
  },
  {
    "term": "Reinforcement Learning (RL)",
    "category": "Foundations",
    "definition": "A paradigm where an agent learns through trial-and-error environmental interactions to maximize cumulative scalar rewards over time.",
    "lessonId": "F04"
  },
  {
    "term": "Residual Connection (Skip Connection)",
    "category": "Deep Learning",
    "definition": "An architectural identity shortcut adding a layer's input directly to its transformed output: $\\mathbf{x} + \\mathcal{F}(\\mathbf{x})$, enabling ultra-deep backpropagation.",
    "lessonId": "D05"
  },
  {
    "term": "ROC-AUC",
    "category": "Foundations",
    "definition": "The Area Under the Receiver Operating Characteristic Curve, measuring a binary classifier's ability to rank positive samples above negative samples across all thresholds.",
    "lessonId": "F05"
  },
  {
    "term": "Self-Attention",
    "category": "Deep Learning",
    "definition": "An attention mechanism relating different positions of a single sequence to compute a contextual representation of the sequence.",
    "lessonId": "D11"
  },
  {
    "term": "SHAP (Shapley Additive exPlanations)",
    "category": "Advanced",
    "definition": "A game-theoretic framework that allocates credit for a prediction among input features based on their marginal contributions across all feature coalitions.",
    "lessonId": "A06"
  },
  {
    "term": "Sigmoid Function",
    "category": "Supervised",
    "definition": "An S-shaped mathematical activation function $\\sigma(z) = 1 / (1 + e^{-z})$ that squashes any real-valued number into a valid probability between 0 and 1.",
    "lessonId": "S02"
  },
  {
    "term": "Silhouette Score",
    "category": "Unsupervised",
    "definition": "A metric evaluating clustering quality measuring how similar an object is to its own cluster compared to other clusters, ranging from -1 to +1.",
    "lessonId": "U01"
  },
  {
    "term": "Softmax",
    "category": "Deep Learning",
    "definition": "A generalization of the sigmoid function that normalizes a vector of arbitrary real numbers into a categorical probability distribution that sums to 1.0.",
    "lessonId": "D01"
  },
  {
    "term": "Stationarity",
    "category": "Advanced",
    "definition": "The statistical property of a time series whose mean, variance, and autocorrelation remain constant over time.",
    "lessonId": "A03"
  },
  {
    "term": "Stochastic Gradient Descent (SGD)",
    "category": "Optimization",
    "definition": "A gradient descent variant that computes loss gradients on random mini-batches of data rather than the entire dataset.",
    "lessonId": "D03"
  },
  {
    "term": "Support Vector Machine (SVM)",
    "category": "Supervised",
    "definition": "A maximum-margin supervised classifier that finds the optimal separating hyperplane and utilizes kernel functions for non-linear classification.",
    "lessonId": "S11"
  },
  {
    "term": "t-SNE",
    "category": "Unsupervised",
    "definition": "A non-linear dimensionality reduction technique modeling local neighborhood probabilities with heavy-tailed Student-t distributions for 2D/3D visualization.",
    "lessonId": "U06"
  },
  {
    "term": "Temperature (Sampling)",
    "category": "Deep Learning",
    "definition": "A hyperparameter scaling logits prior to Softmax: lower values produce deterministic output; higher values increase diversity.",
    "lessonId": "D13"
  },
  {
    "term": "Transfer Learning",
    "category": "Advanced",
    "definition": "The process of taking a foundational model pre-trained on a massive dataset and adapting it to a specific target task with minimal extra training.",
    "lessonId": "A05"
  },
  {
    "term": "Transformer",
    "category": "Deep Learning",
    "definition": "A neural network architecture based entirely on self-attention mechanisms and feedforward blocks that processes tokens in parallel without recurrence.",
    "lessonId": "D11"
  },
  {
    "term": "UMAP",
    "category": "Unsupervised",
    "definition": "Uniform Manifold Approximation and Projection: a fast, theoretically grounded non-linear manifold dimension reduction algorithm.",
    "lessonId": "U06"
  },
  {
    "term": "Underfitting",
    "category": "Foundations",
    "definition": "When a machine learning model lacks sufficient capacity to capture the underlying mathematical structure of the data, exhibiting high training and test error.",
    "lessonId": "F06"
  },
  {
    "term": "Universal Approximation Theorem",
    "category": "Supervised",
    "definition": "The theorem proving that a feedforward network with a single hidden layer and non-linear activation can approximate any continuous function to arbitrary precision.",
    "lessonId": "S13"
  },
  {
    "term": "Variational Autoencoder (VAE)",
    "category": "Deep Learning",
    "definition": "A generative autoencoder that regularizes its bottleneck latent space to follow a standard Gaussian distribution using the reparameterization trick.",
    "lessonId": "D09"
  },
  {
    "term": "Weight Decay",
    "category": "Optimization",
    "definition": "A regularization method that penalizes large parameter weights by decaying them by a fraction $\\lambda$ at each optimization step.",
    "lessonId": "D03"
  },
  {
    "term": "XGBoost",
    "category": "Supervised",
    "definition": "Extreme Gradient Boosting: an optimized distributed gradient boosting library using 2nd-order Taylor approximations, exact quantile splits, and hardware acceleration.",
    "lessonId": "S10"
  }
];

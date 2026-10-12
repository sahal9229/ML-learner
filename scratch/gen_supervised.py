# -*- coding: utf-8 -*-
"""
Module 1: Classical Supervised Learning (S01 - S13)
13 complete lessons with all 15 sections, LaTeX mathematics, hyperparameters, and 3-question quizzes.
"""

def get_supervised():
    return [
        {
            "id": "S01",
            "title": "Linear & Polynomial Regression",
            "module": "supervised",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "F05"],
            "estimatedMinutes": 20,
            "tags": ["regression", "linear", "polynomial", "ols", "residuals"],
            "shortDesc": "Fit optimal hyperplanes and polynomial curves to continuous response variables using Ordinary Least Squares and gradient descent.",
            "sections": {
                "whatItIs": "Linear Regression models the relationship between a scalar continuous dependent variable $y$ and one or more explanatory independent variables $X$ by fitting a linear hyperplane. Polynomial Regression expands this capacity by introducing polynomial powers of the original features ($x, x^2, x^3, \\dots$), allowing linear estimators to fit curved non-linear surfaces.",
                "problemItSolves": "Provides an interpretable, mathematically exact baseline for continuous numerical estimation (e.g., forecasting revenue, energy consumption, or biological metrics) and estimates the statistical effect size of individual predictor variables.",
                "intuition": "Imagine scattering points on a sheet of graph paper. Linear regression is laying a rigid wooden ruler through the middle of the scatter so that the sum of vertical gaps from the ruler to every dot is as small as possible. Polynomial regression replaces the rigid wooden ruler with a flexible plastic curve that bends to follow the terrain.",
                "howItWorks": "1. <strong>Linear Hypothesis:</strong> $\\hat{y} = w_0 + w_1 x_1 + \\dots + w_D x_D = \\mathbf{w}^T \\mathbf{x}$.<br>2. <strong>Polynomial Expansion:</strong> Map feature space $\\phi(x) = [1, x, x^2, \\dots, x^p]^T$.<br>3. <strong>Loss Function:</strong> Compute Sum of Squared Errors (SSE) or Mean Squared Error (MSE).<br>4. <strong>Optimization:</strong> Solve analytically via the closed-form Normal Equation $\\mathbf{w} = (\\mathbf{X}^T \\mathbf{X})^{-1}\\mathbf{X}^T\\mathbf{y}$, or iteratively via Gradient Descent when $N$ or $D$ is massive.",
                "mathematics": "Ordinary Least Squares Objective:<br>$$J(\\mathbf{w}) = \\frac{1}{2N} \\sum_{i=1}^N \\left( \\mathbf{w}^T \\mathbf{x}^{(i)} - y^{(i)} \\right)^2 = \\frac{1}{2N} \\|\\mathbf{X}\\mathbf{w} - \\mathbf{y}\\|^2$$<br>Closed-Form Normal Equation Solution:<br>$$\\mathbf{w}^* = (\\mathbf{X}^T \\mathbf{X})^{-1} \\mathbf{X}^T \\mathbf{y}$$<br>Gradient Descent Update:<br>$$\\mathbf{w} \\leftarrow \\mathbf{w} - \\alpha \\frac{1}{N} \\mathbf{X}^T (\\mathbf{X}\\mathbf{w} - \\mathbf{y})$$",
                "dataRequirements": "Continuous numeric target. Independent variables should ideally be linearly independent (no severe multicollinearity) and errors should be homoscedastic (constant variance across predictions). Highly sensitive to extreme outliers.",
                "hyperparameters": [
                    {"name": "Polynomial Degree (d)", "description": "Maximum power to which feature terms are elevated.", "effect": "Degree 1 is linear. Degrees > 3 risk severe runaway oscillations (Runge phenomenon) at domain boundaries."},
                    {"name": "Learning Rate (\\alpha)", "description": "Step magnitude for gradient descent solvers.", "effect": "Crucial if not using analytical normal equations."},
                    {"name": "Fit Intercept", "description": "Whether to calculate the bias term $w_0$.", "effect": "Allows the hyperplane to shift away from the origin."}
                ],
                "strengths": [
                    "Highly interpretable: coefficients directly represent feature marginal effects.",
                    "Fast training with closed-form mathematical solution.",
                    "Serves as the golden baseline for all regression benchmarks.",
                    "Provides analytical confidence intervals (p-values, standard errors)."
                ],
                "limitations": [
                    "Assumes linear relationship between transformed inputs and target.",
                    "Extreme sensitivity to leveraged outliers.",
                    "Inverting $\\mathbf{X}^T \\mathbf{X}$ scales with cubic complexity $\\mathcal{O}(D^3)$, failing when $D > 10,000$ without iterative solvers."
                ],
                "evaluation": "Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and Coefficient of Determination ($R^2$):<br>$$R^2 = 1 - \\frac{\\sum (y_i - \\hat{y}_i)^2}{\\sum (y_i - \\bar{y})^2}$$",
                "workedExample": "A dataset of house sizes (1000, 1500, 2000 sq ft) with prices ($200k, $300k, $400k). OLS fits $\\hat{y} = 0.2 x + 0$. For a 1800 sq ft home, it predicts $\\hat{y} = 0.2(1800) = \\$360,000$. The $R^2 = 1.0$ because the synthetic data was perfectly collinear.",
                "whenToUse": "Use whenever you need rapid, transparent, baseline continuous predictions or when stakeholders require statistical explanations of variable contributions.",
                "commonMistakes": [
                    "Fitting degree 10+ polynomials to small datasets without L2 regularization, causing wild boundary explosions.",
                    "Failing to standardize features before running gradient-descent-based regression.",
                    "Interpreting correlation coefficients as causal effects."
                ],
                "furtherLearning": [
                    {"title": "An Introduction to Statistical Learning - Ch. 3 Linear Regression", "url": "https://www.statlearning.com/"},
                    {"title": "Scikit-Learn Linear Regression Documentation", "url": "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html"}
                ]
            },
            "quiz": [
                {
                    "question": "What happens to the Normal Equation $\\mathbf{w}^* = (\\mathbf{X}^T \\mathbf{X})^{-1} \\mathbf{X}^T \\mathbf{y}$ if two input features are perfectly collinear?",
                    "options": [
                        "The model trains twice as fast.",
                        "The matrix $\\mathbf{X}^T \\mathbf{X}$ becomes singular (non-invertible), making a unique closed-form solution impossible.",
                        "The $R^2$ score automatically drops to zero.",
                        "Gradient descent will immediately terminate."
                    ],
                    "correct": 1,
                    "explanation": "Perfect multicollinearity makes columns linearly dependent, producing a determinant of zero and a singular matrix that cannot be inverted."
                },
                {
                    "question": "What metric measures the proportion of variance in the target explained by the regression model?",
                    "options": [
                        "Mean Squared Error (MSE)",
                        "Coefficient of Determination ($R^2$)",
                        "Root Mean Squared Error (RMSE)",
                        "Confusion Matrix"
                    ],
                    "correct": 1,
                    "explanation": "$R^2$ ranges from $-\\infty$ to $1.0$, indicating the percentage of variance in $y$ captured by the explanatory features relative to a naive mean baseline."
                },
                {
                    "question": "Why is high-degree polynomial regression prone to severe overfitting?",
                    "options": [
                        "Because it forces all coefficients to zero.",
                        "Because it increases model capacity and curvature, allowing the curve to weave through noisy training samples at the expense of test generalizability.",
                        "Because polynomial functions cannot be differentiated.",
                        "Because computers cannot calculate exponents greater than 3."
                    ],
                    "correct": 1,
                    "explanation": "High-degree polynomials have extreme degrees of freedom, allowing them to oscillate aggressively to touch every training point, resulting in poor generalization on unseen data."
                }
            ]
        },
        {
            "id": "S02",
            "title": "Logistic Regression",
            "module": "supervised",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "F05", "S01"],
            "estimatedMinutes": 20,
            "tags": ["classification", "logistic", "sigmoid", "cross-entropy", "odds-ratio"],
            "shortDesc": "Transform linear outputs through the Sigmoid activation to estimate well-calibrated class probabilities and linear decision boundaries.",
            "sections": {
                "whatItIs": "Logistic Regression is a foundational classification algorithm that models the probability of a categorical outcome (typically binary) by applying the non-linear Sigmoid (logistic) function to a linear combination of features.",
                "problemItSolves": "Applying standard linear regression to binary outcomes yields predictions that extrapolate below 0 and above 1, violating probability axioms. Logistic regression constrains outputs strictly to $[0, 1]$ and models the log-odds (logit) linearly.",
                "intuition": "Imagine rolling a heavy marble across a surface tilted by an incline ($w^T x + b$). The height of the incline can be infinitely high or low. The Sigmoid curve acts as an S-shaped smooth slide that compresses all infinite heights into a valid percentage probability between 0% and 100%.",
                "howItWorks": "1. <strong>Linear Logit:</strong> $z = \\mathbf{w}^T \\mathbf{x} + b$.<br>2. <strong>Sigmoid Squash:</strong> $\\sigma(z) = \\frac{1}{1 + e^{-z}} = P(y=1|x)$.<br>3. <strong>Decision Boundary:</strong> Predict class 1 if $\\sigma(z) \\ge 0.5$ (equivalent to $z \\ge 0$).<br>4. <strong>Optimization:</strong> Maximize the log-likelihood (minimize Binary Cross-Entropy loss) using iterative gradient descent or L-BFGS.",
                "mathematics": "Sigmoid Activation Function:<br>$$\\sigma(z) = \\frac{1}{1 + e^{-z}}, \\quad \\frac{d\\sigma}{dz} = \\sigma(z)(1 - \\sigma(z))$$<br>Log-Odds (Logit):<br>$$\\log\\left(\\frac{p}{1 - p}\\right) = \\mathbf{w}^T \\mathbf{x} + b$$<br>Binary Cross-Entropy Cost Function:<br>$$J(\\mathbf{w}) = -\\frac{1}{N} \\sum_{i=1}^N \\left[ y^{(i)} \\log(\\hat{p}^{(i)}) + (1 - y^{(i)}) \\log(1 - \\hat{p}^{(i)}) \\right]$$",
                "dataRequirements": "Numerical or encoded categorical features. Features should be scaled to avoid slow optimizer convergence. Multicollinearity should be inspected as it inflates parameter standard errors.",
                "hyperparameters": [
                    {"name": "Regularization (C / \\lambda)", "description": "Inverse regularization strength ($C = 1/\\lambda$).", "effect": "Smaller $C$ imposes heavier penalty on large weights, fighting overfitting."},
                    {"name": "Penalty Type", "description": "L1 (Lasso) vs L2 (Ridge) vs ElasticNet.", "effect": "L1 drives non-informative feature weights to absolute zero (automatic feature selection)."},
                    {"name": "Class Weight", "description": "Weights assigned to classes during loss calculation.", "effect": "Crucial for imbalanced datasets (e.g. fraud detection)."}
                ],
                "strengths": [
                    "Outputs well-calibrated posterior probabilities, not just rigid labels.",
                    "Highly interpretable: exponentiated weights $\\exp(w_j)$ represent Odds Ratios.",
                    "Computationally lightweight and fast to serve in high-throughput production.",
                    "Convex loss surface: guaranteed to converge to the global minimum."
                ],
                "limitations": [
                    "Linear decision boundary cannot solve linearly non-separable problems (e.g. XOR) without manual feature engineering or kernel expansions.",
                    "Vulnerable to multicollinearity and complete separation (where weights explode to infinity)."
                ],
                "evaluation": "Evaluated using Log-Loss, ROC-AUC score, Brier score (for probability calibration), Precision, Recall, and Confusion Matrices.",
                "workedExample": "Predicting loan default: Feature $x_1$ = credit score, $w_1 = -0.01$, bias $b = 6$. For a borrower with score 650, $z = -0.01(650) + 6 = -0.5$. Probability of default $p = 1 / (1 + e^{0.5}) = 0.377$ (37.7%). Since $0.377 < 0.5$, the loan is approved.",
                "whenToUse": "The default starting point for binary classification, credit risk modeling, medical survival risk scoring, and ad click-through rate (CTR) prediction.",
                "commonMistakes": [
                    "Interpreting raw probability outputs as accurate risks when trained on severe class imbalance without calibration.",
                    "Failing to scale features when applying L1/L2 penalties (unscaled features get penalized disproportionately).",
                    "Assuming it can naturally learn circular or complex non-linear boundaries."
                ],
                "furtherLearning": [
                    {"title": "Hosmer & Lemeshow: Applied Logistic Regression", "url": "https://www.wiley.com/en-us/Applied+Logistic+Regression%2C+3rd+Edition-p-9780470582473"},
                    {"title": "Scikit-Learn Logistic Regression", "url": "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the shape of the decision boundary formed by standard Logistic Regression in feature space?",
                    "options": [
                        "A hyper-ellipsoid",
                        "A linear hyperplane where $\\mathbf{w}^T \\mathbf{x} + b = 0$",
                        "A fractal curve",
                        "A discontinuous step function"
                    ],
                    "correct": 1,
                    "explanation": "Because the prediction threshold $\\sigma(z) = 0.5$ occurs precisely when $z = \\mathbf{w}^T \\mathbf{x} + b = 0$, the decision boundary is an affine linear hyperplane."
                },
                {
                    "question": "What happens if a dataset is 'completely separable' (a plane can divide the two classes with 100% accuracy) and no regularization is used?",
                    "options": [
                        "The loss function fails to converge, and weights explode toward positive or negative infinity to drive probabilities to 0 and 1.",
                        "The algorithm terminates in exactly one iteration.",
                        "The probabilities will remain fixed at 0.5.",
                        "The Sigmoid function divides by zero."
                    ],
                    "correct": 0,
                    "explanation": "With complete separation and no regularization, the optimizer drives weights to infinity to push $\\sigma(z)$ to asymptotically reach 1 and 0, driving cross-entropy loss to zero."
                },
                {
                    "question": "If a feature's logistic regression weight is $w_1 = 0.693$, what does this imply about the Odds Ratio $\\exp(w_1)$?",
                    "options": [
                        "A 1-unit increase in $x_1$ doubles the odds of the positive outcome ($\\exp(0.693) \\approx 2.0$).",
                        "The feature is completely uninformative.",
                        "The probability of the event increases by 69.3%.",
                        "The model is overfitting."
                    ],
                    "correct": 0,
                    "explanation": "In logistic regression, $\\exp(w_j)$ is the Odds Ratio. Since $e^{0.693} \\approx 2.0$, each unit increase in that feature doubles the odds of the event occurring."
                }
            ]
        },
        {
            "id": "S03",
            "title": "k-Nearest Neighbors (KNN)",
            "module": "supervised",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "F04"],
            "estimatedMinutes": 20,
            "tags": ["instance-based", "non-parametric", "lazy-learning", "distance-metrics"],
            "shortDesc": "A non-parametric, instance-based algorithm that classifies queries by polling the majority label among their k closest metric neighbors.",
            "sections": {
                "whatItIs": "k-Nearest Neighbors (KNN) is an instance-based (or 'lazy') supervised learning algorithm. It makes zero prior assumptions about the underlying data distribution and postpones all computation until query time, predicting outcomes based on the majority class or average value of the $k$ nearest training points.",
                "problemItSolves": "Enables immediate classification and regression without an explicit mathematical training phase, naturally adapting to complex multi-modal decision boundaries that defeat linear models.",
                "intuition": "Think of the old adage: 'You are the average of the five people you spend the most time with.' When deciding whether an unknown animal is a duck, look at its 5 closest neighbors in physical appearance: if 4 are ducks and 1 is a swan, conclude it is a duck.",
                "howItWorks": "1. <strong>Store Training Data:</strong> Store all labeled points $\\{(\\mathbf{x}_i, y_i)\\}$.<br>2. <strong>Calculate Distance:</strong> For a query point $\\mathbf{x}_q$, compute distance to every training sample.<br>3. <strong>Find Top-k:</strong> Identify the $k$ samples with smallest distance.<br>4. <strong>Aggregate:</strong> Classification takes the majority vote (or distance-weighted vote); regression computes the mean or median.",
                "mathematics": "Minkowski Distance metric ($p=2$ is Euclidean, $p=1$ is Manhattan):<br>$$D(\\mathbf{x}, \\mathbf{z}) = \\left( \\sum_{j=1}^D |x_j - z_j|^p \\right)^{1/p}$$<br>Majority Voting Prediction:<br>$$\\hat{y} = \\arg\\max_{c} \\sum_{i \\in \\mathcal{N}_k(\\mathbf{x})} \\mathbb{I}(y_i = c)$$<br>Distance-Weighted Voting:<br>$$w_i = \\frac{1}{D(\\mathbf{x}, \\mathbf{x}_i) + \\epsilon}, \\quad \\hat{y} = \\arg\\max_c \\sum_{i \\in \\mathcal{N}_k} w_i \\mathbb{I}(y_i = c)$$",
                "dataRequirements": "Features MUST be normalized or standardized (e.g. z-score or min-max). If one feature ranges from $0-100,000$ (salary) and another from $18-70$ (age), the salary feature will completely dominate Euclidean distance calculations.",
                "hyperparameters": [
                    {"name": "Number of Neighbors (k)", "description": "The neighborhood size polled for votes.", "effect": "Small $k$ (e.g. $k=1$) yields high variance and complex jagged boundaries; large $k$ increases bias and smooths boundaries."},
                    {"name": "Distance Metric", "description": "Metric used to measure closeness (Euclidean, Manhattan, Cosine).", "effect": "Manhattan works better in higher dimensions; Cosine ignores magnitude."},
                    {"name": "Weights", "description": "Uniform vs Distance-weighted voting.", "effect": "Distance weighting ensures closer neighbors have greater influence."}
                ],
                "strengths": [
                    "Extremely intuitive, transparent, and easy to explain to non-technical stakeholders.",
                    "Zero training time $\\mathcal{O}(1)$ (just storing data points).",
                    "Naturally handles multi-class classification and non-linear boundaries.",
                    "Can be updated instantly online as new training samples arrive."
                ],
                "limitations": [
                    "Inference latency scales with dataset size $\\mathcal{O}(N \\cdot D)$ without spatial trees.",
                    "Suffers severely from the Curse of Dimensionality: in high dimensions, all pairwise distances converge to similar values.",
                    "High memory footprint since the entire dataset must be kept in RAM."
                ],
                "evaluation": "Evaluated using standard classification or regression metrics (Accuracy, F1, RMSE) evaluated via K-Fold Cross Validation.",
                "workedExample": "A 2D plane with 5 points: (1,1, Red), (1,2, Red), (5,5, Blue), (5,6, Blue), (2,1, Red). Query point (1.5, 1.5) with $k=3$. The 3 nearest points are (1,1), (1,2), and (2,1)—all Red. Query is classified as Red with 100% confidence.",
                "whenToUse": "Best for low-dimensional datasets ($D < 30$), recommendation systems based on collaborative item similarity, and small tabular benchmarks.",
                "commonMistakes": [
                    "Forgetting to scale features, rendering all small-range features useless.",
                    "Using an even value for $k$ in binary classification, creating ambiguous tie votes.",
                    "Using brute-force KNN on millions of high-dimensional samples without approximate indexing (e.g. FAISS or HNSW)."
                ],
                "furtherLearning": [
                    {"title": "Nearest Neighbor Pattern Classification - Cover & Hart (1967)", "url": "https://ieeexplore.ieee.org/document/1053964"},
                    {"title": "FAISS: Fast Approximate Nearest Neighbors - Meta", "url": "https://github.com/facebookresearch/faiss"}
                ]
            },
            "quiz": [
                {
                    "question": "What happens when $k=1$ in a k-Nearest Neighbors classifier on the training set?",
                    "options": [
                        "The model makes 50% errors.",
                        "Training error is exactly 0% (excluding duplicate identical points with differing labels), but variance is extremely high.",
                        "The model underfits.",
                        "All predictions equal the global dataset mean."
                    ],
                    "correct": 1,
                    "explanation": "At $k=1$, each training point's nearest neighbor is itself, producing 0% training error while memorizing every noisy outlier (overfitting)."
                },
                {
                    "question": "Why is feature scaling essential before running KNN?",
                    "options": [
                        "Because otherwise the optimizer gradient will explode.",
                        "Because distance metrics are mathematically dominated by features with large absolute numerical scales.",
                        "Because KNN cannot process floating point numbers.",
                        "It is not essential; KNN is scale-invariant."
                    ],
                    "correct": 1,
                    "explanation": "If one feature has values around 100,000 and another around 1, Euclidean distance differences will be entirely determined by the first feature."
                },
                {
                    "question": "What spatial indexing data structure can reduce KNN query search time from $\\mathcal{O}(N)$ to $\\mathcal{O}(\\log N)$ in low dimensions?",
                    "options": [
                        "Hash Table",
                        "KD-Tree or Ball-Tree",
                        "Red-Black Tree",
                        "Adjacency Matrix"
                    ],
                    "correct": 1,
                    "explanation": "KD-Trees and Ball-Trees recursively partition Euclidean space into geometric regions, allowing rapid branch pruning during neighbor search."
                }
            ]
        },
        {
            "id": "S04",
            "title": "Naive Bayes",
            "module": "supervised",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "F04", "F05"],
            "estimatedMinutes": 20,
            "tags": ["probabilistic", "bayes-theorem", "text-classification", "generative"],
            "shortDesc": "Fast probabilistic classifier applying Bayes' Theorem under the naive assumption of conditional feature independence.",
            "sections": {
                "whatItIs": "Naive Bayes is a family of fast, probabilistic classifiers based on Bayes' Theorem. It makes the 'naive' assumption that all features are mutually independent conditioned on the class label: knowing the value of one feature provides zero information about the value of another feature given the class.",
                "problemItSolves": "Estimating full joint probability distributions $P(x_1, \\dots, x_D | y)$ requires exponentially many training examples (intractable for high dimensions). The naive independence assumption reduces the computation from an exponential joint distribution to a product of simple 1D marginal distributions.",
                "intuition": "Imagine diagnosing the flu. The symptoms are high fever, cough, and body aches. Naive Bayes calculates: what is the overall probability someone has flu? Multiplied by how common fever is with flu, how common cough is with flu, and how common aches are with flu. It ignores whether coughing usually happens at the exact same minute as fever—treating each symptom as an independent piece of evidence.",
                "howItWorks": "1. <strong>Prior Estimation:</strong> Calculate class prior probabilities $P(y = c) = N_c / N$.<br>2. <strong>Likelihood Estimation:</strong> Calculate conditional likelihood for each feature $P(x_j | y = c)$ (using Categorical counts, Gaussian distribution, or Multinomial frequency).<br>3. <strong>Laplace Smoothing:</strong> Add pseudo-counts to prevent multiplying by zero for unseen values.<br>4. <strong>Posterior Inference:</strong> Multiply prior by the product of likelihoods and select the class with maximum posterior.",
                "mathematics": "Bayes' Theorem:<br>$$P(y=c | \\mathbf{x}) = \\frac{P(y=c) P(\\mathbf{x} | y=c)}{P(\\mathbf{x})} \\propto P(y=c) \\prod_{j=1}^D P(x_j | y=c)$$<br>Gaussian Likelihood (for continuous features):<br>$$P(x_j | y=c) = \\frac{1}{\\sqrt{2\\pi \\sigma_{jc}^2}} \\exp\\left( -\\frac{(x_j - \\mu_{jc})^2}{2\\sigma_{jc}^2} \\right)$$<br>Laplace Add-1 Smoothing (for word counts):<br>$$\\hat{\\theta}_{jc} = \\frac{N_{jc} + 1}{N_c + |V|}$$",
                "dataRequirements": "Works with discrete word counts (MultinomialNB), binary occurrence flags (BernoulliNB), or continuous features (GaussianNB). Highly effective in high-dimensional sparse text representations.",
                "hyperparameters": [
                    {"name": "Laplace Smoothing (\\alpha)", "description": "Smoothing parameter added to frequency counts (typically $\\alpha = 1.0$).", "effect": "Prevents probabilities from collapsing to zero when evaluating words not seen during training."},
                    {"name": "Prior Probabilities", "description": "Whether to learn class priors from data frequencies or set uniform priors.", "effect": "Controls baseline tendency toward dominant classes."}
                ],
                "strengths": [
                    "Incredibly fast: training takes a single pass over the dataset $\\mathcal{O}(N \\cdot D)$.",
                    "Requires very little training data to establish reliable frequency statistics.",
                    "Immune to irrelevant features (features unassociated with classes get uniform probabilities).",
                    "Excels at sparse text processing (spam filtering, sentiment analysis, document categorization)."
                ],
                "limitations": [
                    "The independence assumption is almost never strictly true in real data (e.g. words 'New' and 'York' are strongly correlated).",
                    "Probability calibration is notoriously poor: tends to output overconfident probabilities near 0.0 or 1.0."
                ],
                "evaluation": "Evaluated using Precision, Recall, Macro/Micro F1-Score, and ROC-AUC.",
                "workedExample": "Classifying email as Spam or Ham. Dataset has 50 Spam, 50 Ham. Word 'jackpot' appears in 20 Spam emails and 1 Ham email. A new email contains 'jackpot'. $P(\\text{Spam}|\\text{jackpot}) \\propto 0.5 \\times (21/52) = 0.2019$; $P(\\text{Ham}|\\text{jackpot}) \\propto 0.5 \\times (2/52) = 0.0192$. Posterior probability is $>91\\%$ Spam.",
                "whenToUse": "Ideal for fast baseline text classification, spam detection, sentiment analysis, and systems requiring real-time sub-millisecond inference on low-power hardware.",
                "commonMistakes": [
                    "Failing to apply Laplace smoothing, causing a single unseen word in a test message to zero out the entire product.",
                    "Using Gaussian Naive Bayes on heavily skewed, non-normal feature distributions without power transforms."
                ],
                "furtherLearning": [
                    {"title": "Manning, Raghavan, Schütze: Text Classification and Naive Bayes", "url": "https://nlp.stanford.edu/IR-book/html/htmledition/naive-bayes-text-classification-1.html"},
                    {"title": "Scikit-Learn Naive Bayes Guide", "url": "https://scikit-learn.org/stable/modules/naive_bayes.html"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the 'naive' assumption that gives Naive Bayes its name?",
                    "options": [
                        "That data points were collected without human error.",
                        "That all features are mutually independent given the class label.",
                        "That the target class distribution is always 50/50.",
                        "That the model requires no mathematical training."
                    ],
                    "correct": 1,
                    "explanation": "It naively assumes that every feature is completely independent of every other feature conditioned on knowing the target class."
                },
                {
                    "question": "Why is Laplace (additive) smoothing necessary in Naive Bayes text classification?",
                    "options": [
                        "To prevent gradient descent from exploding.",
                        "To ensure that words absent from the training set do not yield zero probability, which would wipe out the entire multiplied product.",
                        "To convert negative word counts into positive numbers.",
                        "To reduce the matrix dimension."
                    ],
                    "correct": 1,
                    "explanation": "Because Naive Bayes multiplies feature likelihoods together, a single probability of 0 would force the total posterior probability to 0, regardless of all other evidence."
                },
                {
                    "question": "Which variant of Naive Bayes is designed specifically for word counts in document classification?",
                    "options": [
                        "Gaussian Naive Bayes",
                        "Multinomial Naive Bayes",
                        "Categorical Naive Bayes",
                        "Continuous Naive Bayes"
                    ],
                    "correct": 1,
                    "explanation": "Multinomial Naive Bayes models discrete integer feature counts (like term frequencies in documents)."
                }
            ]
        },
        {
            "id": "S05",
            "title": "Decision Trees",
            "module": "supervised",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "F05", "F06"],
            "estimatedMinutes": 20,
            "tags": ["tree-based", "cart", "entropy", "gini-impurity", "interpretability"],
            "shortDesc": "Hierarchical, recursive partitioning of feature space using orthogonal split criteria to maximize information gain.",
            "sections": {
                "whatItIs": "Decision Trees are non-parametric supervised models that recursively partition feature space into axis-aligned rectangular regions. Each internal node represents an orthogonal threshold test on a single feature, and each leaf node assigns a class label or continuous numerical value.",
                "problemItSolves": "Provides human-readable, auditable decision rules that require zero feature scaling, handle mixed categorical and continuous variables naturally, and automatically capture non-linear feature interactions.",
                "intuition": "Imagine playing the game 'Twenty Questions.' To guess an animal, your first question is: 'Does it live in water?' If yes, you branch to questions about fins and scales. If no, you ask about legs and fur. A decision tree learns the most informative sequence of questions to identify the outcome with the fewest possible guesses.",
                "howItWorks": "1. <strong>Split Search:</strong> At current node, evaluate every feature and every possible threshold value.<br>2. <strong>Impurity Evaluation:</strong> Compute the impurity reduction (Information Gain or Gini reduction) achieved by each split.<br>3. <strong>Best Split:</strong> Select the split yielding maximum impurity reduction.<br>4. <strong>Recursion:</strong> Partition samples into left and right children; repeat recursively until stopping criteria (max depth, min samples) are reached.",
                "mathematics": "Gini Impurity (CART):<br>$$I_G(p) = 1 - \\sum_{k=1}^K p_k^2$$<br>Entropy (ID3 / C4.5):<br>$$H(p) = -\\sum_{k=1}^K p_k \\log_2(p_k)$$<br>Information Gain from split $\\theta = (j, t_m)$:<br>$$IG(D, \\theta) = I(D) - \\frac{|D_{\\text{left}}|}{|D|} I(D_{\\text{left}}) - \\frac{|D_{\\text{right}}|}{|D|} I(D_{\\text{right}})$$",
                "dataRequirements": "No feature normalization, scaling, or centering required. Robust to monotonic transformations of features. Can handle missing values (depending on implementation).",
                "hyperparameters": [
                    {"name": "Max Depth", "description": "Maximum path length from root to leaf.", "effect": "Primary defense against overfitting. Shallow trees have high bias; deep trees overfit."},
                    {"name": "Min Samples Split", "description": "Minimum samples required at an internal node to attempt a split.", "effect": "Higher values prevent splitting on isolated samples."},
                    {"name": "Criterion", "description": "Gini impurity vs Shannon Entropy for classification; MSE vs MAE for regression.", "effect": "Gini is faster to compute; Entropy penalizes mixed nodes slightly more aggressively."}
                ],
                "strengths": [
                    "Completely white-box and interpretable; can be exported to flowcharts or SQL if-then statements.",
                    "Zero feature scaling or normalization required.",
                    "Naturally handles non-linear relationships and high-order feature interactions.",
                    "Provides built-in feature importance rankings."
                ],
                "limitations": [
                    "High variance: slight perturbations in training data can produce a completely different tree topology.",
                    "Axis-aligned splits struggle to approximate diagonal decision boundaries without stepped staircase approximations.",
                    "Greedy top-down optimization can miss optimal sub-trees."
                ],
                "evaluation": "Evaluated using standard classification (Accuracy, F1) or regression (MSE, $R^2$) metrics. Tree complexity evaluated by leaf count and depth.",
                "workedExample": "A dataset of loan applicants. Root split: 'Income > $50,000'. If No $\\to$ 90% default, classify 'Deny'. If Yes $\\to$ next split: 'Credit Score > 700'. If Yes $\\to$ classify 'Approve'; if No $\\to$ classify 'Require Co-signer'. Each decision path forms an auditable rule.",
                "whenToUse": "Use when model interpretability, regulatory compliance (e.g. loan approval explanations), or zero-preprocessing quick baselines are required.",
                "commonMistakes": [
                    "Allowing unpruned trees to grow infinitely until leaves contain 1 sample, causing extreme overfitting.",
                    "Expecting smooth decision surfaces (decision trees produce piecewise constant step functions)."
                ],
                "furtherLearning": [
                    {"title": "Breiman et al.: Classification and Regression Trees (CART Book)", "url": "https://www.routledge.com/Classification-and-Regression-Trees/Breiman-Friedman-Stone-Olshen/p/book/9780412048418"},
                    {"title": "Scikit-Learn Decision Trees Documentation", "url": "https://scikit-learn.org/stable/modules/tree.html"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the Gini Impurity of a completely pure leaf node containing 50 samples of Class A and 0 samples of Class B?",
                    "options": [
                        "1.0",
                        "0.5",
                        "0.0",
                        "-1.0"
                    ],
                    "correct": 2,
                    "explanation": "$I_G = 1 - (1.0^2 + 0.0^2) = 0.0$. A completely pure node has zero impurity."
                },
                {
                    "question": "Why do standard decision trees produce 'staircase' decision boundaries on diagonal distributions?",
                    "options": [
                        "Because computer monitors have pixels.",
                        "Because split conditions test only one feature at a time ($x_j \\le t$), forming orthogonal, axis-aligned partitions.",
                        "Because of floating-point rounding errors.",
                        "Because trees cannot process continuous numbers."
                    ],
                    "correct": 1,
                    "explanation": "Standard CART decision trees evaluate one feature at a time, creating boundaries that are strictly perpendicular to the feature axes."
                },
                {
                    "question": "Which hyperparameter directly limits the maximum vertical growth of a decision tree to combat overfitting?",
                    "options": [
                        "learning_rate",
                        "max_depth",
                        "n_estimators",
                        "subsample"
                    ],
                    "correct": 1,
                    "explanation": "`max_depth` specifies the maximum distance from root to the deepest leaf, preventing the tree from growing overly specific leaf nodes."
                }
            ]
        },
        {
            "id": "S06",
            "title": "Random Forests",
            "module": "supervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F06", "S05"],
            "estimatedMinutes": 25,
            "tags": ["ensemble", "bagging", "random-forest", "variance-reduction", "feature-importance"],
            "shortDesc": "Bagged ensemble of de-correlated decision trees with random feature subsampling that drastically reduces variance.",
            "sections": {
                "whatItIs": "Random Forest is an ensemble learning method that constructs a multitude of deep, unpruned decision trees during training. It combines two core randomization techniques: Bootstrap Aggregation (bagging) of samples and random feature subsampling at every split, outputting the majority vote (classification) or mean prediction (regression).",
                "problemItSolves": "Single decision trees suffer from extreme variance and instability. Random Forests reduce variance exponentially through ensemble averaging without increasing bias, creating a highly resilient 'out-of-the-box' model.",
                "intuition": "Imagine a TV game show. If you ask a single contestant an obscure question, they might make an idiosyncratic guess. But if you poll an audience of 500 diverse people where each person looks at a random subset of clues, the aggregate majority vote is statistically much more likely to be correct.",
                "howItWorks": "1. <strong>Bootstrap Sampling:</strong> For each of $B$ trees, draw a sample of size $N$ with replacement from the training set.<br>2. <strong>Random Feature Selection:</strong> At each node split, choose from a random subset of $m \\approx \\sqrt{D}$ features (rather than all $D$).<br>3. <strong>Grow Deep Trees:</strong> Grow each tree fully without pruning.<br>4. <strong>Aggregate:</strong> At inference, pass the sample through all $B$ trees and average or vote.",
                "mathematics": "Variance of the average of $B$ identical estimators with variance $\\sigma^2$ and pairwise correlation $\\rho$:<br>$$\\text{Var}(\\bar{T}) = \\rho \\sigma^2 + \\frac{1 - \\rho}{B} \\sigma^2$$<br>As $B \\to \\infty$, the second term approaches zero, leaving $\\rho \\sigma^2$. Feature subsampling reduces the inter-tree correlation $\\rho$, driving total variance down.",
                "dataRequirements": "Handles tabular data with mixed numeric and categorical types. Requires minimal preprocessing; no scaling needed. Resistant to outliers and noise.",
                "hyperparameters": [
                    {"name": "n_estimators (B)", "description": "Number of trees in the forest (e.g. 100 to 500).", "effect": "More trees do not cause overfitting; performance plateaus once variance stabilizes."},
                    {"name": "max_features (m)", "description": "Number of features randomly sampled at each split (default $\\sqrt{D}$ for classification, $D/3$ for regression).", "effect": "Smaller $m$ de-correlates trees further, reducing variance at a slight cost to bias."},
                    {"name": "max_depth / min_samples_leaf", "description": "Tree size constraints.", "effect": "Limits individual tree growth to save memory."}
                ],
                "strengths": [
                    "One of the most reliable, robust 'out-of-the-box' algorithms for tabular data.",
                    "Nearly impossible to overfit simply by adding more trees.",
                    "Provides Out-of-Bag (OOB) error estimates, eliminating the strict need for a separate validation split.",
                    "Naturally handles missing values and produces reliable MDI / Permutation feature importances."
                ],
                "limitations": [
                    "Cannot extrapolate beyond the range of training targets in regression.",
                    "Much slower inference speed and larger memory footprint than a single tree or linear model.",
                    "Lacks the clean, human-readable interpretability of a single decision tree."
                ],
                "evaluation": "Evaluated via Out-of-Bag (OOB) score, Test Accuracy, ROC-AUC, and RMSE.",
                "workedExample": "A forest of 100 trees predicting whether a customer will churn. 78 trees vote 'Churn', 22 trees vote 'Stay'. Ensemble outputs 'Churn' with a calibrated probability of 78%.",
                "whenToUse": "The premier baseline for almost any tabular classification or regression problem where deep learning is unwarranted.",
                "commonMistakes": [
                    "Believing that increasing `n_estimators` causes overfitting (it actually decreases variance and asymptotically stabilizes).",
                    "Using it for time-series forecasting where trend extrapolation beyond historical maximums is necessary."
                ],
                "furtherLearning": [
                    {"title": "Leo Breiman: Random Forests (2001 Paper)", "url": "https://link.springer.com/article/10.1023/A:1010933404324"},
                    {"title": "Scikit-Learn Random Forest Guide", "url": "https://scikit-learn.org/stable/modules/ensemble.html#forest"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary effect of randomly sampling a subset of features at each split in a Random Forest?",
                    "options": [
                        "It speeds up compilation.",
                        "It de-correlates the individual trees, lowering the pairwise correlation $\\rho$ and decreasing ensemble variance.",
                        "It forces trees to be linear.",
                        "It prevents trees from using deep leaves."
                    ],
                    "correct": 1,
                    "explanation": "If one feature is overwhelmingly dominant, all standard bagged trees would split on it first, making them highly correlated. Random feature subsets force trees to explore alternate features, de-correlating the ensemble."
                },
                {
                    "question": "What is the 'Out-of-Bag' (OOB) error in a Random Forest?",
                    "options": [
                        "An error caused by insufficient GPU memory.",
                        "The evaluation of each tree on the ~37% of training samples that were left out of its bootstrap sample.",
                        "The percentage of missing values in the test set.",
                        "The classification error on the final test set."
                    ],
                    "correct": 1,
                    "explanation": "In bootstrap sampling with replacement, approximately $1 - 1/e \\approx 63.2\\%$ of unique samples are selected per tree. The remaining ~36.8% 'out-of-bag' samples act as a built-in validation set."
                },
                {
                    "question": "Can a Random Forest regression model predict a target value higher than the maximum value in its training data?",
                    "options": [
                        "Yes, by fitting an upward trend line.",
                        "No, because tree leaves output the mean of observed training targets; it cannot extrapolate beyond the extreme observed values.",
                        "Yes, if `n_estimators` is set to 10,000.",
                        "Only if trained on normalized features."
                    ],
                    "correct": 1,
                    "explanation": "Decision trees partition space into constant leaf regions. The output of any leaf is bounded by the minimum and maximum target values present in the training set."
                }
            ]
        },
        {
            "id": "S07",
            "title": "Extra Trees (Extremely Randomized Trees)",
            "module": "supervised",
            "level": "intermediate",
            "prerequisites": ["S05", "S06"],
            "estimatedMinutes": 15,
            "tags": ["ensemble", "randomization", "extra-trees", "fast-training"],
            "shortDesc": "An ensemble that draws cut-points completely at random for each candidate feature, accelerating training and further dampening variance.",
            "sections": {
                "whatItIs": "Extra Trees (Extremely Randomized Trees) is an ensemble method that takes randomization one step further than Random Forests. While Random Forests find the optimal mathematical split threshold among a random subset of features, Extra Trees picks random split thresholds for each candidate feature and selects the best among those randomly generated candidates.",
                "problemItSolves": "Evaluating the exact optimal threshold across thousands of continuous candidate values is computationally expensive. Extra Trees speeds up tree building substantially while introducing additional stochastic noise that smooths decision boundaries further.",
                "intuition": "In a standard Random Forest, when choosing how to split 'Age', the algorithm sorts all ages and tests every value to find the exact mathematical split point. In Extra Trees, it grabs a random age threshold (e.g. 34.2) without sorting, checks if it's decent, and moves on immediately.",
                "howItWorks": "1. <strong>Whole Dataset or Subsampling:</strong> Usually fits trees on the entire dataset (no bootstrap) or bootstrapped.<br>2. <strong>Random Cut-Points:</strong> For each candidate feature in the random subset, draw a threshold uniformly at random between the feature's minimum and maximum values.<br>3. <strong>Evaluate & Pick:</strong> Select the feature and random threshold pair that gives the best impurity score.<br>4. <strong>Aggregate:</strong> Average or vote across trees at inference.",
                "mathematics": "Threshold selection for feature $j$ with range $[a_j, b_j]$:<br>$$t_j \\sim \\text{Uniform}(a_j, b_j)$$<br>Instead of optimizing:<br>$$t_j^* = \\arg\\max_t IG(D, j, t)$$<br>it evaluates $IG(D, j, t_j)$ for random draws and picks the highest.",
                "dataRequirements": "Same as Random Forest: handles numerical and categorical tabular data without preprocessing or scaling.",
                "hyperparameters": [
                    {"name": "n_estimators", "description": "Number of trees.", "effect": "More trees yield smoother decision surfaces."},
                    {"name": "max_features", "description": "Candidate feature count.", "effect": "Standard is $\\sqrt{D}$."},
                    {"name": "bootstrap", "description": "Whether to use bootstrap samples or whole dataset.", "effect": "Default is False (using whole dataset), relying entirely on random cut-points for diversity."}
                ],
                "strengths": [
                    "Significantly faster training time than Random Forests because features do not need sorting.",
                    "Often yields smoother, less jagged decision boundaries.",
                    "Slightly lower variance than standard Random Forests on noisy datasets."
                ],
                "limitations": [
                    "Slightly higher bias on complex structured tabular datasets with clean boundaries.",
                    "Still cannot extrapolate continuous trends beyond training range."
                ],
                "evaluation": "Evaluated with standard classification (Accuracy, ROC-AUC) and regression (RMSE, $R^2$) benchmarks.",
                "workedExample": "Evaluating 1,000,000 sensor measurements: sorting 1M numbers at each node in standard Random Forest takes $\\mathcal{O}(N \\log N)$. Extra Trees draws a uniform random number between $\\min$ and $\\max$ in $\\mathcal{O}(1)$, completing training in a fraction of the time.",
                "whenToUse": "Use when Random Forest training is too slow on large datasets, or when dealing with highly noisy datasets where extreme randomization prevents fitting to spurious cut-points.",
                "commonMistakes": [
                    "Assuming Extra Trees will always outperform Random Forest (on low-noise data, optimal splits usually beat random thresholds).",
                    "Forgetting that memory consumption during inference is identical to Random Forest."
                ],
                "furtherLearning": [
                    {"title": "Geurts et al.: Extremely Randomized Trees (2006)", "url": "https://link.springer.com/article/10.1007/s10994-006-6226-1"},
                    {"title": "Scikit-Learn ExtraTreesClassifier", "url": "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the key mathematical difference between Random Forests and Extra Trees?",
                    "options": [
                        "Random Forests use neural networks; Extra Trees use linear models.",
                        "Extra Trees chooses split thresholds completely at random between feature min/max, rather than computing the optimal threshold.",
                        "Extra Trees only trains a single tree.",
                        "Extra Trees cannot be used for classification."
                    ],
                    "correct": 1,
                    "explanation": "Extra Trees generates split thresholds uniformly at random for each candidate feature rather than searching for the optimal discriminator."
                },
                {
                    "question": "Why is training Extra Trees typically faster than standard Random Forests?",
                    "options": [
                        "It skips computing leaf outputs.",
                        "It avoids the expensive sorting of sample feature values at every node.",
                        "It uses GPU matrix multiplications.",
                        "It only evaluates one tree."
                    ],
                    "correct": 1,
                    "explanation": "Finding the optimal split requires sorting samples by feature values $\\mathcal{O}(N \\log N)$; picking a random cut-point requires only $\\min$ and $\\max$, saving extensive compute."
                },
                {
                    "question": "What trade-off is typically observed when switching from Random Forests to Extra Trees?",
                    "options": [
                        "Zero variance and infinite bias.",
                        "Faster training and slightly lower variance, but potentially slightly higher bias.",
                        "100% loss of accuracy.",
                        "Extreme overfitting."
                    ],
                    "correct": 1,
                    "explanation": "The extreme randomness lowers variance further and speeds training, but can introduce slightly more bias because splits are not mathematically optimal."
                }
            ]
        },
        {
            "id": "S08",
            "title": "Bagging vs Boosting Principles",
            "module": "supervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F06", "S05", "S06"],
            "estimatedMinutes": 20,
            "tags": ["ensemble", "bagging", "boosting", "theory", "bias-variance"],
            "shortDesc": "Compare parallel variance-reducing ensembles (Bagging) against sequential bias-reducing ensembles (Boosting).",
            "sections": {
                "whatItIs": "Bagging (Bootstrap Aggregation) and Boosting are the two foundational paradigms of ensemble learning. <strong>Bagging</strong> trains multiple independent base models in parallel on random bootstrap data subsets and averages them to reduce <em>variance</em>. <strong>Boosting</strong> trains base models sequentially, with each subsequent model focusing on correcting the mistakes of its predecessors to reduce <em>bias</em>.",
                "problemItSolves": "Provides the conceptual foundation for all state-of-the-art tabular algorithms, clarifying whether an ensemble is targeting underfitting (boosting) or overfitting (bagging).",
                "intuition": "Bagging is a panel of 10 independent doctors examining a patient simultaneously; you take the majority diagnosis, which cancels out individual eccentricities. Boosting is a doctor making a preliminary diagnosis, then passing the difficult, unresolved symptoms to a second specialist, who passes remaining errors to a third specialist, iteratively refining accuracy.",
                "howItWorks": "1. <strong>Bagging:</strong> Resample dataset with replacement $\\to$ Train models in parallel $\\to$ Average outputs: $\\hat{y} = \\frac{1}{M}\\sum f_m(x)$.<br>2. <strong>Boosting:</strong> Initialize predictions $\\to$ Compute residuals/errors $\\to$ Fit new weak learner to residuals $\\to$ Add weighted learner: $F_{m}(x) = F_{m-1}(x) + \\eta h_m(x)$.<br>3. <strong>Independence vs Dependence:</strong> Bagging models are mutually independent; Boosting models are conditionally dependent.",
                "mathematics": "Bagging Variance Reduction:<br>$$\\text{Var}\\left(\\frac{1}{M}\\sum_{m=1}^M X_m\\right) = \\frac{\\sigma^2}{M} \\quad (\\text{if independent})$$<br>Additive Boosting Formulation:<br>$$F_M(x) = F_0(x) + \\sum_{m=1}^M \\alpha_m h_m(x)$$<br>where $h_m(x)$ is a weak learner (typically a shallow decision tree stump).",
                "dataRequirements": "Bagging works best with high-variance, low-bias base learners (e.g. deep unpruned trees). Boosting works best with high-bias, low-variance base learners (e.g. shallow tree stumps of depth 2-6).",
                "hyperparameters": [
                    {"name": "Ensemble Mode", "description": "Parallel (Bagging) vs Sequential (Boosting).", "effect": "Bagging parallelizes across CPU cores; Boosting is inherently sequential."},
                    {"name": "Base Learner Capacity", "description": "Depth of individual trees.", "effect": "Deep for Bagging; Shallow for Boosting."}
                ],
                "strengths": [
                    "Bagging: Highly parallelizable, robust to noise, almost impossible to overfit by increasing ensemble size.",
                    "Boosting: Typically achieves higher top-end predictive accuracy on complex tabular benchmarks."
                ],
                "limitations": [
                    "Bagging cannot fix high bias (if base models underfit, the ensemble underfits).",
                    "Boosting can overfit if trained for too many iterations on noisy datasets."
                ],
                "evaluation": "Compare bias, variance, training time, and generalization error curves across iterations.",
                "workedExample": "A dataset where a linear model achieves 70% accuracy. Bagging 100 linear models still yields ~70% accuracy (averaging lines doesn't create curves). Boosting shallow trees creates piecewise step functions that reach 94% accuracy.",
                "whenToUse": "Choose Bagging when you have deep models and want quick, parallel variance reduction. Choose Boosting when you want maximum possible accuracy on tabular datasets.",
                "commonMistakes": [
                    "Using deep, complex trees as the base learner in Boosting, causing immediate overfitting.",
                    "Thinking Bagging can reduce bias."
                ],
                "furtherLearning": [
                    {"title": "Schapire & Freund: Boosting: Foundations and Algorithms", "url": "https://mitpress.mit.edu/9780262526036/boosting/"},
                    {"title": "Elements of Statistical Learning - Ch. 8, 10", "url": "https://hastie.su.domains/ElemStatLearn/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary target of Bagging versus Boosting?",
                    "options": [
                        "Bagging reduces variance; Boosting primarily reduces bias.",
                        "Bagging reduces bias; Boosting reduces variance.",
                        "Both reduce only irreducible noise.",
                        "Bagging is for images; Boosting is for text."
                    ],
                    "correct": 0,
                    "explanation": "Bagging aggregates independent high-variance models to reduce variance. Boosting iteratively adds weak learners to fit unexplained residuals, driving down bias."
                },
                {
                    "question": "Why are base learners in Boosting typically kept shallow (e.g. max depth 2 to 6)?",
                    "options": [
                        "Deep trees are too fast to train.",
                        "Shallow trees act as weak learners with high bias and low variance, preventing the additive ensemble from overfitting noise too quickly.",
                        "Boosting algorithms cannot mathematically compute trees deeper than 6.",
                        "To reduce disk space only."
                    ],
                    "correct": 1,
                    "explanation": "Boosting combines weak learners. Using deep, low-bias trees causes the additive series to rapidly memorize noise, resulting in severe overfitting."
                },
                {
                    "question": "Which ensemble approach can be easily parallelized across 64 CPU cores during training?",
                    "options": [
                        "Boosting, because each tree depends on the next.",
                        "Bagging, because every bootstrap model is trained completely independently.",
                        "Neither, all ensembles are strictly sequential.",
                        "Only neural network ensembles."
                    ],
                    "correct": 1,
                    "explanation": "In Bagging, each model trains on an independent bootstrap sample, allowing simultaneous parallel execution across arbitrary CPU cores."
                }
            ]
        },
        {
            "id": "S09",
            "title": "Gradient Boosting (GBM)",
            "module": "supervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F06", "S05", "S08"],
            "estimatedMinutes": 25,
            "tags": ["boosting", "gbm", "pseudo-residuals", "gradient-descent", "additive-models"],
            "shortDesc": "Sequentially fit new decision trees to the negative gradient (pseudo-residuals) of an arbitrary loss function.",
            "sections": {
                "whatItIs": "Gradient Boosting Machines (GBM) generalize boosting to arbitrary differentiable loss functions. At each iteration, a new base learner (typically a shallow regression tree) is trained to predict the negative gradient of the loss function with respect to the current ensemble's predictions, executing gradient descent directly in function space.",
                "problemItSolves": "Older boosting methods (like AdaBoost) were constrained to exponential loss. GBM allows boosting to optimize squared error, absolute error, Huber loss, Poisson deviance, or cross-entropy.",
                "intuition": "Imagine playing golf. Your first drive lands 80 yards short of the hole (residual = +80). Your next swing aims not at the hole from the tee, but specifically targets the remaining 80-yard residual. If that shot goes 10 yards past (residual = -10), your third shot gently taps it back 10 yards. Each swing compensates for the cumulative mistakes of the prior swings.",
                "howItWorks": "1. <strong>Base Prediction:</strong> Initialize with a constant: $F_0(x) = \\arg\\min_c \\sum \\mathcal{L}(y_i, c)$ (e.g., mean for MSE).<br>2. <strong>Compute Pseudo-Residuals:</strong> For step $m$, compute $r_{im} = -\\left[\\frac{\\partial \\mathcal{L}(y_i, F(x_i))}{\\partial F(x_i)}\\right]_{F=F_{m-1}}$.<br>3. <strong>Fit Tree:</strong> Train a regression tree $h_m(x)$ to predict targets $r_{im}$.<br>4. <strong>Update Ensemble:</strong> $F_m(x) = F_{m-1}(x) + \\eta h_m(x)$, where $\\eta$ is the learning rate (shrinkage).",
                "mathematics": "Negative Gradient (Pseudo-Residual) for Squared Error $\\mathcal{L} = \\frac{1}{2}(y - F)^2$:<br>$$r_{im} = - \\frac{\\partial \\mathcal{L}}{\\partial F(x_i)} = y_i - F_{m-1}(x_i)$$<br>For Binary Cross-Entropy $\\mathcal{L} = -[y\\log p + (1-y)\\log(1-p)]$, where $p = \\sigma(F)$:<br>$$r_{im} = y_i - \\sigma(F_{m-1}(x_i)) = y_i - p_i$$<br>Additive Update with Shrinkage $\\eta$:<br>$$F_m(x) = F_{m-1}(x) + \\eta \\sum_{j=1}^{J_m} \\gamma_{jm} \\mathbb{I}(x \\in R_{jm})$$",
                "dataRequirements": "Tabular data. Handles continuous and categorical features. Missing values require handling (handled natively in modern variants).",
                "hyperparameters": [
                    {"name": "Learning Rate (\\eta / Shrinkage)", "description": "Step scaling applied to each tree's contribution (e.g. 0.01 to 0.1).", "effect": "Lower $\\eta$ dramatically improves generalization, requiring more trees."},
                    {"name": "n_estimators (M)", "description": "Total number of sequential boosting rounds.", "effect": "Too many trees causes overfitting; tuned via early stopping on validation loss."},
                    {"name": "Max Depth", "description": "Depth of each tree (typically 3 to 6).", "effect": "Depth $d$ allows interaction between up to $d$ variables."}
                ],
                "strengths": [
                    "Consistently wins competitive machine learning contests on tabular datasets.",
                    "Supports any differentiable custom loss function.",
                    "Provides excellent prediction accuracy and ranking performance."
                ],
                "limitations": [
                    "Inherently sequential: slower to train than parallel Random Forests.",
                    "Requires careful tuning of learning rate and tree depth to avoid overfitting.",
                    "Sensitive to noisy labels and extreme outliers when using squared error."
                ],
                "evaluation": "Evaluated using task-specific loss (Log-Loss, RMSE, NDCG) on validation sets monitored with Early Stopping.",
                "workedExample": "Target $y = 100$. Base prediction $F_0 = 70$. Residual $r_1 = 30$. Tree 1 predicts $\\hat{r}_1 = 25$. With learning rate $\\eta = 0.1$, update is $F_1 = 70 + 0.1(25) = 72.5$. Residual is now $100 - 72.5 = 27.5$. Tree 2 fits $27.5$, nudging predictions incrementally closer.",
                "whenToUse": "The go-to method for high-stakes tabular prediction challenges: credit scoring, customer lifetime value, search ranking.",
                "commonMistakes": [
                    "Setting the learning rate too high (e.g. $\\eta = 0.5$) without enough trees.",
                    "Not using early stopping, allowing the model to fit training noise indefinitely."
                ],
                "furtherLearning": [
                    {"title": "Jerome Friedman: Greedy Function Approximation: A Gradient Boosting Machine (2001)", "url": "https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-5/Greedy-function-approximation-A-gradient-boostingmachine/10.1214/aos/1013203451.full"},
                    {"title": "StatQuest: Gradient Boost Part 1 (YouTube)", "url": "https://www.youtube.com/watch?v=3CC4N4z3GJc"}
                ]
            },
            "quiz": [
                {
                    "question": "What target does each new decision tree attempt to predict in Gradient Boosting?",
                    "options": [
                        "The original target variable $y$.",
                        "The negative gradient (pseudo-residuals) of the loss function with respect to current ensemble predictions.",
                        "A random permutation of the features.",
                        "The Out-of-Bag error."
                    ],
                    "correct": 1,
                    "explanation": "Each new tree is fit to the pseudo-residuals (the negative gradient), steering the ensemble down the steepest loss descent trajectory."
                },
                {
                    "question": "What is 'Shrinkage' (learning rate $\\eta$) in Gradient Boosting?",
                    "options": [
                        "A technique to compress the model file size on disk.",
                        "A multiplier between 0 and 1 that scales each tree's contribution, slowing down learning to prevent premature overfitting.",
                        "A method to delete uninformative features.",
                        "A tree pruning algorithm."
                    ],
                    "correct": 1,
                    "explanation": "Shrinkage scales each tree's update by a small fraction $\\eta \\in (0, 1)$, ensuring the model takes gradual, deliberate steps that generalize significantly better."
                },
                {
                    "question": "What stopping criterion is standard practice to prevent Gradient Boosting from overfitting?",
                    "options": [
                        "Training until loss on the training set reaches exactly 0.0.",
                        "Early stopping: halting training when validation loss fails to improve for a preset number of rounds.",
                        "Stopping after exactly 10 seconds.",
                        "Stopping when all tree leaves have 1 sample."
                    ],
                    "correct": 1,
                    "explanation": "Early stopping monitors validation loss; when validation error ceases improving and starts climbing, training terminates to preserve peak generalization."
                }
            ]
        },
        {
            "id": "S10",
            "title": "XGBoost, LightGBM & CatBoost",
            "module": "supervised",
            "level": "intermediate",
            "prerequisites": ["S05", "S08", "S09"],
            "estimatedMinutes": 25,
            "tags": ["xgboost", "lightgbm", "catboost", "histogram-binning", "modern-gbm"],
            "shortDesc": "State-of-the-art modern gradient boosting frameworks: second-order Taylor expansions, histogram binning, and categorical encodings.",
            "sections": {
                "whatItIs": "XGBoost (Extreme Gradient Boosting), LightGBM (Light Gradient Boosting Machine), and CatBoost represent the modern evolution of gradient boosting. They enhance traditional GBM with second-order Taylor loss approximations (Hessians), hardware-accelerated histogram binning, sparsity awareness, leaf-wise tree growth, and automated categorical feature handling.",
                "problemItSolves": "Vanilla GBM is notoriously slow on big data because it computes exact continuous splits. These modern frameworks scale to millions of rows, train 10x-50x faster, handle missing values natively, and automate categorical encodings.",
                "intuition": "If vanilla GBM is a craftsman carefully carving a statue with a manual chisel, LightGBM is a computer-guided laser cutter with pre-binned resolution steps, and CatBoost is an automated robotic factory that also translates foreign blueprints into clean structural pieces on the fly.",
                "howItWorks": "1. <strong>XGBoost:</strong> Uses 2nd-order Taylor expansions ($g_i$ gradient, $h_i$ Hessian) and exact/approximate quantile splits with an analytical leaf weight formula.<br>2. <strong>LightGBM:</strong> Replaces continuous sorting with histogram binning (GOSS - Gradient-based One-Side Sampling) and grows trees <em>leaf-wise</em> rather than depth-wise.<br>3. <strong>CatBoost:</strong> Uses Ordered Boosting (combatting target leakage) and Symmetric (oblivious) trees, handling high-cardinality categoricals natively via target statistics.",
                "mathematics": "Second-Order Taylor Approximation of Loss:<br>$$\\mathcal{L}^{(t)} \\approx \\sum_{i=1}^N \\left[ \\mathcal{L}(y_i, \\hat{y}^{(t-1)}) + g_i f_t(x_i) + \\frac{1}{2} h_i f_t^2(x_i) \\right] + \\Omega(f_t)$$<br>where $g_i = \\partial_{\\hat{y}} \\mathcal{L}$, $h_i = \\partial^2_{\\hat{y}} \\mathcal{L}$, and $\\Omega(f) = \\gamma T + \\frac{1}{2} \\lambda \\sum w_j^2$.<br>Optimal Leaf Weight and Split Gain:<br>$$w_j^* = - \\frac{\\sum_{i \\in I_j} g_i}{\\sum_{i \\in I_j} h_i + \\lambda}, \\quad \\text{Gain} = \\frac{1}{2} \\left[ \\frac{G_L^2}{H_L + \\lambda} + \\frac{G_R^2}{H_R + \\lambda} - \\frac{(G_L + G_R)^2}{H_L + H_R + \\lambda} \\right] - \\gamma$$",
                "dataRequirements": "Tabular datasets. All three handle missing values automatically. CatBoost and LightGBM handle categorical variables natively without manual one-hot encoding.",
                "hyperparameters": [
                    {"name": "max_depth / num_leaves", "description": "Tree size limit. LightGBM tunes `num_leaves`; XGBoost tunes `max_depth`.", "effect": "Primary capacity controller."},
                    {"name": "colsample_bytree / colsample_bylevel", "description": "Subsampling ratio of columns at tree/level.", "effect": "De-correlates trees, preventing dominant features from masking others."},
                    {"name": "reg_lambda (L2) & reg_alpha (L1)", "description": "Regularization penalties on leaf weights.", "effect": "Smooths weights and penalizes complex leaves."}
                ],
                "strengths": [
                    "The undisputed state of the art for structured tabular data across industries.",
                    "Blistering speed and GPU acceleration support.",
                    "Built-in handling of missing values, sparse matrices, and categoricals.",
                    "Extremely robust feature importance diagnostics."
                ],
                "limitations": [
                    "Dozens of interdependent hyperparameters make thorough tuning necessary.",
                    "Black-box nature requires SHAP values for regulatory explainability.",
                    "Inferior to Transformers/CNNs on unstructured data (raw audio, images, text)."
                ],
                "evaluation": "Evaluated using Log-Loss, ROC-AUC, RMSE, and MAP with K-Fold Cross Validation.",
                "workedExample": "A Kaggle competition with 2 million customer transactions and 80 features. A standard random forest takes 45 minutes to train. LightGBM completes 500 boosting rounds in 18 seconds using GPU histogram binning, winning with a higher AUC.",
                "whenToUse": "The primary choice for production tabular classification, regression, and ranking.",
                "commonMistakes": [
                    "Using default hyperparameters on small datasets (LightGBM's default 31 leaves will quickly overfit a small dataset).",
                    "One-hot encoding high-cardinality categoricals when CatBoost or LightGBM can process them natively."
                ],
                "furtherLearning": [
                    {"title": "Chen & Guestrin: XGBoost: A Scalable Tree Boosting System (2016)", "url": "https://arxiv.org/abs/1603.02754"},
                    {"title": "LightGBM Documentation", "url": "https://lightgbm.readthedocs.io/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the key technological innovation in LightGBM that enables massive speedups over traditional GBM?",
                    "options": [
                        "It uses recurrent memory cells.",
                        "Histogram-based feature binning and leaf-wise (best-first) tree growth.",
                        "It only trains on 5% of the data.",
                        "It converts all trees into linear equations."
                    ],
                    "correct": 1,
                    "explanation": "LightGBM buckets continuous values into discrete histogram bins (e.g. 256 bins) and grows trees leaf-wise, reducing computation by orders of magnitude."
                },
                {
                    "question": "What mathematical approximation enables XGBoost to evaluate custom objective functions rapidly?",
                    "options": [
                        "First-order Euler method.",
                        "Second-order Taylor expansion using both first derivatives (gradients) and second derivatives (Hessians).",
                        "Fourier transform.",
                        "Monte Carlo sampling."
                    ],
                    "correct": 1,
                    "explanation": "XGBoost approximates the loss function using a 2nd-order Taylor expansion ($g_i$ gradient and $h_i$ Hessian), giving an analytical closed-form formula for optimal leaf weights."
                },
                {
                    "question": "Which of these three frameworks is particularly celebrated for handling categorical variables natively without manual preprocessing?",
                    "options": [
                        "CatBoost",
                        "Scikit-Learn LinearRegression",
                        "Standard ID3",
                        "Perceptron"
                    ],
                    "correct": 0,
                    "explanation": "CatBoost (Categorical Boosting) was engineered specifically to handle high-cardinality categorical variables natively via target statistics and ordered target encoding."
                }
            ]
        },
        {
            "id": "S11",
            "title": "Support Vector Machines (SVM)",
            "module": "supervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F02", "F05", "S01"],
            "estimatedMinutes": 25,
            "tags": ["svm", "max-margin", "kernel-trick", "support-vectors", "convex-optimization"],
            "shortDesc": "Find the maximum-margin hyperplane separating classes, projecting data into infinite-dimensional spaces via the Kernel Trick.",
            "sections": {
                "whatItIs": "Support Vector Machines (SVM) are maximum-margin classifiers. An SVM finds the unique hyperplane that maximizes the geometric distance (margin) between the separating boundary and the nearest data points of any class (the Support Vectors). Through the <strong>Kernel Trick</strong>, SVMs implicitly map non-linearly separable inputs into high-dimensional feature spaces where linear separation becomes possible.",
                "problemItSolves": "Many linear classifiers find <em>any</em> line that divides classes; an SVM mathematically finds the <em>safest, most robust</em> line by maximizing the buffer zone. The kernel trick solves non-linear problems without explicitly computing coordinates in infinite dimensions.",
                "intuition": "Imagine laying a highway between two towns (Red and Blue). Any thin fence that keeps them apart is acceptable to a simple classifier. An SVM constructs the widest possible interstate highway between them, where the white lines on the shoulders touch the closest houses (the Support Vectors).",
                "howItWorks": "1. <strong>Hard vs Soft Margin:</strong> Allow bounded slack $\\xi_i$ for non-separable points, controlled by penalty $C$.<br>2. <strong>Primal to Dual:</strong> Formulate as a quadratic programming optimization problem and solve the dual problem using Lagrange multipliers $\\alpha_i$.<br>3. <strong>Support Vectors:</strong> Points with $\\alpha_i > 0$ are the support vectors; all other points can be removed without changing the decision boundary.<br>4. <strong>Kernel Substitution:</strong> Replace inner products $\\langle \\mathbf{x}_i, \\mathbf{x}_j \\rangle$ with a kernel function $K(\\mathbf{x}_i, \\mathbf{x}_j)$.",
                "mathematics": "Soft-Margin Primal Objective:<br>$$\\min_{\\mathbf{w}, b, \\boldsymbol{\\xi}} \\frac{1}{2} \\|\\mathbf{w}\\|^2 + C \\sum_{i=1}^N \\xi_i \\quad \\text{s.t.} \\quad y_i(\\mathbf{w}^T \\phi(\\mathbf{x}_i) + b) \\ge 1 - \\xi_i, \\quad \\xi_i \\ge 0$$<br>Radial Basis Function (RBF / Gaussian) Kernel:<br>$$K(\\mathbf{x}, \\mathbf{z}) = \\exp\\left( -\\gamma \\|\\mathbf{x} - \\mathbf{z}\\|^2 \\right)$$<br>Decision Function:<br>$$f(\\mathbf{x}) = \\text{sign}\\left( \\sum_{i \\in \\text{SV}} \\alpha_i y_i K(\\mathbf{x}_i, \\mathbf{x}) + b \\right)$$",
                "dataRequirements": "Features MUST be strictly scaled (standardized to zero mean and unit variance). Distance-based kernels are completely distorted by unscaled variables.",
                "hyperparameters": [
                    {"name": "Cost Penalty (C)", "description": "Trades off margin width against training errors.", "effect": "Large $C$ penalizes misclassifications heavily (narrow margin, high variance); small $C$ permits more violations for a wider margin (high bias)."},
                    {"name": "Kernel Type", "description": "Linear, Polynomial, RBF (Gaussian), Sigmoid.", "effect": "RBF is the versatile non-linear default; Linear is used for high-dimensional text."},
                    {"name": "Gamma (\\gamma)", "description": "Kernel coefficient for RBF (inverse of variance sphere).", "effect": "Large $\\gamma$ makes Gaussian bells tight (complex boundary, overfitting); small $\\gamma$ creates smooth boundaries."}
                ],
                "strengths": [
                    "Guaranteed global optimum due to convex quadratic programming formulation.",
                    "Remarkably effective in high-dimensional spaces where features outnumber samples ($D > N$).",
                    "Memory efficient during inference: depends solely on the subset of Support Vectors, discarding the rest of the training set.",
                    "Theoretical grounding in Vapnik-Chervonenkis (VC) generalization theory."
                ],
                "limitations": [
                    "Training scales cubically $\\mathcal{O}(N^3)$ with dataset size, rendering standard SVMs unusable for datasets with $>100,000$ samples.",
                    "Does not provide native probability estimates (requires Platt scaling).",
                    "Highly sensitive to hyperparameter choices ($C$ and $\\gamma$)."
                ],
                "evaluation": "Evaluated using Accuracy, F1-Score, and ROC-AUC via grid-search cross-validation over $(C, \\gamma)$ pairs.",
                "workedExample": "A circular dataset where Class 1 is an inner circle ($r < 2$) and Class 2 is an outer ring ($r > 3$). Linearly inseparable in 2D. Applying an RBF kernel projects the inner circle upwards in the third dimension, allowing a flat plane to slice cleanly between the two classes.",
                "whenToUse": "Superb for small-to-medium sized datasets with high dimensionality: bioinformatics (gene expression), text classification, and facial landmark recognition.",
                "commonMistakes": [
                    "Failing to standardize features before feeding them into an SVM.",
                    "Attempting to train an RBF SVM on a dataset with 500,000 rows (it will freeze or take days without linear approximation)."
                ],
                "furtherLearning": [
                    {"title": "Cortes & Vapnik: Support-Vector Networks (1995)", "url": "https://link.springer.com/article/10.1007/BF00994018"},
                    {"title": "MIT OpenCourseWare: Support Vector Machines (Patrick Winston)", "url": "https://www.youtube.com/watch?v=_PwhiWxHK8o"}
                ]
            },
            "quiz": [
                {
                    "question": "What are 'Support Vectors' in an SVM?",
                    "options": [
                        "A vector of software dependencies in Python.",
                        "The critical data points that lie directly on or violate the margin boundaries and uniquely define the decision hyperplane.",
                        "The eigenvectors of the covariance matrix.",
                        "The learning rate vectors."
                    ],
                    "correct": 1,
                    "explanation": "Support vectors are the specific training examples lying on the margin edges (or inside the margin). All other points can be completely deleted without moving the boundary."
                },
                {
                    "question": "What is the primary advantage of the 'Kernel Trick'?",
                    "options": [
                        "It allows the model to compute dot products in high (or infinite) dimensional feature space without ever explicitly calculating the transformed coordinates.",
                        "It makes the code run in kernel mode inside the operating system.",
                        "It eliminates the need for test sets.",
                        "It turns classification into clustering."
                    ],
                    "correct": 0,
                    "explanation": "The Kernel Trick computes $K(\\mathbf{x}, \\mathbf{z}) = \\langle \\phi(\\mathbf{x}), \\phi(\\mathbf{z}) \\rangle$ directly from low-dimensional coordinates, bypassing the computationally impossible step of mapping points into infinite-dimensional space."
                },
                {
                    "question": "Why is standard SVM training impractical on datasets with 1,000,000 samples?",
                    "options": [
                        "Because quadratic programming solvers scale between $\\mathcal{O}(N^2)$ and $\\mathcal{O}(N^3)$ with sample size.",
                        "Because SVMs can only process a maximum of 256 numbers.",
                        "Because computers cannot calculate margins greater than 100.",
                        "Because the margin vanishes to zero."
                    ],
                    "correct": 0,
                    "explanation": "Standard SVM solvers (like LIBSVM/SMO) scale roughly with $\\mathcal{O}(N^2)$ to $\\mathcal{O}(N^3)$ computational time and require large kernel cache matrices, making them impractical for massive sample sizes."
                }
            ]
        },
        {
            "id": "S12",
            "title": "The Perceptron",
            "module": "supervised",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "S01"],
            "estimatedMinutes": 15,
            "tags": ["perceptron", "neural-origins", "linear-classifier", "rosenblatt", "hebbian"],
            "shortDesc": "The historical building block of neural networks: Rosenblatt's single-layer threshold neuron and its convergence theorem.",
            "sections": {
                "whatItIs": "The Perceptron, invented by Frank Rosenblatt in 1958, is the earliest mathematical model of an artificial neuron. It takes a vector of real-valued inputs, computes a weighted linear combination, and outputs a binary decision by passing the sum through a hard threshold step function.",
                "problemItSolves": "Provided the historic foundational proof that machines could learn linear decision boundaries from scratch simply by adjusting numerical weights in response to errors.",
                "intuition": "Think of deciding whether to attend an outdoor music festival. You weigh several factors: Is the weather warm? ($w_1 = +3$), Is my favorite band playing? ($w_2 = +5$), Is admission expensive? ($w_3 = -4$). You sum up the factors; if the total exceeds your internal threshold ($b = 2$), you go. If not, you stay home.",
                "howItWorks": "1. <strong>Linear Combination:</strong> Compute $z = \\mathbf{w}^T \\mathbf{x} + b$.<br>2. <strong>Step Function Activation:</strong> Output $\\hat{y} = 1$ if $z \\ge 0$, else $\\hat{y} = -1$ (or 0).<br>3. <strong>Perceptron Learning Rule:</strong> If prediction is incorrect, update weights: $\\mathbf{w} \\leftarrow \\mathbf{w} + \\eta y_i \\mathbf{x}_i$.<br>4. <strong>Convergence:</strong> If data is linearly separable, the Perceptron Convergence Theorem guarantees the algorithm will find a separating hyperplane in a finite number of steps.",
                "mathematics": "Activation Function (Heaviside Step):<br>$$f(z) = \\begin{cases} 1 & \\text{if } z \\ge 0 \\\\ -1 & \\text{if } z < 0 \\end{cases}$$<br>Weight Update Rule upon mistake on sample $(\\mathbf{x}_i, y_i)$:<br>$$\\mathbf{w} \\leftarrow \\mathbf{w} + \\eta \\, y_i \\, \\mathbf{x}_i, \\qquad b \\leftarrow b + \\eta \\, y_i$$<br>Novikoff's Upper Bound on Mistakes ($R = \\max \\|x_i\\|$, margin $\\gamma$):<br>$$M \\le \\left( \\frac{R}{\\gamma} \\right)^2$$",
                "dataRequirements": "Continuous or binary features. Linearly separable data is strictly required for convergence without infinite looping.",
                "hyperparameters": [
                    {"name": "Learning Rate (\\eta)", "description": "Step scale for weight additions.", "effect": "In a pure perceptron, $\\eta$ merely scales the weight vector without changing the angle of the boundary."},
                    {"name": "Max Iterations", "description": "Safety threshold to prevent infinite cycling on non-linearly separable datasets.", "effect": "Halts execution when data cannot be separated linearly."}
                ],
                "strengths": [
                    "Historical stepping stone to all modern deep learning and neural network architectures.",
                    "Extremely simple algorithm: can be implemented in 10 lines of code.",
                    "Online learning: updates weights sample by sample with zero memory overhead."
                ],
                "limitations": [
                    "Cannot solve non-linearly separable problems (famous Minsky & Papert 1969 XOR limitation).",
                    "Does not converge on non-separable data (cycles endlessly without margin stabilization).",
                    "Step activation has zero derivative everywhere except $z=0$, rendering it incompatible with modern gradient backpropagation."
                ],
                "evaluation": "Evaluated using Classification Accuracy and number of mistake epochs to convergence.",
                "workedExample": "Learning the logical AND gate: Inputs $(0,0)\\to 0, (0,1)\\to 0, (1,0)\\to 0, (1,1)\\to 1$. With initial weights $w = [0, 0]$ and bias $b = 0$, misclassifying $(1,1)$ updates weights by adding $(1,1)$. After a few epochs, weights converge to $w_1 = 1, w_2 = 1, b = -1.5$. For $(1,1)$, $z = 2 - 1.5 = +0.5 > 0$ (correct).",
                "whenToUse": "Used primarily for educational and theoretical understanding of neural network origins and online linear learning.",
                "commonMistakes": [
                    "Attempting to train a single perceptron on XOR or circular data.",
                    "Trying to use calculus/gradients on the step function (its derivative is zero almost everywhere)."
                ],
                "furtherLearning": [
                    {"title": "Rosenblatt: The Perceptron: A Probabilistic Model for Information Storage (1958)", "url": "https://psycnet.apa.org/record/1959-09865-001"},
                    {"title": "Minsky & Papert: Perceptrons Book (1969)", "url": "https://mitpress.mit.edu/9780262631111/perceptrons/"}
                ]
            },
            "quiz": [
                {
                    "question": "What famous logical problem can a single-layer Perceptron NOT solve?",
                    "options": [
                        "AND gate",
                        "OR gate",
                        "XOR (Exclusive OR) gate",
                        "NOT gate"
                    ],
                    "correct": 2,
                    "explanation": "XOR outputs 1 for inputs $(0,1)$ and $(1,0)$, and 0 for $(0,0)$ and $(1,1)$. This distribution cannot be separated by any single straight line in 2D space."
                },
                {
                    "question": "What happens if you run the Perceptron learning algorithm on a dataset that is NOT linearly separable?",
                    "options": [
                        "It converges to the maximum margin line.",
                        "It will cycle forever without ever terminating, flipping weights back and forth.",
                        "It raises a math domain error.",
                        "It automatically inserts a hidden layer."
                    ],
                    "correct": 1,
                    "explanation": "Because the update rule fires every time a mistake is encountered, and zero mistakes are impossible on non-separable data, the algorithm loops indefinitely unless capped by max iterations."
                },
                {
                    "question": "Why is the Heaviside step activation function unsuitable for multi-layer backpropagation?",
                    "options": [
                        "Its output values are too large.",
                        "Its derivative is zero everywhere (and undefined at 0), meaning gradients cannot flow backward to update earlier layers.",
                        "It requires GPU compilation.",
                        "It only accepts negative inputs."
                    ],
                    "correct": 1,
                    "explanation": "Backpropagation relies on the chain rule: multiplying layer gradients. A derivative of zero means gradients vanish immediately, making it impossible to train hidden layers."
                }
            ]
        },
        {
            "id": "S13",
            "title": "Multilayer Perceptron (MLP)",
            "module": "supervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F02", "S12"],
            "estimatedMinutes": 25,
            "tags": ["neural-networks", "mlp", "backpropagation", "hidden-layers", "universal-approximation"],
            "shortDesc": "Feedforward neural networks stacking multiple dense layers with non-linear activations to learn arbitrary non-linear mappings.",
            "sections": {
                "whatItIs": "A Multilayer Perceptron (MLP) is a foundational deep feedforward artificial neural network. It consists of an input layer, one or more hidden layers, and an output layer. By interleaving linear matrix transformations with non-linear activation functions (ReLU, Sigmoid, GELU), an MLP can approximate any continuous mathematical function.",
                "problemItSolves": "Overcomes the linear limitations of the single-layer perceptron, solving non-linear problems like XOR and learning complex manifold transformations directly from data.",
                "intuition": "If a single perceptron is a single worker drawing one straight line across a factory floor, an MLP is a team of 100 workers organized into sequential shifts. The first shift draws many line segments; the next shift combines those segments into polygons, curves, and shapes; the final manager uses those shapes to categorize the product.",
                "howItWorks": "1. <strong>Forward Pass:</strong> Propagate inputs through layers: $\\mathbf{a}^{(l)} = \\sigma(\\mathbf{W}^{(l)} \\mathbf{a}^{(l-1)} + \\mathbf{b}^{(l)})$.<br>2. <strong>Loss Evaluation:</strong> Measure prediction error at the output layer.<br>3. <strong>Backward Pass (Backprop):</strong> Compute gradients of loss with respect to all weights using the chain rule: $\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{W}^{(l)}} = \\boldsymbol{\\delta}^{(l)} (\\mathbf{a}^{(l-1)})^T$.<br>4. <strong>Parameter Update:</strong> Update weights and biases via gradient descent or Adam: $\\mathbf{W} \\leftarrow \\mathbf{W} - \\alpha \\nabla_{\\mathbf{W}} \\mathcal{L}$.",
                "mathematics": "Layer Computation Graph:<br>$$\\mathbf{z}^{(l)} = \\mathbf{W}^{(l)} \\mathbf{a}^{(l-1)} + \\mathbf{b}^{(l)}, \\quad \\mathbf{a}^{(l)} = \\sigma(\\mathbf{z}^{(l)})$$<br>Backpropagation Error Signal (Vectorized):<br>$$\\boldsymbol{\\delta}^{(l)} = \\left( (\\mathbf{W}^{(l+1)})^T \\boldsymbol{\\delta}^{(l+1)} \\right) \\odot \\sigma'(\\mathbf{z}^{(l)})$$<br>Universal Approximation Theorem (Cybenko, 1989):<br>A feedforward network with a single hidden layer containing finite neurons and non-linear activation can approximate any continuous function on compact subsets of $\\mathbb{R}^n$ to arbitrary precision $\\epsilon > 0$.",
                "dataRequirements": "Continuous numerical inputs. Features MUST be normalized (zero mean, unit variance). Categorical features must be one-hot encoded or embedded.",
                "hyperparameters": [
                    {"name": "Hidden Layer Architecture", "description": "Number of layers and neurons per layer (e.g. [128, 64]).", "effect": "Determines model capacity and expressive power."},
                    {"name": "Activation Function", "description": "ReLU, LeakyReLU, GELU, ELU, Tanh.", "effect": "ReLU prevents vanishing gradients; Tanh centers activations around zero."},
                    {"name": "Dropout Rate", "description": "Probability of zeroing neuron outputs during training (e.g. 0.2 to 0.5).", "effect": "Prevents co-adaptation of features, fighting overfitting."}
                ],
                "strengths": [
                    "Universal approximator: capable of modeling arbitrary non-linear relationships.",
                    "Forms the modular backbone for modern deep learning architectures.",
                    "Easily parallelized on GPUs via matrix multiplication $\\mathbf{W}\\mathbf{x}$."
                ],
                "limitations": [
                    "Full connectivity produces millions of parameters, causing parameter bloat on spatial (image) or sequential (text) data.",
                    "Prone to vanishing or exploding gradients if unnormalized or poorly initialized.",
                    "Requires careful hyperparameter tuning and regularization."
                ],
                "evaluation": "Monitored using training vs validation loss curves (Loss and Accuracy/RMSE vs Epochs) to detect overfitting.",
                "workedExample": "Solving XOR with an MLP: Hidden layer has 2 neurons with ReLU. Layer 1 creates two lines: $h_1 = \\text{ReLU}(x_1 + x_2 - 0.5)$ and $h_2 = \\text{ReLU}(x_1 + x_2 - 1.5)$. Output layer computes $y = h_1 - 2 h_2$. For $(0,1) \\to h_1 = 0.5, h_2 = 0 \\to y = 0.5 > 0$ (Class 1). For $(1,1) \\to h_1 = 1.5, h_2 = 0.5 \\to y = 1.5 - 1.0 = 0.5 \\to$ calibrated correctly.",
                "whenToUse": "Use on complex non-linear tabular datasets, embedding transformations, and as the dense head of vision/language models.",
                "commonMistakes": [
                    "Omitting non-linear activation functions between layers (a stack of purely linear layers mathematically collapses into a single linear layer: $W_2(W_1 x) = (W_2 W_1) x$).",
                    "Failing to normalize input features, causing exploding or dying gradients."
                ],
                "furtherLearning": [
                    {"title": "Rumelhart, Hinton, Williams: Learning representations by back-propagating errors (Nature 1986)", "url": "https://www.nature.com/articles/323533a0"},
                    {"title": "3Blue1Brown: Neural Networks and Backpropagation Series", "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi"}
                ]
            },
            "quiz": [
                {
                    "question": "What happens if you remove all non-linear activation functions from a 50-layer deep neural network?",
                    "options": [
                        "It runs 50 times faster but still approximates complex curves.",
                        "It mathematically collapses into a simple single-layer linear model because the product of linear matrices is just another linear matrix.",
                        "The network outputs become imaginary numbers.",
                        "Training diverges to infinity."
                    ],
                    "correct": 1,
                    "explanation": "Linear combinations of linear functions remain strictly linear ($W_2(W_1 x) = W_{\\text{combined}} x$). Non-linear activations are required to introduce curvature and universal approximation capacity."
                },
                {
                    "question": "What is the primary algorithm used to compute the gradients of the loss function with respect to every weight in an MLP?",
                    "options": [
                        "Simulated Annealing",
                        "Backpropagation (Reverse-Mode Automatic Differentiation via the Calculus Chain Rule)",
                        "K-Means Clustering",
                        "Genetic Algorithms"
                    ],
                    "correct": 1,
                    "explanation": "Backpropagation computes analytical gradients efficiently by applying the calculus chain rule backwards from output to input."
                },
                {
                    "question": "Why is the ReLU (Rectified Linear Unit) activation preferred over Sigmoid in deep hidden layers?",
                    "options": [
                        "ReLU produces outputs between -1 and +1.",
                        "ReLU has a constant gradient of 1 for all positive inputs, preventing vanishing gradients during backpropagation.",
                        "ReLU is completely smooth and differentiable at 0.",
                        "ReLU requires matrix inversion."
                    ],
                    "correct": 1,
                    "explanation": "Sigmoid saturates at extreme values where its derivative is near zero, causing gradients to vanish when multiplied across many layers. ReLU maintains a gradient of 1 for positive values, facilitating gradient flow."
                }
            ]
        }
    ]
print("Supervised module defined: 13 lessons")

# -*- coding: utf-8 -*-
"""
Curriculum Builder for Free Mind ML
Generates js/catalog.js with complete content for all 52 lessons.
"""
import json

def get_foundations():
    # Return F01 - F07
    return [
        {
            "id": "F01",
            "title": "AI, Machine Learning & Deep Learning",
            "module": "foundations",
            "level": "beginner",
            "prerequisites": [],
            "estimatedMinutes": 15,
            "tags": ["intro", "foundations", "taxonomy", "history"],
            "shortDesc": "Understand the hierarchy connecting Artificial Intelligence, Machine Learning, and Deep Learning, and how rule-based systems differ from learning systems.",
            "sections": {
                "whatItIs": "Artificial Intelligence (AI) is the overarching discipline dedicated to creating systems capable of performing tasks that typically demand human cognition. Machine Learning (ML) is a subset of AI where systems discover patterns from empirical data rather than executing hard-coded rules. Deep Learning (DL) is a specialized branch of ML powered by multi-layered artificial neural networks that automatically extract hierarchical representations directly from raw inputs.",
                "problemItSolves": "Classical software engineering relies on deterministic algorithms: a programmer conceives rules, tests edge cases, and hardcodes logic (if/else branches). However, complex sensory tasks—such as recognizing handwritten digits, translating idiomatic speech, or synthesizing natural proteins—have rules that are intractable to write by hand. ML solves this by shifting the programmer's role from writing deterministic rules to designing learning architectures and objective functions.",
                "intuition": "Think of classical programming as baking a cake by strictly following an ironclad recipe. Machine learning is having a chef taste 10,000 cakes with varying ingredient ratios and their customer review scores, gradually adjusting the recipe to maximize deliciousness. Deep learning is like having that chef also learn how to mill flour, ferment yeast, and temper cocoa beans from raw agricultural grains without being told what flour or chocolate even is.",
                "howItWorks": "1. <strong>Problem Formulation:</strong> Frame the objective as a mapping function $f: X \\to Y$.<br>2. <strong>Data Collection & Preprocessing:</strong> Gather historical observations, clean anomalies, and encode variables into numerical tensors.<br>3. <strong>Model Selection:</strong> Choose a hypothesis class (e.g., linear model, decision tree, or deep neural network).<br>4. <strong>Loss Definition:</strong> Specify an objective function measuring the discrepancy between prediction $\\hat{y}$ and true ground truth $y$.<br>5. <strong>Optimization:</strong> Iteratively update internal parameters using algorithms like Gradient Descent until validation performance converges.",
                "mathematics": "In classical rule-based computing:<br>$$\\text{Output} = \\text{Rules}(\\text{Input})$$<br>In Machine Learning:<br>$$\\text{Model Rules} = \\arg\\min_{\\theta} \\sum_{i=1}^N \\mathcal{L}\\left(f_\\theta(x^{(i)}), y^{(i)}\\right) + \\lambda \\Omega(\\theta)$$<br>where $\\theta$ represents tunable model weights, $\\mathcal{L}$ is the empirical loss function, and $\\Omega(\\theta)$ is a regularization penalty guarding against overfitting.",
                "dataRequirements": "Machine learning systems require statistically representative datasets. Classical ML models (such as SVMs, Random Forests, or Logistic Regression) can deliver strong baseline performance on structured tabular data with hundreds to tens of thousands of samples. Deep learning architectures typically require tens of thousands to billions of samples along with high-dimensional sensory inputs.",
                "hyperparameters": [
                    {"name": "Model Capacity", "description": "The degree of freedom or number of trainable parameters in the architecture.", "effect": "Too low yields underfitting; too high leads to overfitting and high compute cost."},
                    {"name": "Learning Rate (\\alpha)", "description": "The step magnitude taken in parameter space during gradient optimization.", "effect": "Too large causes divergence; too small results in agonizingly slow convergence."},
                    {"name": "Regularization (\\lambda)", "description": "Penalty magnitude imposed on model complexity or parameter norms.", "effect": "Restricts parameter values to promote generalizability to unseen data."}
                ],
                "strengths": [
                    "Eliminates the requirement for manually exhaustive hand-crafted logic.",
                    "Scales gracefully with massive volumes of raw sensor, textual, and transactional data.",
                    "Discovers subtle, non-linear cross-feature correlations invisible to human domain experts.",
                    "Provides probabilistic outputs and decision boundaries that can continuously adapt as fresh data arrives."
                ],
                "limitations": [
                    "Extreme sensitivity to sampling bias and historical prejudices present in training distributions.",
                    "High computational and memory footprints, especially for deep foundation models.",
                    "Lack of interpretability ('black-box' nature) in deep neural architectures.",
                    "Vulnerability to adversarial perturbations and distribution shifts."
                ],
                "evaluation": "Models are assessed by holding out unseen data: partitioning into Train, Validation, and Test subsets. Metrics vary by task: Classification uses Accuracy, Precision, Recall, F1-Score, and ROC-AUC; Regression uses Mean Squared Error (MSE), Root MSE (RMSE), Mean Absolute Error (MAE), and $R^2$.",
                "workedExample": "Consider spam detection: Under classical programming, an engineer creates a dictionary of forbidden words ('viagra', 'lottery', 'wire transfer'). Spammers quickly evade this using leetspeak ('v1agra'). In an ML system (e.g. Naive Bayes), the algorithm computes conditional probabilities $P(\\text{word}|\\text{Spam})$ from millions of emails, naturally assigning high spam weights to n-grams, header patterns, and punctuation distributions without manual keyword maintenance.",
                "whenToUse": "Use ML when the underlying data-generating process is high-dimensional, noisy, or non-linear, and when sufficient historical examples exist. Avoid ML when exact deterministic rules are known (e.g., calculating tax tables), when zero training data exists, or when 100% mathematical guarantees with zero tolerance for probabilistic variance are required.",
                "commonMistakes": [
                    "Attempting Deep Learning on small tabular datasets where XGBoost or Random Forest would perform significantly better.",
                    "Evaluating model accuracy on training data rather than a strictly quarantined test set.",
                    "Treating high correlation as causality without verifying external confounding factors."
                ],
                "furtherLearning": [
                    {"title": "Deep Learning Book (Goodfellow et al.) - Ch. 1 Intro", "url": "https://www.deeplearningbook.org/contents/intro.html"},
                    {"title": "Google ML Crash Course: Framing", "url": "https://developers.google.com/machine-learning/crash-course/framing/check-your-understanding"}
                ]
            },
            "quiz": [
                {
                    "question": "What fundamentally distinguishes Machine Learning from classical rule-based programming?",
                    "options": [
                        "Classical programming requires computers; ML runs on biological neural tissue.",
                        "Classical systems take input rules to generate output; ML takes inputs and outputs to learn the rules.",
                        "Machine learning never produces errors, unlike human-written code.",
                        "Machine learning can only process images and video, not numbers or text."
                    ],
                    "correct": 1,
                    "explanation": "In traditional programming, engineers write explicit rules and algorithms. In machine learning, algorithms optimize their internal parameters using input data and corresponding ground-truth outputs to deduce the underlying rules."
                },
                {
                    "question": "Which of the following is true regarding Deep Learning relative to traditional Machine Learning?",
                    "options": [
                        "Deep Learning requires hand-crafted feature engineering for every single input.",
                        "Deep Learning is a subset of Machine Learning characterized by multi-layered neural networks.",
                        "Deep Learning always uses less computational power than classical models.",
                        "Deep Learning does not use optimization algorithms like gradient descent."
                    ],
                    "correct": 1,
                    "explanation": "Deep Learning is a specialized subfield of Machine Learning that uses deep neural networks with multiple layers to learn hierarchical representations directly from raw data."
                },
                {
                    "question": "Why would you choose a classical tabular model (like Gradient Boosted Trees) over a Deep Neural Network?",
                    "options": [
                        "Tabular datasets with tens of thousands of rows often train faster, require less tuning, and beat DNNs.",
                        "Neural networks cannot mathematically process tabular columns.",
                        "Classical models can only run on cloud supercomputers.",
                        "Decision trees guarantee 100% accuracy on every dataset."
                    ],
                    "correct": 0,
                    "explanation": "On tabular and structured data, tree-based ensembles (such as XGBoost or LightGBM) regularly outperform deep neural networks in training speed, sample efficiency, and baseline accuracy."
                }
            ]
        },
        {
            "id": "F02",
            "title": "Core Vocabulary of Machine Learning",
            "module": "foundations",
            "level": "beginner",
            "prerequisites": ["F01"],
            "estimatedMinutes": 20,
            "tags": ["vocabulary", "features", "labels", "loss-function"],
            "shortDesc": "Master the essential terminology: samples, features, labels, weights, loss functions, objective functions, epochs, and batches.",
            "sections": {
                "whatItIs": "The vocabulary of Machine Learning establishes the formal mathematical language used to describe datasets, model topologies, and optimization procedures. Clear conceptual grounding in these terms prevents subtle implementation bugs and confusion when reading research papers and API documentation.",
                "problemItSolves": "Without standardized definitions, mathematical terms get conflated: people confuse parameters with hyperparameters, loss with cost, and validation sets with test sets. A rigorous taxonomy allows practitioners to communicate system constraints, training mechanics, and performance characteristics unambiguously.",
                "intuition": "Think of an ML system as an Olympic archer. A Sample is an individual arrow shot. Features are ambient environmental measurements (wind speed, target distance, bow tension). The Label is where the arrow hits the bullseye. The Loss Function measures how many centimeters off-center the arrow landed. The Weights are the muscle memories and arm angles the archer adjusts after each practice round (Epoch).",
                "howItWorks": "1. <strong>Samples & Features:</strong> A dataset consists of $N$ rows (samples) and $D$ columns (features), represented as matrix $\\mathbf{X} \\in \\mathbb{R}^{N \\times D}$.<br>2. <strong>Target / Label:</strong> The ground truth vector $\\mathbf{y} \\in \\mathbb{R}^N$ for supervised tasks.<br>3. <strong>Parameters (Weights & Biases):</strong> Internal variables learned by the optimizer.<br>4. <strong>Hyperparameters:</strong> External configuration choices set before training.<br>5. <strong>Batches & Epochs:</strong> A batch is a subset processed in one step; an epoch is a complete sweep over the entire dataset.",
                "mathematics": "Dataset matrix and target vector:<br>$$\\mathbf{X} = \\begin{bmatrix} x_{1,1} & \\cdots & x_{1,D} \\\\ \\vdots & \\ddots & \\vdots \\\\ x_{N,1} & \\cdots & x_{N,D} \\end{bmatrix}, \\quad \\mathbf{y} = \\begin{bmatrix} y_1 \\\\ \\vdots \\\\ y_N \\end{bmatrix}$$<br>Sample loss vs. Dataset cost:<br>$$\\ell_i = \\mathcal{L}(\\hat{y}^{(i)}, y^{(i)}), \\qquad J(\\mathbf{w}, b) = \\frac{1}{N} \\sum_{i=1}^N \\ell_i$$",
                "dataRequirements": "Tabular representations require features to be encoded numerically. Categorical variables must be one-hot encoded or embedded, continuous features scaled, and missing values imputed before computing distance metrics or matrix multiplications.",
                "hyperparameters": [
                    {"name": "Batch Size (B)", "description": "Number of training examples evaluated in a single step of stochastic optimization.", "effect": "Smaller batches introduce gradient noise that can escape shallow local minima; larger batches allow high hardware parallelism."},
                    {"name": "Number of Epochs (E)", "description": "Total full sweeps through the entire training dataset.", "effect": "Too few epochs causes underfitting; too many leads to memorization of training noise (overfitting)."}
                ],
                "strengths": [
                    "Unifies linear algebra, calculus, probability, and software engineering under a consistent framework.",
                    "Allows translation of abstract business problems into concrete mathematical objectives.",
                    "Provides exact diagnostics for debugging model convergence issues."
                ],
                "limitations": [
                    "Terminology varies slightly between mathematical statistics (covariates, estimators) and computer science (features, models).",
                    "Assumes datasets can be structured into discrete independent and identically distributed (i.i.d.) observations."
                ],
                "evaluation": "Vocabulary proficiency is tested through conceptual clarity: differentiating between parameters (e.g. weights $w$) and hyperparameters (e.g. learning rate $\\eta$), and verifying that loss and evaluation metrics match the task.",
                "workedExample": "Predicting real estate prices: A single house is a Sample. Its square footage, number of bedrooms, and postal code are Features. The actual sale price is the Label. The model predicts price $\\hat{y} = w_1 \\cdot (\\text{sqft}) + w_2 \\cdot (\\text{beds}) + b$. The difference $(\\hat{y} - y)^2$ is the squared error Loss. The learning rate is a Hyperparameter.",
                "whenToUse": "Apply standard ML terminology whenever structuring machine learning repositories, defining schema files, discussing system requirements, or writing technical research documentation.",
                "commonMistakes": [
                    "Confusing parameters (learned by optimizer) with hyperparameters (chosen by engineer).",
                    "Using the terms loss function (per sample) and cost function (aggregated over dataset) interchangeably.",
                    "Treating IDs or sequential row counters as predictive features."
                ],
                "furtherLearning": [
                    {"title": "Google Machine Learning Glossary", "url": "https://developers.google.com/machine-learning/glossary"},
                    {"title": "Andrew Ng - Machine Learning Yearning", "url": "https://www.deeplearning.ai/program/machine-learning-yearning/"}
                ]
            },
            "quiz": [
                {
                    "question": "Which of the following is a HYPERPARAMETER rather than an internal MODEL PARAMETER?",
                    "options": [
                        "The weight connecting neuron 1 to neuron 2 in layer 1.",
                        "The bias term $b$ in a linear regression equation.",
                        "The learning rate $\\alpha$ used during gradient descent.",
                        "The split threshold learned at the root of a decision tree."
                    ],
                    "correct": 2,
                    "explanation": "The learning rate $\\alpha$ is chosen by the engineer before training and dictates the optimizer's step size. Weights, biases, and tree split thresholds are model parameters learned directly from data."
                },
                {
                    "question": "What is an 'Epoch' in the context of neural network training?",
                    "options": [
                        "A single forward pass of a single mini-batch.",
                        "One full pass of the optimization algorithm through the entire training dataset.",
                        "The time it takes for a GPU to initialize memory.",
                        "A single update to a single weight parameter."
                    ],
                    "correct": 1,
                    "explanation": "An epoch is completed when the training algorithm has traversed every sample in the training dataset exactly once."
                },
                {
                    "question": "In a supervised dataset represented as matrix $\\mathbf{X}$ with shape $(1000, 20)$ and vector $\\mathbf{y}$ with shape $(1000)$, what do the numbers represent?",
                    "options": [
                        "20 samples, 1000 features, and 1000 models.",
                        "1000 samples, 20 features per sample, and 1000 ground truth labels.",
                        "1000 epochs, 20 batches, and 1000 loss values.",
                        "1000 classes, 20 layers, and 1000 test predictions."
                    ],
                    "correct": 1,
                    "explanation": "In standard notation, rows correspond to individual observations (1000 samples) and columns correspond to attributes (20 features), with a corresponding target label vector of length 1000."
                }
            ]
        },
        {
            "id": "F03",
            "title": "Train, Validation & Test Splits",
            "module": "foundations",
            "level": "beginner",
            "prerequisites": ["F01", "F02"],
            "estimatedMinutes": 20,
            "tags": ["data-splitting", "cross-validation", "data-leakage", "evaluation"],
            "shortDesc": "Learn how to divide datasets properly, prevent data leakage, and validate model generalizability using holdouts and k-fold cross-validation.",
            "sections": {
                "whatItIs": "Data splitting is the practice of partitioning available data into distinct subsets: a Training Set (for fitting weights), a Validation Set (for hyperparameter tuning and model selection), and a Test Set (quarantined until the very end to estimate real-world generalization error).",
                "problemItSolves": "If a model is evaluated on the exact same data it trained on, it can achieve 100% accuracy simply by memorizing noise and idiosyncrasies (overfitting). Splitting guarantees that we assess whether the model learned generalizable mathematical relationships or merely memorized the training examples.",
                "intuition": "Consider preparing for a medical board exam. The Training Set corresponds to textbook chapters and practice quizzes with answers shown in the back. The Validation Set is a mock exam you take to decide if you need to study neurology more or change your revision schedule. The Test Set is the sealed official state exam you take once: if you had seen those exact questions beforehand, your score would be an illusion.",
                "howItWorks": "1. <strong>Shuffle & Stratify:</strong> Ensure classes or target distributions are uniformly preserved across all splits.<br>2. <strong>Holdout Split:</strong> Typically allocate 70% Train, 15% Validation, 15% Test.<br>3. <strong>Fit Preprocessors on Train Only:</strong> Scalers, imputers, and encoders must be computed strictly on the training partition.<br>4. <strong>K-Fold Cross-Validation:</strong> For smaller datasets, split training data into $K$ equal folds, iteratively training on $K-1$ folds and evaluating on the held-out fold.",
                "mathematics": "$$\\mathcal{D}_{\\text{train}} \\cap \\mathcal{D}_{\\text{val}} = \\emptyset, \\quad \\mathcal{D}_{\\text{train}} \\cap \\mathcal{D}_{\\text{test}} = \\emptyset, \\quad \\mathcal{D}_{\\text{val}} \\cap \\mathcal{D}_{\\text{test}} = \\emptyset$$<br>K-Fold CV Score:<br>$$\\text{CV}_K = \\frac{1}{K} \\sum_{k=1}^K \\mathcal{S}\\left(f_{\\theta_{-k}}, \\mathcal{D}_k\\right)$$",
                "dataRequirements": "Requires samples to be independently drawn from the true operational distribution. For temporal or financial time series, random shuffling must NEVER be used; time-based forward-chaining splits are strictly required.",
                "hyperparameters": [
                    {"name": "Split Ratios (Train/Val/Test)", "description": "Proportional allotment of raw data to each subset (e.g. 70/15/15).", "effect": "Larger training sets improve parameter estimation; larger test sets decrease variance in our performance estimates."},
                    {"name": "Number of Folds (K)", "description": "Number of cross-validation partitions (standard is 5 or 10).", "effect": "Higher K reduces evaluation bias but increases computation time by a factor of K."},
                    {"name": "Stratification", "description": "Whether to force each fold to contain the same class proportions as the total dataset.", "effect": "Prevents rare classes from vanishing entirely from validation folds."}
                ],
                "strengths": [
                    "Prevents self-deception and deployment failures caused by memorization.",
                    "Identifies data leakage early in development pipelines.",
                    "K-Fold cross-validation provides statistical confidence intervals around model accuracy."
                ],
                "limitations": [
                    "Reduces total data available for parameter optimization.",
                    "Standard random splits fail on grouped data (e.g., multiple scans from the same patient across splits)."
                ],
                "evaluation": "Monitor the divergence between training loss and validation loss over training iterations. If training loss continues dropping while validation loss reverses and climbs, overfitting has begun.",
                "workedExample": "A hospital builds a tumor classifier with 10,000 patient records (100 malignant, 9,900 benign). An unstratified split might put only 5 malignant samples in the test set. Stratified splitting guarantees the 1% positive rate is preserved in train (80 positives) and test (20 positives).",
                "whenToUse": "Mandatory in every machine learning project without exception. Never report accuracy without an independent, quarantined test evaluation.",
                "commonMistakes": [
                    "Data Leakage: Normalizing or imputing the entire dataset BEFORE splitting.",
                    "Tuning hyperparameters directly on the test set.",
                    "Using random train/test splits on time-series data."
                ],
                "furtherLearning": [
                    {"title": "Scikit-Learn Cross-Validation Guide", "url": "https://scikit-learn.org/stable/modules/cross_validation.html"},
                    {"title": "Fast.ai: Validation Sets Guide", "url": "https://www.fast.ai/posts/2017-11-13-validation-sets.html"}
                ]
            },
            "quiz": [
                {
                    "question": "Why must you NEVER normalize or scale your entire dataset before splitting it into train and test sets?",
                    "options": [
                        "It causes the computer's memory to overflow.",
                        "It causes data leakage, as statistics (mean, std) from the test set contaminate the training process.",
                        "Mathematical libraries like scikit-learn will throw a syntax error.",
                        "Normalization only works on test sets, not training sets."
                    ],
                    "correct": 1,
                    "explanation": "Computing the mean and variance across the whole dataset leaks information about the distribution of the test set into the model's preprocessing pipeline, leading to overly optimistic test performance."
                },
                {
                    "question": "What is the primary purpose of the VALIDATION set as opposed to the TEST set?",
                    "options": [
                        "The validation set is used to calculate final reported accuracy for investors.",
                        "The validation set is used to iteratively tune hyperparameters and choose between models without compromising the final test set.",
                        "The validation set trains the model weights via backpropagation.",
                        "The validation set is discarded and never evaluated."
                    ],
                    "correct": 1,
                    "explanation": "The validation set guides engineering decisions (e.g. tuning learning rates, selecting tree depth). The test set remains completely quarantined until all decisions are finalized to provide an honest, unbiased performance estimate."
                },
                {
                    "question": "When evaluating a stock price prediction model, which splitting strategy must you use?",
                    "options": [
                        "Standard uniform random split.",
                        "Stratified K-Fold random cross-validation.",
                        "Time-series temporal split (train on past, validate on subsequent period, test on latest period).",
                        "Leave-one-out cross-validation."
                    ],
                    "correct": 2,
                    "explanation": "Financial data is ordered chronologically. Shuffling randomly leaks future prices into the training set, creating impossible lookahead bias that collapses completely in live trading."
                }
            ]
        },
        {
            "id": "F04",
            "title": "Learning Paradigms: Supervised, Unsupervised & RL",
            "module": "foundations",
            "level": "beginner",
            "prerequisites": ["F01", "F02"],
            "estimatedMinutes": 20,
            "tags": ["paradigms", "supervised", "unsupervised", "reinforcement-learning", "self-supervised"],
            "shortDesc": "Distinguish between Supervised, Unsupervised, Self-Supervised, and Reinforcement Learning, understanding how feedback mechanisms drive learning.",
            "sections": {
                "whatItIs": "A learning paradigm defines the nature of the learning signal provided to an algorithm. In Supervised Learning, the system receives feature inputs paired with explicit ground-truth targets. In Unsupervised Learning, it seeks underlying structure or manifold geometry in unlabeled data. In Reinforcement Learning (RL), an active agent interacts with a dynamic environment, learning a policy to maximize cumulative scalar rewards.",
                "problemItSolves": "Not all real-world challenges offer clean teacher signals. Annotating 1,000,000 medical scans with ground-truth segmentations costs millions of dollars. Knowing the differences between paradigms allows engineers to select approaches matching their data availability and operational goals.",
                "intuition": "Supervised learning is like studying with a private tutor who marks every homework problem as right or wrong. Unsupervised learning is like exploring an unfamiliar city with no map, noticing which neighborhoods have similar architecture or bustling markets. Reinforcement learning is like learning to ride a bicycle: you steer, pedal, occasionally fall over (penalty), and stay upright (reward), gradually mastering balance through trial and error.",
                "howItWorks": "1. <strong>Supervised:</strong> Input $(x_i, y_i) \\to$ minimize distance $d(f(x_i), y_i)$.<br>2. <strong>Unsupervised:</strong> Input $x_i \\to$ discover clusters, compress dimensions, or model density $p(x)$.<br>3. <strong>Self-Supervised:</strong> Generate pseudo-labels from data (e.g., masking the next word in a sentence: 'The cat sat on the [MASK]').<br>4. <strong>Reinforcement Learning:</strong> Agent observes state $s_t$, executes action $a_t$, receives reward $r_t$, transitions to state $s_{t+1}$.",
                "mathematics": "Supervised Empirical Risk:<br>$$\\min_\\theta \\frac{1}{N} \\sum_{i=1}^N \\mathcal{L}(f_\\theta(x_i), y_i)$$<br>Unsupervised Density Estimation (Log-Likelihood):<br>$$\\max_\\theta \\sum_{i=1}^N \\log p_\\theta(x_i)$$<br>Reinforcement Learning Expected Return:<br>$$\\max_\\pi \\mathbb{E}_{\\tau \\sim \\pi} \\left[ \\sum_{t=0}^T \\gamma^t r(s_t, a_t) \\right]$$",
                "dataRequirements": "Supervised learning requires paired $(X, Y)$ sets where labeling noise is minimized. Unsupervised learning accepts raw $X$ matrices. Reinforcement learning requires a responsive simulator, game engine, or physical robotic feedback loop capable of thousands of iterative rollouts.",
                "hyperparameters": [
                    {"name": "Discount Factor (\\gamma)", "description": "In RL, discounts future rewards relative to immediate payoffs (between 0 and 1).", "effect": "Near 0 makes the agent myopic; near 1 prioritizes long-term strategic compounding."},
                    {"name": "Exploration Rate (\\epsilon)", "description": "Probability of selecting a random exploratory action versus exploiting the best known policy.", "effect": "Prevents getting trapped in suboptimal local strategies."}
                ],
                "strengths": [
                    "Supervised: Direct, highly accurate, straightforward to evaluate.",
                    "Unsupervised: Zero annotation expense; reveals latent patterns, clusters, and anomalies.",
                    "Self-Supervised: Enables pretraining foundational LLMs and vision models on raw internet-scale text and images.",
                    "RL: Capable of superhuman decision-making without requiring human demonstrations (e.g., AlphaGo)."
                ],
                "limitations": [
                    "Supervised: Labeling bottlenecks, high human annotation costs.",
                    "Unsupervised: Ambiguous evaluation metrics; hard to verify ground truth.",
                    "RL: Sample inefficient, unstable training dynamics, high simulation requirements."
                ],
                "evaluation": "Supervised models are verified via holdout accuracy and error metrics. Unsupervised models use silhouette scores, reconstruction loss, or ELBO. RL algorithms are evaluated on mean cumulative reward per episode across diverse random seeds.",
                "workedExample": "Consider autonomous driving: Predicting pedestrian bounding boxes from camera frames is Supervised. Clustering driving behaviors into aggressive vs. calm styles is Unsupervised. Pretraining the vision backbone to predict masked camera frames is Self-Supervised. Training the vehicle to smoothly merge onto a highway without colliding is Reinforcement Learning.",
                "whenToUse": "Use Supervised when clean historical labeled inputs and outputs exist. Use Unsupervised for customer segmentation or anomaly detection. Use Self-Supervised for pretraining feature encoders. Use RL for sequential decision problems with clear reward metrics.",
                "commonMistakes": [
                    "Attempting to solve an RL problem with supervised regression when sequential decisions alter future state transitions.",
                    "Assuming unsupervised clustering will automatically discover human-intended semantic classes without guidance."
                ],
                "furtherLearning": [
                    {"title": "Sutton & Barto: Reinforcement Learning: An Introduction", "url": "http://incompleteideas.net/book/the-book-2nd.html"},
                    {"title": "Yann LeCun: Self-Supervised Learning Talk", "url": "https://ai.meta.com/blog/self-supervised-learning-the-dark-matter-of-intelligence/"}
                ]
            },
            "quiz": [
                {
                    "question": "Which learning paradigm best describes training an algorithm to play Chess from scratch by awarding +1 for a win and -1 for a loss?",
                    "options": [
                        "Supervised Classification",
                        "Reinforcement Learning",
                        "Unsupervised Clustering",
                        "Linear Regression"
                    ],
                    "correct": 1,
                    "explanation": "The agent takes sequential actions (moves), receives delayed scalar rewards (+1 or -1 upon game completion), and updates its policy without move-by-move human labels. This is Reinforcement Learning."
                },
                {
                    "question": "Modern Large Language Models (like GPT-4 and Llama) are initially pretrained using which learning paradigm?",
                    "options": [
                        "Supervised manual classification by annotators.",
                        "Self-Supervised Learning (predicting the next token on vast text corpora).",
                        "Unsupervised K-Means clustering.",
                        "Pure genetic evolutionary algorithms."
                    ],
                    "correct": 1,
                    "explanation": "LLMs are primarily pretrained via self-supervised autoregressive next-token prediction, where the supervisory signal is automatically derived from the text itself."
                },
                {
                    "question": "An e-commerce company groups its customer base into 5 purchasing profiles without any predefined customer categories. This is:",
                    "options": [
                        "Supervised regression",
                        "Unsupervised clustering",
                        "Reinforcement learning",
                        "Binary classification"
                    ],
                    "correct": 1,
                    "explanation": "Because there are no ground-truth customer categories or labels provided, the algorithm discovers latent groupings based on feature similarity—the hallmark of unsupervised clustering."
                }
            ]
        },
        {
            "id": "F05",
            "title": "Task Types: Classification, Regression & Beyond",
            "module": "foundations",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "F04"],
            "estimatedMinutes": 20,
            "tags": ["classification", "regression", "ranking", "generation", "tasks"],
            "shortDesc": "Map real-world problems to fundamental ML tasks: binary, multi-class, multi-label classification, continuous regression, ranking, and generation.",
            "sections": {
                "whatItIs": "Machine learning problems are categorized by the mathematical structure of their target output space $\\mathcal{Y}$. Classification maps inputs to discrete category labels. Regression predicts continuous real-valued numbers. Specialized tasks include Ranking (ordering items by relevance), Multi-label Classification (assigning multiple non-exclusive tags), and Generation (producing new high-dimensional sequences, images, or audio).",
                "problemItSolves": "Framing a problem incorrectly leads to inappropriate loss functions, flawed evaluation metrics, and failing models. For example, framing a discrete 5-star rating as pure regression might predict 3.7 stars, while multi-class classification treats 1 star and 2 stars as equally distant as 1 star and 5 stars. Choosing the right task type ensures mathematical alignment with business goals.",
                "intuition": "Classification asks: 'What category does this belong to?' (Is this transaction fraudulent or legitimate?). Regression asks: 'How much / how many?' (What price will this home sell for?). Ranking asks: 'Which option is better than another?' (Search engine result ordering). Generation asks: 'Create something new that looks like existing examples.' (Writing a paragraph or synthesizing a portrait).",
                "howItWorks": "1. <strong>Binary Classification:</strong> Output $\\hat{y} \\in [0, 1]$ represents the probability of the positive class ($y \\in \\{0, 1\\}$).<br>2. <strong>Multi-Class Classification:</strong> Output is a probability distribution over $K$ mutually exclusive categories using a Softmax activation.<br>3. <strong>Multi-Label Classification:</strong> Output is a vector of $K$ independent probabilities via sigmoid activations.<br>4. <strong>Regression:</strong> Output $\\hat{y} \\in \\mathbb{R}$ is an unbounded real scalar.<br>5. <strong>Ranking:</strong> Optimize pairwise or listwise margins so that relevant items score higher than irrelevant ones.",
                "mathematics": "Binary Cross-Entropy Loss:<br>$$\\mathcal{L}_{\\text{BCE}} = -\\left[ y \\log(\\hat{y}) + (1 - y) \\log(1 - \\hat{y}) \\right]$$<br>Mean Squared Error (Regression):<br>$$\\mathcal{L}_{\\text{MSE}} = \\frac{1}{N} \\sum_{i=1}^N \\left( y^{(i)} - \\hat{y}^{(i)} \\right)^2$$<br>Categorical Cross-Entropy ($K$ classes):<br>$$\\mathcal{L}_{\\text{CCE}} = -\\sum_{k=1}^K y_k \\log(\\hat{y}_k)$$",
                "dataRequirements": "Classification requires balanced class representation or careful threshold adjustment for imbalanced datasets. Regression requires target variables free from extreme unclipped outliers that can distort squared-error gradients.",
                "hyperparameters": [
                    {"name": "Decision Threshold", "description": "Probability cutoff (default 0.5) to assign a sample to the positive class in binary classification.", "effect": "Lowering the threshold increases Recall at the expense of Precision; raising it increases Precision."},
                    {"name": "Loss Formulation", "description": "Choosing MSE vs MAE vs Huber loss for regression.", "effect": "MAE is robust to outliers; MSE penalizes large errors heavily; Huber balances both."}
                ],
                "strengths": [
                    "Clear taxonomy allows standard, battle-tested loss functions to be applied off the shelf.",
                    "Enables standardized evaluation metrics across competing algorithms."
                ],
                "limitations": [
                    "Boundary cases: Ordinal regression (e.g. disease severity stages 1-4) doesn't cleanly fit standard classification or linear regression.",
                    "Multi-modal continuous outputs: When multiple distinct continuous targets are valid for the same input."
                ],
                "evaluation": "Classification uses Confusion Matrix, Precision, Recall, F1-Score, and ROC-AUC. Regression uses RMSE, MAE, MAPE, and $R^2$. Ranking uses NDCG (Normalized Discounted Cumulative Gain) and Mean Reciprocal Rank (MRR).",
                "workedExample": "Predicting hospital stay duration: If modeled as regression, the model outputs $\\hat{y} = 4.2$ days, minimizing mean squared error. If modeled as classification, the target is binned into categories ('<24 hours', '1-3 days', '>3 days') using categorical cross-entropy, predicting probabilities for each tier.",
                "whenToUse": "Determine the task type at the very start of any ML engagement based on how stakeholders will consume the predictions.",
                "commonMistakes": [
                    "Treating an ordinal ranking problem (e.g. ranking credit risk tiers) as an unordered multi-class classification problem.",
                    "Using Mean Squared Error to evaluate classification probabilities.",
                    "Failing to calibrate classification probabilities before using them as risk percentages."
                ],
                "furtherLearning": [
                    {"title": "Classification vs Regression - Google Developers", "url": "https://developers.google.com/machine-learning/crash-course/classification"},
                    {"title": "Introduction to Information Retrieval: Ranking", "url": "https://nlp.stanford.edu/IR-book/"}
                ]
            },
            "quiz": [
                {
                    "question": "A photo tagging model must identify all concepts present in an image (e.g., 'dog', 'park', 'frisbee', 'sunny'). A photo can have any combination of these tags. What task is this?",
                    "options": [
                        "Binary Classification",
                        "Multi-Class Classification",
                        "Multi-Label Classification",
                        "Continuous Regression"
                    ],
                    "correct": 2,
                    "explanation": "Because the classes are not mutually exclusive—an image can contain zero, one, or multiple tags simultaneously—this is Multi-Label Classification."
                },
                {
                    "question": "Which evaluation metric is appropriate for a REGRESSION problem?",
                    "options": [
                        "ROC-AUC",
                        "Root Mean Squared Error (RMSE)",
                        "F1-Score",
                        "Confusion Matrix"
                    ],
                    "correct": 1,
                    "explanation": "RMSE measures the average Euclidean magnitude of differences between continuous predictions and continuous targets. ROC-AUC, F1-Score, and Confusion Matrices are classification metrics."
                },
                {
                    "question": "If a medical diagnostic model predicts probability $P(\\text{Disease}) = 0.35$, but the cost of missing a sick patient is catastrophic, what should the engineer adjust?",
                    "options": [
                        "Lower the classification decision threshold below 0.5 (e.g., to 0.2) to prioritize Recall.",
                        "Switch the task to continuous regression.",
                        "Increase the decision threshold to 0.9.",
                        "Discard the test set."
                    ],
                    "correct": 0,
                    "explanation": "Lowering the classification threshold from 0.5 to 0.2 flags more positive candidates, trading lower precision for significantly higher recall—essential when false negatives carry severe consequences."
                }
            ]
        },
        {
            "id": "F06",
            "title": "Overfitting, Underfitting & Bias-Variance Tradeoff",
            "module": "foundations",
            "level": "intermediate",
            "prerequisites": ["F01", "F02", "F03"],
            "estimatedMinutes": 25,
            "tags": ["bias-variance", "overfitting", "underfitting", "regularization", "generalization"],
            "shortDesc": "Understand the fundamental tradeoff in machine learning: balancing model complexity to avoid both underfitting (high bias) and overfitting (high variance).",
            "sections": {
                "whatItIs": "The Bias-Variance Tradeoff is the fundamental theoretical constraint governing supervised machine learning generalization. Bias is error stemming from erroneous or overly simplistic assumptions in the learning algorithm (leading to underfitting). Variance is error stemming from sensitivity to small fluctuations and random noise in the training set (leading to overfitting). Generalization error decomposes into the sum of Bias squared, Variance, and irreducible noise.",
                "problemItSolves": "Explains why simply making a model larger, deeper, or more expressive does not automatically produce better predictions on unseen real-world data. It provides the diagnostic framework needed to systematically balance capacity and regularization.",
                "intuition": "Imagine studying for a biology exam. Underfitting (High Bias): You only memorize the phrase 'mitochondria is the powerhouse of the cell.' Any detailed question leaves you guessing because your model is too simplistic. Overfitting (High Variance): You memorize the exact font color, page numbers, and coffee stains of your textbook. If the exam changes the wording slightly, you fail. Good Fit: You understand the underlying biological concepts and apply them flexibly to new questions.",
                "howItWorks": "1. <strong>Underfitting (High Bias):</strong> The model has insufficient capacity. Both training error and validation error remain unacceptably high.<br>2. <strong>Overfitting (High Variance):</strong> Model capacity is too high. Training error drops toward zero, while validation error diverges upward.<br>3. <strong>Sweet Spot:</strong> Model capacity balances bias and variance, minimizing total expected generalization error on unseen test data.<br>4. <strong>Modern Deep Learning Twist (Double Descent):</strong> Very large overparameterized deep models can enter an interpolation regime where validation error drops again with extreme capacity, provided proper inductive biases exist.",
                "mathematics": "For an estimator $\\hat{f}(x)$ predicting $y = f(x) + \\epsilon$ with $\\mathbb{E}[\\epsilon] = 0$ and $\\text{Var}(\\epsilon) = \\sigma^2$:<br>$$\\mathbb{E}\\left[ (y - \\hat{f}(x))^2 \\right] = \\underbrace{\\left( \\mathbb{E}[\\hat{f}(x)] - f(x) \\right)^2}_{\\text{Bias}^2} + \\underbrace{\\mathbb{E}\\left[ (\\hat{f}(x) - \\mathbb{E}[\\hat{f}(x)])^2 \\right]}_{\\text{Variance}} + \\underbrace{\\sigma^2}_{\\text{Irreducible Noise}}$$",
                "dataRequirements": "Adding more representative training data is the most reliable way to reduce variance without increasing bias. High bias must be resolved by choosing a more expressive model or engineering informative features.",
                "hyperparameters": [
                    {"name": "Regularization Weight (\\lambda)", "description": "Penalizes large parameter values ($L_1$ Lasso or $L_2$ Ridge).", "effect": "Increases bias slightly while substantially dampening variance, helping prevent overfitting."},
                    {"name": "Polynomial Degree / Tree Depth", "description": "Controls the maximum non-linear degrees of freedom of the hypothesis class.", "effect": "Higher values lower bias but rapidly inflate variance."}
                ],
                "strengths": [
                    "Provides a principled mathematical explanation for prediction errors.",
                    "Directly dictates whether a project needs more data, stronger regularization, or a more expressive model."
                ],
                "limitations": [
                    "Irreducible noise $\\sigma^2$ cannot be eliminated by any modeling technique (represents inherent measurement entropy).",
                    "Classical bias-variance curves do not fully explain modern deep learning 'double descent' phenomena without extended overparameterization theory."
                ],
                "evaluation": "Diagnose by plotting Learning Curves (Train Loss and Validation Loss versus Training Set Size or Training Epochs). A widening gap indicates high variance; high flat curves indicate high bias.",
                "workedExample": "Fitting a 15th-degree polynomial to 10 noisy data points generated from a simple sine wave. The 15th-degree polynomial passes perfectly through all 10 training points ($R^2 = 1.0$), but oscillates wildly between them, yielding catastrophic test error. A 3rd-degree polynomial captures the wave smoothly and generalizes well.",
                "whenToUse": "Use this diagnostic framework whenever your model performs poorly or exhibits discrepancies between training and validation environments.",
                "commonMistakes": [
                    "Adding more training data to fix high bias (more data only helps when you have high variance; high bias requires higher model capacity).",
                    "Blaming the dataset for poor performance when the model family is simply too rigid to represent the underlying patterns.",
                    "Ignoring irreducible error and endlessly chasing zero validation loss on inherently noisy real-world data."
                ],
                "furtherLearning": [
                    {"title": "Scott Fortmann-Roe: Understanding the Bias-Variance Tradeoff", "url": "http://scott.fortmann-roe.com/docs/BiasVariance.html"},
                    {"title": "Nakkiran et al.: Deep Double Descent", "url": "https://openai.com/research/deep-double-descent"}
                ]
            },
            "quiz": [
                {
                    "question": "Your deep neural network achieves 99.8% accuracy on the training set, but only 64.2% on the validation set. What problem are you facing, and what is the proper fix?",
                    "options": [
                        "High Bias (underfitting); increase network depth and train for more epochs.",
                        "High Variance (overfitting); apply dropout, increase regularization, or gather more training data.",
                        "Irreducible error; nothing can be done.",
                        "High Bias; decrease regularization strength."
                    ],
                    "correct": 1,
                    "explanation": "A massive gap between near-perfect training accuracy and poor validation accuracy is the definition of high variance (overfitting). You address it with regularization, dropout, data augmentation, or more training samples."
                },
                {
                    "question": "What comprises the theoretical minimum expected prediction error that no model, regardless of complexity, can surpass?",
                    "options": [
                        "Bias squared",
                        "Variance",
                        "Irreducible error $\\sigma^2$ caused by noise in the data-generating process",
                        "Zero (a perfect model always achieves zero error)"
                    ],
                    "correct": 2,
                    "explanation": "Irreducible error $\\sigma^2$ reflects inherent noise, missing unmeasured variables, and stochasticity in the real-world generation process that no model can eliminate."
                },
                {
                    "question": "If a linear model has high bias (underfitting) on a complex non-linear dataset, what will happen if you double the training dataset size?",
                    "options": [
                        "The training and validation error will drop to zero.",
                        "The model will still underfit because a linear hypothesis class cannot capture non-linear curvature regardless of dataset volume.",
                        "The model will immediately overfit.",
                        "The variance will increase exponentially."
                    ],
                    "correct": 1,
                    "explanation": "Adding more data reduces variance, but does not fix high bias. If a model is fundamentally incapable of representing non-linear patterns, feeding it more data will not make it learn them."
                }
            ]
        },
        {
            "id": "F07",
            "title": "Algorithm vs Model vs Architecture",
            "module": "foundations",
            "level": "beginner",
            "prerequisites": ["F01", "F02"],
            "estimatedMinutes": 15,
            "tags": ["architecture", "models", "algorithms", "engineering"],
            "shortDesc": "Disentangle the subtle distinctions between learning algorithms, model architectures, trained model artifacts, and inference engines.",
            "sections": {
                "whatItIs": "In software and data engineering, the terms Algorithm, Architecture, and Model are often used loosely. An Algorithm is the computational procedure for learning (e.g. Backpropagation, Stochastic Gradient Descent). An Architecture is the structural blueprint or graph topology of the system (e.g. ResNet-50, Transformer). A Model is the specific artifact: an architecture instantiated with concrete learned numerical parameters (weights $\\theta$).",
                "problemItSolves": "Eliminates architectural confusion during deployment, serialization, and version control. Knowing whether a team needs to retrain an existing model, swap an optimization algorithm, or design a new architecture is essential for accurate project scoping.",
                "intuition": "Think of constructing a skyscraper. The Architecture is the architectural blueprint detailing where the pillars, elevators, and beams go. The Algorithm is the construction crew, cranes, and protocols used to pour concrete and weld steel. The Trained Model is the completed, standing skyscraper with solid concrete and furnished offices ready for tenants.",
                "howItWorks": "1. <strong>Design Architecture:</strong> Define the mathematical computation graph $f_\\theta(x)$.<br>2. <strong>Select Algorithm:</strong> Choose an optimizer to solve the objective function (e.g., AdamW with cosine annealing schedule).<br>3. <strong>Execute Training:</strong> Run the algorithm over the dataset to optimize parameters $\\theta^*$.<br>4. <strong>Serialize Trained Model:</strong> Save learned weights and graph metadata for low-latency inference.",
                "mathematics": "$$\\underbrace{f_\\theta(\\cdot)}_{\\text{Architecture Blueprint}} \\quad \\xrightarrow[\\text{Optimizer Algorithm } \\mathcal{A}(\\mathcal{D})]{\\text{Training Process}} \\quad \\underbrace{f_{\\theta^*}(\\cdot)}_{\\text{Trained Model Artifact}}$$<br>where $\\theta^* = \\mathcal{A}(\\mathcal{D}, f_\\theta)$ represents the frozen weights after optimization.",
                "dataRequirements": "Architectures dictate memory and compute hardware constraints (RAM, VRAM, FLOPS). Algorithms dictate training time and stability. Datasets populate the parameters.",
                "hyperparameters": [
                    {"name": "Layer Width / Depth", "description": "Architectural hyperparameters defining structural dimensions.", "effect": "Directly determines theoretical capacity and inference latency."},
                    {"name": "Optimizer Momentum (\\beta)", "description": "Algorithmic hyperparameter governing parameter trajectory updates.", "effect": "Dampens oscillations and speeds traversal through flat ravines."}
                ],
                "strengths": [
                    "Allows modular decoupling: you can use the same algorithm (e.g. AdamW) to train vastly different architectures (CNNs, Transformers, GNNs).",
                    "Enables model sharing via checkpoints without needing to distribute proprietary training datasets."
                ],
                "limitations": [
                    "A superior architecture will still fail if paired with an unsuitable learning algorithm or corrupt dataset.",
                    "Serialized model formats can introduce dependency incompatibilities across hardware and framework versions."
                ],
                "evaluation": "Measure training efficiency (FLOPS and wall-clock time required by the algorithm) versus inference efficiency (latency and memory footprint of the trained model artifact).",
                "workedExample": "Consider Llama-3: The Architecture is a decoder-only Transformer with RoPE embeddings and SwiGLU activations. The Algorithm was AdamW with cross-entropy loss and cosine learning rate decay run over 15 trillion tokens. The Model is the resulting 8-billion float16 weights checkpoint file saved to disk.",
                "whenToUse": "Keep these distinctions clear when structuring CI/CD pipelines, model registries (e.g., MLflow, Hugging Face Hub), and technical documentation.",
                "commonMistakes": [
                    "Saying 'I am training a new algorithm' when you are actually training an existing architecture with a standard optimization algorithm on a new dataset.",
                    "Shipping training source code to production servers instead of compiled, quantized model artifacts."
                ],
                "furtherLearning": [
                    {"title": "MLOps: Model Management and Versioning - Martin Fowler", "url": "https://martinfowler.com/articles/cd4ml.html"},
                    {"title": "Hugging Face Model Hub Architecture Docs", "url": "https://huggingface.co/docs/transformers/index"}
                ]
            },
            "quiz": [
                {
                    "question": "When you download a 4 GB `.safetensors` checkpoint file from Hugging Face, what have you obtained?",
                    "options": [
                        "An optimization algorithm.",
                        "A trained model artifact containing specific learned weight parameters.",
                        "A training dataset.",
                        "A compiler."
                    ],
                    "correct": 1,
                    "explanation": "A checkpoint file contains the concrete learned numerical weights and parameters—the trained model artifact ready for evaluation or inference."
                },
                {
                    "question": "In the phrase 'We trained a Convolutional Neural Network using AdamW', what are 'CNN' and 'AdamW' respectively?",
                    "options": [
                        "CNN is the algorithm; AdamW is the architecture.",
                        "CNN is the model architecture; AdamW is the optimization algorithm.",
                        "Both are training algorithms.",
                        "Both are model checkpoints."
                    ],
                    "correct": 1,
                    "explanation": "CNN defines the structural computation graph (the architecture), while AdamW is the mathematical optimization procedure used to update its parameters (the algorithm)."
                },
                {
                    "question": "Why is it important to decouple model architecture from training code in production deployment?",
                    "options": [
                        "Because production inference only needs the frozen weights and computation graph, not gradient history or optimizer states.",
                        "Because architectures cannot run on CPUs.",
                        "Because training algorithms are strictly proprietary and cannot be compiled.",
                        "It is not important; production systems always run full backpropagation on every query."
                    ],
                    "correct": 0,
                    "explanation": "Inference requires only forward-pass evaluation of the trained weights. Decoupling strips out optimizer memory, gradient tracking, and training baggage, delivering faster execution and a smaller footprint."
                }
            ]
        }
    ]
print("Foundations module defined: 7 lessons")

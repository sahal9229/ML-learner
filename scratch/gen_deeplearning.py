# -*- coding: utf-8 -*-
"""
Module 3: Deep Learning (D01 - D16)
16 complete lessons with all 15 sections, LaTeX mathematics, hyperparameters, and 3-question quizzes.
"""

def get_deeplearning():
    return [
        {
            "id": "D01",
            "title": "Neurons, Layers & Activation Functions",
            "module": "deeplearning",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "S12", "S13"],
            "estimatedMinutes": 20,
            "tags": ["deep-learning", "neurons", "activations", "relu", "sigmoid", "gelu"],
            "shortDesc": "The anatomical building blocks of deep neural networks: artificial neurons, stacked layers, affine transformations, and non-linear activations.",
            "sections": {
                "whatItIs": "An artificial neuron is the core computational unit of deep learning. It receives multiple scalar inputs, computes a weighted sum offset by a bias, and passes the result through a non-linear activation function. Neurons are organized into sequential tensor layers (input, hidden, output) where depth represents compositional feature abstraction.",
                "problemItSolves": "Linear algebra alone ($W_2 W_1 x$) collapses into a single linear matrix. Non-linear activation functions bend Euclidean space, enabling deep neural networks to learn intricate, highly curved decision boundaries and complex multi-modal functions.",
                "intuition": "Think of a sound engineering mixing console. Each fader knob is a weight multiplying a musical instrument's volume. All tracks are summed together with an ambient baseline noise level (bias). The master audio limiter (activation function) prevents distortion, clipping quiet sounds or saturating loud peaks before sending the music to speakers.",
                "howItWorks": "1. <strong>Linear Affine Transformation:</strong> $z = \\sum_{j=1}^D w_j x_j + b = \\mathbf{w}^T \\mathbf{x} + b$.<br>2. <strong>Non-linear Activation:</strong> $a = g(z)$, where $g(\\cdot)$ is a non-linear mapping.<br>3. <strong>Layer Stacking:</strong> Outputs of layer $l-1$ serve as inputs to layer $l$: $\\mathbf{a}^{(l)} = g\\left( \\mathbf{W}^{(l)} \\mathbf{a}^{(l-1)} + \\mathbf{b}^{(l)} \\right)$.<br>4. <strong>Common Activations:</strong> ReLU ($max(0, z)$), LeakyReLU, GELU (standard in Transformers), Sigmoid, and Tanh.",
                "mathematics": "Activation Functions and their Derivatives:<br>$$\\text{ReLU}(z) = \\max(0, z), \\quad \\text{ReLU}'(z) = \\begin{cases} 1 & z > 0 \\\\ 0 & z < 0 \\end{cases}$$<br>$$\\text{GELU}(z) = z \\cdot \\Phi(z) = z \\cdot P(X \\le z) \\approx 0.5z \\left( 1 + \\tanh\\left(\\sqrt{2/\\pi}(z + 0.044715 z^3)\\right) \\right)$$<br>$$\\text{Softmax}(\\mathbf{z})_i = \\frac{e^{z_i}}{\\sum_{k=1}^K e^{z_k}}$$",
                "dataRequirements": "Normalized continuous tensors. Weights must be initialized using variance-scaling schemes (He initialization for ReLU; Xavier/Glorot for Tanh/Sigmoid) to prevent exploding or vanishing signal variances across deep layers.",
                "hyperparameters": [
                    {"name": "Activation Function Type", "description": "ReLU, LeakyReLU, GELU, SwiGLU, Tanh.", "effect": "GELU and SwiGLU are standard for modern LLMs; ReLU is default for CNNs and MLPs."},
                    {"name": "Layer Width", "description": "Number of parallel neurons in a layer.", "effect": "Determines the dimensionality of the intermediate latent representation."},
                    {"name": "Weight Initialization", "description": "He (Kaiming) vs Xavier (Glorot) normal/uniform distribution.", "effect": "Preserves activation variance across deep stacks."}
                ],
                "strengths": [
                    "Modular and composable: layers can be stacked arbitrarily deep.",
                    "Universal function approximation when paired with non-linear activations.",
                    "Vectorized execution scales efficiently on GPU/TPU tensor cores."
                ],
                "limitations": [
                    "Dying ReLU problem: neurons with negative pre-activations receive zero gradients and permanently deactivate.",
                    "Saturating activations (Sigmoid, Tanh) cause severe vanishing gradients in networks deeper than a few layers."
                ],
                "evaluation": "Evaluated by monitoring activation distributions (mean, variance, dead neuron fraction) using TensorBoard or Weights & Biases.",
                "workedExample": "A neuron with inputs $x = [2.0, -1.0]$, weights $w = [0.5, 3.0]$, and bias $b = 1.0$. Pre-activation: $z = (2.0 \\times 0.5) + (-1.0 \\times 3.0) + 1.0 = 1.0 - 3.0 + 1.0 = -1.0$. If using ReLU, output $a = \\max(0, -1.0) = 0.0$. If using Sigmoid, output $a = 1 / (1 + e^1) = 0.269$.",
                "whenToUse": "The fundamental foundation for every deep neural network architecture.",
                "commonMistakes": [
                    "Using Sigmoid activations in deep hidden layers (causes vanishing gradients; reserve Sigmoid for binary output layers).",
                    "Using Xavier initialization with ReLU activations (leads to signal variance decaying by half at every layer; use He initialization).",
                    "Ignoring dying ReLU neurons when learning rates are set too high."
                ],
                "furtherLearning": [
                    {"title": "Glorot & Bengio: Understanding the difficulty of training deep feedforward neural networks (AISTATS 2010)", "url": "https://proceedings.mlr.press/v9/glorot10a.html"},
                    {"title": "He et al.: Delving Deep into Rectifiers (He Init Paper 2015)", "url": "https://arxiv.org/abs/1502.01852"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the 'Dying ReLU' problem in deep neural networks?",
                    "options": [
                        "Neurons catch fire due to excessive GPU heat.",
                        "When a neuron's pre-activation $z$ remains persistently negative, its gradient is strictly 0, preventing optimizer updates and causing the neuron to remain permanently inactive.",
                        "The loss function drops to negative infinity.",
                        "Weights become non-numerical NaN values."
                    ],
                    "correct": 1,
                    "explanation": "Because the derivative of ReLU is 0 for all $z < 0$, a neuron that outputs negative values receives zero backpropagated gradient, rendering it permanently dead to future gradient updates."
                },
                {
                    "question": "Which weight initialization scheme is mathematically tailored specifically for ReLU activation functions?",
                    "options": [
                        "Zero Initialization (all weights = 0)",
                        "He (Kaiming) Initialization ($Var(W) = 2/n_{in}$)",
                        "Glorot / Xavier Initialization ($Var(W) = 2/(n_{in} + n_{out})$)",
                        "Uniform random between -100 and +100"
                    ],
                    "correct": 1,
                    "explanation": "Because ReLU zeroes out half of all activations on average, He initialization scales variance by $2/n_{in}$ to compensate for the lost signal energy."
                },
                {
                    "question": "Which activation function is most widely used in modern Transformer LLMs like GPT-3, BERT, and LLaMA?",
                    "options": [
                        "Step function",
                        "GELU (Gaussian Error Linear Unit) or SwiGLU",
                        "Sigmoid",
                        "Linear pass-through"
                    ],
                    "correct": 1,
                    "explanation": "GELU and SwiGLU weight inputs by their continuous probability under a Gaussian cumulative distribution, providing smoother gradients that enhance Transformer training dynamics."
                }
            ]
        },
        {
            "id": "D02",
            "title": "Forward & Backpropagation",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["D01"],
            "estimatedMinutes": 25,
            "tags": ["backpropagation", "autodiff", "chain-rule", "computation-graph", "gradients"],
            "shortDesc": "Trace data through the forward computation graph and backpropagate error derivatives via the multivariate chain rule.",
            "sections": {
                "whatItIs": "Forward propagation evaluates a neural network's computation graph from inputs to output loss. Backpropagation (Reverse-Mode Automatic Differentiation) computes the analytical gradient of that scalar loss with respect to every internal weight and bias by systematically traversing the graph in reverse using the calculus chain rule.",
                "problemItSolves": "A modern neural network can have billions of parameters. Computing numerical finite-difference gradients $(\\frac{f(w+\\epsilon) - f(w)}{\\epsilon})$ would require billions of forward passes per training step (taking weeks). Backpropagation computes the exact gradients for ALL parameters simultaneously in a single backward pass.",
                "intuition": "Imagine a bucket brigade of 10 people passing water uphill to put out a fire. The forward pass is pouring the water buckets up the line to see how much water reaches the flames. The backward pass is the firefighter yelling back down the line: 'Person 10 spilled 20% of their bucket, Person 9 tilted too fast, Person 8 hesitated!' Every person receives their specific feedback score simultaneously based on how their actions contributed to the final shortfall.",
                "howItWorks": "1. <strong>Forward Pass:</strong> Compute intermediate activations $\\mathbf{z}^{(l)}$ and $\\mathbf{a}^{(l)}$ and store them in an activation cache.<br>2. <strong>Loss Evaluation:</strong> Calculate scalar loss $\\mathcal{L}(\\hat{y}, y)$.<br>3. <strong>Output Gradient:</strong> Compute error derivative at the output layer $\\boldsymbol{\\delta}^{(L)} = \\nabla_{\\mathbf{a}^{(L)}} \\mathcal{L} \\odot g'(\\mathbf{z}^{(L)})$.<br>4. <strong>Recursive Chain Rule:</strong> Backpropagate error signals: $\\boldsymbol{\\delta}^{(l)} = \\left( (\\mathbf{W}^{(l+1)})^T \\boldsymbol{\\delta}^{(l+1)} \\right) \\odot g'(\\mathbf{z}^{(l)})$.<br>5. <strong>Weight Gradients:</strong> Accumulate parameter gradients $\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{W}^{(l)}} = \\boldsymbol{\\delta}^{(l)} (\\mathbf{a}^{(l-1)})^T$ and $\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{b}^{(l)}} = \\boldsymbol{\\delta}^{(l)}$.",
                "mathematics": "Multivariate Chain Rule for node $z$ affecting output $\\mathcal{L}$ through children $\\{y_1, \\dots, y_k\\}$:<br>$$\\frac{\\partial \\mathcal{L}}{\\partial z} = \\sum_{i=1}^k \\frac{\\partial \\mathcal{L}}{\\partial y_i} \\frac{\\partial y_i}{\\partial z}$$<br>Matrix Calculus Vectorized Gradients for layer $l$:<br>$$\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{W}^{(l)}} = \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{z}^{(l)}} (\\mathbf{a}^{(l-1)})^T, \\qquad \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{b}^{(l)}} = \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{z}^{(l)}}$$<br>$$\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{a}^{(l-1)}} = (\\mathbf{W}^{(l)})^T \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{z}^{(l)}}$$",
                "dataRequirements": "Continuous differentiable operators. Every operation in the computation graph must have a defined Jacobian-vector product (JVP) or vector-Jacobian product (VJP). Non-differentiable operations (e.g. hard argmax or step functions) must be approximated via continuous relaxations (like Gumbel-Softmax).",
                "hyperparameters": [
                    {"name": "Gradient Clipping Threshold", "description": "Maximum allowed norm for gradient vectors ($||g|| \\le c$).", "effect": "Clips exploding gradients, stabilizing training in RNNs and deep Transformers."},
                    {"name": "Mixed Precision (FP16 / BF16)", "description": "Computing forward and backward passes in 16-bit floating point.", "effect": "Halves VRAM usage and doubles tensor computation throughput."}
                ],
                "strengths": [
                    "Exact analytical gradients computed in computational time proportional to a single forward pass $\\mathcal{O}(|V| + |E|)$.",
                    "Powers all modern deep learning frameworks (PyTorch, JAX, TensorFlow).",
                    "Allows arbitrary directed acyclic computation graphs (skip connections, multi-loss heads)."
                ],
                "limitations": [
                    "Requires caching all intermediate activations during the forward pass, creating high VRAM memory consumption.",
                    "Susceptible to vanishing and exploding gradients when propagated through long sequential chains."
                ],
                "evaluation": "Gradient checking (Finite Difference verification) during debugging: compare analytical backprop gradient against $(J(\\theta + \\epsilon) - J(\\theta - \\epsilon))/(2\\epsilon)$; relative difference should be $< 10^{-7}$.",
                "workedExample": "Simple graph: $f(x, w, b) = \\sigma(w x + b)$. Input $x=2, w=3, b=1$. Forward: $z = 3(2)+1 = 7$; $a = \\sigma(7) \\approx 0.999$. Target $y=1$. Loss $\\mathcal{L} = \\frac{1}{2}(a - y)^2 = \\frac{1}{2}(0.999 - 1)^2 = 0.0000005$. Backward: $\\frac{\\partial \\mathcal{L}}{\\partial a} = (a - 1) = -0.001$. $\\frac{\\partial a}{\\partial z} = \\sigma(7)(1 - \\sigma(7)) \\approx 0.001$. $\\frac{\\partial z}{\\partial w} = x = 2$. Gradient $\\frac{\\partial \\mathcal{L}}{\\partial w} = (-0.001) \\times (0.001) \\times 2 = -0.000002$.",
                "whenToUse": "The computational engine for training every deep neural network.",
                "commonMistakes": [
                    "Retaining the computation graph across training loops in PyTorch by forgetting `optimizer.zero_grad()`, causing gradients to accumulate endlessly.",
                    "Creating in-place tensor mutations that overwrite intermediate activations needed by backpropagation."
                ],
                "furtherLearning": [
                    {"title": "Olah: Calculus on Computational Graphs: Backpropagation", "url": "https://colah.github.io/posts/2015-08-Backprop/"},
                    {"title": "Andrej Karpathy: Micrograd (Autograd engine in 100 lines of Python)", "url": "https://github.com/karpathy/micrograd"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary computational reason reverse-mode automatic differentiation (backpropagation) is used instead of forward-mode autodiff in deep learning?",
                    "options": [
                        "Reverse-mode is written in Python; forward-mode is written in C.",
                        "In deep learning, models have millions of inputs (weights) and a single scalar output (loss); reverse-mode computes all weight gradients in ONE pass, whereas forward-mode would require one pass per weight.",
                        "Forward-mode cannot compute derivatives of trigonometric functions.",
                        "Reverse-mode requires zero computer memory."
                    ],
                    "correct": 1,
                    "explanation": "When functions have many inputs $N$ and few outputs $M$ ($M \\ll N$), reverse-mode autodiff computes all $\\nabla_W \\mathcal{L}$ in $\\mathcal{O}(M)$ passes—a single backward sweep for scalar loss."
                },
                {
                    "question": "Why does training deep networks require significantly more GPU VRAM than performing inference with the same network?",
                    "options": [
                        "Because inference deletes the weights.",
                        "Because backpropagation requires storing all intermediate layer activations in memory during the forward pass so they can be referenced in chain-rule calculations.",
                        "Because training requires running at 4K monitor resolution.",
                        "Because GPUs double in clock speed during training."
                    ],
                    "correct": 1,
                    "explanation": "During backpropagation, weight gradients depend on layer activations $\\mathbf{a}^{(l-1)}$. These must be kept in VRAM throughout the forward pass, creating the dominant memory footprint."
                },
                {
                    "question": "What happens if an engineer forgets to zero the gradients between training batches (`optimizer.zero_grad()`) in PyTorch?",
                    "options": [
                        "The model crashes immediately with a syntax error.",
                        "Gradients from the current batch add to gradients from preceding batches, resulting in incorrect exploding steps.",
                        "The model automatically reverts to random guessing.",
                        "Weights freeze permanently."
                    ],
                    "correct": 1,
                    "explanation": "Frameworks like PyTorch accumulate gradients by default (`param.grad += dL/dw`) to support multi-step gradient accumulation. Forgetting to zero them sums gradients across batches, causing erratic optimization."
                }
            ]
        },
        {
            "id": "D03",
            "title": "Gradient Descent & Modern Optimizers",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["F01", "D01", "D02"],
            "estimatedMinutes": 25,
            "tags": ["optimizers", "sgd", "adam", "adamw", "momentum", "rmsprop"],
            "shortDesc": "Navigate non-convex loss surfaces: Stochastic Gradient Descent, Momentum, RMSProp, Adam, and AdamW weight decay decoupling.",
            "sections": {
                "whatItIs": "Optimizers are the numerical algorithms that update neural network parameters to minimize the loss function. While classical Stochastic Gradient Descent (SGD) takes steps proportional to the negative gradient, modern adaptive optimizers (Adam, AdamW, RMSProp) compute running exponentially decaying averages of past gradients (momentum) and past squared gradients (adaptive learning rates per parameter).",
                "problemItSolves": "Deep neural loss surfaces are non-convex, littered with ravines, saddle points, and plateaus. Vanilla SGD oscillates violently across narrow ravines and crawls along plateaus. Adaptive optimizers accelerate progress along flat ravines and temper updates for volatile parameters.",
                "intuition": "Imagine rolling a heavy iron ball down a foggy, bumpy mountain landscape. Pure SGD is a blind hiker who looks at the steepness directly under their shoes and takes one step: they get stuck in every shallow pothole. Momentum adds physical inertia to the iron ball, allowing it to blast through minor bumps. Adam adds individual shock absorbers and rocket thrusters to every wheel.",
                "howItWorks": "1. <strong>SGD with Momentum:</strong> Accumulate velocity vector $v_t = \\beta v_{t-1} + (1 - \\beta) g_t$.<br>2. <strong>RMSProp:</strong> Divide by the running root-mean-square of recent gradients: $s_t = \\beta_2 s_{t-1} + (1 - \\beta_2) g_t^2$.<br>3. <strong>Adam:</strong> Combine momentum ($m_t$, 1st moment) and RMSProp ($v_t$, 2nd moment) with bias correction.<br>4. <strong>AdamW:</strong> Decouple $L_2$ weight decay directly from gradient updates, fixing a historical flaw in Adam.",
                "mathematics": "Adam Update Equations:<br>$$m_t = \\beta_1 m_{t-1} + (1 - \\beta_1) g_t \\quad \\text{(1st moment / momentum)}$$<br>$$v_t = \\beta_2 v_{t-1} + (1 - \\beta_2) g_t^2 \\quad \\text{(2nd moment / uncentered variance)}$$<br>Bias corrections (for $t \\approx 1$):<br>$$\\hat{m}_t = \\frac{m_t}{1 - \\beta_1^t}, \\qquad \\hat{v}_t = \\frac{v_t}{1 - \\beta_2^t}$$<br>AdamW Parameter Update with decoupled weight decay $\\lambda$:<br>$$\\theta_t = \\theta_{t-1} - \\alpha \\left( \\frac{\\hat{m}_t}{\\sqrt{\\hat{v}_t} + \\epsilon} + \\lambda \\theta_{t-1} \\right)$$",
                "dataRequirements": "Mini-batch inputs. Batch sizes typically range from 32 to 4096. Gradients must be computed on statistically unbiased mini-batch samples.",
                "hyperparameters": [
                    {"name": "Learning Rate (\\alpha)", "description": "Base step size (e.g. 1e-4 for AdamW; 0.1 for SGD).", "effect": "The most sensitive hyperparameter. Paired with learning rate schedulers (Cosine Annealing, Warmup)."},
                    {"name": "Betas (\\beta_1, \\beta_2)", "description": "Momentum coefficients (standard: $\\beta_1 = 0.9, \\beta_2 = 0.999$).", "effect": "Controls memory duration of past gradient direction and variance."},
                    {"name": "Weight Decay (\\lambda)", "description": "Decoupled L2 regularization rate (e.g. 0.01 to 0.1).", "effect": "Prevents weight explosion without distorting adaptive scale."}
                ],
                "strengths": [
                    "AdamW is the battle-tested gold standard across NLP, Computer Vision, and Generative AI.",
                    "Robust out of the box; requires far less manual tuning than vanilla SGD.",
                    "Adaptive learning rates scale individual feature updates according to gradient sparsity."
                ],
                "limitations": [
                    "Adam requires storing two additional running state tensors ($m$ and $v$) for every weight, tripling optimizer memory footprint.",
                    "SGD with Momentum can sometimes achieve slightly superior final generalization test error on vision models if tuned with extreme care."
                ],
                "evaluation": "Evaluated by tracking Loss curves, Learning Rate schedules, and Gradient Norms across training iterations.",
                "workedExample": "Training a Transformer LLM. If a rare token appears once every 10,000 steps, its gradient is mostly zero. Vanilla SGD barely updates its embedding. Adam's second moment $v_t$ for that token is tiny, automatically scaling its step size up by $1/\\sqrt{v_t}$ so the rare token learns immediately.",
                "whenToUse": "Use AdamW as the default starting optimizer for virtually all deep learning architectures (Transformers, CNNs, GNNs).",
                "commonMistakes": [
                    "Using standard Adam with L2 regularization instead of AdamW (in standard Adam, L2 penalties get scaled inversely by adaptive variance, failing to regularize large weights).",
                    "Training deep Transformers without a Learning Rate Warmup schedule (causes early gradient explosions)."
                ],
                "furtherLearning": [
                    {"title": "Kingma & Ba: Adam: A Method for Stochastic Optimization (ICLR 2015)", "url": "https://arxiv.org/abs/1412.6980"},
                    {"title": "Loshchilov & Hutter: Decoupled Weight Decay Regularization (AdamW 2019)", "url": "https://arxiv.org/abs/1711.05101"}
                ]
            },
            "quiz": [
                {
                    "question": "What was the critical flaw in original Adam that the AdamW optimizer corrected?",
                    "options": [
                        "Adam could not run on GPUs.",
                        "In original Adam, $L_2$ regularization was implemented as gradient additions, which caused weights with large or frequent gradients to be penalized LESS than weights with small gradients; AdamW decouples weight decay directly into the update step.",
                        "Adam ran out of memory after 10 epochs.",
                        "Adam could only process binary classification."
                    ],
                    "correct": 1,
                    "explanation": "Loshchilov & Hutter proved that adding $L_2$ penalties to gradients in adaptive optimizers distorts regularization. AdamW decouples weight decay directly from gradient moments, restoring proper regularization."
                },
                {
                    "question": "How much additional memory does the Adam optimizer require to store its internal state relative to model parameters?",
                    "options": [
                        "Zero additional memory.",
                        "Twice the model parameter memory (one tensor for the 1st moment $m$, and one tensor for the 2nd moment $v$).",
                        "Ten times the model size.",
                        "50 Megabytes fixed."
                    ],
                    "correct": 1,
                    "explanation": "For every trainable float32 parameter, Adam must maintain a float32 first moment $m_t$ and a float32 second moment $v_t$, consuming $2 \\times$ the memory of the model weights."
                },
                {
                    "question": "Why is 'Learning Rate Warmup' commonly applied during the first few thousand steps of Transformer training?",
                    "options": [
                        "To heat up the physical GPU hardware.",
                        "Early in training, gradient moments ($m_t, v_t$) are uncalibrated and noisy; ramping up the learning rate gradually prevents destructive early parameter divergence.",
                        "To force all activations to zero.",
                        "To test the validation set."
                    ],
                    "correct": 1,
                    "explanation": "At the start of training, adaptive statistics have seen few samples and variance is high. Gradually ramping the learning rate from 0 avoids destabilizing early updates."
                }
            ]
        },
        {
            "id": "D04",
            "title": "Loss Functions, Regularization & Normalization",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["F05", "D01", "D03"],
            "estimatedMinutes": 25,
            "tags": ["regularization", "dropout", "batchnorm", "layernorm", "cross-entropy", "weight-decay"],
            "shortDesc": "Loss formulations (Cross-Entropy, Focal, MSE) paired with stabilizing mechanics: Dropout, Batch Normalization, and Layer Normalization.",
            "sections": {
                "whatItIs": "Loss functions define the mathematical objective that models minimize. Regularization techniques (Dropout, Weight Decay, Label Smoothing) prevent deep networks from memorizing training data. Normalization layers (Batch Normalization, Layer Normalization, RMSNorm) standardize internal activations across layers, stabilizing gradient flow and accelerating training.",
                "problemItSolves": "Deep networks easily overfit millions of parameters. Furthermore, as weights update during training, the distribution of inputs to each layer shifts continuously (internal covariate shift), causing training to stall or diverge. Normalization and regularization resolve both issues.",
                "intuition": "Regularization is like a fitness trainer who randomly ties one of your hands behind your back during boxing practice (Dropout): you are forced to learn how to punch with both arms independently. Normalization is an air conditioning thermostat on each floor of a 100-story skyscraper: no matter how hot or cold the weather outside, every floor maintains a steady, comfortable temperature (mean 0, variance 1) so everyone can work smoothly.",
                "howItWorks": "1. <strong>Dropout:</strong> During training, randomly set a fraction $p$ of neuron activations to 0; scale remaining activations by $1/(1-p)$.<br>2. <strong>Batch Normalization (BatchNorm):</strong> Normalize activations across the mini-batch dimension; track running population stats for inference (standard in CNNs).<br>3. <strong>Layer Normalization (LayerNorm):</strong> Normalize across the feature/channel dimensions independently for each sample (standard in Transformers/RNNs).<br>4. <strong>RMSNorm:</strong> Simplified LayerNorm that scales by root-mean-square without mean centering (standard in Llama models).",
                "mathematics": "Layer Normalization for vector $\\mathbf{x} \\in \\mathbb{R}^D$:<br>$$\\mu = \\frac{1}{D} \\sum_{i=1}^D x_i, \\quad \\sigma^2 = \\frac{1}{D} \\sum_{i=1}^D (x_i - \\mu)^2$$<br>$$\\hat{\\mathbf{x}} = \\frac{\\mathbf{x} - \\mu}{\\sqrt{\\sigma^2 + \\epsilon}} \\odot \\boldsymbol{\\gamma} + \\boldsymbol{\\beta}$$<br>Focal Loss (for extreme class imbalance):<br>$$\\text{FL}(p_t) = -\\alpha_t (1 - p_t)^\\gamma \\log(p_t)$$<br>Dropout Inverted Scaling:<br>$$\\tilde{a}_i = \\frac{a_i \\cdot m_i}{1 - p}, \\quad m_i \\sim \\text{Bernoulli}(1 - p)$$",
                "dataRequirements": "Continuous tensors. BatchNorm requires sufficiently large mini-batch sizes ($B \\ge 32$) to calculate stable batch statistics. LayerNorm operates on individual samples and has zero batch size constraints.",
                "hyperparameters": [
                    {"name": "Dropout Probability (p)", "description": "Fraction of activations randomly masked (typically 0.1 to 0.5).", "effect": "Higher $p$ prevents co-adaptation; disabled during inference."},
                    {"name": "Normalization Type", "description": "BatchNorm, LayerNorm, GroupNorm, RMSNorm.", "effect": "BatchNorm for Vision CNNs; LayerNorm/RMSNorm for NLP Transformers."},
                    {"name": "Focal Gamma (\\gamma)", "description": "Focusing parameter in Focal Loss.", "effect": "Down-weights easy well-classified examples, focusing gradients on hard examples."}
                ],
                "strengths": [
                    "Enables training of ultra-deep networks (100+ layers) without vanishing/exploding gradients.",
                    "Significantly dampens overfitting and improves generalization.",
                    "Allows much higher learning rates, accelerating convergence by 5x-10x."
                ],
                "limitations": [
                    "BatchNorm introduces discrepancy between training mode and evaluation mode (`model.eval()`).",
                    "Dropout increases required training epochs to reach convergence.",
                    "BatchNorm fails with small batch sizes ($B < 8$)."
                ],
                "evaluation": "Monitored via training vs validation loss curves and tracking weight/activation distributions.",
                "workedExample": "A medical imaging dataset where 99% of pixels are background and 1% are cancerous lesions. Standard cross-entropy is dominated by background pixels. Using Focal Loss with $\\gamma = 2$ reduces loss on easy background samples by a factor of $(1 - 0.99)^2 = 0.0001$, forcing gradients to concentrate on detecting the tiny tumor.",
                "whenToUse": "Mandatory in all deep learning architectures: use LayerNorm/RMSNorm for sequence models, and BatchNorm/GroupNorm for vision models.",
                "commonMistakes": [
                    "Forgetting to call `model.eval()` during validation/inference in PyTorch (leaving Dropout active and BatchNorm updating running stats).",
                    "Using Batch Normalization with batch size 2, causing massive noise in batch statistics.",
                    "Using Layer Normalization along the batch dimension instead of feature dimension."
                ],
                "furtherLearning": [
                    {"title": "Ioffe & Szegedy: Batch Normalization (ICML 2015)", "url": "https://arxiv.org/abs/1502.03167"},
                    {"title": "Ba, Kiros, Hinton: Layer Normalization (2016)", "url": "https://arxiv.org/abs/1607.06450"},
                    {"title": "Lin et al.: Focal Loss for Dense Object Detection (RetinaNet 2017)", "url": "https://arxiv.org/abs/1708.02002"}
                ]
            },
            "quiz": [
                {
                    "question": "Why is Layer Normalization preferred over Batch Normalization in Transformers and Natural Language Processing?",
                    "options": [
                        "Layer Normalization is only compatible with text.",
                        "Sentences have variable lengths and batch sizes are often small; LayerNorm normalizes across the hidden feature dimension for each token independently, without depending on batch statistics.",
                        "BatchNorm cannot compute square roots.",
                        "LayerNorm eliminates all parameters."
                    ],
                    "correct": 1,
                    "explanation": "BatchNorm depends on computing statistics across the batch dimension, which fails when sequence lengths vary and batch sizes are small. LayerNorm computes mean and variance across the feature dimension of each individual token."
                },
                {
                    "question": "What must you always do before running validation or inference on a PyTorch model that contains Dropout and BatchNorm?",
                    "options": [
                        "Delete the model weights.",
                        "Call `model.eval()` to disable Dropout and freeze BatchNorm running statistics.",
                        "Multiply all weights by 2.",
                        "Re-initialize optimizer states."
                    ],
                    "correct": 1,
                    "explanation": "`model.eval()` switches off stochastic Dropout (allowing all neurons to fire deterministically) and tells BatchNorm to use accumulated population running statistics instead of mini-batch statistics."
                },
                {
                    "question": "What is the primary mechanism of Focal Loss?",
                    "options": [
                        "It magnifies loss on easy examples.",
                        "It adds a modulating factor $(1 - p_t)^\\gamma$ to cross-entropy that automatically down-weights easy, well-classified examples, focusing learning on hard, misclassified samples.",
                        "It converts classification into regression.",
                        "It removes negative gradients."
                    ],
                    "correct": 1,
                    "explanation": "When an example is well-classified ($p_t \\to 1$), $(1 - p_t)^\\gamma \\to 0$, reducing its loss contribution to near zero and focusing gradient updates on difficult samples."
                }
            ]
        },
        {
            "id": "D05",
            "title": "Deep Multilayer Perceptrons & Training Dynamics",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["S13", "D01", "D02", "D03", "D04"],
            "estimatedMinutes": 25,
            "tags": ["deep-mlp", "residual-connections", "skip-connections", "depth", "training-dynamics"],
            "shortDesc": "Scale MLPs to deep regimes using residual skip connections, monitoring gradient flow, loss landscapes, and spectral radius.",
            "sections": {
                "whatItIs": "Deep Multilayer Perceptrons scale feedforward architectures beyond shallow 2-layer models into deep 10-to-100 layer regimes. Achieving stable training in deep feedforward networks requires architectural innovations such as Residual Skip Connections ($x + F(x)$), careful spectral weight normalization, and learning rate scheduling.",
                "problemItSolves": "Historically, simply stacking dense layers caused catastrophic degradation: beyond 5-10 layers, training loss would saturate or increase because gradients decayed exponentially as they traveled backward through repeated matrix multiplications.",
                "intuition": "Imagine whisper down the lane with 50 people. The original message is inevitably garbled or lost by the 10th person. A Residual Skip Connection is like giving the first person a loudspeaker so everyone along the chain can hear the original sentence directly while each person only whispers minor edits or corrections.",
                "howItWorks": "1. <strong>Dense Blocks:</strong> Stack linear layers followed by LayerNorm/BatchNorm and non-linear activations.<br>2. <strong>Residual Connections:</strong> Add the input tensor directly to the block output: $\\mathbf{x}_{l+1} = \\mathbf{x}_l + \\mathcal{F}(\\mathbf{x}_l, \\mathbf{W}_l)$.<br>3. <strong>Identity Mapping:</strong> Gradients can flow directly backward through the $+ \\mathbf{x}_l$ identity highway without being multiplied by weight matrices.<br>4. <strong>Learning Dynamics:</strong> Monitor gradient norms at each layer to verify uniform gradient flow from output back to input.",
                "mathematics": "Residual Block Formulation:<br>$$\\mathbf{x}_{l+1} = \\mathbf{x}_l + \\mathcal{F}(\\mathbf{x}_l, \\mathbf{W}_l)$$<br>Recursive expansion for layer $L$ given layer $l$:<br>$$\\mathbf{x}_L = \\mathbf{x}_l + \\sum_{i=l}^{L-1} \\mathcal{F}(\\mathbf{x}_i, \\mathbf{W}_i)$$<br>Gradient Backpropagation through Residual Highway:<br>$$\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{x}_l} = \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{x}_L} \\frac{\\partial \\mathbf{x}_L}{\\partial \\mathbf{x}_l} = \\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{x}_L} \\left( \\mathbf{I} + \\frac{\\partial}{\\partial \\mathbf{x}_l} \\sum_{i=l}^{L-1} \\mathcal{F}(\\mathbf{x}_i, \\mathbf{W}_i) \\right)$$<br>The identity matrix $\\mathbf{I}$ guarantees gradients flow directly backward even if weight gradients vanish.",
                "dataRequirements": "Normalized high-dimensional continuous tensors. Tabular datasets with complex non-linear feature interactions (e.g. TabNet, ResNet for Tabular Data).",
                "hyperparameters": [
                    {"name": "Network Depth", "description": "Number of sequential residual blocks (e.g. 8 to 32).", "effect": "Increases representation capacity and abstraction hierarchy."},
                    {"name": "Residual Dropout", "description": "Dropout applied inside the branch before the addition.", "effect": "Regularizes deep residual representations."}
                ],
                "strengths": [
                    "Can be trained stably to arbitrary depths (100+ layers) without gradient degradation.",
                    "Learns identity mappings naturally (if a layer is unneeded, weights can safely decay to zero).",
                    "Forms the structural core of modern tabular deep learning and Transformer feedforward sub-layers."
                ],
                "limitations": [
                    "Dense connections on tabular data still lack the spatial/temporal inductive biases of CNNs/Transformers.",
                    "Can still be outperformed on standard tabular datasets by modern Gradient Boosted Trees (XGBoost/LightGBM) unless carefully regularized."
                ],
                "evaluation": "Evaluated using Validation Loss convergence curves, gradient norm histograms across layers, and test benchmarks.",
                "workedExample": "A tabular fraud detection network with 16 dense layers. A standard plain MLP fails to converge, with training loss stuck at 0.69. Adding residual skip connections every 2 layers allows gradients to propagate cleanly, dropping loss to 0.12 in 20 epochs.",
                "whenToUse": "Use when building deep feature transformation heads, multi-task representations, or competitive deep tabular architectures.",
                "commonMistakes": [
                    "Building deep plain feedforward networks without skip connections and wondering why gradients vanish.",
                    "Mismatched dimensions: attempting residual addition $\\mathbf{x} + \\mathcal{F}(\\mathbf{x})$ when channel dimensions do not match without a linear projection."
                ],
                "furtherLearning": [
                    {"title": "He et al.: Deep Residual Learning for Image Recognition (ResNet 2015)", "url": "https://arxiv.org/abs/1512.03385"},
                    {"title": "Gorishniy et al.: Revisiting Deep Learning Models for Tabular Data (NeurIPS 2021)", "url": "https://arxiv.org/abs/2106.11959"}
                ]
            },
            "quiz": [
                {
                    "question": "What mathematical property of residual connections ($x_{l+1} = x_l + F(x_l)$) solves the vanishing gradient problem in deep networks?",
                    "options": [
                        "The addition operation creates an identity shortcut $\\mathbf{I}$ in the gradient chain rule, allowing error signals to flow directly backward without decaying through repeated matrix multiplications.",
                        "It eliminates all negative numbers.",
                        "It sets the loss to zero.",
                        "It divides the gradient by 2."
                    ],
                    "correct": 0,
                    "explanation": "Because $\\frac{\\partial x_{l+1}}{\\partial x_l} = \\mathbf{I} + \\frac{\\partial F}{\\partial x_l}$, the gradient contains an uninterrupted $+1$ term that flows directly across the entire network depth without diminishing."
                },
                {
                    "question": "What happens if a residual layer's input $x$ and output $F(x)$ have different vector dimensions?",
                    "options": [
                        "The network crashes unless $x$ is projected via a linear matrix $W_s x$ to match the dimension of $F(x)$ before addition.",
                        "The smaller vector is filled with random numbers.",
                        "The residual connection is automatically deleted.",
                        "It converts into a decision tree."
                    ],
                    "correct": 0,
                    "explanation": "Vector addition requires identical tensor shapes. If dimensions change, a linear projection (or 1x1 convolution) $W_s x$ must be applied to match dimensions."
                },
                {
                    "question": "How do deep tabular ResNets compare to Gradient Boosted Trees (like XGBoost) on typical tabular benchmarks?",
                    "options": [
                        "Deep ResNets always win by 50%.",
                        "XGBoost and LightGBM often still achieve superior or equal accuracy with significantly less tuning and faster training, though deep ResNets are competitive with proper regularization.",
                        "Deep ResNets cannot run on tabular data.",
                        "Decision trees are obsolete."
                    ],
                    "correct": 1,
                    "explanation": "Benchmark studies (e.g. Gorishniy et al.) consistently show that tuned GBDTs remain formidable on tabular data, though deep tabular ResNets narrow the gap and excel when combining embeddings with raw tables."
                }
            ]
        },
        {
            "id": "D06",
            "title": "Convolutional Neural Networks (CNNs)",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["D01", "D02", "D04", "D05"],
            "estimatedMinutes": 25,
            "tags": ["cnn", "computer-vision", "convolutions", "pooling", "spatial-inductive-bias", "resnet"],
            "shortDesc": "Exploit spatial locality and translation equivariance in images using learnable sliding filter kernels and pooling layers.",
            "sections": {
                "whatItIs": "Convolutional Neural Networks (CNNs) are specialized neural architectures designed for grid-structured data (images, video, spectrograms). Instead of fully connected matrix multiplications, CNNs use small learnable filter kernels that slide (convolve) across spatial dimensions, sharing weights and enforcing translation equivariance.",
                "problemItSolves": "A 1000x1000 RGB image has 3 million inputs. A single dense hidden neuron would require 3 million weights, leading to parameter explosion and severe overfitting. CNNs solve this via local receptive fields and weight sharing, drastically reducing parameters while respecting spatial geometry.",
                "intuition": "Imagine scanning a document with a magnifying glass searching for the letter 'A'. You slide the exact same magnifying lens over every square inch of the page. You do not need a separate magnifying glass for the top-left corner and a different one for the bottom-right corner. The pattern 'A' looks identical wherever it appears.",
                "howItWorks": "1. <strong>2D Convolution:</strong> Slide a small kernel (e.g. $3 \\times 3$) across the input tensor, computing element-wise dot products to produce a <strong>Feature Map</strong>.<br>2. <strong>Stride & Padding:</strong> Stride controls step size; padding ('same' vs 'valid') controls border preservation.<br>3. <strong>Activation:</strong> Pass feature map through ReLU/GELU.<br>4. <strong>Pooling:</strong> Downsample spatial dimensions (e.g. $2 \\times 2$ Max Pooling) to provide translation invariance and reduce compute.<br>5. <strong>Hierarchical Abstraction:</strong> Early layers detect edges and textures; middle layers detect motifs and parts; deep layers recognize whole objects.",
                "mathematics": "2D Discrete Cross-Correlation (Convolution in DL):<br>$$S(i, j) = (I * K)(i, j) = \\sum_{m} \\sum_{n} I(i + m, j + n) K(m, n)$$<br>Feature Map Output Spatial Dimensions for input $W$, kernel $K$, padding $P$, stride $S$:<br>$$W_{\\text{out}} = \\left\\lfloor \\frac{W - K + 2P}{S} \\right\\rfloor + 1$$<br>Parameter Count for Conv layer with $C_{\\text{in}}$ input channels, $C_{\\text{out}}$ output filters of size $K \\times K$:<br>$$\\text{Params} = C_{\\text{out}} \\times (K \\times K \\times C_{\\text{in}} + 1)$$",
                "dataRequirements": "2D or 3D tensors: $(B, C, H, W)$ in PyTorch or $(B, H, W, C)$ in TensorFlow. Pixel values normalized to $[0, 1]$ or $[-1, 1]$. Data augmentation (flips, crops, color jitter) is standard.",
                "hyperparameters": [
                    {"name": "Kernel Size (K)", "description": "Spatial dimension of the sliding window (standard: $3 \\times 3$ or $5 \\times 5$).", "effect": "Small $3 \\times 3$ kernels stacked deep capture large receptive fields with fewer parameters."},
                    {"name": "Stride (S)", "description": "Step size taken by the filter across pixels.", "effect": "Stride $> 1$ downsamples spatial resolution."},
                    {"name": "Padding (P)", "description": "Zeroes added to image borders.", "effect": "'Same' padding preserves input height and width."}
                ],
                "strengths": [
                    "Translation Equivariance: an object is detected regardless of where it appears in the frame.",
                    "Massive parameter efficiency compared to fully connected layers.",
                    "Hierarchical representation learning mirroring biological mammalian visual cortex (Hubel & Wiesel).",
                    "Hardware optimized with highly parallelized GPU GEMM (im2col) routines."
                ],
                "limitations": [
                    "Lacks understanding of coordinate relationships and rotation (mitigated by data augmentation).",
                    "Fixed receptive fields require deep stacking to capture global image context (Vision Transformers overcome this).",
                    "Requires large annotated image datasets (ImageNet) to train from scratch."
                ],
                "evaluation": "Evaluated using Top-1 and Top-5 Accuracy (classification), mAP (object detection), and IoU (segmentation).",
                "workedExample": "Processing a $224 \\times 224 \\times 3$ image with a Conv layer having 64 filters of size $3 \\times 3$, padding 1, stride 1. Output shape is $224 \\times 224 \\times 64$. Total parameters: $64 \\times (3 \\times 3 \\times 3 + 1) = 1,792$ weights. A fully connected layer for the same input would require over 48 million parameters!",
                "whenToUse": "The foundational standard for computer vision: image classification, medical radiography, autonomous vehicle perception, and optical character recognition.",
                "commonMistakes": [
                    "Using large filter kernels (e.g. $11 \\times 11$) when a stack of small $3 \\times 3$ filters achieves a wider receptive field with far fewer weights.",
                    "Forgetting to normalize pixel values from $[0, 255]$ down to $[0, 1]$ or standard z-scores."
                ],
                "furtherLearning": [
                    {"title": "LeCun et al.: Gradient-Based Learning Applied to Document Recognition (LeNet-5 1998)", "url": "http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf"},
                    {"title": "Stanford CS231n: Convolutional Neural Networks for Visual Recognition", "url": "https://cs231n.github.io/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary spatial inductive bias built into Convolutional Neural Networks?",
                    "options": [
                        "Words in a sentence follow grammatical order.",
                        "Spatial locality (nearby pixels are strongly correlated) and translation equivariance (patterns can appear anywhere in the image).",
                        "Data is always organized in alphabetical order.",
                        "All images are black and white."
                    ],
                    "correct": 1,
                    "explanation": "CNNs explicitly assume local pixel connectivity and translation equivariance through shared filter weights convolving across the visual field."
                },
                {
                    "question": "How many trainable parameters are in a Conv2D layer with 32 filters of size $3 \\times 3$ operating on an RGB image (3 input channels), including biases?",
                    "options": [
                        "896",
                        "288",
                        "32",
                        "27"
                    ],
                    "correct": 0,
                    "explanation": "Each filter has $3 \\times 3 \\times 3 = 27$ weights $+ 1$ bias $= 28$ parameters. With 32 filters: $32 \\times 28 = 896$ parameters."
                },
                {
                    "question": "Why did modern architectures replace large kernels (like $7 \\times 7$) with stacks of multiple $3 \\times 3$ kernels?",
                    "options": [
                        "Two stacked $3 \\times 3$ kernels cover the same $5 \\times 5$ effective receptive field with fewer parameters and incorporate more non-linear activation layers.",
                        "Computers cannot divide by 7.",
                        "Large kernels produce inverted images.",
                        "To eliminate the need for GPU memory."
                    ],
                    "correct": 0,
                    "explanation": "Stacking two $3 \\times 3$ convs has the same receptive field as a $5 \\times 5$ conv ($18$ vs $25$ params) while introducing an extra non-linear activation, increasing expressive capacity."
                }
            ]
        },
        {
            "id": "D07",
            "title": "Recurrent Neural Networks (RNNs)",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["D01", "D02", "D05"],
            "estimatedMinutes": 25,
            "tags": ["rnn", "sequence-modeling", "hidden-state", "bptt", "vanishing-gradients"],
            "shortDesc": "Model sequential and temporal data by maintaining a recurrent hidden state memory across unrolled time steps.",
            "sections": {
                "whatItIs": "Recurrent Neural Networks (RNNs) are neural networks designed for sequential data (text, time series, audio). Unlike feedforward networks that process inputs independently, an RNN maintains an internal recurring hidden state vector $\\mathbf{h}_t$ that acts as memory, updating at each time step based on the current input $\\mathbf{x}_t$ and previous hidden state $\\mathbf{h}_{t-1}$.",
                "problemItSolves": "Feedforward networks require fixed-size inputs and cannot naturally model variable-length sequences or temporal dependencies where meaning depends on historical context.",
                "intuition": "Imagine reading a murder mystery novel. You do not forget Chapter 1 when you start reading Chapter 2. Instead, your mental summary of the plot (the hidden state) is continually updated as each new sentence (input) unfolds, allowing you to understand the detective's final revelation.",
                "howItWorks": "1. <strong>Sequential Traversal:</strong> Unroll the network over $T$ time steps.<br>2. <strong>Recurrent State Update:</strong> Compute new hidden state: $\\mathbf{h}_t = \\tanh(\\mathbf{W}_{hh} \\mathbf{h}_{t-1} + \\mathbf{W}_{xh} \\mathbf{x}_t + \\mathbf{b}_h)$.<br>3. <strong>Output Prediction:</strong> Output prediction at step $t$: $\\hat{\\mathbf{y}}_t = \\text{softmax}(\\mathbf{W}_{hy} \\mathbf{h}_t + \\mathbf{b}_y)$.<br>4. <strong>Backpropagation Through Time (BPTT):</strong> Unroll the entire computation graph over time and backpropagate gradients across all time steps.",
                "mathematics": "Hidden State Transition Equation:<br>$$\\mathbf{h}_t = \\tanh\\left( \\mathbf{W}_{hh} \\mathbf{h}_{t-1} + \\mathbf{W}_{xh} \\mathbf{x}_t + \\mathbf{b}_h \\right)$$<br>Backpropagation Through Time Gradient Chain:<br>$$\\frac{\\partial \\mathcal{L}}{\\partial \\mathbf{W}_{hh}} = \\sum_{t=1}^T \\frac{\\partial \\mathcal{L}_t}{\\partial \\mathbf{W}_{hh}}, \\quad \\text{where } \\frac{\\partial \\mathcal{L}_T}{\\partial \\mathbf{h}_1} = \\frac{\\partial \\mathcal{L}_T}{\\partial \\mathbf{h}_T} \\prod_{k=2}^T \\frac{\\partial \\mathbf{h}_k}{\\partial \\mathbf{h}_{k-1}}$$<br>Jacobian factor $\\frac{\\partial \\mathbf{h}_k}{\\partial \\mathbf{h}_{k-1}} = \\text{diag}(1 - \\mathbf{h}_k^2) \\mathbf{W}_{hh}^T$. If the largest eigenvalue of $\\mathbf{W}_{hh} < 1$, gradients decay exponentially to zero (Vanishing Gradient); if $> 1$, they blow up to infinity (Exploding Gradient).",
                "dataRequirements": "Sequential 3D tensors: $(\\text{Batch}, \\text{Time Steps}, \\text{Features})$. Padded to equal lengths or handled via packed sequences.",
                "hyperparameters": [
                    {"name": "Hidden Dimension", "description": "Size of the internal memory vector $\\mathbf{h}_t$.", "effect": "Determines capacity to retain complex sequential context."},
                    {"name": "BPTT Truncation Length", "description": "Maximum historical steps unrolled during backpropagation.", "effect": "Caps computational graph memory to prevent OOM errors."},
                    {"name": "Gradient Clip Value", "description": "Norm ceiling for gradients.", "effect": "Essential to prevent exploding gradients."}
                ],
                "strengths": [
                    "Can process sequences of arbitrary, variable lengths.",
                    "Weight sharing across time: parameters do not scale with sequence duration.",
                    "Models temporal dynamics and time-series transitions naturally."
                ],
                "limitations": [
                    "Severe vanishing gradient problem: vanilla RNNs cannot retain information beyond ~10-15 time steps.",
                    "Inherently sequential: cannot parallelize forward or backward passes across time on GPUs (unlike Transformers).",
                    "Prone to exploding gradients requiring mandatory gradient clipping."
                ],
                "evaluation": "Evaluated using Perplexity (language modeling), Token Accuracy, or Mean Squared Error (time series).",
                "workedExample": "Sentiment classification of a sentence: 'The movie was not good'. At $t=1$, $\\mathbf{h}_1$ encodes 'The'. At $t=2$, $\\mathbf{h}_2$ combines 'movie' with 'The'. At $t=3$, 'not' flips the valence of the hidden state. At $t=4$, 'good' is interpreted in light of the 'not' in $\\mathbf{h}_3$, outputting a Negative sentiment score.",
                "whenToUse": "Historical baseline; primarily used in low-latency microcontroller sensor monitoring where Transformers are too heavy.",
                "commonMistakes": [
                    "Using vanilla RNNs for long text documents (gradients vanish completely; use LSTMs or Transformers).",
                    "Forgetting to clip gradients, causing sudden numerical NaN crashes during training."
                ],
                "furtherLearning": [
                    {"title": "Elman: Finding Structure in Time (Cognitive Science 1990)", "url": "https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog1402_1"},
                    {"title": "Andrej Karpathy: The Unreasonable Effectiveness of Recurrent Neural Networks", "url": "https://karpathy.github.io/2015/05/21/rnn-effectiveness/"}
                ]
            },
            "quiz": [
                {
                    "question": "Why do vanilla Recurrent Neural Networks struggle to learn long-term dependencies (e.g. connecting words separated by 50 tokens)?",
                    "options": [
                        "Because text cannot be represented as numbers.",
                        "Because the continuous matrix multiplication of $\\mathbf{W}_{hh}$ over 50 steps causes gradients to decay exponentially toward zero (Vanishing Gradient problem).",
                        "Because RNNs can only remember 2 words at a time.",
                        "Because hidden states reset to random values every 5 steps."
                    ],
                    "correct": 1,
                    "explanation": "In BPTT, gradients flow through repeated products of the recurrent weight matrix $\\prod \\mathbf{W}_{hh}$. If eigenvalues are $< 1$, the gradient decays exponentially to zero, blinding the network to early inputs."
                },
                {
                    "question": "What is the primary architectural limitation of RNNs compared to Transformers on modern hardware?",
                    "options": [
                        "RNNs cannot be trained on GPUs because each time step $t$ strictly depends on completing the previous step $t-1$, preventing parallel execution across sequence tokens.",
                        "RNNs use too many parameters.",
                        "RNNs cannot do classification.",
                        "Transformers do not use matrix multiplication."
                    ],
                    "correct": 0,
                    "explanation": "The recurrent step $\\mathbf{h}_t = f(\\mathbf{h}_{t-1}, \\mathbf{x}_t)$ is inherently sequential. You cannot compute step 100 without sequentially computing steps 1 through 99, preventing parallel GPU saturation."
                },
                {
                    "question": "Which mathematical technique is universally used to prevent exploding gradients in RNN training?",
                    "options": [
                        "Gradient Clipping (rescaling gradient vectors if their $L_2$ norm exceeds a threshold $c$).",
                        "Setting all weights to 1.0.",
                        "Deleting the loss function.",
                        "Multiplying by infinity."
                    ],
                    "correct": 0,
                    "explanation": "Gradient clipping monitors the norm $||g||$; if it exceeds threshold $c$, it rescales $g \\leftarrow c \\frac{g}{||g||}$, preserving direction while preventing numerical explosions."
                }
            ]
        },
        {
            "id": "D08",
            "title": "LSTMs & GRUs",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["D01", "D02", "D07"],
            "estimatedMinutes": 25,
            "tags": ["lstm", "gru", "gating-mechanisms", "cell-state", "long-term-memory"],
            "shortDesc": "Overcome vanishing gradients with gating mechanisms: Long Short-Term Memory cells and Gated Recurrent Units.",
            "sections": {
                "whatItIs": "Long Short-Term Memory (LSTM) networks and Gated Recurrent Units (GRUs) are specialized recurrent architectures designed to capture long-term sequential dependencies. They introduce an explicit memory conveyor belt (the <strong>Cell State</strong> $\\mathbf{c}_t$) regulated by multiplicative gating mechanisms (Forget, Input, and Output gates) that control what to remember, forget, and write.",
                "problemItSolves": "Vanilla RNNs suffer from vanishing gradients that wipe out memory after a dozen time steps. LSTMs maintain an additive linear gradient highway along the cell state, allowing gradients to flow backward across hundreds of time steps without decaying.",
                "intuition": "Imagine a shared notebook passed around a team. The <strong>Forget Gate</strong> is an eraser: it looks at new information and erases outdated notes (e.g., 'The actor was male' $\\to$ now a female character enters). The <strong>Input Gate</strong> is a pen: it decides which new facts to write down. The <strong>Output Gate</strong> is a highlighter: it decides which parts of the notebook to read out loud to the manager right now.",
                "howItWorks": "1. <strong>Forget Gate:</strong> $f_t = \\sigma(W_f [h_{t-1}, x_t] + b_f)$ outputs values between 0 (completely forget) and 1 (completely keep).<br>2. <strong>Input Gate:</strong> $i_t = \\sigma(W_i [h_{t-1}, x_t] + b_i)$ decides which values to update; candidate $\\tilde{c}_t = \\tanh(W_c [h_{t-1}, x_t] + b_c)$.<br>3. <strong>Update Cell State:</strong> $c_t = f_t \\odot c_{t-1} + i_t \\odot \\tilde{c}_t$ (linear additive update).<br>4. <strong>Output Gate:</strong> $o_t = \\sigma(W_o [h_{t-1}, x_t] + b_o)$; hidden state $h_t = o_t \\odot \\tanh(c_t)$.<br>5. <strong>GRU Simplification:</strong> Merges cell and hidden states into a single $h_t$ using only Reset and Update gates.",
                "mathematics": "LSTM Gating Equations:<br>$$\\mathbf{f}_t = \\sigma(\\mathbf{W}_f [\\mathbf{h}_{t-1}, \\mathbf{x}_t] + \\mathbf{b}_f)$$<br>$$\\mathbf{i}_t = \\sigma(\\mathbf{W}_i [\\mathbf{h}_{t-1}, \\mathbf{x}_t] + \\mathbf{b}_i)$$<br>$$\\tilde{\\mathbf{c}}_t = \\tanh(\\mathbf{W}_c [\\mathbf{h}_{t-1}, \\mathbf{x}_t] + \\mathbf{b}_c)$$<br>$$\\mathbf{c}_t = \\mathbf{f}_t \\odot \\mathbf{c}_{t-1} + \\mathbf{i}_t \\odot \\tilde{\\mathbf{c}}_t$$<br>$$\\mathbf{o}_t = \\sigma(\\mathbf{W}_o [\\mathbf{h}_{t-1}, \\mathbf{x}_t] + \\mathbf{b}_o)$$<br>$$\\mathbf{h}_t = \\mathbf{o}_t \\odot \\tanh(\\mathbf{c}_t)$$",
                "dataRequirements": "Sequential continuous tensors $(B, T, D)$. Masking or packing required for variable-length batches.",
                "hyperparameters": [
                    {"name": "Hidden Size", "description": "Dimensionality of hidden vector and cell state.", "effect": "Determines model capacity."},
                    {"name": "Bidirectional", "description": "Whether to run two LSTMs (forward and backward in time) and concatenate outputs.", "effect": "Essential for NLP classification where future context informs current word meaning."},
                    {"name": "Forget Gate Bias Init", "description": "Initialize $b_f$ to 1.0 or 2.0.", "effect": "Forces the network to remember everything by default at the start of training."}
                ],
                "strengths": [
                    "Retains dependencies across hundreds of time steps.",
                    "Additive cell state highway prevents vanishing gradients.",
                    "GRUs provide comparable accuracy with ~25% fewer parameters and faster training.",
                    "Remains highly effective for sensor telemetry and acoustic modeling."
                ],
                "limitations": [
                    "Still sequential: cannot fully saturate GPU parallelism during training.",
                    "Surpassed by Transformers on large-scale NLP and generative text tasks.",
                    "High parameter count per step compared to vanilla RNNs (4 weight matrices per layer)."
                ],
                "evaluation": "Evaluated using Perplexity, BLEU score (translation), and sequence prediction metrics.",
                "workedExample": "Processing a document: 'Alice went to the store... [50 sentences] ... She bought apples'. When the LSTM encounters 'Alice', the input gate writes female singular subject into the cell state $c_t$. Across 50 irrelevant sentences, the forget gate maintains $f_t \\approx 1.0$. When reaching 'She', the cell state provides the stored gender context immediately.",
                "whenToUse": "Use for audio waveform processing, speech recognition acoustic models, sensor telemetry forecasting, and lightweight sequential tasks.",
                "commonMistakes": [
                    "Initializing forget gate bias to 0 instead of 1.0 (causes the model to forget everything at step 0).",
                    "Using unidirectional LSTMs for text classification where future context is available."
                ],
                "furtherLearning": [
                    {"title": "Hochreiter & Schmidhuber: Long Short-Term Memory (1997 Original Paper)", "url": "https://www.bioinf.jku.at/publications/older/2604.pdf"},
                    {"title": "Colah: Understanding LSTM Networks", "url": "https://colah.github.io/posts/2015-08-Understanding-LSTMs/"},
                    {"title": "Cho et al.: Learning Phrase Representations using RNN Encoder-Decoder (GRU 2014)", "url": "https://arxiv.org/abs/1406.1078"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary mathematical reason LSTMs do not suffer from the severe vanishing gradient problem of vanilla RNNs?",
                    "options": [
                        "LSTMs do not use backpropagation.",
                        "The cell state update $\\mathbf{c}_t = \\mathbf{f}_t \\odot \\mathbf{c}_{t-1} + \\dots$ is linear and additive, creating an uninterrupted gradient highway where backpropagated error does not vanish.",
                        "LSTMs force all weights to 1.",
                        "LSTMs only train for 2 epochs."
                    ],
                    "correct": 1,
                    "explanation": "Because cell state updates are additive rather than multiplicative, $\\frac{\\partial c_t}{\\partial c_{t-1}} = f_t$. If the forget gate is near 1, gradients propagate across long time horizons with zero decay."
                },
                {
                    "question": "Why is it best practice to initialize the LSTM forget gate bias $b_f$ to a positive value (such as 1.0 or 2.0)?",
                    "options": [
                        "To prevent computer memory leaks.",
                        "To ensure the Sigmoid output $\\sigma(b_f) \\approx 1.0$ at the start of training, forcing the network to remember past information by default rather than forgetting everything.",
                        "To convert the LSTM into a GRU.",
                        "To reduce training time to zero."
                    ],
                    "correct": 1,
                    "explanation": "If $b_f = 0$, $\\sigma(0) = 0.5$, meaning the network halves its memory at every single time step. Initializing $b_f = 1$ ensures $f_t \\approx 0.73-0.88$, preserving memory from day one."
                },
                {
                    "question": "How does a Gated Recurrent Unit (GRU) differ from an LSTM?",
                    "options": [
                        "GRU has no gates.",
                        "GRU merges the cell state and hidden state into a single vector and uses only 2 gates (Reset and Update), making it faster to train with fewer parameters.",
                        "GRU is strictly a computer vision model.",
                        "GRU cannot process sequential data."
                    ],
                    "correct": 1,
                    "explanation": "The GRU simplifies the LSTM by eliminating the separate cell state and combining gates into a Reset gate and an Update gate, reducing parameters by ~25%."
                }
            ]
        },
        {
            "id": "D09",
            "title": "Autoencoders & Variational Autoencoders (VAEs)",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["D01", "D02", "U05"],
            "estimatedMinutes": 25,
            "tags": ["autoencoders", "vae", "latent-space", "generative", "reparameterization"],
            "shortDesc": "Compress high-dimensional data into bottleneck latent spaces and generate new samples via variational inference and reparameterization.",
            "sections": {
                "whatItIs": "An Autoencoder is a neural network trained to reconstruct its input through an informational bottleneck (latent space $\\mathbf{z}$). A <strong>Variational Autoencoder (VAE)</strong> is a generative probabilistic model that regularizes the latent space into a continuous, smooth standard Gaussian distribution $\\mathcal{N}(0, \\mathbf{I})$ using the Reparameterization Trick.",
                "problemItSolves": "Standard autoencoders learn unconstrained, discontinuous latent spaces with empty voids: sampling a random point from empty space yields unrecognizable garbage. VAEs enforce a smooth, continuous probabilistic latent manifold, enabling true generative sampling and latent space interpolation.",
                "intuition": "Imagine an architect summarizing a 100-page building blueprint on a 3x5 index card (Encoder), and a builder constructing the building using only that card (Decoder). A standard autoencoder might write obscure abbreviations that only that specific builder understands. A VAE forces the architect to write using a standardized universal coordinate system (mean and variance). You can now tweak the coordinates slightly to generate a building that never existed before.",
                "howItWorks": "1. <strong>Encoder:</strong> Maps input $\\mathbf{x}$ to distribution parameters: mean $\\boldsymbol{\\mu}(\\mathbf{x})$ and log-variance $\\log \\boldsymbol{\\sigma}^2(\\mathbf{x})$.<br>2. <strong>Reparameterization Trick:</strong> Sample $\\boldsymbol{\\epsilon} \\sim \\mathcal{N}(0, \\mathbf{I})$; compute $\\mathbf{z} = \\boldsymbol{\\mu} + \\boldsymbol{\\sigma} \\odot \\boldsymbol{\\epsilon}$ (enabling backprop through random nodes).<br>3. <strong>Decoder:</strong> Reconstructs input from latent vector: $\\hat{\\mathbf{x}} = g(\\mathbf{z})$.<br>4. <strong>Loss Optimization:</strong> Minimize Reconstruction Loss (MSE/BCE) plus KL Divergence to force latent distribution toward $\\mathcal{N}(0, \\mathbf{I})$.",
                "mathematics": "Evidence Lower Bound (ELBO) Loss Function:<br>$$\\mathcal{L}_{\\text{VAE}}(\\theta, \\phi; \\mathbf{x}) = \\underbrace{\\mathbb{E}_{q_\\phi(\\mathbf{z}|\\mathbf{x})}[\\log p_\\theta(\\mathbf{x}|\\mathbf{z})]}_{\\text{Reconstruction Fidelity}} - \\underbrace{\\text{KL}\\left( q_\\phi(\\mathbf{z}|\\mathbf{x}) \\parallel p(\\mathbf{z}) \\right)}_{\\text{Latent Regularization to } \\mathcal{N}(0, \\mathbf{I})}$$<br>Analytical KL Divergence for Gaussian prior $p(\\mathbf{z}) = \\mathcal{N}(0, \\mathbf{I})$:<br>$$\\text{KL} = -\\frac{1}{2} \\sum_{j=1}^J \\left( 1 + \\log(\\sigma_j^2) - \\mu_j^2 - \\sigma_j^2 \\right)$$<br>Reparameterization Trick:<br>$$\\mathbf{z} = \\boldsymbol{\\mu} + \\boldsymbol{\\sigma} \\odot \\boldsymbol{\\epsilon}, \\quad \\boldsymbol{\\epsilon} \\sim \\mathcal{N}(0, \\mathbf{I})$$",
                "dataRequirements": "Continuous or binary image, audio, or tabular tensors. Normalization to $[0, 1]$ or standard z-scores required.",
                "hyperparameters": [
                    {"name": "Latent Dimension (J)", "description": "Size of the bottleneck vector $\\mathbf{z}$ (e.g. 16 to 512).", "effect": "Too small causes blurry reconstructions; too large risks latent collapse."},
                    {"name": "Beta Weight (\\beta)", "description": "Multiplier scaling the KL divergence term ($\\beta$-VAE).", "effect": "$\\beta > 1$ encourages disentangled, independent latent factor representations."}
                ],
                "strengths": [
                    "Learns smooth, interpretable, continuous latent manifolds.",
                    "Generative: can synthesize novel data by sampling $\\mathbf{z} \\sim \\mathcal{N}(0, \\mathbf{I})$.",
                    "Enables semantic latent arithmetic (e.g., face with glasses - face without glasses = glasses vector).",
                    "Provides probabilistic anomaly detection via reconstruction error."
                ],
                "limitations": [
                    "Reconstructed images are notoriously blurry compared to GANs and Diffusion models due to Gaussian likelihood assumptions.",
                    "Posterior collapse: decoder ignores latent codes if paired with overly powerful autoregressive models."
                ],
                "evaluation": "Evaluated using ELBO loss, Reconstruction MSE, Fréchet Inception Distance (FID), and latent traversal plots.",
                "workedExample": "Generating handwritten digits (MNIST). Encoder maps digit images to a 2D latent space $(z_1, z_2)$. Slicing across a 2D grid from -3 to +3 and passing through the decoder smoothly transitions from a '0' into a '6', then into an '8', without any sudden jumps or corrupt artifacts.",
                "whenToUse": "Use for generative modeling, unsupervised representation learning, anomaly detection, drug discovery molecule generation, and latent space interpolation.",
                "commonMistakes": [
                    "Sampling $\\mathbf{z}$ directly from $\\mathcal{N}(\\mu, \\sigma^2)$ without the reparameterization trick (breaks backpropagation because sampling is non-differentiable).",
                    "Ignoring KL divergence weight, causing the latent space to develop discontinuities."
                ],
                "furtherLearning": [
                    {"title": "Kingma & Welling: Auto-Encoding Variational Bayes (VAE 2013)", "url": "https://arxiv.org/abs/1312.6114"},
                    {"title": "Doersch: Tutorial on Variational Autoencoders", "url": "https://arxiv.org/abs/1606.05908"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the 'Reparameterization Trick' in Variational Autoencoders, and why is it necessary?",
                    "options": [
                        "It is an algorithm to compress neural network files.",
                        "It isolates the stochastic random sampling into an external noise parameter $\\boldsymbol{\\epsilon} \\sim \\mathcal{N}(0, \\mathbf{I})$, allowing gradients to backpropagate cleanly through the deterministic parameters $\\boldsymbol{\\mu}$ and $\\boldsymbol{\\sigma}$.",
                        "It converts the decoder into a decision tree.",
                        "It eliminates the need for training data."
                    ],
                    "correct": 1,
                    "explanation": "Directly sampling from a distribution is a non-differentiable stochastic operation that blocks backpropagation. Reparameterizing $\\mathbf{z} = \\boldsymbol{\\mu} + \\boldsymbol{\\sigma} \\odot \\boldsymbol{\\epsilon}$ makes the graph differentiable with respect to $\\boldsymbol{\\mu}$ and $\\boldsymbol{\\sigma}$."
                },
                {
                    "question": "What happens if you set the KL Divergence weight to 0 in a VAE loss function?",
                    "options": [
                        "The model becomes a deterministic autoencoder with no regularization on its latent space, creating gaps and rendering random generative sampling ineffective.",
                        "The model generates perfect realistic photos.",
                        "The loss function explodes to infinity.",
                        "All latent dimensions collapse to zero."
                    ],
                    "correct": 0,
                    "explanation": "Without the KL penalty forcing the latent space toward $\\mathcal{N}(0, \\mathbf{I})$, the encoder will spread clusters far apart in arbitrary patterns, creating voids where the decoder has never been trained."
                },
                {
                    "question": "Why do standard VAEs often generate slightly blurry image reconstructions compared to GANs?",
                    "options": [
                        "Because VAEs use low-resolution monitors.",
                        "Because optimizing pixel-wise Mean Squared Error or Gaussian log-likelihood averages all possible plausible high-frequency textures, producing a smooth, blurry mean.",
                        "Because VAEs cannot use convolutional layers.",
                        "Because VAEs run only on CPUs."
                    ],
                    "correct": 1,
                    "explanation": "Pixel-wise MSE penalizes being off on individual pixels. Averaging across multi-modal valid sharp textures mathematically minimizes squared error by outputting a blurry average."
                }
            ]
        },
        {
            "id": "D10",
            "title": "Generative Adversarial Networks (GANs)",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["D01", "D02", "D06", "D09"],
            "estimatedMinutes": 25,
            "tags": ["gan", "generative", "adversarial", "minimax", "generator", "discriminator"],
            "shortDesc": "Pitting two neural networks in a minimax game: a Generator synthesizing realistic samples and a Discriminator detecting fakes.",
            "sections": {
                "whatItIs": "Generative Adversarial Networks (GANs), introduced by Ian Goodfellow in 2014, formulate generative modeling as a two-player zero-sum game. A <strong>Generator</strong> $G$ maps random noise vectors $\\mathbf{z}$ to synthetic data samples, while a <strong>Discriminator</strong> $D$ learns to distinguish real training examples from synthetic fakes. As they compete, the Generator learns to synthesize remarkably realistic data.",
                "problemItSolves": "Overcomes the blurry sample limitations of VAEs. Instead of optimizing rigid pixel-wise distance metrics, GANs learn a dynamic, adaptive loss function directly through the Discriminator.",
                "intuition": "Think of an art forger (Generator) and an art detective (Discriminator). At first, the forger produces childish scrawls; the detective easily identifies them as fakes. The forger studies why the fakes were caught and refines their brushwork. The detective buys newer microscopes. Eventually, the forger produces masterpieces so flawless that even the detective cannot tell them apart from genuine Rembrandts.",
                "howItWorks": "1. <strong>Sample Noise:</strong> Draw latent vector $\\mathbf{z} \\sim \\mathcal{N}(0, \\mathbf{I})$.<br>2. <strong>Generate Fake:</strong> Generator produces synthetic sample $\\mathbf{x}_{\\text{fake}} = G(\\mathbf{z})$.<br>3. <strong>Train Discriminator:</strong> Maximize probability of assigning label 1 to real images and 0 to fake images.<br>4. <strong>Train Generator:</strong> Maximize probability of Discriminator mistakenly labeling fake images as real ($D(G(\\mathbf{z})) \\approx 1$).<br>5. <strong>Nash Equilibrium:</strong> Training reaches equilibrium when $D(\\mathbf{x}) = 0.5$ everywhere.",
                "mathematics": "Minimax Objective Function:<br>$$\\min_G \\max_D V(D, G) = \\mathbb{E}_{\\mathbf{x} \\sim p_{\\text{data}}(\\mathbf{x})}\\left[ \\log D(\\mathbf{x}) \\right] + \\mathbb{E}_{\\mathbf{z} \\sim p_{\\mathbf{z}}(\\mathbf{z})}\\left[ \\log(1 - D(G(\\mathbf{z}))) \\right]$$<br>At global optimality, the generator reproduces the true data distribution $p_g = p_{\\text{data}}$, minimizing the Jensen-Shannon Divergence:<br>$$V(D^*, G) = -\\log(4) + 2 \\cdot \\text{JSD}(p_{\\text{data}} \\parallel p_g)$$<br>Wasserstein GAN (WGAN) Earth Mover's Distance with 1-Lipschitz condition:<br>$$\\min_G \\max_{D \\in \\mathcal{D}_L} \\mathbb{E}[D(\\mathbf{x})] - \\mathbb{E}[D(G(\\mathbf{z}))]$$",
                "dataRequirements": "Unlabeled image, audio, or video datasets. Pixel values normalized to $[-1, 1]$ (matching Generator Tanh output layer).",
                "hyperparameters": [
                    {"name": "Learning Rates", "description": "Often tuned independently for $G$ and $D$ (e.g. TTUR - Two Time-scale Update Rule).", "effect": "Prevents one network from overpowering the other."},
                    {"name": "Gradient Penalty Weight (\\lambda)", "description": "Penalty enforcing 1-Lipschitz continuity in WGAN-GP.", "effect": "Prevents discriminator gradient explosion, drastically stabilizing training."}
                ],
                "strengths": [
                    "Generates razor-sharp, high-frequency realistic visual details.",
                    "No explicit probability density calculation required (implicit generative model).",
                    "Enables creative tasks: image-to-image translation (CycleGAN, Pix2Pix), style transfer (StyleGAN), super-resolution."
                ],
                "limitations": [
                    "Training instability: non-convergence, oscillations, and vanishing gradients.",
                    "<strong>Mode Collapse:</strong> Generator finds a single realistic sample (e.g. only generating one specific face) and outputs it repeatedly.",
                    "No direct inference mechanism to map real images back into latent space $\\mathbf{z}$."
                ],
                "evaluation": "Evaluated using **Fréchet Inception Distance (FID)** (lower is better, measuring distance between feature distributions in Inception-v3) and Inception Score (IS).",
                "workedExample": "StyleGAN synthesizing hyper-realistic human faces at $1024 \\times 1024$ resolution. The generator disentangles coarse styles (pose, face shape), middle styles (hair, facial features), and fine styles (micro-texture, eye color) into an intermediate latent space $\\mathcal{W}$, creating portraits indistinguishable from real photography.",
                "whenToUse": "Use for high-fidelity image-to-image translation, super-resolution, video frame synthesis, and photorealistic asset generation.",
                "commonMistakes": [
                    "Letting the Discriminator become too powerful early in training, causing Generator gradients to vanish.",
                    "Evaluating GAN quality purely by looking at loss curves (GAN loss curves oscillate and do not reflect image quality; use FID instead)."
                ],
                "furtherLearning": [
                    {"title": "Goodfellow et al.: Generative Adversarial Networks (NIPS 2014)", "url": "https://arxiv.org/abs/1406.2661"},
                    {"title": "Arjovsky, Chintala, Bottou: Wasserstein GAN (2017)", "url": "https://arxiv.org/abs/1701.07875"},
                    {"title": "Karras et al.: A Style-Based Generator Architecture for GANs (StyleGAN 2019)", "url": "https://arxiv.org/abs/1812.04948"}
                ]
            },
            "quiz": [
                {
                    "question": "What is 'Mode Collapse' in GAN training?",
                    "options": [
                        "When the GPU runs out of memory.",
                        "When the Generator learns to produce only a very limited variety of outputs (or a single sample) that reliably fools the Discriminator, ignoring the diversity of the training distribution.",
                        "When the Discriminator accuracy reaches 100%.",
                        "When all weights become zero."
                    ],
                    "correct": 1,
                    "explanation": "Mode collapse occurs when the generator discovers a few specific modes that fool the discriminator and simply outputs those repeatedly, completely failing to capture the full diversity of the real dataset."
                },
                {
                    "question": "What is currently the standard quantitative metric for evaluating GAN image synthesis quality and diversity?",
                    "options": [
                        "Mean Squared Error (MSE)",
                        "Fréchet Inception Distance (FID)",
                        "Accuracy",
                        "R-Squared"
                    ],
                    "correct": 1,
                    "explanation": "FID measures the Wasserstein-2 distance between Gaussian approximations of features extracted by an Inception network on real vs generated images. Lower FID scores indicate higher realism and diversity."
                },
                {
                    "question": "Why did Wasserstein GAN (WGAN) replace Jensen-Shannon divergence with the Earth Mover's Distance?",
                    "options": [
                        "Because Earth Mover's distance provides continuous, meaningful gradients everywhere, even when the real and generated distributions have disjoint, non-overlapping supports.",
                        "Because JS divergence cannot run on GPUs.",
                        "To turn GANs into supervised models.",
                        "To eliminate the Generator."
                    ],
                    "correct": 0,
                    "explanation": "When two distributions do not overlap in high-dimensional space, JS divergence saturates at a constant $\\log 2$, producing zero gradients. Wasserstein distance provides smooth, linear gradients everywhere."
                }
            ]
        },
        {
            "id": "D11",
            "title": "Attention Mechanisms & Transformers",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["D01", "D02", "D05", "D07"],
            "estimatedMinutes": 30,
            "tags": ["transformers", "attention", "self-attention", "query-key-value", "multi-head"],
            "shortDesc": "The architecture powering modern AI: Scaled Dot-Product Attention, Multi-Head Self-Attention, and Transformer blocks.",
            "sections": {
                "whatItIs": "The Transformer, introduced in 'Attention Is All You Need' (Vaswani et al., 2017), is the foundational deep learning architecture underpinning modern Large Language Models, Vision Transformers, and Multimodal systems. It completely replaces recurrent sequential processing with **Multi-Head Self-Attention**, allowing every token in a sequence to attend directly to every other token in parallel.",
                "problemItSolves": "RNNs and LSTMs process text sequentially step-by-step, making long-distance context decay and preventing GPU hardware parallelization. Transformers compute all pairwise token interactions simultaneously in $\\mathcal{O}(1)$ sequential operations.",
                "intuition": "Imagine a cocktail party with 20 people. An RNN is like whispering a message down a single file line. Self-Attention is everyone standing in an open circle: when someone speaks the word 'bank', they instantly make direct eye contact with the person wearing a fishing vest ('river bank') or the person holding a checkbook ('financial bank'), resolving word meaning through simultaneous pairwise context.",
                "howItWorks": "1. <strong>Linear Projections:</strong> Project input embeddings into Queries ($\\mathbf{Q}$), Keys ($\\mathbf{K}$), and Values ($\\mathbf{V}$) via learnable matrices.<br>2. <strong>Scaled Dot-Product:</strong> Compute attention scores: $\\text{Score} = \\frac{\\mathbf{Q} \\mathbf{K}^T}{\\sqrt{d_k}}$.<br>3. <strong>Softmax Normalization:</strong> Convert scores into probability weights that sum to 1.<br>4. <strong>Weighted Sum:</strong> Multiply weights by Values: $\\text{Attention} = \\text{softmax}\\left(\\frac{\\mathbf{Q}\\mathbf{K}^T}{\\sqrt{d_k}}\\right) \\mathbf{V}$.<br>5. <strong>Multi-Head:</strong> Run $H$ attention heads in parallel to capture distinct relational subspaces (syntax, coreference, semantics).<br>6. <strong>Feedforward & Norm:</strong> Apply LayerNorm, residual skip connections, and position-wise MLPs.",
                "mathematics": "Scaled Dot-Product Attention:<br>$$\\text{Attention}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V}) = \\text{softmax}\\left( \\frac{\\mathbf{Q}\\mathbf{K}^T}{\\sqrt{d_k}} + \\mathbf{M} \\right) \\mathbf{V}$$<br>where $\\mathbf{M}$ is an optional causal mask (setting future tokens to $-\\infty$).<br>Multi-Head Attention:<br>$$\\text{MultiHead}(\\mathbf{Q}, \\mathbf{K}, \\mathbf{V}) = \\text{Concat}(\\text{head}_1, \\dots, \\text{head}_h) \\mathbf{W}^O$$<br>$$\\text{where } \\text{head}_i = \\text{Attention}(\\mathbf{Q}\\mathbf{W}_i^Q, \\mathbf{K}\\mathbf{W}_i^K, \\mathbf{V}\\mathbf{W}_i^V)$$<br>Scaling factor $\\frac{1}{\\sqrt{d_k}}$ prevents dot products from growing excessively large in high dimensions, which would push softmax into regions with vanishing gradients.",
                "dataRequirements": "Tokenized text sequences converted into dense embedding vectors plus Positional Encodings (Sinusoidal, RoPE, or Learned) since self-attention is permutation-invariant by default.",
                "hyperparameters": [
                    {"name": "Number of Heads (h)", "description": "Number of parallel attention projections (e.g. 8 to 128).", "effect": "Allows the model to attend to multiple semantic relationships simultaneously."},
                    {"name": "Hidden Dimension (d_model)", "description": "Embedding size (e.g. 768 in BERT-Base; 4096 in Llama-3-8B).", "effect": "Determines model capacity and width."},
                    {"name": "Context Window Length (N)", "description": "Maximum sequence token length.", "effect": "Attention matrix scales quadratically $\\mathcal{O}(N^2)$ in compute and memory."}
                ],
                "strengths": [
                    "Fully parallelizable training across GPUs: all tokens are processed concurrently.",
                    "Direct path length $\\mathcal{O}(1)$ between any two tokens across arbitrary distances.",
                    "State-of-the-art across natural language processing, computer vision (ViT), and audio processing.",
                    "Remarkable emergent capabilities and scaling laws as parameters and data increase."
                ],
                "limitations": [
                    "Quadratic complexity $\\mathcal{O}(N^2)$ in time and memory with respect to sequence length (mitigated by FlashAttention).",
                    "Requires massive compute clusters and billions of tokens to train effectively.",
                    "Zero inherent concept of sequential word order without explicit positional encodings."
                ],
                "evaluation": "Evaluated using Perplexity on held-out text corpora and standard task benchmarks (MMLU, HumanEval, GSM8K).",
                "workedExample": "Disambiguating pronouns: 'The animal didn't cross the street because it was too tired.' When computing the attention representation for 'it', the query vector of 'it' has the highest dot product with the key vector of 'animal' (score 0.82), transferring 'animal's properties into 'it'. If the sentence ended with 'too wide', 'it' would attend to 'street'.",
                "whenToUse": "The architecture of choice for all frontier natural language, multimodal, and generative modeling applications.",
                "commonMistakes": [
                    "Forgetting positional encodings (without them, the Transformer treats 'dog bites man' and 'man bites dog' as identical bag of words).",
                    "Not using causal masking during autoregressive language pretraining, allowing tokens to cheat by looking into the future."
                ],
                "furtherLearning": [
                    {"title": "Vaswani et al.: Attention Is All You Need (NeurIPS 2017 Original Transformer Paper)", "url": "https://arxiv.org/abs/1706.03762"},
                    {"title": "Jay Alammar: The Illustrated Transformer", "url": "https://jalammar.github.io/illustrated-transformer/"},
                    {"title": "Dao et al.: FlashAttention: Fast and Memory-Efficient Exact Attention", "url": "https://arxiv.org/abs/2205.14135"}
                ]
            },
            "quiz": [
                {
                    "question": "Why is the dot product $\\mathbf{Q}\\mathbf{K}^T$ scaled by $\\frac{1}{\\sqrt{d_k}}$ in Scaled Dot-Product Attention?",
                    "options": [
                        "To make the matrix square.",
                        "For large values of $d_k$, dot products grow large in magnitude, pushing the Softmax function into regions with near-zero gradients (vanishing gradients); dividing by $\\sqrt{d_k}$ keeps variance at 1.0.",
                        "To convert negative attention to positive.",
                        "To reduce the number of tokens."
                    ],
                    "correct": 1,
                    "explanation": "If components of $Q$ and $K$ are independent with variance 1, their dot product has variance $d_k$. For large dimensions, large scores saturate softmax, causing gradients to vanish. Scaling by $\\sqrt{d_k}$ stabilizes softmax gradients."
                },
                {
                    "question": "What would happen if you removed Positional Encodings from a Transformer model?",
                    "options": [
                        "The model could not output words.",
                        "The model would be completely permutation-invariant, treating 'Alice likes Bob' and 'Bob likes Alice' as identical inputs.",
                        "Training would take twice as long.",
                        "The model would crash."
                    ],
                    "correct": 1,
                    "explanation": "Self-attention computes pairwise set operations without any intrinsic concept of order. Without positional encodings, any permutation of the input tokens yields identical attention representations."
                },
                {
                    "question": "What is the computational complexity of standard self-attention with respect to sequence length $N$?",
                    "options": [
                        "$\\mathcal{O}(N)$ linear",
                        "$\\mathcal{O}(N^2)$ quadratic",
                        "$\\mathcal{O}(\\log N)$ logarithmic",
                        "$\\mathcal{O}(1)$ constant"
                    ],
                    "correct": 1,
                    "explanation": "Computing pairwise dot products between all $N$ queries and all $N$ keys creates an $N \\times N$ attention matrix, scaling quadratically $\\mathcal{O}(N^2)$ in compute and memory."
                }
            ]
        },
        {
            "id": "D12",
            "title": "Embeddings & Representation Learning",
            "module": "deeplearning",
            "level": "intermediate",
            "prerequisites": ["D01", "D11"],
            "estimatedMinutes": 20,
            "tags": ["embeddings", "word2vec", "vector-space", "representation-learning", "cosine-similarity"],
            "shortDesc": "Map discrete categorical entities into dense, continuous vector spaces where geometric distances reflect semantic meaning.",
            "sections": {
                "whatItIs": "An Embedding is a learned mapping that translates high-dimensional, discrete entities (words, users, items, graphs) into low-dimensional, dense continuous vector spaces $\\mathbb{R}^d$. In this learned space, geometric proximity (Euclidean distance, Cosine similarity) and directional vectors encode semantic relationships and analogies.",
                "problemItSolves": "One-hot encodings are high-dimensional, sparse ($|V| > 100,000$), and orthogonal: the dot product between 'cat' and 'kitten' is 0, treating them as no more similar than 'cat' and 'submarine'. Embeddings compress vocabulary into dense continuous representations where similar concepts cluster together.",
                "intuition": "Imagine placing every animal in the world in a 3D room. You place mammals near the floor, birds near the ceiling; carnivores on the left, herbivores on the right; pets near the door, wild beasts by the window. The physical 3D coordinates $(x, y, z)$ of each animal are its embedding, capturing its biological traits without spelling them out.",
                "howItWorks": "1. <strong>Embedding Lookup Table:</strong> A matrix $\\mathbf{E} \\in \\mathbb{R}^{|V| \\times d}$ where row $i$ contains the vector for token $i$.<br>2. <strong>Word2Vec (Skip-Gram with Negative Sampling):</strong> Predict context words given a target word, maximizing dot product of true co-occurrences while minimizing dot products with random noise words.<br>3. <strong>Subword Embeddings (BPE / WordPiece):</strong> Break words into subword units (e.g. 'un' + 'break' + 'able') to handle out-of-vocabulary words.<br>4. <strong>Contextual Embeddings:</strong> Modern Transformer models generate dynamic embeddings that change based on surrounding text context.",
                "mathematics": "Skip-Gram with Negative Sampling (SGNS) Objective:<br>$$\\mathcal{L} = \\log \\sigma(\\mathbf{v}_{w_O}'^T \\mathbf{v}_{w_I}) + \\sum_{i=1}^k \\mathbb{E}_{w_i \\sim P_n(w)} \\left[ \\log \\sigma(-\\mathbf{v}_{w_i}'^T \\mathbf{v}_{w_I}) \\right]$$<br>Cosine Similarity between vectors $\\mathbf{u}$ and $\\mathbf{v}$:<br>$$\\text{CosineSim}(\\mathbf{u}, \\mathbf{v}) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\| \\|\\mathbf{v}\\|} = \\cos(\\theta)$$<br>Famous Vector Analogy Arithmetic (Mikolov et al., 2013):<br>$$\\mathbf{v}_{\\text{King}} - \\mathbf{v}_{\\text{Man}} + \\mathbf{v}_{\\text{Woman}} \\approx \\mathbf{v}_{\\text{Queen}}$$",
                "dataRequirements": "Large corpora of raw text. Subword tokenization (Byte-Pair Encoding) is required to ensure fixed vocabulary sizes (typically 32,000 to 128,000 tokens).",
                "hyperparameters": [
                    {"name": "Embedding Dimension (d)", "description": "Vector length (typically 128 to 1536).", "effect": "Higher dimensions capture subtle semantic nuances but increase compute."},
                    {"name": "Window Size", "description": "Context window used during pretraining.", "effect": "Small windows capture syntactic roles; large windows capture broad topical semantics."}
                ],
                "strengths": [
                    "Dense representations prevent the Curse of Dimensionality.",
                    "Captures rich semantic and relational analogies geometrically.",
                    "Serves as the universal input interface for text, recommendation items, and multimodal models."
                ],
                "limitations": [
                    "Static embeddings (Word2Vec, GloVe) cannot handle polysemy: 'bank' has only one vector, conflating river banks and financial banks.",
                    "Embeddings inherit and amplify societal, gender, and racial biases present in training corpora."
                ],
                "evaluation": "Evaluated using Word Analogy test accuracy ($A:B :: C:D$), WordSim similarity benchmarks, and Retrieval MRR/NDCG.",
                "workedExample": "Semantic vector search: A customer queries 'cheap winter footwear'. The query is embedded into a 512D vector. Running Approximate Nearest Neighbor search (e.g. HNSW/FAISS) finds product vectors with highest cosine similarity, retrieving 'budget snow boots' even though none of the exact query words match the product title.",
                "whenToUse": "Everywhere in modern AI: semantic search, retrieval-augmented generation (RAG), vector databases, recommendation collaborative filtering, and text classification.",
                "commonMistakes": [
                    "Using raw Euclidean distance instead of Cosine Similarity without normalizing vector lengths first.",
                    "Assuming static embeddings can resolve context-dependent word meanings."
                ],
                "furtherLearning": [
                    {"title": "Mikolov et al.: Distributed Representations of Words and Phrases (Word2Vec 2013)", "url": "https://arxiv.org/abs/1310.4546"},
                    {"title": "Pennington et al.: GloVe: Global Vectors for Word Representation (2014)", "url": "https://nlp.stanford.edu/pubs/glove.pdf"}
                ]
            },
            "quiz": [
                {
                    "question": "What classic vector arithmetic demonstration proved that Word2Vec embeddings capture linear semantic relationships?",
                    "options": [
                        "Cat + Dog = Horse",
                        "Vector('King') - Vector('Man') + Vector('Woman') $\\approx$ Vector('Queen')",
                        "Apple - Banana = Orange",
                        "Red + Blue = Green"
                    ],
                    "correct": 1,
                    "explanation": "Mikolov et al. demonstrated that subtracting the male gender direction from 'King' and adding 'Woman' yielded a vector whose closest nearest neighbor was 'Queen'."
                },
                {
                    "question": "What is the primary limitation of static word embeddings (like Word2Vec and GloVe) that modern Transformers solve?",
                    "options": [
                        "Static embeddings cannot run on GPUs.",
                        "Static embeddings assign a single fixed vector to each word, failing to handle polysemy (words with multiple meanings depending on context, like 'Apple' the fruit vs 'Apple' the company).",
                        "Static embeddings only work in English.",
                        "Static embeddings are too slow."
                    ],
                    "correct": 1,
                    "explanation": "In static embeddings, every word has one fixed vector. Transformers compute dynamic contextual embeddings where the representation of 'Apple' adapts based on surrounding tokens."
                },
                {
                    "question": "What metric is most commonly used to measure the directional alignment between two normalized embedding vectors?",
                    "options": [
                        "Cosine Similarity",
                        "Gini Impurity",
                        "Hamming Distance",
                        "Mean Absolute Percentage Error"
                    ],
                    "correct": 0,
                    "explanation": "Cosine similarity measures the cosine of the angle between two vectors, ranging from -1 to +1, ignoring vector magnitude to measure purely semantic alignment."
                }
            ]
        },
        {
            "id": "D13",
            "title": "Large Language Models (LLMs)",
            "module": "deeplearning",
            "level": "advanced",
            "prerequisites": ["D01", "D03", "D11", "D12"],
            "estimatedMinutes": 30,
            "tags": ["llm", "transformers", "pretraining", "temperature", "prompting", "rlhf"],
            "shortDesc": "Pretraining, scaling laws, generation decoding (Temperature, Top-p), instruction tuning, RLHF, and failure modes of Large Language Models.",
            "sections": {
                "whatItIs": "Large Language Models (LLMs) are massive autoregressive decoder-only Transformers trained on trillions of tokens from the public internet. By learning to predict the next token via self-supervised cross-entropy loss, these models develop broad world knowledge, in-context learning capabilities, and reasoning patterns across billions of parameters.",
                "problemItSolves": "Eliminates the historical requirement of training task-specific narrow models for every individual NLP problem (translation, summarization, entity extraction, coding). A single foundation LLM can perform all these tasks through natural language prompting.",
                "intuition": "Think of an LLM as the world's most sophisticated autocomplete engine. Having read virtually all digitized human literature, it has learned the statistical grammar, logical structure, and factual connections of human language. Prompting it is like beginning an improv theater scene: the model completes the scene by predicting the most statistically coherent continuation.",
                "howItWorks": "1. <strong>Autoregressive Pretraining:</strong> Maximize log-likelihood of predicting token $t$ given past tokens $1 \\dots t-1$.<br>2. <strong>Inference Decoding:</strong> Convert output logits into probabilities via Softmax with <strong>Temperature</strong> scaling ($T$).<br>3. <strong>Sampling Strategies:</strong> Nucleus (Top-p) sampling filters the smallest set of tokens whose cumulative probability exceeds $p$.<br>4. <strong>Post-Training Alignment:</strong> Supervised Fine-Tuning (SFT) on conversational instructions followed by Reinforcement Learning from Human Feedback (RLHF / DPO) to steer models toward helpfulness, honesty, and safety.",
                "mathematics": "Autoregressive Next-Token Objective:<br>$$\\mathcal{L}(\\theta) = -\\sum_{i=1}^N \\log P_\\theta(x_i \\mid x_1, x_2, \\dots, x_{i-1})$$<br>Temperature-Scaled Softmax over vocabulary logits $z_i$:<br>$$P(x = i) = \\frac{\\exp(z_i / T)}{\\sum_j \\exp(z_j / T)}$$<br>As $T \\to 0$, distribution collapses to greedy argmax (deterministic); as $T \\to \\infty$, distribution flattens toward uniform random noise.<br>Chinchilla Scaling Laws (Hoffmann et al., 2022):<br>$$\\text{Optimal Parameters } N \\propto C^{0.5}, \\quad \\text{Optimal Tokens } D \\propto C^{0.5}$$",
                "dataRequirements": "Trillions of tokens of high-quality, filtered, de-duplicated web text, code repositories, academic papers, and books. Rigorous data curation is critical to remove toxicity and low-quality synthetic spam.",
                "hyperparameters": [
                    {"name": "Temperature (T)", "description": "Logit scaling factor (typically 0.0 to 1.0).", "effect": "Low $T$ (0.0-0.2) is focused and deterministic (coding/math); high $T$ (0.7-1.0) is creative."},
                    {"name": "Top-p (Nucleus)", "description": "Cumulative probability threshold (e.g. 0.9).", "effect": "Cuts off the long tail of bizarre or incoherent low-probability tokens."},
                    {"name": "Repetition Penalty", "description": "Penalizes logits of tokens that have already appeared.", "effect": "Prevents repetitive looping loops."}
                ],
                "strengths": [
                    "Extraordinary zero-shot and few-shot in-context learning capabilities.",
                    "Unified interface: natural language text in, natural language text or code out.",
                    "Emergent reasoning abilities through Chain-of-Thought (CoT) prompting."
                ],
                "limitations": [
                    "<strong>Hallucination:</strong> Confidently asserts factually false statements with high fluency.",
                    "Massive training compute cost (millions of dollars in GPU clusters).",
                    "Knowledge cutoff: static weights do not know real-time events without RAG or web search.",
                    "Susceptible to prompt injections and jailbreaks."
                ],
                "evaluation": "Evaluated using standardized benchmarks: MMLU (multitask knowledge), GSM8K (grade-school math), HumanEval (Python coding), and LMSYS Chatbot Arena Elo ratings.",
                "workedExample": "Code generation: Prompt: 'Write a Python function to verify palindrome strings.' An LLM with temperature $T=0.1$ samples greedily: `def is_palindrome(s): s = ''.join(c.lower() for c in s if c.isalnum()); return s == s[::-1]`, completing the task with production-ready syntax.",
                "whenToUse": "Use for text summarization, conversational AI, code synthesis, complex semantic extraction, and agentic workflows.",
                "commonMistakes": [
                    "Relying on an LLM as a deterministic database (LLMs are probabilistic generative models, prone to factual hallucinations).",
                    "Setting temperature too high for analytical, structured JSON extraction tasks.",
                    "Failing to implement Retrieval-Augmented Generation (RAG) when proprietary corporate knowledge is required."
                ],
                "furtherLearning": [
                    {"title": "Brown et al.: Language Models are Few-Shot Learners (GPT-3 2020)", "url": "https://arxiv.org/abs/2005.14165"},
                    {"title": "Ouyang et al.: Training language models to follow instructions (InstructGPT/RLHF 2022)", "url": "https://arxiv.org/abs/2203.02155"},
                    {"title": "LMSYS Chatbot Arena Leaderboard", "url": "https://chat.lmsys.org/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary effect of setting the sampling Temperature to 0.0 during LLM inference?",
                    "options": [
                        "The model generates completely random words.",
                        "The model becomes fully deterministic, always picking the single token with the highest predicted probability (Greedy decoding).",
                        "The model stops generating output.",
                        "The model runs backwards."
                    ],
                    "correct": 1,
                    "explanation": "At $T \\to 0$, the logit distribution becomes infinitely sharp, forcing the probability of the top token to 1.0 (pure greedy argmax selection)."
                },
                {
                    "question": "According to the Chinchilla scaling laws (Hoffmann et al.), what was the primary error in early LLM training like GPT-3?",
                    "options": [
                        "Models were trained for too few epochs on too many GPUs.",
                        "Models were severely undertrained: for optimal compute efficiency, dataset token count should scale equally with parameter count (roughly 20 tokens per parameter).",
                        "Models were using too many attention heads.",
                        "Transformers should have been replaced with RNNs."
                    ],
                    "correct": 1,
                    "explanation": "DeepMind's Chinchilla paper proved that most existing LLMs were over-parameterized and under-trained. For optimal compute, parameter count and training token count should scale in equal proportion."
                },
                {
                    "question": "What is 'Hallucination' in Large Language Models?",
                    "options": [
                        "When the model generates text in languages other than English.",
                        "When an LLM produces plausible-sounding statements that are factually false, ungrounded, or completely fabricated.",
                        "When the GPU runs out of VRAM.",
                        "A technique to increase token speed."
                    ],
                    "correct": 1,
                    "explanation": "Hallucination is the generation of fluent, convincing text that contradicts real-world facts or source materials, arising because LLMs optimize statistical likelihood rather than factual truth."
                }
            ]
        },
        {
            "id": "D14",
            "title": "Diffusion Models",
            "module": "deeplearning",
            "level": "advanced",
            "prerequisites": ["D01", "D02", "D06", "D09"],
            "estimatedMinutes": 25,
            "tags": ["diffusion", "generative", "score-matching", "ddpm", "denoising", "stable-diffusion"],
            "shortDesc": "Generate high-fidelity media by learning to reverse a gradual forward noise corruption process.",
            "sections": {
                "whatItIs": "Denoising Diffusion Probabilistic Models (DDPM) are the premier generative models for high-resolution images, video, and audio (powering Stable Diffusion, Midjourney, and DALL-E 3). They define a forward process that systematically corrupts data by adding Gaussian noise over hundreds of discrete time steps, and train a neural network (typically a U-Net) to reverse this process step-by-step to synthesize clean data from pure noise.",
                "problemItSolves": "Overcomes the training instability and mode collapse of GANs, as well as the blurry sample limitations of VAEs. Diffusion models offer stable training objectives and superior sample fidelity and diversity.",
                "intuition": "Imagine dropping a drop of blue ink into a glass of water. Over time, the ink particles diffuse until the water is a completely uniform, hazy blue cloud (Forward Process). A diffusion model is like training a magical microscopic robot that watches the cloud and learns how to push every water molecule backwards, step by step, until the uniform blue haze re-coalesces into a single pristine ink droplet (Reverse Process).",
                "howItWorks": "1. <strong>Forward Diffusion Process ($q$):</strong> Gradually add Gaussian noise according to variance schedule $\\beta_1, \\dots, \\beta_T$, converting input image $\\mathbf{x}_0$ into pure white noise $\\mathbf{x}_T \\sim \\mathcal{N}(0, \\mathbf{I})$.<br>2. <strong>Closed-Form Forward Jump:</strong> Sample $\\mathbf{x}_t$ at any arbitrary step $t$ directly without calculating intermediate steps: $\\mathbf{x}_t = \\sqrt{\\bar{\\alpha}_t} \\mathbf{x}_0 + \\sqrt{1 - \\bar{\\alpha}_t} \\boldsymbol{\\epsilon}$.<br>3. <strong>Training:</strong> Train a U-Net $\\boldsymbol{\\epsilon}_\\theta(\\mathbf{x}_t, t)$ to predict the added noise vector $\\boldsymbol{\\epsilon}$.<br>4. <strong>Reverse Generation ($p_\\theta$):</strong> Start with pure Gaussian noise $\\mathbf{x}_T$; iteratively subtract the predicted noise at each step $t$ down to $t=0$.",
                "mathematics": "Forward Noise Sampling at step $t$ (where $\\alpha_t = 1 - \\beta_t$ and $\\bar{\\alpha}_t = \\prod_{s=1}^t \\alpha_s$):<br>$$\\mathbf{x}_t = \\sqrt{\\bar{\\alpha}_t} \\mathbf{x}_0 + \\sqrt{1 - \\bar{\\alpha}_t} \\boldsymbol{\\epsilon}, \\quad \\boldsymbol{\\epsilon} \\sim \\mathcal{N}(0, \\mathbf{I})$$<br>Simplified DDPM Training Objective (Ho et al., 2020):<br>$$\\mathcal{L}_{\\text{simple}}(\\theta) = \\mathbb{E}_{t, \\mathbf{x}_0, \\boldsymbol{\\epsilon}}\\left[ \\left\\| \\boldsymbol{\\epsilon} - \\boldsymbol{\\epsilon}_\\theta\\left( \\sqrt{\\bar{\\alpha}_t} \\mathbf{x}_0 + \\sqrt{1 - \\bar{\\alpha}_t} \\boldsymbol{\\epsilon}, t \\right) \\right\\|^2 \\right]$$<br>Classifier-Free Guidance (CFG) for prompt conditioning $\\mathbf{c}$ with guidance scale $w$:<br>$$\\tilde{\\boldsymbol{\\epsilon}}_\\theta(\\mathbf{x}_t, \\mathbf{c}) = \\boldsymbol{\\epsilon}_\\theta(\\mathbf{x}_t, \\emptyset) + w \\left( \\boldsymbol{\\epsilon}_\\theta(\\mathbf{x}_t, \\mathbf{c}) - \\boldsymbol{\\epsilon}_\\theta(\\mathbf{x}_t, \\emptyset) \\right)$$",
                "dataRequirements": "Images, audio spectrograms, or 3D point clouds. In <strong>Latent Diffusion Models</strong> (Stable Diffusion), the diffusion process runs inside a compressed latent space learned by a pre-trained VAE, reducing compute by 10x.",
                "hyperparameters": [
                    {"name": "Sampling Steps", "description": "Number of denoising steps during inference (e.g. 20 to 50 using fast DDIM/Euler samplers).", "effect": "More steps improve fine detail at the cost of latency."},
                    {"name": "Classifier-Free Guidance (CFG)", "description": "Weight $w$ amplifying adherence to text prompt (typically 5.0 to 8.0).", "effect": "Higher CFG forces strict prompt adherence; too high causes oversaturated color burn."},
                    {"name": "Noise Schedule", "description": "Linear, Cosine, or Sigmoid variance schedule $\\beta_t$.", "effect": "Controls rate of noise corruption."}
                ],
                "strengths": [
                    "Exceptional photorealism and fine detail generation.",
                    "Extremely stable training dynamics with standard Mean Squared Error loss.",
                    "No mode collapse: reliably covers all modes of the data distribution.",
                    "Flexible conditioning: text-to-image, inpainting, outpainting, and depth conditioning (ControlNet)."
                ],
                "limitations": [
                    "Slow inference: requires multiple iterative forward passes through a heavy U-Net/DiT to produce a single image.",
                    "High compute required during iterative sampling (accelerated by distillation techniques like LCM/SDXL-Turbo)."
                ],
                "evaluation": "Evaluated using Fréchet Inception Distance (FID), Inception Score (IS), and CLIP Score (measuring text-image prompt alignment).",
                "workedExample": "Generating an astronaut riding a horse. Latent Diffusion starts with a $64 \\times 64 \\times 4$ tensor of pure Gaussian noise. The text prompt is encoded via a CLIP text encoder. Over 30 denoising steps, the model predicts and subtracts noise vectors conditioned on the text embedding, until decoding produces a crisp $1024 \\times 1024$ photo.",
                "whenToUse": "The state-of-the-art choice for high-resolution visual synthesis, video generation (Sora), audio generation, and structural protein design (AlphaFold3).",
                "commonMistakes": [
                    "Setting the CFG scale too high (>15), producing high-contrast artifacts and burned colors.",
                    "Using naive DDPM sampling with 1000 steps in production instead of modern accelerated ODE solvers (DDIM, DPM-Solver) that take 20 steps."
                ],
                "furtherLearning": [
                    {"title": "Ho, Jain, Abbeel: Denoising Diffusion Probabilistic Models (DDPM 2020)", "url": "https://arxiv.org/abs/2006.11239"},
                    {"title": "Rombach et al.: High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion 2022)", "url": "https://arxiv.org/abs/2112.10752"},
                    {"title": "Lilian Weng: What are Diffusion Models?", "url": "https://lilianweng.github.io/posts/2021-07-11-diffusion-models/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary operational role of the neural network (U-Net or DiT) in a Denoising Diffusion Probabilistic Model?",
                    "options": [
                        "It classifies images into 1000 categories.",
                        "It predicts the exact noise vector $\\boldsymbol{\\epsilon}$ that was added to a noisy image at time step $t$.",
                        "It compresses the image file to JPEG.",
                        "It calculates the gradient of the learning rate."
                    ],
                    "correct": 1,
                    "explanation": "During training, an image is corrupted with known Gaussian noise $\\boldsymbol{\\epsilon}$ at step $t$. The neural network is trained via MSE to predict that exact noise vector so it can be subtracted during reverse generation."
                },
                {
                    "question": "How did Latent Diffusion Models (like Stable Diffusion) make diffusion training computationally feasible on consumer hardware?",
                    "options": [
                        "They stopped using GPUs.",
                        "They perform the diffusion process inside the low-dimensional latent space of a pre-trained Autoencoder rather than in high-resolution pixel space.",
                        "They only generate black and white images.",
                        "They eliminated all denoising steps."
                    ],
                    "correct": 1,
                    "explanation": "Diffusing in raw pixel space ($512 \\times 512 \\times 3$) is computationally crushing. Latent Diffusion encodes the image into an $8x$ smaller latent space ($64 \\times 64 \\times 4$), reducing computation by an order of magnitude."
                },
                {
                    "question": "What is the function of Classifier-Free Guidance (CFG) in text-to-image diffusion?",
                    "options": [
                        "It acts as a spellchecker for prompts.",
                        "It extrapolates the generated trajectory toward the conditional prompt direction and away from the unconditional prediction, dramatically improving text-image alignment.",
                        "It deletes all images with people.",
                        "It converts diffusion into a GAN."
                    ],
                    "correct": 1,
                    "explanation": "CFG combines an unconditional prediction with a text-conditioned prediction, pushing the denoising step in the direction of the prompt vector to ensure high prompt fidelity."
                }
            ]
        },
        {
            "id": "D15",
            "title": "Graph Neural Networks (GNNs)",
            "module": "deeplearning",
            "level": "advanced",
            "prerequisites": ["D01", "D02", "D05"],
            "estimatedMinutes": 25,
            "tags": ["gnn", "graph-convolution", "message-passing", "molecular-ml", "relational"],
            "shortDesc": "Learn on non-Euclidean graph topologies using iterative message passing between neighboring nodes and edges.",
            "sections": {
                "whatItIs": "Graph Neural Networks (GNNs) are deep architectures specialized for non-Euclidean graph-structured data $\\mathcal{G} = (\\mathcal{V}, \\mathcal{E})$. Through the **Message Passing** paradigm, nodes iteratively aggregate feature vectors from their local topological neighbors, updating their internal representations to encode both local attributes and structural graph connectivity.",
                "problemItSolves": "Standard CNNs and MLPs assume rigid Euclidean grids (1D sequences or 2D image matrices). Real-world structures like molecules (atoms & bonds), social networks, citation networks, and financial transaction graphs have arbitrary, irregular connectivity that defeats standard architectures.",
                "intuition": "Imagine a social gossip network. Each person has a list of hobbies (node features). In Round 1, everyone tells their immediate friends what their hobbies are. In Round 2, people share what their friends told them. By Round 3, everyone's personal knowledge incorporates information from people three handshakes away, reflecting both who they are and where they sit in the social web.",
                "howItWorks": "1. <strong>Message Generation:</strong> For each directed edge $(u, v)$, compute a message vector $\\mathbf{m}_{u \\to v} = \\text{MSG}(\\mathbf{h}_u, \\mathbf{h}_v, \\mathbf{e}_{uv})$.<br>2. <strong>Permutation-Invariant Aggregation:</strong> Aggregate all incoming messages to node $v$ using an order-independent function (Sum, Mean, Max).<br>3. <strong>Node Update:</strong> Update target node's state: $\\mathbf{h}_v^{(k)} = \\text{UPDATE}(\\mathbf{h}_v^{(k-1)}, \\mathbf{a}_v^{(k)})$.<br>4. <strong>Tasks:</strong> Node classification, Edge link prediction, or Global graph readout (pooling all nodes to classify an entire molecule).",
                "mathematics": "Generic Message Passing Formulation (Gilmer et al., 2017):<br>$$\\mathbf{m}_v^{(k)} = \\sum_{u \\in \\mathcal{N}(v)} M_k\\left(\\mathbf{h}_u^{(k-1)}, \\mathbf{h}_v^{(k-1)}, \\mathbf{e}_{uv}\\right)$$<br>$$\\mathbf{h}_v^{(k)} = U_k\\left(\\mathbf{h}_v^{(k-1)}, \\mathbf{m}_v^{(k)}\\right)$$<br>Graph Convolutional Network (GCN - Kipf & Welling, 2016) Layer:<br>$$\\mathbf{H}^{(k+1)} = \\sigma\\left( \\mathbf{\\tilde{D}}^{-\\frac{1}{2}} \\mathbf{\\tilde{A}} \\mathbf{\\tilde{D}}^{-\\frac{1}{2}} \\mathbf{H}^{(k)} \\mathbf{W}^{(k)} \\right)$$<br>where $\\mathbf{\\tilde{A}} = \\mathbf{A} + \\mathbf{I}_N$ is the adjacency matrix with added self-loops and $\\mathbf{\\tilde{D}}$ is its diagonal degree matrix.",
                "dataRequirements": "Graph data: Node feature matrix $\\mathbf{X} \\in \\mathbb{R}^{N \\times D}$, sparse adjacency matrix or edge index tensor $\\mathbf{E} \\in \\mathbb{R}^{2 \\times |E|}$, and optional edge attribute matrix.",
                "hyperparameters": [
                    {"name": "Number of Layers (K)", "description": "Number of message-passing iterations (typically 2 to 6).", "effect": "Determines neighborhood hop radius. Too many layers causes **Oversmoothing**."},
                    {"name": "Aggregation Function", "description": "Sum vs Mean vs Max vs Attention (GAT).", "effect": "Sum distinguishes structural multiset differences (GIN); Attention dynamically weights neighbor significance."},
                    {"name": "Readout Function", "description": "Global pooling operator (Sum, Mean, Set2Set).", "effect": "Aggregates node embeddings into a single graph-level embedding."}
                ],
                "strengths": [
                    "Permutation Invariance: graph labeling order does not change output.",
                    "Handles arbitrary, dynamic graph topologies naturally.",
                    "Revolutionized drug discovery, quantum chemistry, and molecular property prediction.",
                    "Excels at fraud ring detection and recommender systems (Pinterest, Uber Eats)."
                ],
                "limitations": [
                    "<strong>Oversmoothing:</strong> Stacking deep GNN layers causes all node embeddings to converge to identical uniform vectors.",
                    "Expressive upper bound: Standard message-passing GNNs cannot be more expressive than the 1-Weisfeiler-Lehman (1-WL) graph isomorphism test.",
                    "Scalability challenges on massive giant graphs (e.g. billion-node social graphs require neighbor sampling algorithms like GraphSAGE)."
                ],
                "evaluation": "Evaluated using Node Accuracy/F1, Link Prediction ROC-AUC, and Graph-level RMSE (e.g. molecular binding affinity).",
                "workedExample": "Predicting drug toxicity (e.g. MoleculeNet). Atoms are nodes (encoded by element type, formal charge); chemical bonds are edges (single, double, aromatic). A 3-layer GCN propagates electronic information across rings and functional groups. A global sum readout pools all atomic representations into a molecular vector, predicting mutagenic toxicity with 91% accuracy.",
                "whenToUse": "Use for molecular chemistry, material science, protein folding, fraud ring network analysis, knowledge graphs, and chip design.",
                "commonMistakes": [
                    "Stacking 20 GNN layers expecting higher accuracy (causes complete oversmoothing; keep GNNs shallow, 2-5 layers, or use residual skip connections).",
                    "Forgetting self-loops in the adjacency matrix (a node ignores its own existing state during neighbor aggregation)."
                ],
                "furtherLearning": [
                    {"title": "Kipf & Welling: Semi-Supervised Classification with Graph Convolutional Networks (ICLR 2017)", "url": "https://arxiv.org/abs/1609.02907"},
                    {"title": "Hamilton: Graph Representation Learning Book (Free PDF)", "url": "https://www.cs.mcgill.ca/~wlh/grl_book/"},
                    {"title": "PyTorch Geometric (PyG) Documentation", "url": "https://pytorch-geometric.readthedocs.io/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the 'Oversmoothing' problem in Graph Neural Networks?",
                    "options": [
                        "The graph loses all edges.",
                        "When stacking too many message-passing layers, repeated averaging causes node embeddings across the entire graph to converge toward identical, indistinguishable vectors.",
                        "The computer runs out of disk storage.",
                        "Graph nodes become disconnected."
                    ],
                    "correct": 1,
                    "explanation": "Because message passing acts like Laplacian smoothing across the graph, repeatedly mixing neighbor features over many layers washes out distinct individual node differences."
                },
                {
                    "question": "What is the theoretical upper bound on the expressive power of standard message-passing GNNs to distinguish non-isomorphic graphs?",
                    "options": [
                        "Turing completeness.",
                        "The 1-Weisfeiler-Lehman (1-WL) graph isomorphism test.",
                        "Linear regression capacity.",
                        "Zero expressive capacity."
                    ],
                    "correct": 1,
                    "explanation": "Morris et al. and Xu et al. (GIN paper) proved that standard message passing cannot distinguish graph topologies that fool the classical 1-WL color refinement algorithm."
                },
                {
                    "question": "Which algorithm enabled GNNs to scale to massive graphs with millions of nodes by sampling a fixed number of neighbors per layer rather than full neighborhoods?",
                    "options": [
                        "GraphSAGE",
                        "Standard K-Means",
                        "Vanilla Perceptron",
                        "DBSCAN"
                    ],
                    "correct": 0,
                    "explanation": "GraphSAGE introduced uniform neighbor sampling, allowing mini-batch training on arbitrary giant graphs without expanding into full exponential neighborhood blowups."
                }
            ]
        },
        {
            "id": "D16",
            "title": "Deep Reinforcement Learning (DQN & PPO)",
            "module": "deeplearning",
            "level": "advanced",
            "prerequisites": ["D01", "D02", "D03", "F04"],
            "estimatedMinutes": 30,
            "tags": ["deep-rl", "dqn", "ppo", "q-learning", "policy-gradient", "reinforcement-learning"],
            "shortDesc": "Train neural network agents to master complex environments: Deep Q-Networks (DQN) and Proximal Policy Optimization (PPO).",
            "sections": {
                "whatItIs": "Deep Reinforcement Learning (Deep RL) merges deep neural networks with reinforcement learning. Instead of maintaining tabular lookup tables, deep neural networks approximate value functions (Deep Q-Networks / DQN) or parameterize stochastic policy actions directly (Proximal Policy Optimization / PPO), allowing agents to master high-dimensional visual and continuous control environments.",
                "problemItSolves": "Classical tabular RL fails when state spaces are vast or continuous (e.g. raw video pixels $256^{210 \\times 160}$ in Atari or joint torques in robotics). Deep neural function approximators generalize across continuous states.",
                "intuition": "DQN is like learning to play Super Mario by estimating the future point value of every button press: 'If I press Jump right now, this state is worth 50 points; if I do nothing, it's worth 0.' PPO is like an athletic gymnast with a coach: the gymnast performs a routine (policy), and the coach suggests gentle, bounded form adjustments (clipping ratio) to improve performance without risking severe injury from radical changes.",
                "howItWorks": "1. <strong>DQN (Value-Based):</strong> Neural network $Q_\\theta(s, a)$ predicts expected discounted return. Employs an <strong>Experience Replay Buffer</strong> to break temporal correlation and a separate <strong>Target Network</strong> $Q_{\\theta^-}$ to stabilize Bellman targets.<br>2. <strong>Policy Gradients:</strong> Directly parameterize policy $\\pi_\\theta(a|s)$ and update via Policy Gradient Theorem $\\nabla_\\theta J = \\mathbb{E}[\\nabla \\log \\pi_\\theta(a|s) A(s, a)]$.<br>3. <strong>PPO (Actor-Critic):</strong> Clips probability ratios $r_t(\\theta) = \\frac{\\pi_\\theta(a_t|s_t)}{\\pi_{\\theta_{\\text{old}}}(a_t|s_t)}$ within $[1-\\epsilon, 1+\\epsilon]$ to prevent catastrophic policy collapse.",
                "mathematics": "DQN Bellman Loss with Target Network $\\theta^-$:<br>$$\\mathcal{L}(\\theta) = \\mathbb{E}_{(s, a, r, s') \\sim \\mathcal{D}}\\left[ \\left( r + \\gamma \\max_{a'} Q_{\\theta^-}(s', a') - Q_\\theta(s, a) \\right)^2 \\right]$$<br>PPO Clipped Surrogate Objective:<br>$$L^{\\text{CLIP}}(\\theta) = \\hat{\\mathbb{E}}_t \\left[ \\min\\left( r_t(\\theta) \\hat{A}_t, \\; \\text{clip}(r_t(\\theta), 1-\\epsilon, 1+\\epsilon) \\hat{A}_t \\right) \\right]$$<br>where $r_t(\\theta) = \\frac{\\pi_\\theta(a_t|s_t)}{\\pi_{\\theta_{\\text{old}}}(a_t|s_t)}$ and $\\hat{A}_t$ is the Generalized Advantage Estimate (GAE).",
                "dataRequirements": "Interactive gym environments or physics engines (Gymnasium, MuJoCo, Isaac Sim). Requires millions of simulated step rollouts.",
                "hyperparameters": [
                    {"name": "Discount Factor (\\gamma)", "description": "Future reward discount (e.g. 0.99).", "effect": "Prioritizes long-term strategy over instant gratification."},
                    {"name": "PPO Clip Epsilon (\\epsilon)", "description": "Clipping range boundary (typically 0.1 to 0.2).", "effect": "Guarantees conservative policy updates, preventing catastrophic forgetting."},
                    {"name": "Entropy Coefficient", "description": "Bonus added for policy stochasticity.", "effect": "Encourages exploration, preventing premature convergence to suboptimal habits."}
                ],
                "strengths": [
                    "Achieved historic superhuman breakthroughs: Atari 2600, AlphaGo, Dota 2, and robotic manipulation.",
                    "PPO is robust, sample-efficient, and serves as the core engine for LLM RLHF / Alignment.",
                    "Can solve complex control tasks where human demonstrations are impossible."
                ],
                "limitations": [
                    "Extreme sample inefficiency: requires millions of trials.",
                    "High sensitivity to random seeds and hyperparameter configurations.",
                    "Reward hacking: agents exploit simulator bugs to maximize score without solving the intended task."
                ],
                "evaluation": "Evaluated using Mean Cumulative Episode Return across 10+ random seeds, tracking learning curves over millions of environment interaction steps.",
                "workedExample": "Training a 4-legged robotic dog to walk over rough terrain in MuJoCo simulation using PPO. The state is 30 sensor signals (joint angles, gyro rates); action is 12 joint motor torques. After 10 million simulation steps with rewards for forward velocity, the robot discovers a natural trotting gait robust to terrain bumps.",
                "whenToUse": "Use for robotics control, game AI, resource optimization (data center cooling), and LLM alignment (RLHF).",
                "commonMistakes": [
                    "Omitting the Target Network in DQN (causes moving-target divergence, where the network chases its own tail).",
                    "Designing poorly specified reward functions that lead to bizarre reward-hacking behaviors."
                ],
                "furtherLearning": [
                    {"title": "Mnih et al.: Human-level control through deep reinforcement learning (Nature DQN 2015)", "url": "https://www.nature.com/articles/nature14236"},
                    {"title": "Schulman et al.: Proximal Policy Optimization Algorithms (PPO 2017)", "url": "https://arxiv.org/abs/1707.06347"},
                    {"title": "OpenAI Spinning Up in Deep RL", "url": "https://spinningup.openai.com/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the purpose of the Experience Replay Buffer in Deep Q-Networks (DQN)?",
                    "options": [
                        "It records video replays for the user to watch.",
                        "It stores past transitions $(s, a, r, s')$ and samples them uniformly at random, breaking temporal correlations between consecutive steps and stabilizing gradient descent.",
                        "It increases the screen framerate.",
                        "It eliminates the need for rewards."
                    ],
                    "correct": 1,
                    "explanation": "Sequential gameplay produces highly correlated consecutive states that destabilize neural network gradient updates. Replay buffers decorrelate training data by sampling past transitions at random."
                },
                {
                    "question": "Why does Proximal Policy Optimization (PPO) clip the probability ratio $r_t(\\theta)$ within $[1-\\epsilon, 1+\\epsilon]$?",
                    "options": [
                        "To prevent the policy from making excessively large, destructive parameter updates that could cause policy collapse from which the agent cannot recover.",
                        "To force the model to take only positive actions.",
                        "To save GPU memory.",
                        "To make the policy deterministic."
                    ],
                    "correct": 0,
                    "explanation": "Unconstrained policy updates can push policy parameters into catastrophic regions where the agent unlearns good behavior. The clipping ratio enforces conservative, bounded policy updates."
                },
                {
                    "question": "What is 'Reward Hacking' in Reinforcement Learning?",
                    "options": [
                        "When someone hacks the player's account password.",
                        "When an agent discovers unintended loopholes or glitches in the environment simulator to accumulate massive rewards without fulfilling the actual human goal.",
                        "When rewards are negative.",
                        "When training terminates early."
                    ],
                    "correct": 1,
                    "explanation": "RL agents optimize literal reward functions mathematically. If a reward function has loopholes, the agent will exploit them (e.g. driving a boat in endless circles to rack up bonus points rather than finishing the race)."
                }
            ]
        }
    ]
print("Deep Learning module defined: 16 lessons")

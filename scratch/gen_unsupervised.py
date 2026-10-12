# -*- coding: utf-8 -*-
"""
Module 2: Unsupervised Learning & Representation (U01 - U08)
8 complete lessons with all 15 sections, LaTeX mathematics, hyperparameters, and 3-question quizzes.
"""

def get_unsupervised():
    return [
        {
            "id": "U01",
            "title": "k-Means & k-Medoids",
            "module": "unsupervised",
            "level": "beginner",
            "prerequisites": ["F01", "F02", "F04"],
            "estimatedMinutes": 20,
            "tags": ["clustering", "kmeans", "kmedoids", "centroids", "inertia"],
            "shortDesc": "Partition unlabelled data into k Voronoi cells by iteratively alternating between cluster assignment and centroid recalculation.",
            "sections": {
                "whatItIs": "k-Means is the most popular centroid-based clustering algorithm. Given an unlabelled dataset and an integer $k$, it partitions samples into $k$ non-overlapping clusters by minimizing the within-cluster sum of squares (Inertia). k-Medoids adapts this by forcing cluster centers to be actual observed data points (medoids), making it robust to extreme outliers.",
                "problemItSolves": "Discovers latent groupings in customer segments, astronomical data, or image color quantization without requiring costly human manual annotations.",
                "intuition": "Imagine placing $k$ flags on a sports field filled with wandering people. Each person runs to stand next to whichever flag is physically closest to them (Assignment Step). Then, each flag bearer looks at the crowd standing around them and walks to the exact geographic center of that crowd (Update Step). Repeating this dance settles everyone into natural neighborhood groups.",
                "howItWorks": "1. <strong>Initialization:</strong> Pick $k$ initial centers (ideally using k-Means++ probabilistic distance weighting).<br>2. <strong>Assignment Step:</strong> Assign each sample $\\mathbf{x}_i$ to its nearest centroid $c_j$ using Euclidean distance.<br>3. <strong>Update Step:</strong> Recalculate each centroid as the arithmetic mean of all samples assigned to that cluster: $\\boldsymbol{\\mu}_j = \\frac{1}{|S_j|} \\sum_{i \\in S_j} \\mathbf{x}_i$.<br>4. <strong>Convergence:</strong> Repeat steps 2-3 until centroid positions stop shifting or within-cluster variance stabilizes.",
                "mathematics": "Within-Cluster Sum of Squares (Inertia Objective):<br>$$J(\\boldsymbol{\\mu}_1, \\dots, \\boldsymbol{\\mu}_k) = \\sum_{j=1}^k \\sum_{\\mathbf{x}_i \\in S_j} \\|\\mathbf{x}_i - \\boldsymbol{\\mu}_j\\|^2$$<br>k-Means++ Initialization probability of choosing point $\\mathbf{x}$ as next centroid:<br>$$P(\\mathbf{x}) = \\frac{D(\\mathbf{x})^2}{\\sum_{\\mathbf{x}' \\in X} D(\\mathbf{x}')^2}$$<br>where $D(\\mathbf{x})$ is the shortest Euclidean distance from $\\mathbf{x}$ to the closest already chosen centroid.",
                "dataRequirements": "Continuous numerical features. Crucially requires feature scaling (standardization); unscaled features with large ranges distort distance metrics. Assumes isotropic, spherical clusters of roughly equal variance.",
                "hyperparameters": [
                    {"name": "Number of Clusters (k)", "description": "The number of clusters to discover.", "effect": "Selected using the Elbow method or Silhouette score."},
                    {"name": "Init Method", "description": "'k-means++' vs 'random'.", "effect": "k-Means++ spreads initial centroids far apart, avoiding poor local minima."},
                    {"name": "n_init", "description": "Number of times the algorithm restarts with different random seeds.", "effect": "Higher values ensure convergence to the lowest inertia run."}
                ],
                "strengths": [
                    "Fast and computationally scalable with linear complexity per iteration $\\mathcal{O}(N \\cdot k \\cdot D)$.",
                    "Simple, intuitive geometric mechanics that are easy to explain.",
                    "Guaranteed mathematical convergence to a local minimum of inertia."
                ],
                "limitations": [
                    "Requires specifying $k$ in advance.",
                    "Fails on non-spherical clusters (e.g. concentric circles, elongated ribbons).",
                    "Highly sensitive to initialization without k-Means++.",
                    "Arithmetic mean in k-Means is vulnerable to extreme outliers (mitigated by k-Medoids)."
                ],
                "evaluation": "Evaluated using **Silhouette Analysis** (ranges from -1 to +1, measuring cluster cohesion vs separation), Davies-Bouldin Index, and the **Elbow Curve** of inertia.",
                "workedExample": "Compressing an image from 16 million colors to 16 colors (Color Quantization). Each pixel is a 3D point $(R, G, B)$. Run k-Means with $k=16$. Replace every pixel's original color with the RGB values of its assigned cluster centroid, reducing image file size by >80%.",
                "whenToUse": "Use for customer segmentation, image compression, feature discretization, and quick exploratory data analysis.",
                "commonMistakes": [
                    "Using k-Means on concentric circles or crescent-shaped clusters (where density-based algorithms like DBSCAN are needed).",
                    "Forgetting to standardize features before clustering.",
                    "Picking $k$ blindly without inspecting Elbow or Silhouette plots."
                ],
                "furtherLearning": [
                    {"title": "Arthur & Vassilvitskii: k-means++: The Advantages of Careful Seeding (2007)", "url": "http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf"},
                    {"title": "Scikit-Learn Clustering User Guide", "url": "https://scikit-learn.org/stable/modules/clustering.html#k-means"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary benefit of the 'k-means++' initialization algorithm over naive random seeding?",
                    "options": [
                        "It automatically chooses the optimal $k$ value.",
                        "It selects initial centroids with probability proportional to their squared distance from existing centers, spreading them out and preventing poor local minima.",
                        "It converts k-Means into a supervised model.",
                        "It eliminates the need for distance calculations."
                    ],
                    "correct": 1,
                    "explanation": "k-means++ spreads initial seeds across feature space by weighting probability by distance to the nearest existing center, drastically accelerating convergence and reducing final inertia."
                },
                {
                    "question": "Which cluster shape causes standard k-Means to fail completely?",
                    "options": [
                        "Globular, spherical Gaussian balls.",
                        "Concentric rings or interlocking intertwined spirals.",
                        "Equal-sized isotropic clusters.",
                        "Dense circular clusters."
                    ],
                    "correct": 1,
                    "explanation": "k-Means partitions space into convex polyhedral Voronoi cells. It cannot separate non-convex shapes like concentric rings or complex spiral ribbons."
                },
                {
                    "question": "What does a Silhouette Coefficient close to +1.0 indicate for a sample?",
                    "options": [
                        "The sample is equidistant between two clusters.",
                        "The sample is misclassified and belongs to the neighboring cluster.",
                        "The sample is tightly clustered within its assigned group and far from neighboring clusters.",
                        "The dataset has zero variance."
                    ],
                    "correct": 2,
                    "explanation": "Silhouette score measures $(b - a) / \\max(a, b)$, where $a$ is intra-cluster distance and $b$ is nearest-cluster distance. A value near +1 indicates optimal cohesion and separation."
                }
            ]
        },
        {
            "id": "U02",
            "title": "Hierarchical Clustering",
            "module": "unsupervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F04", "U01"],
            "estimatedMinutes": 20,
            "tags": ["clustering", "hierarchical", "dendrogram", "agglomerative", "linkage"],
            "shortDesc": "Build nested hierarchies of clusters bottom-up (Agglomerative) or top-down (Divisive), visualized as a tree-like Dendrogram.",
            "sections": {
                "whatItIs": "Hierarchical Clustering is a family of clustering algorithms that constructs a nested tree of partitions. In <strong>Agglomerative</strong> (bottom-up) clustering, every data point starts as its own singleton cluster, and the closest pair of clusters is iteratively merged until a single tree remains. The entire clustering history is visualized as a <strong>Dendrogram</strong>.",
                "problemItSolves": "Unlike k-Means, hierarchical clustering does not require pre-specifying $k$. A practitioner can inspect the full taxonomy at multiple granularities and cut the dendrogram at any desired threshold.",
                "intuition": "Think of the biological taxonomy of life. You start with individual organisms (a lion, a tiger, a wolf). Lions and tigers merge into 'Big Cats' (genus Panthera); cats and wolves merge into 'Carnivora'; carnivores merge into 'Mammalia'. The dendrogram displays this family tree, allowing you to slice at the species, genus, or family level.",
                "howItWorks": "1. <strong>Initialization:</strong> Treat each point as a cluster of size 1; compute pairwise distance matrix $\\mathcal{O}(N^2)$.<br>2. <strong>Find Nearest Pair:</strong> Search matrix for the two clusters with minimum linkage distance.<br>3. <strong>Merge:</strong> Combine the two clusters into a single parent node in the dendrogram.<br>4. <strong>Update Matrix:</strong> Recompute distance from the new cluster to all remaining clusters.<br>5. <strong>Repeat:</strong> Continue until one root cluster encompasses all samples.",
                "mathematics": "Linkage Criteria between clusters $A$ and $B$:<br>Single Linkage (Minimum distance):<br>$$D_{\\text{single}}(A, B) = \\min_{\\mathbf{x} \\in A, \\mathbf{z} \\in B} \\|\\mathbf{x} - \\mathbf{z}\\|$$<br>Complete Linkage (Maximum distance):<br>$$D_{\\text{complete}}(A, B) = \\max_{\\mathbf{x} \\in A, \\mathbf{z} \\in B} \\|\\mathbf{x} - \\mathbf{z}\\|$$<br>Ward's Minimum Variance Linkage:<br>$$\\Delta \\text{ESS}_{AB} = \\frac{|A||B|}{|A| + |B|} \\|\\boldsymbol{\\mu}_A - \\boldsymbol{\\mu}_B\\|^2$$",
                "dataRequirements": "Continuous numerical features, or a precomputed distance/dissimilarity matrix. Ward's linkage strictly requires Euclidean distance; Single and Complete accept arbitrary metrics (Manhattan, Cosine, Jaccard).",
                "hyperparameters": [
                    {"name": "Linkage Criterion", "description": "Single, Complete, Average, or Ward.", "effect": "Single causes 'chaining' of stringy clusters; Complete creates compact, spherical clusters; Ward minimizes within-cluster variance."},
                    {"name": "Distance Cut Threshold", "description": "Height at which the dendrogram is sliced to yield flat clusters.", "effect": "Determines the number of active clusters."}
                ],
                "strengths": [
                    "Does not require pre-specifying the number of clusters $k$.",
                    "The dendrogram provides a visually intuitive, auditable taxonomic structure.",
                    "Ward's linkage often outperforms k-Means on real-world datasets with unequal sizes."
                ],
                "limitations": [
                    "Computationally expensive: memory complexity $\\mathcal{O}(N^2)$ and time complexity $\\mathcal{O}(N^3)$ (or $\\mathcal{O}(N^2 \\log N)$ with heaps).",
                    "Scales poorly to datasets beyond tens of thousands of samples without spatial graphs.",
                    "Merges are irreversible: a suboptimal early merge can never be undone."
                ],
                "evaluation": "Evaluated using Cophenetic Correlation Coefficient (measuring how faithfully the dendrogram preserves original pairwise distances) and Silhouette analysis.",
                "workedExample": "Clustering genes based on expression levels across 10 disease states. Hierarchical clustering produces a dendrogram where genes participating in the same metabolic pathway cluster tightly together, revealing regulatory sub-networks without pre-specifying pathway counts.",
                "whenToUse": "Best for bioinformatics (gene trees), document categorization taxonomies, and exploratory analysis on small-to-moderate datasets ($N < 5,000$).",
                "commonMistakes": [
                    "Using Single Linkage on noisy data, leading to the 'chaining phenomenon' where points form long stringy paths instead of compact clusters.",
                    "Trying to run raw hierarchical clustering on 100,000 samples (will cause out-of-memory errors on distance matrix)."
                ],
                "furtherLearning": [
                    {"title": "Müllner: Modern Hierarchical, Agglomerative Clustering Algorithms (2011)", "url": "https://arxiv.org/abs/1109.2378"},
                    {"title": "Scikit-Learn AgglomerativeClustering", "url": "https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html"}
                ]
            },
            "quiz": [
                {
                    "question": "What is a 'Dendrogram' in hierarchical clustering?",
                    "options": [
                        "A scatterplot of residuals.",
                        "A tree diagram that illustrates the arrangement of clusters produced by successive merges or splits at varying distance thresholds.",
                        "A loss curve plotting gradient descent steps.",
                        "A matrix of eigenvalues."
                    ],
                    "correct": 1,
                    "explanation": "A dendrogram is a 2D tree diagram where the vertical axis represents the linkage distance threshold at which clusters are merged."
                },
                {
                    "question": "What is the 'chaining phenomenon' associated with Single Linkage clustering?",
                    "options": [
                        "Clusters form long, straggly snake-like chains because points are merged based on the minimum distance between any single pair of points.",
                        "The algorithm runs out of RAM.",
                        "All data points get assigned to zero clusters.",
                        "The dendrogram branches cross over each other."
                    ],
                    "correct": 0,
                    "explanation": "Single linkage looks only at the closest pair of points between two clusters. A sequence of intermediate noise points can 'bridge' two distinct clusters into a long, continuous chain."
                },
                {
                    "question": "Why is standard hierarchical clustering impractical for 500,000 samples?",
                    "options": [
                        "It requires computing and storing an $\\mathcal{O}(N^2)$ pairwise distance matrix, requiring roughly 1,000 GB of RAM.",
                        "It cannot handle more than 2 features.",
                        "It only works on binary labels.",
                        "The dendrogram would be taller than the computer screen."
                    ],
                    "correct": 0,
                    "explanation": "A distance matrix for 500,000 float64 elements requires $(500,000^2 \\times 8) / 2$ bytes $\\approx 1,000$ Gigabytes of memory, rendering naive implementation impossible."
                }
            ]
        },
        {
            "id": "U03",
            "title": "DBSCAN & HDBSCAN",
            "module": "unsupervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F04", "U01"],
            "estimatedMinutes": 25,
            "tags": ["clustering", "dbscan", "hdbscan", "density-based", "noise-detection"],
            "shortDesc": "Discover arbitrary non-linear cluster shapes based on local point densities, cleanly isolating noise and outliers.",
            "sections": {
                "whatItIs": "DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a density-based clustering algorithm. It defines clusters as continuous regions of high point density separated by regions of low density. Points in sparse regions that do not belong to any cluster are explicitly flagged as noise (outliers). HDBSCAN extends this by building a hierarchy of density estimates across varying scale thresholds.",
                "problemItSolves": "Centroid models (like k-Means) fail when clusters have arbitrary, non-spherical shapes (e.g. interlocking rings, rivers, coastlines) and force every single outlier into a cluster. DBSCAN solves both problems naturally.",
                "intuition": "Imagine looking at an aerial photograph of an archipelago. Islands are clusters of land where trees and houses are packed closely together. The open ocean is empty space (low density). A solitary boat floating far out at sea is treated as an isolated noise point—not forced into being an island.",
                "howItWorks": "1. <strong>Classify Points:</strong> For each point, count neighbors within radius $\\epsilon$. If $\\ge \\text{minPts}$, label as a <strong>Core Point</strong>.<br>2. <strong>Expand Clusters:</strong> Connect core points whose $\\epsilon$-neighborhoods overlap into a shared cluster.<br>3. <strong>Border Points:</strong> Points within $\\epsilon$ of a core point but with fewer than $\\text{minPts}$ neighbors become border points.<br>4. <strong>Noise:</strong> Any point that is neither a core point nor a border point is labeled as noise (label -1).",
                "mathematics": "$\\epsilon$-neighborhood of point $\\mathbf{p}$:<br>$$N_\\epsilon(\\mathbf{p}) = \\{ \\mathbf{q} \\in D \\mid \\text{dist}(\\mathbf{p}, \\mathbf{q}) \\le \\epsilon \\}$$<br>Core Point condition:<br>$$|N_\\epsilon(\\mathbf{p})| \\ge \\text{minPts}$$<br>Density-Reachability:<br>A point $\\mathbf{q}$ is directly density-reachable from $\\mathbf{p}$ if $\\mathbf{p}$ is a core point and $\\mathbf{q} \\in N_\\epsilon(\\mathbf{p})$. Clusters are maximal sets of density-connected points.",
                "dataRequirements": "Continuous numerical features. Absolutely requires feature scaling; otherwise the distance radius $\\epsilon$ becomes distorted across dimensions. Best in low-to-medium dimensions ($D < 20$).",
                "hyperparameters": [
                    {"name": "Epsilon (\\epsilon)", "description": "Maximum neighborhood radius to search for nearby points.", "effect": "Too small leaves most points as noise; too large merges distinct clusters into one giant group. Tuned via k-distance elbow plot."},
                    {"name": "minPts", "description": "Minimum points required within $\\epsilon$ to form a core point.", "effect": "Rule of thumb: $\\ge 2 \\times D$. Larger values suppress noise in dense datasets."}
                ],
                "strengths": [
                    "Discovers arbitrary, complex non-linear cluster geometries (crescents, rings, spirals).",
                    "Does not require pre-specifying the number of clusters $k$.",
                    "Robustly detects and isolates noise and outliers (labeled as -1).",
                    "Fast with spatial indexing (KD-Tree/Ball-Tree): $\\mathcal{O}(N \\log N)$."
                ],
                "limitations": [
                    "Struggles on datasets with clusters of varying densities (mitigated by HDBSCAN).",
                    "Extremely sensitive to choice of $\\epsilon$.",
                    "Degrades in high dimensions due to the Curse of Dimensionality."
                ],
                "evaluation": "Evaluated using Silhouette score (computed only on non-noise points) and inspecting the percentage of samples classified as noise.",
                "workedExample": "GPS crime mapping in a metropolitan area. Crimes naturally concentrate along specific nightlife avenues and transit hubs, forming winding, irregular density shapes. DBSCAN groups these hotspots into distinct corridors while labeling isolated crimes in residential suburbs as noise.",
                "whenToUse": "Use when cluster shapes are non-spherical, when outlier rejection is critical, or when spatial geolocation coordinates (latitude, longitude) need clustering.",
                "commonMistakes": [
                    "Using DBSCAN without standardizing features first.",
                    "Setting $\\epsilon$ arbitrarily without plotting the k-Nearest Neighbor distance graph to find the inflection elbow."
                ],
                "furtherLearning": [
                    {"title": "Ester et al.: A Density-Based Algorithm for Discovering Clusters (KDD 1996 Original Paper)", "url": "https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf"},
                    {"title": "McInnes et al.: HDBSCAN: Hierarchical Density-Based Spatial Clustering", "url": "https://hdbscan.readthedocs.io/"}
                ]
            },
            "quiz": [
                {
                    "question": "In DBSCAN, what label is assigned to data points that are neither core points nor border points?",
                    "options": [
                        "Cluster 0",
                        "Noise (typically encoded as -1)",
                        "Cluster $\\infty$",
                        "Centroid"
                    ],
                    "correct": 1,
                    "explanation": "Points in low-density regions that fail to meet the core point criteria and do not lie within the $\\epsilon$-radius of any core point are flagged as noise (-1)."
                },
                {
                    "question": "How can an engineer systematically choose an appropriate value for $\\epsilon$ in DBSCAN?",
                    "options": [
                        "Set it equal to the number of rows.",
                        "Plot the k-Nearest Neighbor distance graph sorted in ascending order and select the value at the sharp 'elbow' inflection point.",
                        "Pick a random number between 0 and 1.",
                        "Use gradient descent on cross-entropy."
                    ],
                    "correct": 1,
                    "explanation": "Calculating the distance to the $k$-th nearest neighbor for all points and plotting them sorted reveals an 'elbow' where noise begins to diverge from dense clusters."
                },
                {
                    "question": "What is the primary advantage of HDBSCAN over standard DBSCAN?",
                    "options": [
                        "HDBSCAN requires zero RAM.",
                        "HDBSCAN extracts clusters across varying local densities, eliminating the need to select a single fixed global $\\epsilon$ radius.",
                        "HDBSCAN converts clustering into supervised regression.",
                        "HDBSCAN forces all clusters to be spheres."
                    ],
                    "correct": 1,
                    "explanation": "DBSCAN assumes a single global density via fixed $\\epsilon$. HDBSCAN builds a cluster tree across all density levels, finding clusters of varying densities automatically."
                }
            ]
        },
        {
            "id": "U04",
            "title": "Gaussian Mixture Models (GMM) & EM",
            "module": "unsupervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F04", "S04", "U01"],
            "estimatedMinutes": 25,
            "tags": ["gmm", "expectation-maximization", "soft-clustering", "probabilistic", "gaussian"],
            "shortDesc": "Represent complex data distributions as weighted mixtures of multivariate Gaussians using the Expectation-Maximization algorithm.",
            "sections": {
                "whatItIs": "A Gaussian Mixture Model (GMM) is a generative probabilistic model that assumes all data points are generated from a mixture of a finite number of multivariate Gaussian distributions with unknown parameters. While k-Means assigns points rigidly to a single cluster ('hard clustering'), GMM computes posterior probabilities of membership across all components ('soft clustering').",
                "problemItSolves": "Real clusters often have elliptical shapes, varying spreads, and overlapping boundaries. GMM accommodates cluster-specific covariance matrices (allowing tilted ellipsoids) and provides principled probabilistic assignments.",
                "intuition": "Imagine multiple smoke machines placed around a room, each puffing out an elliptical cloud of colored smoke (Red, Blue, Green). A smoke particle in the center of the room might be 70% likely to have drifted from the Blue machine, 20% from the Green, and 10% from the Red. GMM learns the position, shape, and intensity of each smoke machine.",
                "howItWorks": "1. <strong>Initialize:</strong> Set initial component weights $\\pi_k$, means $\\boldsymbol{\\mu}_k$, and covariances $\\boldsymbol{\\Sigma}_k$ (often via k-Means).<br>2. <strong>E-Step (Expectation):</strong> Calculate the posterior responsibility $\\gamma_{ik}$ that component $k$ generated sample $\\mathbf{x}_i$.<br>3. <strong>M-Step (Maximization):</strong> Update $\\pi_k, \\boldsymbol{\\mu}_k, \\boldsymbol{\\Sigma}_k$ using weighted maximum likelihood estimates.<br>4. <strong>Iterate:</strong> Repeat E-Step and M-Step until log-likelihood converges.",
                "mathematics": "GMM Probability Density Function:<br>$$p(\\mathbf{x}) = \\sum_{k=1}^K \\pi_k \\mathcal{N}(\\mathbf{x} \\mid \\boldsymbol{\\mu}_k, \\boldsymbol{\\Sigma}_k), \\quad \\sum_{k=1}^K \\pi_k = 1$$<br>E-Step (Responsibilities):<br>$$\\gamma_{ik} = \\frac{\\pi_k \\mathcal{N}(\\mathbf{x}_i \\mid \\boldsymbol{\\mu}_k, \\boldsymbol{\\Sigma}_k)}{\\sum_{j=1}^K \\pi_j \\mathcal{N}(\\mathbf{x}_i \\mid \\boldsymbol{\\mu}_j, \\boldsymbol{\\Sigma}_j)}$$<br>M-Step (Mean and Covariance Update):<br>$$\\boldsymbol{\\mu}_k = \\frac{\\sum_{i=1}^N \\gamma_{ik} \\mathbf{x}_i}{\\sum_{i=1}^N \\gamma_{ik}}, \\quad \\boldsymbol{\\Sigma}_k = \\frac{\\sum_{i=1}^N \\gamma_{ik} (\\mathbf{x}_i - \\boldsymbol{\\mu}_k)(\\mathbf{x}_i - \\boldsymbol{\\mu}_k)^T}{\\sum_{i=1}^N \\gamma_{ik}}$$",
                "dataRequirements": "Continuous numerical features. Standardization recommended for numerical stability during covariance matrix inversion.",
                "hyperparameters": [
                    {"name": "n_components (K)", "description": "Number of mixture Gaussians.", "effect": "Selected using Bayesian Information Criterion (BIC) or Akaike Information Criterion (AIC)."},
                    {"name": "Covariance Type", "description": "'full', 'tied', 'diag', or 'spherical'.", "effect": "'full' allows independent ellipsoids with arbitrary rotation; 'diag' forces axis-aligned ellipses; 'spherical' mimics k-Means."}
                ],
                "strengths": [
                    "Provides soft, probabilistic cluster assignments (uncertainty quantification).",
                    "Learns arbitrary elliptical, rotated cluster geometries.",
                    "Generative: can sample new synthetic data points from the learned distribution $p(\\mathbf{x})$."
                ],
                "limitations": [
                    "EM can get trapped in local optima depending on initialization.",
                    "Full covariance matrices have $\\mathcal{O}(D^2)$ parameters per cluster, risking overfitting when samples per cluster are small.",
                    "Singularities can occur if a component collapses onto a single isolated data point."
                ],
                "evaluation": "Evaluated using Log-Likelihood, AIC, and BIC (penalizing model parameters to prevent overfitting):<br>$$\\text{BIC} = -2 \\ln(\\hat{L}) + p \\ln(N)$$",
                "workedExample": "Speaker diarization in an audio recording with 2 speakers. Pitch and frequency features are modeled as a 2-component GMM. For each audio frame, the model outputs $P(\\text{Speaker 1}) = 0.85$ and $P(\\text{Speaker 2}) = 0.15$, smoothly identifying who is speaking even during soft transitions.",
                "whenToUse": "Use when clusters overlap, when soft probabilities are required, or when performing density estimation and generative data sampling.",
                "commonMistakes": [
                    "Using 'full' covariance on high-dimensional data with few samples, causing non-positive-definite covariance collapse.",
                    "Assuming GMM can model arbitrary non-convex crescent manifolds without chaining multiple components."
                ],
                "furtherLearning": [
                    {"title": "Dempster, Laird, Rubin: Maximum Likelihood from Incomplete Data via the EM Algorithm (1977)", "url": "https://www.jstor.org/stable/2984875"},
                    {"title": "Bishop: Pattern Recognition and Machine Learning - Ch. 9 Mixture Models", "url": "https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/"}
                ]
            },
            "quiz": [
                {
                    "question": "What is the primary difference between k-Means and Gaussian Mixture Models?",
                    "options": [
                        "k-Means is supervised; GMM is unsupervised.",
                        "k-Means performs hard assignment to spherical clusters; GMM provides soft probabilistic assignments to elliptical Gaussians with learned covariances.",
                        "GMM does not use mathematics.",
                        "k-Means cannot run on computers."
                    ],
                    "correct": 1,
                    "explanation": "k-Means assigns each point 100% to a single center based on Euclidean distance. GMM models clusters as Gaussians with arbitrary covariance, outputting posterior probabilities across all clusters."
                },
                {
                    "question": "What does the 'E-step' (Expectation step) in the EM algorithm calculate?",
                    "options": [
                        "The updated means and covariances of the Gaussians.",
                        "The posterior responsibilities $\\gamma_{ik}$, representing the probability that component $k$ generated observation $i$.",
                        "The final accuracy score.",
                        "The gradient of weights."
                    ],
                    "correct": 1,
                    "explanation": "In the E-step, current parameters are held fixed to compute the expected responsibilities (probabilities) of each component for each sample."
                },
                {
                    "question": "Which criterion is commonly minimized to choose the optimal number of GMM components $K$ while penalizing excess parameters?",
                    "options": [
                        "Bayesian Information Criterion (BIC)",
                        "Mean Absolute Error",
                        "Learning Rate",
                        "Gini Impurity"
                    ],
                    "correct": 0,
                    "explanation": "BIC balances model fit (log-likelihood) against model complexity ($p \\ln N$), penalizing overparameterized models with too many components."
                }
            ]
        },
        {
            "id": "U05",
            "title": "Principal Component Analysis (PCA)",
            "module": "unsupervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F02", "F04"],
            "estimatedMinutes": 25,
            "tags": ["pca", "dimensionality-reduction", "eigenvalues", "svd", "variance"],
            "shortDesc": "Orthogonal linear projection that maximizes variance along uncorrelated principal components via SVD.",
            "sections": {
                "whatItIs": "Principal Component Analysis (PCA) is an unsupervised linear dimensionality reduction technique. It projects high-dimensional data onto a lower-dimensional subspace spanned by orthogonal axes (Principal Components) that sequentially maximize the variance of the projected data points.",
                "problemItSolves": "High-dimensional datasets suffer from the Curse of Dimensionality, extreme computational cost, multicollinearity, and inability to visualize beyond 3D. PCA compresses the feature space while retaining the maximum possible statistical information (variance).",
                "intuition": "Imagine holding a 3D teapot in front of a flashlight against a white wall. If you orient the teapot flat from the side, the 2D shadow clearly shows the handle, body, and spout—capturing nearly all its visual structure. If you orient it pointing straight at the light, the shadow is just an unrecognizable round blob. PCA mathematically finds the optimal angles to cast the most informative shadow.",
                "howItWorks": "1. <strong>Standardize:</strong> Mean-center the data (subtract feature means so $\\mathbb{E}[\\mathbf{X}] = \\mathbf{0}$).<br>2. <strong>Covariance Matrix:</strong> Compute sample covariance matrix $\\boldsymbol{\\Sigma} = \\frac{1}{N-1} \\mathbf{X}^T \\mathbf{X}$.<br>3. <strong>Eigendecomposition / SVD:</strong> Compute eigenvectors $\\mathbf{v}_j$ and eigenvalues $\\lambda_j$ via Singular Value Decomposition $\\mathbf{X} = \\mathbf{U} \\boldsymbol{\\Sigma} \\mathbf{V}^T$.<br>4. <strong>Project:</strong> Select top $k$ eigenvectors with largest eigenvalues to construct projection matrix $\\mathbf{W}_k$; project $\\mathbf{Z} = \\mathbf{X} \\mathbf{W}_k$.",
                "mathematics": "Covariance Matrix and Eigenvalue Equation:<br>$$\\boldsymbol{\\Sigma} \\mathbf{v}_j = \\lambda_j \\mathbf{v}_j, \\quad \\|\\mathbf{v}_j\\| = 1$$<br>Explained Variance Ratio of component $j$:<br>$$\\text{EVR}_j = \\frac{\\lambda_j}{\\sum_{m=1}^D \\lambda_m}$$<br>Reconstruction from $k$ components:<br>$$\\hat{\\mathbf{X}} = \\mathbf{Z} \\mathbf{W}_k^T = \\mathbf{X} \\mathbf{W}_k \\mathbf{W}_k^T$$",
                "dataRequirements": "Continuous numerical features. Mean centering is strictly mandatory. Standardization (scaling to unit variance) is essential whenever features have differing units (e.g. income in dollars vs age in years).",
                "hyperparameters": [
                    {"name": "n_components (k)", "description": "Number of dimensions to retain, or minimum cumulative variance threshold (e.g. 0.95).", "effect": "Trades off compression ratio against information loss."},
                    {"name": "SVD Solver", "description": "'full', 'arpack', or 'randomized'.", "effect": "Randomized SVD drastically accelerates computation when $N, D$ are large and $k \\ll D$."}
                ],
                "strengths": [
                    "Drastically reduces storage, memory, and training time for downstream models.",
                    "Eliminates multicollinearity by producing strictly mutually orthogonal components.",
                    "Optimal linear reconstruction: minimizes Mean Squared Error between original and reconstructed points.",
                    "Enables 2D and 3D visual exploration of complex high-dimensional datasets."
                ],
                "limitations": [
                    "Purely linear: fails to capture non-linear manifold geometry (e.g. Swiss Roll).",
                    "Principal components are linear combinations of all original features, making individual components hard to interpret.",
                    "Sensitive to unscaled features and extreme outliers."
                ],
                "evaluation": "Evaluated using **Scree Plot** (eigenvalue vs component rank) and Cumulative Explained Variance Ratio curve.",
                "workedExample": "Facial recognition (Eigenfaces). Each face image is $100 \\times 100 = 10,000$ pixels. Running PCA retains the top 50 principal components capturing 90% of facial structure variance (lighting, eye distance, jaw shape). Downstream classifiers train on 50 numbers instead of 10,000, running 200x faster.",
                "whenToUse": "Use for exploratory data visualization (2D/3D), preprocessing to eliminate multicollinearity, noise filtering, and data compression.",
                "commonMistakes": [
                    "Forgetting to scale features before PCA, allowing high-magnitude variables to dictate all top components.",
                    "Applying PCA to categorical or one-hot encoded variables (use Multiple Correspondence Analysis instead)."
                ],
                "furtherLearning": [
                    {"title": "Jolliffe: Principal Component Analysis (Springer)", "url": "https://link.springer.com/book/10.1007/b98835"},
                    {"title": "StatQuest: Principal Component Analysis (PCA) Step-by-Step", "url": "https://www.youtube.com/watch?v=FgakZw6K1QQ"}
                ]
            },
            "quiz": [
                {
                    "question": "Why is mean centering strictly required before performing Principal Component Analysis?",
                    "options": [
                        "To prevent the first principal component from simply pointing toward the dataset's offset from the origin rather than the axis of maximum variance.",
                        "Because eigenvalues cannot be calculated for non-zero data.",
                        "To convert negative numbers into positive numbers.",
                        "To double the number of dimensions."
                    ],
                    "correct": 0,
                    "explanation": "If data is not centered at the origin, the first component will simply trace the vector from the origin to the mean of the data, rather than aligning with the true axis of maximum variance."
                },
                {
                    "question": "What is the mathematical relationship between the principal component directions?",
                    "options": [
                        "They are parallel to each other.",
                        "They are mutually orthogonal (perpendicular), with zero linear correlation between their scores.",
                        "They are curved polynomials.",
                        "They must sum to 1.0."
                    ],
                    "correct": 1,
                    "explanation": "Eigenvectors of a symmetric covariance matrix are strictly orthogonal, guaranteeing that the resulting principal component dimensions are uncorrelated."
                },
                {
                    "question": "What does a cumulative explained variance ratio of 0.92 for the first 3 components mean?",
                    "options": [
                        "The model has an accuracy of 92%.",
                        "The 3 components retain 92% of the total statistical variance present in the original high-dimensional dataset.",
                        "8% of the data points were discarded as noise.",
                        "The dataset has only 3 rows."
                    ],
                    "correct": 1,
                    "explanation": "The explained variance ratio indicates the fraction of total variance captured. 0.92 means 92% of the dataset's total variance is preserved in the 3D subspace."
                }
            ]
        },
        {
            "id": "U06",
            "title": "t-SNE & UMAP",
            "module": "unsupervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F04", "U05"],
            "estimatedMinutes": 25,
            "tags": ["tsne", "umap", "manifold-learning", "non-linear", "visualization"],
            "shortDesc": "Non-linear manifold learning algorithms that preserve local neighborhood topologies for rich 2D/3D visualization.",
            "sections": {
                "whatItIs": "t-SNE (t-Distributed Stochastic Neighbor Embedding) and UMAP (Uniform Manifold Approximation and Projection) are state-of-the-art non-linear dimensionality reduction algorithms designed primarily for exploratory data visualization. They preserve local manifold geometry, ensuring points that are close neighbors in high-dimensional space remain clustered close together in low-dimensional embeddings.",
                "problemItSolves": "Linear methods like PCA fail to unfold non-linear manifolds (e.g. swiss rolls, nested spheres). t-SNE and UMAP successfully unroll complex curved manifolds, resolving the 'crowding problem' through heavy-tailed probability distributions.",
                "intuition": "Imagine a crumple of tissue paper with clusters of colored ink dots. PCA merely flattens the ball with a hydraulic press, causing unrelated layers to squash on top of each other. t-SNE and UMAP act like a patient restorer who gently steams and flattens the tissue sheet so local neighborhoods remain intact without overlapping unrelated folds.",
                "howItWorks": "1. <strong>High-D Probabilities:</strong> Model pairwise affinities as Gaussian conditional probabilities $p_{j|i}$.<br>2. <strong>Low-D Probabilities:</strong> Model low-dimensional map points using a Student-t distribution (t-SNE) or fuzzy simplicial sets (UMAP).<br>3. <strong>Heavy Tails:</strong> The heavy-tailed Student-t distribution allows intermediate-distance points to spread out, solving the crowding problem.<br>4. <strong>Optimization:</strong> Minimize Kullback-Leibler (KL) divergence (t-SNE) or cross-entropy (UMAP) via gradient descent.",
                "mathematics": "High-dimensional affinity (t-SNE):<br>$$p_{j|i} = \\frac{\\exp(-\\|\\mathbf{x}_i - \\mathbf{x}_j\\|^2 / 2\\sigma_i^2)}{\\sum_{k \\ne i} \\exp(-\\|\\mathbf{x}_i - \\mathbf{x}_k\\|^2 / 2\\sigma_i^2)}, \\quad p_{ij} = \\frac{p_{j|i} + p_{i|j}}{2N}$$<br>Low-dimensional Student-t affinity ($q_{ij}$ with 1 degree of freedom):<br>$$q_{ij} = \\frac{(1 + \\|\\mathbf{y}_i - \\mathbf{y}_j\\|^2)^{-1}}{\\sum_{k} \\sum_{l \\ne k} (1 + \\|\\mathbf{y}_k - \\mathbf{y}_l\\|^2)^{-1}}$$<br>Kullback-Leibler Loss:<br>$$\\mathcal{L} = \\text{KL}(P \\parallel Q) = \\sum_{i \\ne j} p_{ij} \\log\\left( \\frac{p_{ij}}{q_{ij}} \\right)$$",
                "dataRequirements": "Continuous numerical features. It is standard best practice to reduce dimensionality with PCA first (e.g. down to 50 dimensions) before running t-SNE/UMAP to suppress noise and speed optimization.",
                "hyperparameters": [
                    {"name": "Perplexity (t-SNE) / n_neighbors (UMAP)", "description": "Effective number of nearest neighbors each point considers.", "effect": "Low values emphasize fine micro-clusters; high values capture broader global topology."},
                    {"name": "min_dist (UMAP)", "description": "Minimum distance between points in low-D space.", "effect": "Smaller values pack points densely; larger values spread clusters loosely."},
                    {"name": "Learning Rate / Early Exaggeration", "description": "Optimization step and cluster separation pressure.", "effect": "Early exaggeration inflates initial cluster gaps."}
                ],
                "strengths": [
                    "Produces visually stunning, well-separated cluster plots for complex datasets (e.g. single-cell RNA, word embeddings, image features).",
                    "Discovers intricate non-linear manifold topologies that PCA cannot reveal.",
                    "UMAP is significantly faster than t-SNE and preserves more global topological structure."
                ],
                "limitations": [
                    "Distances between distant clusters cannot be directly interpreted as meaningful metric distances.",
                    "Stochastic: different random seeds produce different spatial layouts.",
                    "t-SNE cannot project new unseen query points without rerunning optimization (UMAP can)."
                ],
                "evaluation": "Evaluated qualitatively via visual cluster separation and quantitatively via Trustworthiness and Continuity metrics.",
                "workedExample": "Visualizing 70,000 MNIST handwritten digits (784 dimensions). PCA produces an overlapping murky blur. t-SNE cleanly isolates 10 distinct, beautifully separated color-coded islands, with each island representing a unique digit (0 through 9).",
                "whenToUse": "The premier choice for exploratory data visualization, single-cell genomics, latent embedding visualization, and clustering sanity checks.",
                "commonMistakes": [
                    "Interpreting cluster sizes or distances between far-apart clusters in t-SNE as physical geometric truths.",
                    "Using t-SNE as a feature preprocessing step for downstream linear models (UMAP or PCA is preferred)."
                ],
                "furtherLearning": [
                    {"title": "van der Maaten & Hinton: Visualizing Data using t-SNE (JMLR 2008)", "url": "https://www.jmlr.org/papers/v9/vandermaaten08a.html"},
                    {"title": "McInnes et al.: UMAP: Uniform Manifold Approximation and Projection (2018)", "url": "https://arxiv.org/abs/1802.03426"},
                    {"title": "Distill.pub: How to Use t-SNE Effectively", "url": "https://distill.pub/2016/misread-tsne/"}
                ]
            },
            "quiz": [
                {
                    "question": "Why does t-SNE use a Student-t distribution (heavy tails) in the low-dimensional space instead of a Gaussian distribution?",
                    "options": [
                        "To solve the 'crowding problem' by pushing moderately distant points further apart, preventing moderate-distance points from collapsing into a dense ball.",
                        "Because computers cannot calculate exponential functions.",
                        "To force all points onto a circle.",
                        "To reduce the number of iterations to 1."
                    ],
                    "correct": 0,
                    "explanation": "In high dimensions, the volume of a sphere grows exponentially, meaning there is far more room for points to be equidistant. Using a heavy-tailed Student-t distribution in 2D accommodates this volume discrepancy, eliminating the crowding problem."
                },
                {
                    "question": "Can you reliably interpret the physical Euclidean distance between two distant cluster islands in a t-SNE plot as global similarity?",
                    "options": [
                        "Yes, the distance is mathematically exact.",
                        "No, t-SNE prioritizes local neighborhood structure; relative distances between distant clusters are largely arbitrary and dependent on perplexity.",
                        "Only if perplexity is set to 0.",
                        "Yes, but only in 3D plots."
                    ],
                    "correct": 1,
                    "explanation": "t-SNE focuses almost entirely on preserving local neighbor probabilities. Global distances between separated clusters are non-metric and cannot be interpreted as true global distances."
                },
                {
                    "question": "What is a major operational advantage of UMAP over standard t-SNE?",
                    "options": [
                        "UMAP is significantly faster, preserves more global structure, and can transform new unseen out-of-sample points.",
                        "UMAP is a supervised classification tree.",
                        "UMAP does not require data inputs.",
                        "UMAP guarantees 100% test accuracy."
                    ],
                    "correct": 0,
                    "explanation": "UMAP scales much faster than t-SNE, preserves more global topology, and supports an out-of-sample `transform()` method to project new data points into the learned embedding."
                }
            ]
        },
        {
            "id": "U07",
            "title": "Association Rule Learning",
            "module": "unsupervised",
            "level": "beginner",
            "prerequisites": ["F01", "F04"],
            "estimatedMinutes": 20,
            "tags": ["association-rules", "apriori", "fp-growth", "market-basket", "support-confidence-lift"],
            "shortDesc": "Discover actionable co-occurrence relationships and 'if-then' purchase patterns in transactional databases.",
            "sections": {
                "whatItIs": "Association Rule Learning is a rule-based machine learning method for discovering interesting relationships, co-occurrences, and correlations between items in large transactional databases. Common algorithms include <strong>Apriori</strong> and <strong>FP-Growth</strong> (Frequent Pattern Growth).",
                "problemItSolves": "Identifies cross-selling opportunities (Market Basket Analysis), recommendation combos, and medical co-morbidity associations from millions of unstructured transaction records without requiring supervised target labels.",
                "intuition": "Think of an e-commerce shopping cart. If a customer adds peanut butter and bread to their basket, there is an 85% statistical likelihood they will also add jelly. Finding these frequent item combinations allows supermarkets to place complementary items together and optimize promotional discounting.",
                "howItWorks": "1. <strong>Identify Frequent Itemsets:</strong> Find all item combinations that exceed a minimum <strong>Support</strong> threshold.<br>2. <strong>Apriori Principle:</strong> Any subset of a frequent itemset must also be frequent (if $\\{A, B\\}$ is infrequent, $\\{A, B, C\\}$ cannot possibly be frequent).<br>3. <strong>Generate Rules:</strong> Form candidate implications $X \\implies Y$.<br>4. <strong>Filter by Confidence & Lift:</strong> Retain rules meeting minimum <strong>Confidence</strong> and having <strong>Lift</strong> $> 1.0$.",
                "mathematics": "Support of itemset $X$ in transaction database $T$:<br>$$\\text{Support}(X) = \\frac{|\\{t \\in T \\mid X \\subseteq t\\}|}{|T|}$$<br>Confidence of rule $X \\implies Y$:<br>$$\\text{Confidence}(X \\implies Y) = \\frac{\\text{Support}(X \\cup Y)}{\\text{Support}(X)} = P(Y \\mid X)$$<br>Lift (independence ratio):<br>$$\\text{Lift}(X \\implies Y) = \\frac{\\text{Support}(X \\cup Y)}{\\text{Support}(X) \\times \\text{Support}(Y)} = \\frac{P(Y \\mid X)}{P(Y)}$$<br>$\\text{Lift} > 1$ implies positive correlation; $\\text{Lift} = 1$ implies complete statistical independence; $\\text{Lift} < 1$ implies negative correlation.",
                "dataRequirements": "Transaction logs or one-hot boolean matrices (rows = transactions, columns = items). Sparse matrix representations essential for catalogs with millions of SKUs.",
                "hyperparameters": [
                    {"name": "Min Support", "description": "Minimum fraction of transactions an itemset must appear in.", "effect": "Too high misses niche patterns; too low causes combinatorial explosion."},
                    {"name": "Min Confidence", "description": "Minimum conditional probability threshold for the rule.", "effect": "Ensures generated rules are reliable."},
                    {"name": "Min Lift", "description": "Minimum lift threshold (typically $> 1.2$).", "effect": "Filters out coincidental co-occurrences of universally popular items."}
                ],
                "strengths": [
                    "Completely transparent, business-friendly 'if-then' rules.",
                    "Requires no mathematical parameter training or differentiable loss functions.",
                    "Directly actionable for retail layout, marketing bundles, and website navigation."
                ],
                "limitations": [
                    "Combinatorial explosion: candidate itemsets scale exponentially $2^{|I|}$ with catalog size.",
                    "Apriori requires multiple expensive scans over the entire database (mitigated by FP-Growth's prefix tree).",
                    "Does not account for sequential order or timing (use Sequential Pattern Mining instead)."
                ],
                "evaluation": "Evaluated using Support, Confidence, Lift, and Leverage metrics.",
                "workedExample": "A database of 10,000 supermarket baskets. Beer appears in 2,000 baskets ($S=0.2$). Diapers appear in 1,000 baskets ($S=0.1$). Both appear together in 500 baskets ($S=0.05$). Rule: $\\text{Diapers} \\implies \\text{Beer}$. Confidence $= 500 / 1000 = 0.50$ (50%). Lift $= 0.05 / (0.1 \\times 0.2) = 2.5$. Customers buying diapers are 2.5x more likely to buy beer than random customers.",
                "whenToUse": "Use for market basket analysis, product bundle recommendations, website clickstream page associations, and medical prescription interaction mining.",
                "commonMistakes": [
                    "Relying solely on Confidence without checking Lift (if 90% of all shoppers buy Milk, any rule $X \\implies \\text{Milk}$ has high confidence by coincidence, even if Lift is 1.0).",
                    "Setting min_support too low in Apriori on massive catalogs, crashing server memory."
                ],
                "furtherLearning": [
                    {"title": "Agrawal & Srikant: Fast Algorithms for Mining Association Rules (VLDB 1994)", "url": "https://www.vldb.org/conf/1994/P487.PDF"},
                    {"title": "Han et al.: Mining Frequent Patterns without Candidate Generation (FP-Growth 2000)", "url": "https://dl.acm.org/doi/10.1145/335191.335372"}
                ]
            },
            "quiz": [
                {
                    "question": "What does a Lift score of 1.0 indicate for the association rule $X \\implies Y$?",
                    "options": [
                        "Item $X$ and Item $Y$ are completely independent; buying $X$ has zero effect on the likelihood of buying $Y$.",
                        "Item $X$ causes Item $Y$ with 100% certainty.",
                        "Item $Y$ is never purchased.",
                        "The rule is invalid."
                    ],
                    "correct": 0,
                    "explanation": "When $\\text{Lift} = 1.0$, $P(Y|X) = P(Y)$, meaning the co-occurrence of $X$ and $Y$ occurs purely at random due to chance independence."
                },
                {
                    "question": "What core mathematical principle enables the Apriori algorithm to prune candidate itemsets without checking them?",
                    "options": [
                        "The Central Limit Theorem.",
                        "The Apriori Anti-Monotonicity Principle: if an itemset is infrequent, all of its supersets must also be infrequent.",
                        "The Chain Rule of Calculus.",
                        "Bayes' Theorem."
                    ],
                    "correct": 1,
                    "explanation": "If itemset $\\{A, B\\}$ does not meet minimum support, no superset containing $\\{A, B\\}$ (e.g. $\\{A, B, C\\}$) can possibly meet minimum support, safely pruning massive sub-trees."
                },
                {
                    "question": "Why is FP-Growth generally much faster than Apriori on large transaction databases?",
                    "options": [
                        "It uses a neural network.",
                        "It compresses the database into a compact Frequent Pattern Tree (FP-Tree) and mines frequent patterns with only two passes over the data.",
                        "It deletes all items that cost less than $10.",
                        "It runs only on GPUs."
                    ],
                    "correct": 1,
                    "explanation": "FP-Growth avoids costly candidate generation and repeated disk scans by building a compact memory-efficient FP-Tree structure."
                }
            ]
        },
        {
            "id": "U08",
            "title": "Anomaly & Outlier Detection",
            "module": "unsupervised",
            "level": "intermediate",
            "prerequisites": ["F01", "F04", "S06", "U01"],
            "estimatedMinutes": 25,
            "tags": ["anomaly-detection", "outliers", "isolation-forest", "local-outlier-factor", "one-class-svm"],
            "shortDesc": "Detect rare, aberrant observations using Isolation Forests, Local Outlier Factor (LOF), and One-Class SVMs.",
            "sections": {
                "whatItIs": "Anomaly Detection (outlier detection) is the task of identifying rare observations, items, or events that differ significantly from the vast majority of data points. Key unsupervised methods include <strong>Isolation Forest</strong> (isolating points via random orthogonal cuts), <strong>Local Outlier Factor (LOF)</strong> (comparing local densities), and <strong>One-Class SVM</strong> (bounding standard data in feature space).",
                "problemItSolves": "In high-stakes domains—like credit card fraud, cyber intrusion, aircraft sensor failure, and manufacturing defects—anomalies are extremely rare (<0.01% of data) and continually evolve, rendering traditional supervised binary classification ineffective due to severe label scarcity.",
                "intuition": "Imagine finding a zebra in a crowd of thousands of pigeons in a city park. If you slice the park randomly in half, then slice the halves randomly, it will take dozens of cuts to isolate an individual pigeon surrounded by other pigeons. But the solitary zebra standing off in the corner will be isolated in just 1 or 2 cuts. Isolation Forest exploits this exact principle: anomalies are few and different, making them easy to isolate.",
                "howItWorks": "1. <strong>Build Isolation Trees:</strong> Subsample data; recursively partition by picking a random feature and a random split threshold.<br>2. <strong>Compute Path Length:</strong> Measure the tree depth $h(x)$ required to isolate sample $x$ in an external leaf.<br>3. <strong>Average Depth:</strong> Average path lengths across an ensemble of trees $\\mathbb{E}[h(x)]$.<br>4. <strong>Score Anomalies:</strong> Points with short average paths get anomaly scores near 1.0; normal cluster points have long paths and scores near 0.5.",
                "mathematics": "Isolation Forest Anomaly Score for sample $x$ with subsample size $n$:<br>$$s(x, n) = 2^{-\\frac{\\mathbb{E}[h(x)]}{c(n)}}$$<br>where $c(n)$ is the average path length of unsuccessful searches in a Binary Search Tree (BST):<br>$$c(n) = 2 \\ln(n - 1) + 0.5772156649 \\text{ (Euler's constant)} - \\frac{2(n-1)}{n}$$<br>If $\\mathbb{E}[h(x)] \\to 0$, $s \\to 1$ (definite anomaly); if $\\mathbb{E}[h(x)] \\to n-1$, $s \\to 0$ (normal inlier).",
                "dataRequirements": "Continuous numerical features. Isolation Forest is scale-invariant and does not strictly require normalization; distance-based models (LOF, One-Class SVM) require standard feature scaling.",
                "hyperparameters": [
                    {"name": "contamination", "description": "Expected proportion of outliers in the dataset (e.g. 0.01).", "effect": "Sets the decision threshold on anomaly score."},
                    {"name": "n_estimators", "description": "Number of isolation trees (typically 100 to 200).", "effect": "More trees stabilize path length estimates."},
                    {"name": "max_samples", "description": "Number of samples drawn to build each tree (standard default is 256).", "effect": "Subsampling eliminates 'swamping' and 'masking' effects."}
                ],
                "strengths": [
                    "Isolation Forest has linear time complexity $\\mathcal{O}(n \\cdot t)$ and low memory footprint.",
                    "Completely unsupervised: requires zero labeled fraudulent examples.",
                    "Subsampling prevents swamping (labeling normal points as anomalies) and masking (anomalies clustering together to hide).",
                    "Works well in high-dimensional spaces."
                ],
                "limitations": [
                    "Contamination threshold must be estimated or tuned by business constraints.",
                    "Axis-aligned splits can create artificial artifact score bands (resolved by Extended Isolation Forest).",
                    "Unsupervised: flags statistical outliers, which may not always correspond to domain-meaningful business defects."
                ],
                "evaluation": "Evaluated via Precision-Recall AUC (PR-AUC) and ROC-AUC when rare ground-truth labels are available, or through manual domain audits of top-scoring candidates.",
                "workedExample": "Monitoring a jet engine sensor stream with 50 telemetry channels (turbine temperature, oil pressure, vibration). Isolation Forest flags an anomaly score of 0.89 on a flight: while individual sensor values were technically within historical limits, their rare joint combination required only 3 random tree splits to isolate, alerting maintenance crews before mechanical failure.",
                "whenToUse": "Use for fraud detection, network intrusion detection, industrial equipment monitoring, and data cleaning (detecting corrupt sensor records).",
                "commonMistakes": [
                    "Evaluating anomaly detection with Accuracy (a model predicting 'everything is normal' achieves 99.9% accuracy on a dataset with 0.1% fraud).",
                    "Using full dataset sizes per tree in Isolation Forest (subsampling with 256 points works drastically better due to masking avoidance)."
                ],
                "furtherLearning": [
                    {"title": "Liu, Ting, Zhou: Isolation Forest (ICDM 2008 Original Paper)", "url": "https://cs.nju.edu.cn/zhouzh/zhouzh.files/publication/icdm08b.pdf"},
                    {"title": "Breunig et al.: LOF: Identifying Density-Based Local Outliers (SIGMOD 2000)", "url": "https://dl.acm.org/doi/10.1145/342009.335388"}
                ]
            },
            "quiz": [
                {
                    "question": "Why do anomalies have shorter average path lengths $\\mathbb{E}[h(x)]$ in an Isolation Forest?",
                    "options": [
                        "Because they are located in sparse regions far from the bulk of data, requiring very few random cuts to be partitioned into an isolated leaf.",
                        "Because anomalies are deleted before building the tree.",
                        "Because anomalies have negative numbers.",
                        "Because trees stop training when an anomaly appears."
                    ],
                    "correct": 0,
                    "explanation": "Because anomalies are few and attribute-different, random orthogonal splits quickly separate them from dense clusters, leading to very short path lengths from the root."
                },
                {
                    "question": "What is the danger of evaluating an anomaly detection model using standard Accuracy?",
                    "options": [
                        "Accuracy cannot be calculated on computers.",
                        "Because anomalies are so rare (e.g. 0.05%), a naive baseline that classifies 100% of samples as normal will have 99.95% accuracy while failing completely.",
                        "Accuracy only works for regression.",
                        "Accuracy requires 1,000 classes."
                    ],
                    "correct": 1,
                    "explanation": "Under extreme class imbalance, accuracy is completely deceptive. Precision, Recall, F1, and PR-AUC are required."
                },
                {
                    "question": "Why does Isolation Forest use small subsamples (e.g., 256 samples per tree) rather than the entire dataset?",
                    "options": [
                        "To prevent swamping (normal points masked by nearby anomalies) and masking (clusters of anomalies masking each other), while drastically speeding up training.",
                        "Because memory cannot store more than 256 items.",
                        "Because decision trees cannot have more than 256 leaves.",
                        "To make the model deterministic."
                    ],
                    "correct": 0,
                    "explanation": "Subsampling keeps anomalies rare and isolated. Using the full dataset allows anomalies to clump together in small groups ('masking'), making them harder to isolate."
                }
            ]
        }
    ]
print("Unsupervised module defined: 8 lessons")

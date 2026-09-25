#  Complete Python, Data Science & Deep Learning Curriculum

Welcome to my portfolio repository! This archive tracks my complete progression in programming—moving systematically from my very first days writing basic Python logic up to engineering automated web scrapers, data pipelines, and advanced deep learning neural architectures.


## Repository Directory & File Translation Key

To keep my local development workspace lightweight, I used shorthand names during class. Here is the architectural guide to how my 10+ mini-folders are organized across my learning timeline:

### Module 1: Python Programming Foundations
* `01_basicpython/`: Core logic blocks, functions, arrays, and variables.
  * `liff.py` / `liff.ipynb`: **Logical Conditionals** — Practice files using `if-elif-else` structures.
  * `sec.py` / `sec.ipynb`: **Section Lessons** — Core syntax benchmarks covering variables, loops, and lists.
###  Module 2: Data Engineering & Exploratory Analysis (EDA)
* `03_datacleaning/`: Heavy structural prep work using `Pandas` and `NumPy`.
  * `eda.ipynb`: Eliminating dataset anomalies and extreme outliers via IQR filtering.
  * Correlation Matrix: Constructing custom heatmaps and frequency bar charts with `Seaborn` and `Matplotlib`.

###  Module 3: Advanced Machine Learning & Deep Learning
* `Advanced_ML_Deep_Learning/`: Scaling code systems beyond linear baselines to tackle complex algorithms.
  * `decision_tree.py` & `random_forest.py`: Implementing non-linear branching logic paths.
  * `k_means_clustering.py`: Segmenting data profiles via unsupervised clustering.
  * `web_scraping.py`: **Data Sourcing** — Building automated scripts to harvest raw data directly from web pages.
  * `rnn_neural_network.ipynb`: **Deep Learning** — Implementing Recurrent Neural Networks (RNN) to process sequential arrays.
##  Project Application Showcase: Google Play Store Rating Predictor

As a practical application of the skills learned across this curriculum, this repository includes a dedicated Jupyter Notebook module (`reg.ipynb`) that runs an end-to-end predictive simulation pipeline using a trained Linear Regression model.

* **The Input Blueprint:** The pipeline accepts raw application metadata features (such as Review counts, Size in MB, Estimated Installations, Price, Type, and Content Age Ratings).
* **The Encoding Pipeline:** Implements an automated `.reindex()` alignment strategy to dynamically expand a single-row app profile to match the multi-column dummy-encoded structure of the training dataset.
* **Live Prediction Simulation:** When fed a brand-new app profile representing a Free Gaming App (25MB size, 1,500 reviews, 100,000 installs), the pipeline executes the learned weights to forecast a market-realistic rating of **4.17 Stars**.

###  Critical Metric Insight: Why the R² Score is Low (0.0029)
During model evaluation on an 80/20 data split, the model achieved a very tight, highly accurate **Mean Absolute Error (MAE) of 0.3885** and a **Mean Squared Error (MSE) of 0.3070**. However, the R² score returned near zero. 

This provides a vital data science discovery: **Human rating behavior is highly subjective, unpredictable, and inherently non-linear.** App store scores are driven by emotional user experiences and content quality, which means they cannot be plotted on a simple straight mathematical line based on structural metadata like file size, install count, or price. 

---

## 📄 Presentation Slides
* A complete `.pdf` presentation deck is included in the root folder, summarizing the business impact, error boundaries, and development phases of this data journey.

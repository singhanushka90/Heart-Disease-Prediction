<!-- 🔥 HERO BANNER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:ef4444&height=200&section=header&text=Heart%20Disease%20Prediction%20System&fontSize=35&fontColor=ffffff" />
</p>

<h1 align="center">🫀 Heart Disease Prediction System</h1>
<h3 align="center">AI-Powered Cardiovascular Risk Assessment</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Web-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-green?style=for-the-badge" />
</p>

<hr/>

<!-- 🔥 OVERVIEW -->
<h2>🧠 Overview</h2>

<p>
A <b>high-performance machine learning system</b> designed for early-stage heart disease detection.
Built with a focus on <b>accuracy, interpretability, and real-world healthcare impact</b>.
</p>

<p>
<b>Goal:</b> Assist in classifying patients as having <b>Heart Disease</b> or <b>Normal</b> using clinical and diagnostic data.
</p>

> 🔬 **Research Focus**: This project demonstrates the application of machine learning in healthcare for early cardiovascular risk detection.

<hr/>

<!-- 🔥 PIPELINE -->
<h2>⚙️ System Pipeline</h2>

```
┌─────────────────┐
│  Data Ingestion │
│   (heart.csv)   │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Data Preprocessing│
│  • Categorical  │
│    Encoding     │
│  • Missing Val  │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Missing Value   │
│ Handling (KNN)  │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Feature Scaling │
│ (StandardScaler)│
└────────┬────────┘
         ↓
┌─────────────────┐
│ Model Training  │
│  • SVM          │
│  • AdaBoost     │
│  • DecisionTree │
└────────┬────────┘
         ↓
┌─────────────────┐
│   Evaluation    │
│  • F1 Score     │
│  • Cross-Val    │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Web Deployment  │
│  (Streamlit)    │
└─────────────────┘
```

<hr/>

<!-- 🔥 FEATURES -->
<h2>✨ Key Features</h2>

| Feature | Description |
|---------|-------------|
| 🔎 **Multi-Model Support** | Compare SVM, AdaBoost, Decision Tree, Random Forest, XGBoost |
| 📊 **Comprehensive EDA** | Exploratory data analysis with Plotly visualizations |
| 🧹 **Data Cleaning** | KNN Imputer for missing value handling |
| 🎯 **Kernel Optimization** | Automatic SVM kernel selection (Linear, Poly, RBF, Sigmoid) |
| 🌐 **Web Interface** | Interactive Streamlit application |
| 📈 **Risk Probability** | Patient risk percentage estimation |

<hr/>

<!-- 🔥 TECH IMPLEMENTATION -->
<h2>⚙️ Technical Implementation</h2>

<ul>
  <li><b>Scikit-learn based modular pipeline</b></li>
  <li>Multiple models implemented for benchmarking</li>
  <li>Data preprocessing:
    <ul>
      <li>Encoding categorical features (Sex, ChestPainType, RestingECG, etc.)</li>
      <li>Handling zero values as missing (Cholesterol, RestingBP)</li>
      <li>KNN Imputer for missing value estimation</li>
      <li>Feature scaling with StandardScaler</li>
    </ul>
  </li>
  <li>Train-test split (80-20) with validation strategy</li>
  <li>Reproducible and clean experimentation workflow</li>
</ul>

<hr/>

<!-- 🔥 MODELS -->
<h2>🤖 Models Used</h2>

| Model | Type | Status |
|-------|------|--------|
| <b>AdaBoost Classifier</b> | Ensemble | Baseline model |
| <b>Support Vector Machine (SVM)</b> | Classification | ✅ Final selected |
| <b>Decision Tree</b> | Tree-based | GridSearchCV tuned |
| <b>Random Forest</b> | Ensemble | Additional testing |
| <b>XGBoost</b> | Gradient Boosting | Additional testing |

> 💡 **Best Model**: SVM with optimized kernel provides the best performance for this dataset.

<hr/>

<!-- 🔥 PERFORMANCE -->
<h2>📊 Performance Metrics</h2>

<ul>
  <li><b>F1 Score:</b> Weighted evaluation</li>
  <li><b>Cross-Validation:</b> 5-fold CV for robust assessment</li>
  <li><b>Kernel Optimization:</b> Linear, Poly, RBF, Sigmoid comparison</li>
  <li><b>Confusion Matrix:</b> FP vs FN analysis</li>
</ul>

<p><b>Extendable:</b> ROC-AUC • Precision-Recall • Feature Importance</p>

<hr/>

<!-- 🔥 DATASET -->
<h2>🫀 Dataset</h2>

<p><b>Heart Disease Dataset (~1000+ records)</b></p>

| Feature | Description | Type |
|---------|-------------|------|
| Age | Patient age | Numeric |
| Sex | Male/Female | Categorical |
| ChestPainType | ATA/NAP/ASY/TA | Categorical |
| RestingBP | Resting Blood Pressure | Numeric |
| Cholesterol | Serum Cholesterol | Numeric |
| FBS | Fasting Blood Sugar > 120 | Binary |
| RestingECG | Resting ECG results | Categorical |
| MaxHR | Maximum Heart Rate | Numeric |
| ExerciseAngina | Exercise Induced Angina | Binary |
| Oldpeak | ST depression | Numeric |
| ST_Slope | ST Slope | Categorical |

<p><b>Target:</b> Binary Classification → Heart Disease (1) vs Normal (0)</p>

<hr/>

<!-- 🔥 ENGINEERING -->
<h2>🧠 Key Engineering Decisions</h2>

<ul>
  <li>Focus on <b>generalization over overfitting</b></li>
  <li>Designed <b>scalable and reusable pipeline</b></li>
  <li>Balanced classification performance</li>
  <li>Emphasis on <b>interpretability</b> (critical for healthcare)</li>
  <li>KNN Imputer for realistic missing value handling</li>
  <li>Kernel comparison for optimal SVM performance</li>
  <li>StandardScaler for consistent feature scaling</li>
</ul>

<hr/>

<!-- 🔥 CAPABILITIES -->
<h2>⚡ System Capabilities</h2>

<ul>
  <li>🔎 Accurate Heart Disease Classification</li>
  <li>🧠 Generalizable Model Performance</li>
  <li>📊 Explainable Predictions</li>
  <li>⚡ Efficient Training Pipeline</li>
  <li>🌐 Interactive Web Interface (Streamlit)</li>
  <li>📈 Risk Probability Estimation</li>
  <li>📉 Data Visualization (Plotly)</li>
</ul>

<hr/>

<!-- 🔥 TECH STACK -->
<h2>🛠️ Tech Stack</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" />
  <img src="https://skillicons.dev/icons?i=scikit" />
  <img src="https://skillicons.dev/icons?i=numpy" />
  <img src="https://skillicons.dev/icons?i=pandas" />
  <img src="https://skillicons.dev/icons?i=matplotlib" />
  <img src="https://skillicons.dev/icons?i=streamlit" />
  <img src="https://skillicons.dev/icons?i=plotly" />
</p>

| Library | Purpose |
|---------|---------|
| 🔢 NumPy | Numerical computing |
| 📊 Pandas | Data manipulation |
| 📈 Matplotlib/Seaborn | Visualization |
| 🎨 Plotly | Interactive charts |
| 🤖 Scikit-learn | ML algorithms |
| 🌐 Streamlit | Web application |

<hr/>

<!-- 🔥 FILES -->
<h2>📁 Project Files</h2>

```
Heart_Prediction/
├── 📓 heart_predict.ipynb    # Complete ML pipeline
├── 🌐 heart.py               # Streamlit web app
├── 🤖 heart_model.pkl        # Trained SVM model
├── 📊 heart_scaler.pkl       # Fitted StandardScaler
├── 📋 heart.csv              # Dataset
└── 📖 README.md              # This file
```

<hr/>

<!-- 🔥 INSTALLATION -->
<h2>🚀 Installation</h2>

```bash
# Clone the repository
git clone https://github.com/yourusername/Heart_Prediction.git
cd Heart_Prediction

# Install required packages
pip install -r requirements.txt

# Run the Streamlit app
streamlit run heart.py
```

### Requirements
```
pandas
numpy
scikit-learn
streamlit
plotly
xgboost
pickle
```

<hr/>

<!-- 🔥 USAGE -->
<h2>💻 Usage</h2>

### Run Web Application
```bash
streamlit run heart.py
```

### Run Jupyter Notebook
```bash
jupyter notebook heart_predict.ipynb
```

### Load Model in Python
```python
import pickle
import numpy as np

model = pickle.load(open('heart_model.pkl', 'rb'))
scaler = pickle.load(open('heart_scaler.pkl', 'rb'))

# Example prediction
features = np.array([[45, 1, 2, 120, 200, 0, 1, 150, 0, 1.0, 1]])
scaled_features = scaler.transform(features)
prediction = model.predict(scaled_features)
```

<hr/>

<!-- 🔥 HIGHLIGHTS -->
<h2>📊 Engineering Highlights</h2>

<ul>
  <li>🧩 <b>Modular ML pipeline</b> - Clean, reusable code structure</li>
  <li>⚡ <b>Clean & reproducible workflow</b> - Well-documented steps</li>
  <li>📈 <b>Strong validation strategy</b> - 5-fold cross-validation</li>
  <li>🧠 <b>Healthcare-focused design</b> - Interpretable results</li>
  <li>🌐 <b>Interactive web deployment</b> - User-friendly interface</li>
  <li>🎯 <b>Kernel optimization for SVM</b> - Automatic best kernel selection</li>
  <li>🔍 <b>Missing value handling</b> - KNN imputation</li>
</ul>

<hr/>

<!-- 🔥 IMPACT -->
<h2>💡 Real-World Impact</h2>

<ul>
  <li>🏥 <b>Supports early heart disease detection</b> - Critical for patient outcomes</li>
  <li>👨‍⚕️ <b>Assists doctors in diagnosis</b> - Second opinion system</li>
  <li>📊 <b>Reduces manual analysis time</b> - Automated risk assessment</li>
  <li>🌍 <b>Scalable healthcare AI solution</b> - Can be deployed globally</li>
  <li>💓 <b>Patient risk probability estimation</b> - Quantitative risk scores</li>
</ul>

<hr/>

<!-- 🔥 FUTURE -->
<h2>🔮 Future Enhancements</h2>

| Enhancement | Description | Priority |
|-------------|-------------|----------|
| 🧠 Deep Learning | ANN/CNN models | High |
| 📊 Explainability | SHAP/LIME integration | High |
| 🌐 API Deployment | FastAPI wrapper | Medium |
| 🏥 Hospital Integration | EHR system connection | Medium |
| 📱 Mobile App | React Native/Flutter | Low |
| 🔔 Alert System | Email/SMS notifications | Low |

<hr/>

<!-- 🔥 RESEARCH -->
<h2>📄 Research Perspective</h2>

<h3>Abstract</h3>
<p>
This system demonstrates how machine learning can assist in early-stage heart disease detection using structured clinical data. It balances <b>accuracy, interpretability, and generalization</b>, making it suitable for real-world healthcare deployment.
</p>

<h3>Key Insight</h3>
<p>
<b>Reliable AI in healthcare = Accuracy + Interpretability + Generalization</b>
</p>

<h3>Methodology</h3>
<ul>
  <li>Data preprocessing with KNN imputation for missing values</li>
  <li>Multiple model comparison for optimal performance</li>
  <li>GridSearchCV for hyperparameter tuning</li>
  <li>5-fold cross-validation for robust evaluation</li>
</ul>

<hr/>

<!-- 🔥 LICENSE -->
<h2>📜 License</h2>

<p>This project is for educational and research purposes.</p>

<hr/>

<!-- 🔥 AUTHOR -->
<h2>👨‍💻 Author</h2>

<p align="center">
  <b>Anushka Singh</b><br/>
  AI Engineer | ML Systems | Healthcare AI<br/>
  <br/>
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=linkedin" />
  <img src="https://skillicons.dev/icons?i=kaggle" />
</p>

<hr/>

<!-- 🔥 FINAL INSIGHT -->
<h2 align="center">⚡ Final Insight</h2>

<p align="center">
<b>“Building AI systems that don’t just predict — but assist in saving lives.”</b>
</p>

<p align="center">
<em>Early detection saves lives. Machine learning is the tool, healthcare is the purpose.</em>
</p>

<hr/>

<p align="center">
  ⭐ If you found this project helpful, please star the repository!
</p>

<!-- 🔥 FOOTER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:ef4444,100:0f172a&height=120&section=footer"/>
</p>

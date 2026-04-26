<!-- 🔥 HERO BANNER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:ef4444&height=200&section=header&text=Heart%20Disease%20Prediction%20System&fontSize=35&fontColor=ffffff" />
</p>

<h1 align="center">🫀 Heart Disease Prediction System</h1>
<h3 align="center">AI-Powered Cardiovascular Risk Assessment</h3>

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

<hr/>

<!-- 🔥 PIPELINE -->
<h2>⚙️ System Pipeline</h2>

<pre>
Data Ingestion
      ↓
Data Preprocessing
      ↓
Missing Value Handling (KNN Imputer)
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Evaluation
      ↓
Web Deployment (Streamlit)
</pre>

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

<ul>
  <li><b>AdaBoost Classifier</b> → Baseline model</li>
  <li><b>Support Vector Machine (SVM)</b> → Final selected model (with kernel optimization)</li>
  <li><b>Decision Tree</b> → With GridSearchCV hyperparameter tuning</li>
  <li><b>Random Forest & XGBoost</b> → Additional benchmarking</li>
</ul>

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

<ul>
  <li>Age</li>
  <li>Sex (Male/Female)</li>
  <li>Chest Pain Type (ATA, NAP, ASY, TA)</li>
  <li>Resting Blood Pressure</li>
  <li>Cholesterol</li>
  <li>Fasting Blood Sugar</li>
  <li>Resting ECG</li>
  <li>Max Heart Rate</li>
  <li>Exercise Angina</li>
  <li>Oldpeak (ST depression)</li>
  <li>ST Slope</li>
</ul>

<p><b>Target:</b> Binary Classification → Heart Disease vs Normal</p>

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
</ul>

<hr/>

<!-- 🔥 TECH STACK -->
<h2>🛠️ Tech Stack</h2>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange" />
  <img src="https://img.shields.io/badge/Pandas-Data-blue" />
  <img src="https://img.shields.io/badge/NumPy-Compute-green" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-red" />
  <img src="https://img.shields.io/badge/Streamlit-Web-blue" />
  <img src="https://img.shields.io/badge/Plotly-Visualization-purple" />
</p>

<hr/>

<!-- 🔥 FILES -->
<h2>📁 Project Files</h2>

<ul>
  <li><b>heart_predict.ipynb</b> - Complete ML pipeline with EDA and model training</li>
  <li><b>heart.py</b> - Streamlit web application for predictions</li>
  <li><b>heart_model.pkl</b> - Trained SVM model</li>
  <li><b>heart_scaler.pkl</b> - Fitted StandardScaler</li>
  <li><b>heart.csv</b> - Dataset</li>
</ul>

<hr/>

<!-- 🔥 HIGHLIGHTS -->
<h2>📊 Engineering Highlights</h2>

<ul>
  <li>🧩 Modular ML pipeline</li>
  <li>⚡ Clean & reproducible workflow</li>
  <li>📈 Strong validation strategy</li>
  <li>🧠 Healthcare-focused design</li>
  <li>🌐 Interactive web deployment</li>
  <li>🎯 Kernel optimization for SVM</li>
</ul>

<hr/>

<!-- 🔥 IMPACT -->
<h2>💡 Real-World Impact</h2>

<ul>
  <li>🏥 Supports early heart disease detection</li>
  <li>👨‍⚕️ Assists doctors in diagnosis</li>
  <li>📊 Reduces manual analysis time</li>
  <li>🌍 Scalable healthcare AI solution</li>
  <li>💓 Patient risk probability estimation</li>
</ul>

<hr/>

<!-- 🔥 FUTURE -->
<h2>🔮 Future Enhancements</h2>

<ul>
  <li>Deep Learning models (ANN / CNN)</li>
  <li>Explainability tools (SHAP, LIME)</li>
  <li>API Deployment (FastAPI)</li>
  <li>Hospital system integration</li>
  <li>Ensemble methods for improved accuracy</li>
</ul>

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

<hr/>

<!-- 🔥 USAGE -->
<h2>🚀 Usage</h2>

<pre>
# Run the Streamlit web app
streamlit run heart.py
</pre>

<hr/>

<!-- 🔥 AUTHOR -->
<h2>👨‍💻 Author</h2>

<p align="center">
  <b>Anushka Singh</b><br/>
  AI Engineer | ML Systems | Healthcare AI
</p>

<hr/>

<!-- 🔥 FINAL INSIGHT -->
<h2 align="center">⚡ Final Insight</h2>

<p align="center">
<b>“Building AI systems that don’t just predict — but assist in saving lives.”</b>
</p>

<!-- 🔥 FOOTER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:ef4444,100:0f172a&height=120&section=footer"/>
</p>

## Credit Card Fraud Detection

Project to detect credit card fraud using advanced machine learning and techniques for imbalanced data.

---

## Key Technologies and Techniques

- Python (pandas, numpy, scikit-learn)  
- Models: CatBoost, XGBoost, LightGBM, Stacking Ensemble  
- Balancing: SMOTE, SMOTEENN  
- Hyperparameter Optimization: Optuna  
- Interpretability: SHAP  

---

## Test Set Results

| Metric     | Value       |  
|------------|-------------|  
| PR-AUC     | 0.8625      |  
| F1-score   | 0.8233      |  
| Recall     | 0.8156      |  

---

## Critical Evaluation

Multiple techniques were compared to handle imbalance and optimize fraud detection, with dynamic threshold tuning to improve the trade-off between false positives and false negatives.  
Stacking showed the best balance, reflecting a robust and scalable approach for production.

---

## Project Structure

Credit_Card_Fraud_Prediction/

├── notebooks/

├── src/

├── models/

├── data/

├── reports/

├── requirements.txt

└── README.md

## Next Steps

- Modularize code for production  
- Deploy API with FastAPI  
- Dockerize and orchestrate with CI/CD  
- Automate retraining and monitoring  

---

## Contact

Heberth Caripa  
heberthcaripa@gmail.com
https://www.linkedin.com/in/heberth-caripa/
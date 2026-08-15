# 💧 Water Consumption Prediction

A beginner-friendly machine learning project that predicts daily water usage for households using Linear Regression.

## 📋 Project Overview
This project demonstrates how machine learning can be used to solve a real-world problem. It predicts the daily water consumption of a household based on simple household features.

## 🎯 Objective
- To predict daily water usage for households
- To understand machine learning fundamentals
- To build a practical AI application
- To create a project suitable for college presentation

## 📚 Libraries Used
- `pandas` - Data handling and manipulation
- `numpy` - Numerical computations
- `scikit-learn` - Machine learning algorithms
- `streamlit` - Interactive web interface
- `pickle` - Model serialization

## 📊 Dataset Description
The dataset contains 300 rows with the following features:
- **Family_Members**: Number of family members (1-7)
- **Bathrooms**: Number of bathrooms (1-3)
- **Washing_Machine**: Whether the household has a washing machine (0 or 1)
- **Garden**: Whether the household has a garden (0 or 1)
- **Daily_Water_Usage**: Daily water usage in litres (Target variable)

### Data Generation Formula
Water Usage = (120 × Family Members) + (25 × Bathrooms) + (50 × Washing Machine) + (80 × Garden) + Random Variation (±20)

## 🤖 Machine Learning Algorithm
**Linear Regression** is used because:
- Simple and easy to understand
- Suitable for beginners
- Fast to train
- Excellent for this prediction task

## 📁 Folder Structure
```
Water Consumption Prediction/
├── app.py                          # Streamlit web application
├── train_model.py                  # Training script
├── water_dataset.csv               # Generated dataset
├── model.pkl                       # Trained model
├── requirements.txt                # Required libraries
└── README.md                       # Project documentation
```

## 🚀 Installation Steps
1. Clone or download the project folder
2. Navigate to the project directory
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ How to Run

### Step 1: Train the Model
```bash
python train_model.py
```
This will:
- Generate the dataset
- Display dataset information
- Train the Linear Regression model
- Save the model as `model.pkl`

### Step 2: Run the Streamlit App
```bash
python -m streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`

## 📈 Expected Output
When you enter household details and click "Predict", you'll see:
- Estimated daily water usage in litres
- Input summary
- A note about prediction accuracy

## 🔍 Model Performance
- **R² Score**: Typically 1.00 (perfect fit for synthetic data)
- **Mean Absolute Error**: Varies based on dataset generation

## 💡 How to Use the App
1. Enter the number of family members
2. Enter the number of bathrooms
3. Select "Yes" or "No" for washing machine
4. Select "Yes" or "No" for garden
5. Click "Predict Water Usage"
6. View the estimated water consumption

## 🐛 Common Errors and Solutions

### Error: Model not found
**Solution**: Run `python train_model.py` first to train the model

### Error: Module not found
**Solution**: Install required libraries: `pip install -r requirements.txt`

### Error: Port already in use
**Solution**: Use a different port: `streamlit run app.py --server.port 8503`

## 🎓 Project Features
✅ Beginner-friendly code  
✅ Clear comments and explanations  
✅ Realistic dataset generation  
✅ Interactive Streamlit interface  
✅ Professional output format  
✅ Easy to explain in viva  

## 🚀 Future Scope
- Add more features (e.g., climate, season)
- Implement multiple machine learning algorithms
- Create data visualization and charts
- Deploy the app online
- Collect real-world water consumption data

## 📝 Notes
- The predictions are approximate
- Actual water usage may vary based on real-life conditions
- This is a demonstration project for educational purposes

## 👨‍🎓 Suitable For
- College AI/Data Science projects
- Machine learning beginners
- Viva presentations
- Portfolio projects

---

**Created for**: College AI & Data Science Project  
**Algorithm**: Linear Regression  
**Status**: Complete and Ready to Use ✓

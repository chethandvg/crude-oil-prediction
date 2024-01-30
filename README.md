# crude-oil-prediction
Predicting crude oil prices accurately is crucial for making well-informed decisions, managing risks, and allocating resources effectively within the petroleum industry. The challenge lies in developing a strong supervised learning model that can predict crude oil prices by utilizing historical data and relevant features. The complexity of factors influencing oil prices, such as geopolitical events, economic indicators, and supply-demand dynamics, makes it challenging to create a reliable predictive model. The goal is to design a model capable of analyzing diverse datasets, including historical crude oil prices, economic indicators,and other relevant variables. The model should be proficient in understanding complex patterns and relationships within the data to provide accurate predictions for both short-term and long-term scenarios. Key considerations include using data preprocessing techniques to handle missing values, outliers, and ensure data consistency. Feature engineering is crucial for extracting meaningful information from input variables, and the model should be capable of handling non-linear relationships and temporal dependencies inherent in time-series data. The choice of an appropriate supervised learning algorithm, whether regression-based models, support vector machines, or neural networks, should be based on its ability to capture the intricate dynamics of crude oil price movements. The success of the proposed model will be evaluated based on its accuracy in predicting future crude oil prices, using performance metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared. Additionally, the model's interpretability and explainability will be crucial for gaining insights into the underlying factors influencing its predictions. In essence, addressing this problem not only contributes to improved financial decision-making within the petroleum industry but also enhances our understanding of the complex dynamics influencing crude oil prices on the global stage.

datasets-It contains the data set of historical oil data
src- The file contains the machine learning ipynb file which has the ETL techniques and model building
UserInterface- The folder contains the models which the streamlit file use and the UI_SRH.py file which handles the front ens streamlit code
Install_dependencies.sh Contains the required dependencies and the requirements

Step 1:Install dependencies
'''
!bash install_dependencies.sh
'''

Step 2:
'''
!python UI_SRH.py
'''

Step 3:
'''
streamlit run lstm.py
'''
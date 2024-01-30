# Crude Oil Prediction

Predicting crude oil prices accurately is crucial for making well-informed decisions, managing risks, and allocating resources effectively within the petroleum industry. This project aims to design a robust supervised learning model capable of predicting crude oil prices by leveraging historical data and relevant features.

## Project Overview

### Project Structure

- **datasets:** Contains the dataset of historical oil data.
- **src:** Includes the machine learning Jupyter Notebook file with ETL techniques and model building.
- **UserInterface:** Houses the models used by the Streamlit file and the `UI_SRH.py` file, which handles the front-end Streamlit code.
- **Install_dependencies.sh:** Shell script containing the required dependencies and the `install_dependencies.sh` file.

## Getting Started

### Prerequisites

Make sure you have [Python](https://www.python.org/downloads/) installed on your system.

### Installation

Run the following command to install project dependencies:

```bash
bash install_dependencies.sh
```

### Usage

1. Run the Streamlit UI:

```bash
streamlit run UI_SRH.py
```

2. Start Streamlit:

```bash
streamlit run lstm.py
```

## Project Members

- **VENKAT CHAVAN N** - 3121282
- **CHETHAN D V** - 3119674
- **PRADYUMNA S R** - 3119640

## Evaluation Metrics

The success of the proposed model will be evaluated based on its accuracy in predicting future crude oil prices, using performance metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared. The interpretability and explainability of the model will be crucial for gaining insights into the underlying factors influencing its predictions.

## Acknowledgments

- Special thanks to the project members for their contributions.

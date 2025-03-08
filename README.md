# AntiMoney-Laundering
# Anti-Money Laundering (AML) Network Analysis

This project leverages **network analysis** techniques in Python to detect suspicious transactions and relationships in financial data. Using graph-based methodologies, we identify high-risk entities and analyze transaction networks for anti-money laundering (AML) insights.

## Features
- Load and process transaction data efficiently
- Build transaction graphs using **NetworkX**
- Identify key entities using **PageRank and Degree Centrality**
- Detect suspicious clusters with **Louvain community detection**
- Visualize transaction networks with **Matplotlib & NetworkX**

## Installation
Ensure you have Python installed, then install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AML-Network-Analysis.git
   cd AML-Network-Analysis
   ```
2. Run the Jupyter Notebook inside the `notebooks/` directory to explore the analysis.
3. Alternatively, execute the Python script for a quick transaction graph analysis:
   ```bash
   python scripts/transaction_analysis.py
   ```

## Data
The `data/` folder should contain a **CSV file** with transaction data, formatted as follows:
```
Sender,Receiver,Amount,Timestamp
A,B,100,2024-01-01 10:00:00
B,C,250,2024-01-02 11:30:00
C,D,90,2024-01-03 15:45:00
...
```

## License
This project is licensed under the **MIT License**. Feel free to use and contribute!

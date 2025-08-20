# 📊 KeyStone — LSTM-BERT Stock Movement Predictor

KeyStone is a full-stack machine learning system that forecasts stock market movements using a hybrid **BiLSTM + BERT** architecture. It captures temporal dependencies through LSTM and incorporates news/textual sentiment via BERT. The project includes a powerful scraping engine and a modular pipeline for data preprocessing, model training, and prediction.

---

## 🧠 Core Features

- 🔁 **BiLSTM Model** — Captures time-series patterns in stock data.
- 🧾 **BERT Model** — Processes and integrates news headlines for sentiment-based prediction.
- 🧹 **Custom Preprocessing Pipelines** — Efficient data transformation and slicing.
- 🌐 **Scraper System** — Collects financial news using Playwright/Selenium.
- 🚀 **Frontend (WIP)** — Built with React + Vite + TypeScript.
- ⚙️ **Highly Modular Codebase** — Organized for iterative development and experimentation.

---

## 📁 Project Structure

```bash
KeyStone/
├── BERT_Model/           # Fine-tuned BERT model & training scripts
├── BERT_Preprocess/      # Text preprocessing and tokenization
├── BiLSTM_Model/         # BiLSTM architecture, trainer, loss
├── BiLSTM_Preprocess/    # Scalers, transforms, time slicing
├── Checkpoints/          # Saved PyTorch models
├── Datasets/             # News and stock datasets (JSON, CSV)
├── Scraper/              # Playwright/Selenium-based news scrapers
├── frontend/             # React + Vite + TypeScript frontend (WIP)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
````

---

## ⚙️ Setup Instructions

### 🔹 Backend (Python + Flask + PyTorch)

# 1. Clone the repository
```
git clone https://github.com/Danyl101/KeyStone.git
```

# 2. Set up virtual environment
```
python -m venv venv
```
# On Windows:
```
venv\Scripts\activate
```
# On macOS/Linux:
```
source venv/bin/activate
```

# 3. Install required packages
```
pip install -r requirements.txt
```

### 🔹 Run Model Training

# Train BiLSTM
```
python BiLSTM_Model/main.py
```

# Train BERT
```
python BERT_Model/main.py
```

### 🔹 (Optional) Start Flask API


# If Flask API endpoints are implemented
```
python frontend/src/api/endpoint_api.py
```

---

### 🔹 Frontend (React + Vite + TypeScript) — \[WIP]

> Ensure Node.js is installed before proceeding.

bash
# Navigate to frontend directory
```
cd frontend
```

# Install dependencies
```
npm install
```

# Start development server
```
npm run dev
```

---

## 🧪 Workflow

1. **Data Scraping** → News is collected using automated scrapers.
2. **Preprocessing**:

   * `BERT`: Cleans, tokenizes, and embeds news data.
   * `BiLSTM`: Processes time series into sliding windows with features.
3. **Model Training**:

   * Separate training pipelines for BERT and BiLSTM.
   * Possible fusion via ensemble or stacked models.
4. **Prediction**:

   * Predictions stored locally or returned via Flask API.

---

## 🛠 Tech Stack

| Layer     | Technology                           |
| --------- | ------------------------------------ |
| Backend   | Python, Flask, PyTorch               |
| Frontend  | React, Vite, TypeScript              |
| Scraping  | Selenium, Playwright, BeautifulSoup  |
| ML Models | BERT (HuggingFace), BiLSTM (PyTorch) |
| DevOps    | Git, GitHub                          |

---

### BiLSTM Results

### 📊 Metrics & Results

| Metric   | Result   |
| -------- | -------- |
| MSE      | \~0.0299 |
| RMSE     | \~0.1730 |
| MAE      | \~0.1493 |
| MAPE     | \~6.08 % |

### 🔍 Visualization

<img width="1504" height="853" alt="Screenshot 2025-08-06 105231" src="https://github.com/user-attachments/assets/bbdc25dd-91b6-4548-844e-7a5c9249c133" />


## 📌 Roadmap / TODO

* [ ] Build robust Flask API endpoints
* [ ] Complete React frontend integration
* [ ] Add Docker support
* [ ] Automate evaluation + model dashboard
* [ ] CI/CD setup for deployment

---

## 📄 License

This project is licensed under the MIT License.
See the `LICENSE` file for details.

---

## 🤝 Contributions

Feel free to fork this repo, open issues, or submit pull requests!
For significant changes, please discuss via GitHub issues first.

## Run Locally — ML Pipeline

### 1) Create and activate virtual environment

```bash
python -m venv .venv

# Linux / Mac
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate
```

### 2) Install dependencies

```bash
pip install --upgrade pip
pip install -r data-generator/requirements.txt
pip install -r ml/requirements.txt
```

### 3) Generate mock dataset

```bash
python data-generator/generate_mock_data.py \
  --rows 5000 \
  --out data-generator/output/clientes.csv
```

### 4) Train model

```bash
python ml/train.py \
  --input data-generator/output/clientes.csv \
  --model ml/model.pkl
```

### 5) Run predictions

```bash
python ml/predict.py \
  --model ml/model.pkl \
  --input data-generator/output/clientes.csv
```

### Expected Output

- Trained model file:

```
ml/model.pkl
```

- Sample prediction output:

```
 customer_id | churn_score
------------|-------------
 1          | 0.12
 2          | 0.87
 3          | 0.34
```

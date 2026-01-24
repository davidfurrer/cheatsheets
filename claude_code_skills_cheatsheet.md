# Claude Code Skills Cheatsheet

Practical examples of using Claude Code for Data Science and AI Engineering tasks.

## Data Science Skills

### 1. Exploratory Data Analysis (EDA)

**Scenario**: Analyze a dataset and create visualizations

```bash
claude "analyze the customer_data.csv file and create visualizations for:
- Distribution of customer ages
- Correlation between purchase amount and customer lifetime value
- Monthly sales trends
Save the plots in the analysis/ folder"
```

**What Claude Code does**:
1. Reads and validates the CSV file
2. Performs statistical analysis (mean, median, outliers)
3. Creates matplotlib/seaborn visualizations
4. Generates summary statistics
5. Saves plots and creates a summary report

**Example Implementation**:

```python
# Claude Code will create something like:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and explore data
df = pd.read_csv('customer_data.csv')
print(df.describe())
print(df.info())

# Age distribution
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=30, edgecolor='black')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('analysis/age_distribution.png')
plt.close()

# Correlation analysis
correlation = df[['purchase_amount', 'customer_lifetime_value']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.savefig('analysis/correlation_heatmap.png')
plt.close()

# Monthly trends
df['date'] = pd.to_datetime(df['date'])
monthly_sales = df.groupby(df['date'].dt.to_period('M'))['sales'].sum()
monthly_sales.plot(kind='line', figsize=(12, 6))
plt.title('Monthly Sales Trends')
plt.savefig('analysis/monthly_trends.png')
plt.close()
```

**Best Practices**:
- Specify exact columns and metrics needed
- Request statistical summaries alongside visualizations
- Ask for data quality checks (missing values, outliers)
- Specify visualization library preferences (matplotlib, plotly, seaborn)

---

### 2. Machine Learning Pipeline Development

**Scenario**: Build and evaluate a classification model

```bash
claude "create a machine learning pipeline for the fraud_detection.csv:
1. Split data into train/test (80/20)
2. Handle missing values and scale features
3. Train Random Forest and XGBoost classifiers
4. Compare models using accuracy, precision, recall, and F1-score
5. Create confusion matrices and ROC curves
6. Save the best model to models/fraud_detector.pkl"
```

**What Claude Code does**:
1. Loads and preprocesses data
2. Creates train/test splits with proper stratification
3. Implements preprocessing pipeline (imputation, scaling)
4. Trains multiple models with cross-validation
5. Generates comprehensive evaluation metrics
6. Creates visualizations for model comparison
7. Saves the best performing model

**Example Implementation**:

```python
# Claude Code will create:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score,
                             confusion_matrix, roc_curve, auc)
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# Load data
df = pd.read_csv('fraud_detection.csv')
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Preprocessing pipeline
imputer = SimpleImputer(strategy='median')
scaler = StandardScaler()

X_train_processed = scaler.fit_transform(imputer.fit_transform(X_train))
X_test_processed = scaler.transform(imputer.transform(X_test))

# Train models
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'XGBoost': XGBClassifier(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    # Train
    model.fit(X_train_processed, y_train)

    # Predict
    y_pred = model.predict(X_test_processed)
    y_pred_proba = model.predict_proba(X_test_processed)[:, 1]

    # Metrics
    results[name] = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred),
        'model': model,
        'predictions': y_pred,
        'probabilities': y_pred_proba
    }

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{name} - Confusion Matrix')
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.savefig(f'models/{name.lower().replace(" ", "_")}_confusion_matrix.png')
    plt.close()

    # ROC Curve
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'{name} - ROC Curve')
    plt.legend()
    plt.savefig(f'models/{name.lower().replace(" ", "_")}_roc_curve.png')
    plt.close()

# Compare models
print("\nModel Comparison:")
print("-" * 70)
for name, metrics in results.items():
    print(f"\n{name}:")
    print(f"  Accuracy:  {metrics['accuracy']:.4f}")
    print(f"  Precision: {metrics['precision']:.4f}")
    print(f"  Recall:    {metrics['recall']:.4f}")
    print(f"  F1-Score:  {metrics['f1']:.4f}")

# Save best model (by F1-score)
best_model_name = max(results.items(), key=lambda x: x[1]['f1'])[0]
best_model = results[best_model_name]['model']
joblib.dump(best_model, 'models/fraud_detector.pkl')
print(f"\nBest model ({best_model_name}) saved to models/fraud_detector.pkl")
```

**Advanced Usage**:

```bash
# Feature engineering
claude "add feature engineering to the pipeline:
- Create interaction features between amount and location
- Encode categorical variables using target encoding
- Add polynomial features for numerical columns"

# Hyperparameter tuning
claude "add GridSearchCV for hyperparameter tuning on the Random Forest model
with 5-fold cross-validation"

# Feature importance analysis
claude "create a feature importance plot showing top 20 features
for the trained Random Forest model"
```

**Best Practices**:
- Always use stratified splits for imbalanced datasets
- Request cross-validation for robust evaluation
- Compare multiple models before selecting
- Ask for feature importance analysis
- Specify random seeds for reproducibility
- Request proper handling of imbalanced classes if applicable

---

## AI Engineering Skills

### 1. Fine-tuning LLM Models

**Scenario**: Fine-tune a model for custom task

```bash
claude "set up a fine-tuning pipeline for GPT model:
1. Prepare the training data from conversations.jsonl
2. Validate data format (prompt/completion pairs)
3. Create train/validation split
4. Set up training configuration with appropriate hyperparameters
5. Implement evaluation metrics (perplexity, BLEU score)
6. Add early stopping and checkpointing"
```

**Example Implementation**:

```python
# Claude Code will create:
import json
import openai
from datasets import load_dataset
from transformers import (
    GPT2Tokenizer, GPT2LMHeadModel,
    TrainingArguments, Trainer,
    DataCollatorForLanguageModeling
)
import torch
from torch.utils.data import random_split
import evaluate

# Load and validate data
def load_and_validate_data(file_path):
    with open(file_path, 'r') as f:
        data = [json.loads(line) for line in f]

    # Validate format
    required_keys = ['prompt', 'completion']
    for idx, item in enumerate(data):
        if not all(key in item for key in required_keys):
            raise ValueError(f"Invalid format at line {idx}")

    return data

data = load_and_validate_data('conversations.jsonl')
print(f"Loaded {len(data)} examples")

# Prepare dataset
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token

def preprocess_function(examples):
    texts = [f"Prompt: {ex['prompt']}\nCompletion: {ex['completion']}"
             for ex in examples]
    return tokenizer(texts, truncation=True, padding='max_length',
                     max_length=512)

# Create train/val split
train_size = int(0.9 * len(data))
val_size = len(data) - train_size

train_data = data[:train_size]
val_data = data[train_size:]

print(f"Training examples: {len(train_data)}")
print(f"Validation examples: {len(val_data)}")

# Load model
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Training configuration
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=100,
    eval_strategy="steps",
    eval_steps=500,
    save_steps=1000,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

# Evaluation metrics
perplexity_metric = evaluate.load("perplexity")

def compute_metrics(eval_preds):
    predictions, labels = eval_preds
    perplexity = perplexity_metric.compute(
        predictions=predictions,
        model_id='gpt2'
    )
    return {"perplexity": perplexity}

# Initialize trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=val_data,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

# Train
trainer.train()

# Save final model
model.save_pretrained('./fine_tuned_model')
tokenizer.save_pretrained('./fine_tuned_model')
print("Model saved to ./fine_tuned_model")
```

**Best Practices**:
- Validate data format before training
- Use appropriate batch sizes for GPU memory
- Implement early stopping to prevent overfitting
- Monitor multiple metrics (loss, perplexity, task-specific metrics)
- Save checkpoints regularly
- Use gradient accumulation for larger effective batch sizes

---

### 2. Building RAG (Retrieval Augmented Generation) Systems

**Scenario**: Create a document QA system with RAG

```bash
claude "create a RAG system for our documentation:
1. Set up vector database (ChromaDB or FAISS)
2. Implement document chunking with overlap
3. Create embeddings using OpenAI/Sentence Transformers
4. Build retrieval function with similarity search
5. Implement prompt template for context injection
6. Add re-ranking for better results
7. Create a simple API endpoint"
```

**Example Implementation**:

```python
# Claude Code will create:
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader, TextLoader
import chromadb
from typing import List
import numpy as np

# 1. Load documents
loader = DirectoryLoader('./docs', glob="**/*.md", loader_cls=TextLoader)
documents = loader.load()
print(f"Loaded {len(documents)} documents")

# 2. Chunk documents with overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)
chunks = text_splitter.split_documents(documents)
print(f"Created {len(chunks)} chunks")

# 3. Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
vectorstore.persist()

# 4. Set up retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

# 5. Create prompt template
from langchain.prompts import PromptTemplate

prompt_template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context:
{context}

Question: {question}

Answer: Let me provide a detailed answer based on the documentation:"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# 6. Set up LLM
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0
)

# 7. Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

# Advanced: Re-ranking function
from sentence_transformers import CrossEncoder

def rerank_documents(query: str, documents: List, top_k: int = 3):
    """Re-rank documents using cross-encoder for better relevance"""
    cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

    pairs = [[query, doc.page_content] for doc in documents]
    scores = cross_encoder.predict(pairs)

    # Sort by score
    sorted_indices = np.argsort(scores)[::-1][:top_k]
    return [documents[i] for i in sorted_indices]

# Query function with re-ranking
def query_with_reranking(question: str):
    # Initial retrieval
    docs = retriever.get_relevant_documents(question)

    # Re-rank
    reranked_docs = rerank_documents(question, docs, top_k=3)

    # Create context
    context = "\n\n".join([doc.page_content for doc in reranked_docs])

    # Generate answer
    result = qa_chain({"query": question})

    return {
        "answer": result["result"],
        "sources": [doc.metadata for doc in result["source_documents"]],
        "confidence": "high" if len(reranked_docs) >= 3 else "medium"
    }

# 8. Simple API endpoint (FastAPI)
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str
    sources: List[dict]
    confidence: str

@app.post("/query", response_model=Answer)
async def answer_question(query: Query):
    result = query_with_reranking(query.question)
    return Answer(**result)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Run with: uvicorn rag_api:app --reload

# Example usage:
if __name__ == "__main__":
    # Test query
    question = "How do I configure the authentication system?"
    result = query_with_reranking(question)

    print(f"Question: {question}")
    print(f"\nAnswer: {result['answer']}")
    print(f"\nSources: {result['sources']}")
    print(f"Confidence: {result['confidence']}")
```

**Advanced Features**:

```bash
# Add semantic caching
claude "implement semantic caching to avoid re-computing similar queries"

# Hybrid search (keyword + semantic)
claude "add BM25 keyword search and combine with vector search using
reciprocal rank fusion"

# Multi-query retrieval
claude "implement multi-query retrieval where we generate multiple
variations of the user query for better coverage"

# Streaming responses
claude "add streaming support so answers are generated token by token"
```

**Best Practices**:
- Use appropriate chunk sizes (typically 500-1500 tokens)
- Include chunk overlap to preserve context
- Implement re-ranking for better relevance
- Add metadata filtering for domain-specific searches
- Monitor retrieval quality with metrics (MRR, NDCG)
- Cache embeddings to reduce API costs
- Use hybrid search for better recall

---

### 3. Model Deployment and Monitoring

**Scenario**: Deploy model with monitoring

```bash
claude "create a production deployment setup for the fraud detection model:
1. Create FastAPI endpoint with input validation
2. Add model versioning and A/B testing capability
3. Implement request logging and monitoring
4. Add Prometheus metrics (latency, throughput, error rate)
5. Create health check and readiness probes
6. Add request/response schema validation
7. Implement rate limiting"
```

**Example Implementation**:

```python
# Claude Code will create:
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, validator
import joblib
import numpy as np
import pandas as pd
from prometheus_client import Counter, Histogram, generate_latest
from fastapi.responses import Response
import time
import logging
from typing import List, Optional
import hashlib

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter(
    'model_requests_total',
    'Total model prediction requests',
    ['model_version', 'endpoint']
)
REQUEST_LATENCY = Histogram(
    'model_request_latency_seconds',
    'Model prediction latency',
    ['model_version']
)
PREDICTION_DISTRIBUTION = Counter(
    'model_predictions',
    'Distribution of predictions',
    ['model_version', 'prediction']
)

app = FastAPI(title="Fraud Detection API", version="1.0.0")

# Model versioning
MODELS = {
    'v1': joblib.load('models/fraud_detector_v1.pkl'),
    'v2': joblib.load('models/fraud_detector_v2.pkl')
}
DEFAULT_MODEL = 'v2'

# A/B testing configuration
AB_TEST_CONFIG = {
    'enabled': True,
    'traffic_split': {'v1': 0.2, 'v2': 0.8}
}

# Request/Response schemas
class PredictionRequest(BaseModel):
    transaction_amount: float
    merchant_id: str
    customer_age: int
    transaction_hour: int
    days_since_last_transaction: float
    model_version: Optional[str] = None

    @validator('transaction_amount')
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('transaction_amount must be positive')
        return v

    @validator('customer_age')
    def age_must_be_valid(cls, v):
        if not 18 <= v <= 120:
            raise ValueError('customer_age must be between 18 and 120')
        return v

class PredictionResponse(BaseModel):
    is_fraud: bool
    fraud_probability: float
    model_version: str
    request_id: str

# A/B testing logic
def select_model_version(request_id: str) -> str:
    if not AB_TEST_CONFIG['enabled']:
        return DEFAULT_MODEL

    # Deterministic assignment based on request_id
    hash_val = int(hashlib.md5(request_id.encode()).hexdigest(), 16)
    rand_val = (hash_val % 100) / 100.0

    cumulative = 0
    for version, split in AB_TEST_CONFIG['traffic_split'].items():
        cumulative += split
        if rand_val < cumulative:
            return version
    return DEFAULT_MODEL

# Rate limiting (simple in-memory)
from collections import defaultdict
from datetime import datetime, timedelta

request_counts = defaultdict(list)
RATE_LIMIT = 100  # requests per minute

def check_rate_limit(client_id: str) -> bool:
    now = datetime.now()
    minute_ago = now - timedelta(minutes=1)

    # Clean old requests
    request_counts[client_id] = [
        ts for ts in request_counts[client_id] if ts > minute_ago
    ]

    if len(request_counts[client_id]) >= RATE_LIMIT:
        return False

    request_counts[client_id].append(now)
    return True

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest, req: Request):
    start_time = time.time()

    # Generate request ID
    request_id = f"{int(time.time() * 1000)}_{hash(str(request.dict()))}"

    # Rate limiting
    client_id = req.client.host
    if not check_rate_limit(client_id):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    # Model selection
    model_version = request.model_version or select_model_version(request_id)

    if model_version not in MODELS:
        raise HTTPException(status_code=400, detail="Invalid model version")

    model = MODELS[model_version]

    # Prepare features
    features = pd.DataFrame([{
        'transaction_amount': request.transaction_amount,
        'merchant_id_encoded': hash(request.merchant_id) % 1000,
        'customer_age': request.customer_age,
        'transaction_hour': request.transaction_hour,
        'days_since_last_transaction': request.days_since_last_transaction
    }])

    # Predict
    try:
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        # Update metrics
        REQUEST_COUNT.labels(
            model_version=model_version,
            endpoint='/predict'
        ).inc()
        PREDICTION_DISTRIBUTION.labels(
            model_version=model_version,
            prediction='fraud' if prediction == 1 else 'legitimate'
        ).inc()

        # Log request
        logger.info(
            f"Prediction made - RequestID: {request_id}, "
            f"Model: {model_version}, Fraud: {bool(prediction)}, "
            f"Probability: {probability:.4f}"
        )

        response = PredictionResponse(
            is_fraud=bool(prediction),
            fraud_probability=float(probability),
            model_version=model_version,
            request_id=request_id
        )

        return response

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction failed")

    finally:
        # Record latency
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(model_version=model_version).observe(latency)

@app.get("/health")
async def health_check():
    """Liveness probe"""
    return {"status": "healthy"}

@app.get("/ready")
async def readiness_check():
    """Readiness probe - checks if models are loaded"""
    try:
        for version, model in MODELS.items():
            # Quick prediction test
            test_features = pd.DataFrame([{
                'transaction_amount': 100.0,
                'merchant_id_encoded': 1,
                'customer_age': 30,
                'transaction_hour': 12,
                'days_since_last_transaction': 5.0
            }])
            model.predict(test_features)
        return {"status": "ready", "models_loaded": list(MODELS.keys())}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Not ready: {str(e)}")

@app.get("/metrics")
async def metrics():
    """Prometheus metrics endpoint"""
    return Response(content=generate_latest(), media_type="text/plain")

# Run with: uvicorn fraud_api:app --host 0.0.0.0 --port 8000
```

**Kubernetes Deployment**:

```bash
claude "create Kubernetes deployment manifest with:
- 3 replicas for high availability
- Resource limits and requests
- Liveness and readiness probes
- Horizontal Pod Autoscaler
- Service and Ingress configuration"
```

**Best Practices**:
- Always validate input data
- Implement comprehensive logging
- Add monitoring and alerting
- Use model versioning for rollbacks
- Implement A/B testing for model comparison
- Add rate limiting to prevent abuse
- Use health checks for orchestration
- Monitor latency, throughput, and error rates

---

## Tips for Using Claude Code

1. **Be Specific**: Include file paths, library preferences, and exact requirements
2. **Iterate**: Start with basic implementation, then add advanced features
3. **Review Code**: Always review generated code for security and best practices
4. **Test**: Ask Claude to include tests and validation
5. **Documentation**: Request inline comments for complex logic

## Common Patterns

### Ask for complete workflows:
```bash
claude "create end-to-end pipeline from data loading to model deployment"
```

### Request best practices:
```bash
claude "add error handling, logging, and validation to this code"
```

### Iterate and improve:
```bash
claude "optimize this code for better performance"
claude "add type hints and docstrings"
claude "refactor this to be more maintainable"
```

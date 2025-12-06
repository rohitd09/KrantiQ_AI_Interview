# KrantiQ - AI Interview & Resume Processing System

A comprehensive Python project that demonstrates AI-driven interview scoring, resume processing with embeddings, and various utility modules for AI applications.

## Project Overview

This project contains several modules:

- **Section 1: Resume Embeddings** - Extract and store resume embeddings using FAISS vector database
- **Section 2: Face Detection** - Real-time face detection from webcam with tracking
- **Section 7: Utilities** - Rate limiting (Token Bucket) and text splitting modules
- **Answers.txt** - Comprehensive answers to interview questions about LLM-driven systems

## Prerequisites

- Python 3.8 or higher
- Pip package manager
- Virtual environment (recommended)
- Webcam (for face detection module)

## Installation

### Step 1: Clone or Extract the Repository

```bash
cd "c:\Users\rohit\OneDrive\Dropty\KrantiQ"
```

### Step 2: Create a Virtual Environment

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

All dependencies are listed in `requirements.txt`. Install them using:

```powershell
pip install -r requirements.txt
```

#### Key Dependencies

- **langchain** (1.1.2) & **langchain-community** (0.4.1) - LLM framework and utilities
- **faiss-cpu** (1.13.1) - Vector database for embeddings
- **fastembed** (0.7.4) - Fast embedding generation
- **opencv-python** (4.12.0.88) - Computer vision library for face detection
- **langchain-text-splitters** (1.0.0) - Text chunking utilities
- **python-dotenv** (1.2.1) - Environment variable management

### Step 4: Environment Configuration

Create a `.env` file in the Section 1 directory

```
# Example .env file
GOOGLE_API_KEY="[INSERT_GEMINI_API_KEY_HERE]"
```

## Module Documentation

### 1. Resume Embeddings (Section 1)

**File:** `Section 1/resume_embeddings.py`

**Purpose:** Generate embeddings for resumes and store them in a FAISS vector database for similarity search.

**Components:**
- `get_resume_embeddings()` - Loads CSV file, generates embeddings, stores in FAISS
- `get_relevant_resumes()` - Retrieves top 5 similar resumes based on query

**Data Files:**
- `Resume.csv` - Input CSV file containing resume data
- `faiss_index/index.faiss` - Persisted FAISS vector database

**Features:**
- Uses `FastEmbedEmbeddings` with BAAI/bge-small-en-v1.5 model (local embedding)
- Randomly samples 50 resumes for efficient processing
- Automatic FAISS index creation and persistence
- Returns top 5 similar resumes for any query

**Running the Module:**

```powershell
cd "Section 1"
python resume_embeddings.py
```

**Expected Output:**
```
----- Resume 0 -----
[Resume content]

----- Resume 1 -----
[Resume content]
...
```

---

### 2. Face Detection (Section 2)

**File:** `Section 2/face_detector.py`

**Purpose:** Real-time face detection using webcam with automatic tracking and missing face alerts.

**Components:**
- Haar Cascade classifier for face detection
- Real-time video stream processing
- Face tracking with timeout detection (3 seconds)

**Features:**
- Detects faces in real-time from webcam
- Draws green rectangles around detected faces
- Alerts when face is missing for more than 3 seconds
- Displays "FACE MISSING" warning in red
- Press 'q' to quit the application

**Running the Module:**

```powershell
cd "Section 2"
python face_detector.py
```

**Controls:**
- Press 'q' to exit the face detection window

**Output:**
- Live video feed with face detection rectangles
- Console output: "FACE MISSING" when face not detected for >3 seconds

---

### 3. Rate Limiter (Section 7)

**File:** `Section 7/rate_limiter.py`

**Purpose:** Implement Token Bucket algorithm for rate limiting API requests.

**Components:**
- `TokenBucketRateLimiter` class - Per-user rate limiting
- Configurable capacity (default: 20 tokens)
- Configurable refill rate (default: 20 requests/60 seconds)

**Features:**
- Thread-safe using locks
- Per-user token bucket tracking
- Automatic token refill over time
- Returns boolean indicating if request is allowed

**Parameters:**
- `capacity` (int) - Maximum tokens in bucket (default: 20)
- `refill_rate` (float) - Tokens added per second (default: 20/60 = ~0.33)

**Running the Module:**

```powershell
cd "Section 7"
python rate_limiter.py
```

**Example Usage:**

```python
from rate_limiter import TokenBucketRateLimiter

limiter = TokenBucketRateLimiter(capacity=20, refill_rate=20/60.0)

user_id = "user_123"
if limiter.allow_request(user_id):
    # Process request
    pass
else:
    # Rate limit exceeded
    pass
```

**Expected Output:**
```
Testing Token Bucket Rate Limiter (20 req/min limit)...
-------------------------------------------------------
Phase 1: Testing initial burst...
[  0.00s] Req  1: ALLOWED | Tokens: 19.00
[  0.50s] Req  2: ALLOWED | Tokens: 18.00
...
[  9.50s] Req 20: ALLOWED | Tokens:  0.00

    *** BURST LIMIT OF 20 REACHED ***

[ 10.00s] Req 21: BLOCKED | Tokens:  0.00
```

---

### 4. Text Splitter (Section 7)

**File:** `Section 7/text_splitter.py`

**Purpose:** Split text documents into overlapping chunks for LLM processing.

**Components:**
- `CharacterTextSplitter` - Splits text by character count
- Configurable chunk size and overlap
- Document loader for text files

**Configuration:**
- Chunk size: 400 characters
- Chunk overlap: 80 characters

**Data Files:**
- `sample_text.txt` - Input text file to split

**Features:**
- Splits documents into manageable chunks
- Maintains overlap between chunks for context preservation
- Counts total chunks created
- Alternative: RecursiveCharacterTextSplitter available for complex splitting

**Running the Module:**

```powershell
cd "Section 7"
python text_splitter.py
```

**Expected Output:**
```
Number of text chunks: X

--- Chunk 1 ---

[Chunk content with 400 characters and 80 character overlap with previous]

--- Chunk 2 ---

[Next chunk...]
```

---

## Complete Workflow Examples

### Example 1: Resume Processing Pipeline

```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Navigate to Section 1
cd "Section 1"

# Run the resume embedding script
python resume_embeddings.py
```

### Example 2: Real-time Face Detection

```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Navigate to Section 2
cd "Section 2"

# Run face detection
python face_detector.py

# Press 'q' to quit
```

### Example 3: Testing Rate Limiter

```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Navigate to Section 7
cd "Section 7"

# Run rate limiter
python rate_limiter.py
```

### Example 4: Text Processing

```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Navigate to Section 7
cd "Section 7"

# Run text splitter
python text_splitter.py
```

---

## Project Structure

```
KrantiQ/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── Answers.txt                        # Interview Q&A documentation
│
├── Section 1/
│   ├── resume_embeddings.py          # Resume embedding extraction
│   ├── Resume.csv                    # Resume data
│   └── faiss_index/
│       └── index.faiss               # Persisted FAISS index
│
├── Section 2/
│   └── face_detector.py              # Face detection module
│
├── Section 6/                         # (Empty/reserved)
│
└── Section 7/
    ├── rate_limiter.py               # Token bucket rate limiter
    ├── text_splitter.py              # Text chunking utility
    └── sample_text.txt               # Sample text for splitting
```

---

## Troubleshooting

### Virtual Environment Not Activating

```powershell
# If activation fails, try:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

### Module Not Found Errors

```powershell
# Ensure dependencies are installed:
pip install -r requirements.txt

# Verify installation:
pip list
```

### Face Detection Issues

- Ensure webcam is connected and accessible
- Check that opencv-python is correctly installed
- Try accessing camera in another application first to verify it works

### FAISS Index Issues

```powershell
# If FAISS index is corrupted, delete and regenerate:
cd "Section 1"
rmdir /s faiss_index
python resume_embeddings.py
```

---

## Performance Notes

- **Resume Embeddings**: Uses local FastEmbeddings (BAAI/bge-small-en-v1.5) model for fast processing
- **Face Detection**: Real-time processing at webcam FPS
- **Rate Limiter**: O(1) per-request complexity with thread-safe operations
- **Text Splitter**: Efficient chunk generation with configurable parameters

---

## Additional Resources

- **Answers.txt**: Contains detailed answers to LLM interview scoring system design questions
- Documentation covers:
  - Fair and unbiased interview scoring
  - Cheating detection methods
  - Resume embedding extraction techniques

---

## Running All Modules (Sequential)

```powershell
# Activate environment once
.\.venv\Scripts\Activate.ps1

# Run each module
echo "Running Resume Embeddings..."
cd "Section 1"; python resume_embeddings.py

echo "Running Text Splitter..."
cd ..\Section\ 7; python text_splitter.py

echo "Running Rate Limiter..."
python rate_limiter.py

# For face detection (interactive), run separately
echo "Starting Face Detection (press q to exit)..."
cd ..\Section\ 2; python face_detector.py
```

---

## Notes

- All modules are designed to be run independently
- Each section contains its own data files where needed
- Virtual environment should be activated before running any scripts
- The project uses CPU-based FAISS for compatibility across systems
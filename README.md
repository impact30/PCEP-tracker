# PCEP Study Tracker (Streamlit App)

This is a simple, minimal, multi-file Streamlit application that helps learners
prepare for the **PCEP (Certified Entry-Level Python Programmer)** exam.

It includes:

* Full 9-section PCEP checklist
* Auto-saving progress
* A text progress bar
* Timeline visualization
* JSON-based local storage
* Clean, readable code
* No database or backend required

---

## Features

* Track completion of all PCEP study items
* Save your progress locally
* See an interactive progress bar
* View your study window (start date → target exam date)
* Works completely offline
* Cross-platform: Windows, macOS, Linux

---

## How to Run

### 1. Install Python 3.8+

Make sure Python is installed:

```
python --version
```

### 2. Install required libraries

```
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```
streamlit run app.py
```

### 4. Progress Storage

Your progress is saved automatically in:

```
data/pcep_checklist.json
```

To reset progress, delete this file.

---

## Project Structure

```
pcep-tracker/
├── app.py
├── checklist.py
├── storage.py
├── utils.py
├── data/
│   └── pcep_checklist.json
├── README.md
└── requirements.txt
```

---

## Requirements

* Python 3.8+
* Streamlit

Install using:

```
pip install -r requirements.txt
```

---

## License

Free to use for any learner.

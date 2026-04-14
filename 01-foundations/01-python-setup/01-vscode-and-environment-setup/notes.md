# VS Code, Virtual Environment & First Python Execution

---

## 🧠 Overview

This lecture focuses on setting up a clean and scalable Python development environment using Visual Studio Code and virtual environments.

This setup forms the foundation for all future Machine Learning and AI projects.

---

## 🟢 Why Visual Studio Code?

Visual Studio Code (VS Code) is used as the primary IDE because:

- Supports `.py` (Python scripts)
- Supports `.ipynb` (Jupyter notebooks)
- Seamless virtual environment integration
- Rich ecosystem of extensions

👉 One tool for coding, experimentation, and documentation.

---

## 🔵 Virtual Environment (VERY IMPORTANT)

### 📌 What is a Virtual Environment?

A virtual environment is an isolated workspace where:

- A specific Python version is used
- Project-specific dependencies are installed

---

### 🎯 Why Use Virtual Environments?

- Avoid dependency conflicts between projects
- Manage different package versions easily
- Maintain clean and reproducible project setups

#### Example:

- Project A → TensorFlow 2.10  
- Project B → TensorFlow 2.15  

➡️ Both can coexist without conflict using separate environments.

---

## ⚙️ Creating Environment (Conda)

```bash
conda create -p venv python==3.12
```

### 🔍 Breakdown:

- `conda create` → Creates a new environment  
- `-p venv` → Specifies environment path/name  
- `python==3.12` → Installs specific Python version  

---

## ▶️ Activate Environment

```bash
conda activate venv
```

👉 All commands now run inside this isolated environment.

---

## 📦 What Happens Internally?

- Python interpreter is installed  
- Required system libraries are configured  
- Environment folder structure is created:
  - DLLs  
  - Libraries  
  - Scripts  

---

## 💻 Running a Python File

### Example: `app.py`

```python
print(1 + 1)
```

### Execution:

```bash
python app.py
```

### Output:

```
2
```

---

## 📁 Project Structure Approach

```
project/
│
├── python-setup/
│   ├── app.py
│   ├── test.ipynb
│   └── requirements.txt
```

👉 Organizing files properly improves clarity and scalability.

---

## 🟣 Jupyter Notebook in VS Code

### 📌 Features

- Code cells  
- Markdown cells  
- Interactive execution  

---

### ▶️ Run Cells

```
Shift + Enter
```

---

### 📌 Markdown Usage

Used for:

- Titles  
- Notes  
- Documentation  

#### Example:

```md
# Python Example
```

---

## ⚠️ Important Package: ipykernel

### ❗ Why is it needed?

- Enables Jupyter Notebook execution  
- Connects Python environment to VS Code notebooks  

---

### 📦 Install Command

```bash
pip install ipykernel
```

---

## 📄 requirements.txt

### 📌 Purpose

Stores all project dependencies

### Example:

```
ipykernel
numpy
pandas
```

---

### 🎯 Benefit

Install all dependencies at once:

```bash
pip install -r requirements.txt
```

---

## 🔁 Execution Difference

| File Type | Execution Method |
|----------|----------------|
| `.py`    | `python file.py` |
| `.ipynb` | `Shift + Enter` |

---

## ⚡ Quick Revision

- Use VS Code as primary IDE  
- Always create a virtual environment  
- Use `conda create` and `conda activate`  
- Install `ipykernel` for notebooks  
- Use `requirements.txt` for dependency management  
- `.py` → Terminal execution  
- `.ipynb` → Interactive execution  

---

## 🧭 Practical Task

- Create a virtual environment (Python 3.12)  
- Activate the environment  
- Create:
  - `app.py`
  - `test.ipynb`
  - `requirements.txt`
- Install:

```bash
pip install ipykernel
```

---

## 🔥 Real-World Insight

A clean environment setup ensures:

- Reproducibility of ML experiments  
- Smooth team collaboration  
- No dependency conflicts  

👉 This is the backbone of MLOps and production-grade systems

---

## ⚔️ Final Thought

This is not just setup.

This is:

🧱 The foundation of every AI system you will ever build  

If your base is clean → everything scales  
If your base is messy → everything breaks  

# Creating Virtual Environments – All Methods

---

## Overview

Virtual environments are essential for isolating dependencies across different projects.

Without them:
- Library conflicts occur
- Version mismatches break code
- Projects become unmanageable

Solution: Create a separate environment per project.

---

## Method 1: Using Python (venv)

### Create Environment

```bash
python -m venv myenv
```

Creates:

```
myenv/
```

### Activate (Windows)

```bash
myenv\Scripts\activate
```

### Install Packages

```bash
pip install numpy
pip install pandas
```

### Limitations

- Uses system Python version  
- Cannot easily switch Python versions  

### Use Case

- Small or simple projects  
- When Conda is not available  

---

## Method 2: Using virtualenv

### Install

```bash
pip install virtualenv
```

### Create Environment

```bash
virtualenv -p python3 myenv
```

### Activate

```bash
myenv\Scripts\activate
```

### Notes

- Slightly more flexible than venv  
- Still tied to system Python versions  

---

## Method 3: Using Conda (Recommended)

### Create Environment

```bash
conda create -p envs/python-core python=3.12
```

### Activate

```bash
conda activate envs/python-core
```

### Advantages

- Full control over Python versions  
- Better dependency resolution  
- Suitable for ML/DL workflows  

---

## Practical Insight

Even if your system has:

- Python 3.8  

You can create:

- Python 3.10 or 3.12  

Easily done using Conda.

---

## Comparison

| Method       | Python Version Control | Ease   | Recommendation |
|--------------|----------------------|--------|----------------|
| venv         | Limited           | Easy   | Basic use      |
| virtualenv   | Moderate          | Medium | Legacy         |
| Conda        | Full control      | Easy   | Best        |

---

## Key Insight

The core difference:

- venv → Uses system Python  
- conda → Creates independent Python environments  

---

## Quick Revision

- Always use separate environments per project  
- Three methods:
  - venv (basic)
  - virtualenv (older)
  - conda (recommended)
- Conda enables flexible Python versioning  

---

## 🧭 Recommendation

Use:

```bash
conda create -p envs/python-core python=3.12
```

Because:

- ML/DL projects require flexibility  
- Version control is critical  
- Industry workflows prefer reproducibility  

---

## 🔥 Real-World Insight

Environment management is the first step of MLOps.

Poor environment handling leads to:

- Broken pipelines  
- Deployment failures  
- Inconsistent results  

Clean environments = reliable systems  

---

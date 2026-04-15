# Fix: "conda is not recognized" Issue

---

## Problem

Error:

```bash
'conda' is not recognized as an internal or external command
```

Meaning:  
Conda is installed, but not added to the system PATH.

---

## Why This Happens

During Anaconda installation:

- "Add Anaconda to PATH" was not selected  
- OR PATH was not configured correctly  

---

## Solution 1: Temporary Fix (Quick)

Use:

Anaconda Prompt instead of CMD  

### Why it works:

- PATH is pre-configured internally  

---

## Solution 2: Permanent Fix (Recommended)

### Step 1: Locate Anaconda Path

Typical location:

```
C:\Users\yourname\anaconda3
```

---

### Step 2: Open Environment Variables

Search:

```
Edit System Environment Variables
```

→ Click **Environment Variables**

---

### Step 3: Edit PATH

Add:

```
C:\Users\yourname\anaconda3
C:\Users\yourname\anaconda3\Scripts
C:\Users\yourname\anaconda3\Library\bin
```

---

### Step 4: Restart Terminal

- Close CMD / PowerShell  
- Open again  

---

### Step 5: Verify

```bash
conda --version
```

👉 If version appears → ✅ Fixed  

---

## Alternative Fix (Advanced)

Run inside Anaconda Prompt:

```bash
conda init
```

Then restart terminal.

---

## Important Note

Conda officially does not recommend adding itself to PATH.

However:

For development and learning, it is practical and widely used.

---

## Quick Revision

- Error occurs when Conda is not in PATH  
- Temporary fix → Use Anaconda Prompt  
- Permanent fix → Add paths manually  
- Verify using `conda --version`  

---

## Real-World Insight

Environment issues are one of the most common problems in development.

Knowing how to debug setup issues:

- Saves hours of frustration  
- Makes you self-reliant  
- Prepares you for real-world systems  

Debugging setup = first step toward becoming an engineer  

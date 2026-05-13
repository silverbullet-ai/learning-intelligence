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

Check if Anaconda is installed at:

```
C:\Users\Aahish\anaconda3
```

> Replace `Aahish` with your actual system username.

---

### Step 2: Open Environment Variables

1. Press **Windows key**
2. Search:
   ```
   Edit the system environment variables
   ```
3. Click on it  
4. In the window that opens, click:
   **Environment Variables**

---

### Step 3: Edit PATH Variable

1. Under **User Variables** (top section):
   - Select **Path**
   - Click **Edit**

2. Click **New** and add these paths one by one:

```
C:\Users\Aahish\anaconda3
C:\Users\Aahish\anaconda3\Scripts
C:\Users\Aahish\anaconda3\Library\bin
```

> ⚠️ Important:
> - Do NOT delete existing entries  
> - Just add the above paths

---

### Step 4: Restart Terminal

- Close CMD / PowerShell / VS Code terminal  
- Open it again  

---

### Step 5: Verify

Run:

```bash
conda --version
```

👉 If it shows a version → ✅ **Issue Fixed**

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

---

## Resources

[Fix: "conda is not recognized as internal or external command"](https://stackoverflow.com/questions/44515769/conda-is-not-recognized-as-internal-or-external-command)

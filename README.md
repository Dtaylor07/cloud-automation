# AWS IAM Key Auto-Deactivation using GitHub Actions

## Overview
This repository contains an automated solution to **deactivate AWS IAM keys** that have been **active but unused for more than 2 hours**. 

It uses:
- **Python & AWS Boto3** to check the last usage time of IAM keys.
- **GitHub Actions** to run the script every 2 hours.
- **AWS IAM API** to deactivate unused IAM keys.

## How It Works
1. The workflow runs **every 2 hours**.
2. It **lists all active IAM keys** for the `deployment` user.
3. If a key has been **unused for more than 2 hours**, it **deactivates** the key.
4. The security team is **notified in GitHub logs**.

---

## **How This Works**
1. **The GitHub Action runs every 2 hours.**
2. **Python script (`check_iam_keys.py`) checks IAM keys** using `boto3`.
3. **If an IAM key is inactive for 2 hours, it is deactivated.**

---

## **Benefits**
✅ Fully **automated** key management  
✅ Reduces **security risks** from unused & active IAM keys  
✅ Uses **GitHub Actions & AWS SDK for automation**  
✅ Ensures **best security practices** in IAM usage  

---

This **ensures that IAM keys are not left active accidentally**, minimizing security risks! 🚀


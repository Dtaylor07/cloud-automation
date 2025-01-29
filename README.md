# AWS IAM Key Auto-Deactivation using GitHub Actions

## Overview
This repository contains an automated solution to **deactivate AWS IAM keys** that have been **active but unused for more than 2 minutes**. 

It uses:
- **Python & AWS Boto3** to check the last usage time of IAM keys.
- **GitHub Actions** to run the script every 2 minutes.
- **AWS IAM API** to deactivate unused IAM keys.

## How It Works
1. The workflow runs **every 2 minutes**.
2. It **lists all active IAM keys** for the `deployment` user.
3. If a key has been **unused for more than 2 minutes**, it **deactivates** the key.
4. The security team is **notified in GitHub logs**.

## Setup Instructions
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/iam-key-automation.git
cd iam-key-automation

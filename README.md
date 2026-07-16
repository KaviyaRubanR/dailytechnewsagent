# 📱 Daily Tech News Agent

An automated serverless application built using AWS that delivers daily technology news directly to your email every morning at 7:00 AM.

---

## 🚀 Project Overview

The Daily Tech News Agent is a cloud-based automation system that runs without any manual intervention. It uses AWS services to trigger a function daily, generate a summary of tech news, and send it via email.

This project demonstrates how to build a real-world serverless workflow using AWS.

---

## ⚙️ How It Works

⏰ 7:00 AM Daily  
↓  
Amazon EventBridge Scheduler  
↓  
AWS Lambda Function Executes  
↓  
Generates Tech News Summary  
↓  
Amazon SES Sends Email  
↓  
📧 Email Delivered to User  

---

## 🧰 AWS Services Used

- AWS Lambda → Runs the backend code  
- Amazon EventBridge Scheduler → Triggers the function daily  
- Amazon Simple Email Service (SES) → Sends email notifications  
- Amazon Bedrock (Optional) → AI-generated content  

---

## 📦 Features

- Fully automated (no manual execution required)  
- Serverless architecture  
- Daily scheduled email delivery  
- Beginner-friendly implementation  
- Easily extendable  

---

## 🛠️ Setup Instructions

### 1. Create AWS Account
https://aws.amazon.com/free

---

### 2. Create Lambda Function
- Runtime: Python 3.x  
- Paste code from lambda_function.py  
- Deploy  

---

### 3. Verify Email in SES
- Go to Amazon SES  
- Add and verify your email address  

---

### 4. Add Permissions
Attach this policy to Lambda:
AmazonSESFullAccess

---

### 5. Create Schedule
- Go to EventBridge Scheduler  
- Create a cron job:
cron(0 7 * * ? *)
- Set your timezone (example: Asia/Kolkata)  
- Target → Lambda function  

---

## 📧 Example Email Output

Subject: Daily Tech News  

Good Morning 🌞  

Here is your Daily Tech News:  

• AI tools are transforming everyday work  
• Cloud computing demand is rising  
• Cybersecurity awareness is increasing  
• New smartphones focus on AI features  
• Remote work tools are improving  

Have a great day 🚀  

---

## 📁 Project Structure

daily-tech-news-agent/  
│── lambda_function.py  
│── README.md  
│── requirements.txt  

---

## 🎯 Learning Outcomes

- Understanding serverless architecture  
- Working with AWS Lambda  
- Scheduling tasks using EventBridge  
- Sending emails using SES  
- Building automated cloud workflows  

---

## 🔮 Future Improvements

- Add AI-generated news using Amazon Bedrock  
- Add weather updates  
- Send WhatsApp/SMS notifications  
- Build a frontend dashboard  

---

## 👨‍💻 Author

Kaviyaruban  

---

## ⭐ Acknowledgment

This project was built as part of a hands-on AWS learning journey to understand automation and serverless computing.

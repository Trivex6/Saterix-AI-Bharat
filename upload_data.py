import streamlit as st
import boto3

# Securely fetch credentials from Streamlit Cloud
session = boto3.Session(
    aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
    region_name="ap-south-1" # Region for Kolkata/India
)

dynamodb = session.resource('dynamodb')
table = dynamodb.Table('SaterixThreatMatrix')

# The rest of your 80-item upload logic goes here...

# Data structure based on your 80-item matrix
categories = {
    "Digital Arrest": "Impersonates law enforcement and creates panic.",
    "Electricity": "Threatens service disruption to force immediate payment.",
    "KYC/Bank": "Pressures user to share sensitive bank data via fake urgency.",
    "Government Subsidy": "Misuses government scheme branding to harvest personal info."
}

messages = {
    "Digital Arrest": {
        "english": "Legal notice from Cyber Cell. Respond immediately to avoid arrest.",
        "hindi": "साइबर सेल से कानूनी नोटिस। गिरफ्तारी से बचने के लिए तुरंत जवाब दें।",
        "hinglish": "Cyber Cell ka legal notice hai, turant reply karo warna arrest.",
        "bengali": "সাইবার সেল থেকে আইনি নোটিস। সঙ্গে সঙ্গে উত্তর দিন।"
    },
    "Electricity": {
        "english": "Electricity service will be disconnected due to unpaid bill.",
        "hindi": "बकाया बिल के कारण बिजली सेवा बंद की जाएगी।",
        "hinglish": "Bill pending hai, electricity disconnect ho jayegi.",
        "bengali": "বকেয়া বিলের কারণে বিদ্যুৎ সংযোগ বিচ্ছিন্ন হবে।"
    },
    "KYC/Bank": {
        "english": "Bank account restricted due to incomplete KYC.",
        "hindi": "अधूरी केवाईसी के कारण बैंक खाता प्रतिबंधित।",
        "hinglish": "KYC incomplete hai, account restrict ho gaya.",
        "bengali": "অসম্পূর্ণ KYC-এর কারণে অ্যাকাউন্ট সীমাবদ্ধ।"
    },
    "Government Subsidy": {
        "english": "Government subsidy pending. Verify to receive funds.",
        "hindi": "सरकारी सब्सिडी लंबित है। राशि पाने के लिए सत्यापन करें।",
        "hinglish": "Government subsidy pending hai, verify karo.",
        "bengali": "সরকারি ভর্তুকি বাকি আছে। যাচাই করুন।"
    }
}

print("🚀 Starting bulk upload of 80 items...")

with table.batch_writer() as batch:
    for i in range(1, 81):
        # Determine category based on ID ranges
        if i <= 20: cat = "Digital Arrest"
        elif i <= 40: cat = "Electricity"
        elif i <= 60: cat = "KYC/Bank"
        else: cat = "Government Subsidy"

        batch.put_item(
            Item={
                'pattern_id': str(i),
                'category': cat,
                'messages': messages[cat],
                'technical_reason': categories[cat]
            }
        )

print("✅ Success! 80 items uploaded. Your 'Cognitive Firewall' is now active.")
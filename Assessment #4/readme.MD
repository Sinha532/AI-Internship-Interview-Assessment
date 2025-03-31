# AI Clinic Communication System

## Overview
The **AI Clinic Communication System** is a Python-based simulation designed to optimize patient communication and appointment confirmation using multiple channels (IVR, SMS, WhatsApp, etc.). The system personalizes messages based on patient preferences, conducts A/B testing to refine engagement strategies, and analyzes patient feedback to improve communication effectiveness.

## Features
- **Multi-Channel Messaging**: Supports IVR, SMS, and WhatsApp for appointment confirmations.
- **Personalized Communication**: Tailors messages based on language preference, age, and effectiveness score.
- **A/B Testing**: Evaluates different message styles and greetings to optimize patient engagement.
- **Survey & Feedback Analysis**: Collects and analyzes patient feedback on language clarity, message ease, and channel preference.
- **Performance Reporting**: Generates statistical insights on confirmation rates, channel effectiveness, and A/B test outcomes.

## Technology Stack
- **Python**: Core programming language.
- **JSON**: Data storage for reports.
- **Random Module**: Simulates patient responses.
- **Datetime Module**: Handles appointment scheduling.

## Installation & Execution
### Prerequisites
Ensure you have Python installed (>=3.7). If not, download and install it from [Python Official Website](https://www.python.org/).

### Steps to Run
1. Clone the repository or download the script.
2. Navigate to the script directory.
3. Run the script using:
   ```bash
   python skeletonCodeAssessment4.py
   ```
4. The system will generate a `report.json` file with performance metrics and survey results.

## How It Works
1. **Patient Data Handling**: The system loads predefined patient data, including language preference, communication channel, and effectiveness score.
2. **Message Formatting**: Customizes messages for each patient based on age and preferred language.
3. **Message Dispatch & Confirmation**: Sends messages using the most effective channel and logs confirmation status.
4. **Survey Collection & Analysis**: Conducts patient surveys on message clarity and ease of understanding.
5. **Performance Report Generation**: Aggregates results, including confirmation rates, A/B test outcomes, and patient preferences.

## Data Format
### Example Patient Data:
```json
{
    "id": 1,
    "name": "Ravi Kumar",
    "age": 69,
    "language": "Tamil",
    "preferred_channels": ["IVR", "SMS"],
    "effectiveness": 0.6,
    "preferred_slot": "morning"
}
```

### Sample Appointment Confirmation Message:
**Tamil (IVR)**: "உங்கள் பரிந்துரை நாள் உறுதிசெய்யப்பட்டது. தயவுசெய்து 15 நிமிடங்கள் முன்னதாக வருக!"

## Results & Performance Metrics
The script generates a report summarizing:
- **Overall Confirmation Rate**
- **Channel Effectiveness**
- **Language-based Performance**
- **Age Group Analysis**
- **Survey Insights**
- **A/B Test Results**

### Sample Report
```json
{
    "total_patients": 5,
    "confirmed_patients": 4,
    "channel_preferences": {"IVR": 2, "SMS": 1, "WhatsApp": 1},
    "ab_testing": {
        "group_A": {"total": 2, "confirmed": 1, "rate": 50.0},
        "group_B": {"total": 3, "confirmed": 3, "rate": 100.0}
    }
}
```

## Future Enhancements
- **Integration with Real Communication APIs** (Twilio, Firebase, WhatsApp Business API)
- **Advanced Natural Language Processing** for message customization
- **Predictive Analytics** to improve confirmation rates

## Author
Developed by **Lokesh Sinha N**

**Mail:** lokeshsinha746@gmail.com

**Contact:** 8985042381

**video explanation here :** https://drive.google.com/file/d/1WQDg9xbUQWjDFa6uHTwCegCun0S3BLIz/view?usp=sharing




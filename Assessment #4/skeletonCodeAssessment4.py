import random
import json
from datetime import datetime, timedelta

class AIClinicCommunicationSystem:
    def __init__(self):
        self.patients = [
            {
                "id": 1, "name": "Ravi Kumar", "age": 69,
                "language": "Tamil", "preferred_channels": ["IVR", "SMS"],
                "effectiveness": 0.6, "preferred_slot": "morning"
            },
            {
                "id": 2, "name": "Ananya Rao", "age": 35,
                "language": "Telugu", "preferred_channels": ["WhatsApp", "SMS"],
                "effectiveness": 0.9, "preferred_slot": "afternoon"
            },
            {
                "id": 3, "name": "Joseph Mathew", "age": 71,
                "language": "Malayalam", "preferred_channels": ["IVR"],
                "effectiveness": 0.7, "preferred_slot": "evening"
            },
            {
                "id": 4, "name": "Rahul Sharma", "age": 45,
                "language": "Hindi", "preferred_channels": ["SMS"],
                "effectiveness": 0.8, "preferred_slot": "morning"
            },
            {
                "id": 5, "name": "David Thomas", "age": 40,
                "language": "English", "preferred_channels": ["WhatsApp"],
                "effectiveness": 0.9, "preferred_slot": "afternoon"
            }
        ]

        self.time_slots = {
            "morning": "09:00 AM",
            "afternoon": "02:00 PM",
            "evening": "05:00 PM"
        }

        self.templates = {
            "appointment_confirmation": {
                "Tamil": {
                    "simple": "உங்கள் பரிந்துரை நாள் உறுதிசெய்யப்பட்டது. தயவுசெய்து 15 நிமிடங்கள் முன்னதாக வருக!",
                    "detailed": "உங்கள் மருத்துவ நாள்: {date}, நேரம்: {time}. தயவுசெய்து 15 நிமிடங்கள் முன்னதாக வரவும்."
                },
                "Telugu": {
                    "simple": "మీ అపాయింట్‌మెంట్ నిర్ధారించబడింది. దయచేసి 15 నిమిషాల ముందు వచ్చి ఉండండి!",
                    "detailed": "మీ మెడికల్ అపాయింట్‌మెంట్: తేదీ {date}, సమయం {time}. దయచేసి 15 నిమిషాల ముందు వస్తారు."
                },
                "Malayalam": {
                    "simple": "നിങ്ങളുടെ അപ്പോയിന്റ്മെന്റ് സ്ഥിരീകരിച്ചിരിക്കുന്നു. ദയവായി 15 മിനിറ്റ് മുമ്പായി വരിക!",
                    "detailed": "നിങ്ങളുടെ മെഡിക്കൽ അപ്പോയിന്റ്മെന്റ്: തീയതി {date}, സമയം {time}. ദയവായി 15 മിനിറ്റ് മുമ്പായി വരിക."
                },
                "Hindi": {
                    "simple": "आपका अपॉइंटमेंट कन्फर्म हो गया है। कृपया 15 मिनट पहले पहुंचें!",
                    "detailed": "आपकी चिकित्सा अपॉइंटमेंट: तारीख {date}, समय {time}. कृपया 15 मिनट पहले आएं।"
                },
                "English": {
                    "simple": "Appointment confirmed. Please arrive 15 minutes early!",
                    "detailed": "Your medical appointment is confirmed for {date} at {time}. Please arrive 15 minutes prior."
                }
            }
        }

        self.survey_data = {
            'questions': [
                {'id': 'language_clarity', 'type': 'rating'},
                {'id': 'message_ease', 'type': 'rating'},
                {'id': 'channel_preference', 'type': 'choice'}
            ],
            'responses': []
        }
        self.ab_variants = {
            "greeting": {
                "Tamil": "அன்பான {},",
                "Telugu": "ప్రియమైన {},",
                "Malayalam": "പ്രിയപ്പെട്ട {},",
                "Hindi": "प्यारा {},",
                "English": "Dear {},"
            }
        }

    def select_channel(self, patient):
        return "IVR" if patient["age"] > 65 else patient["preferred_channels"][0]

    def format_message(self, patient, channel, time_str):
        template = self.templates["appointment_confirmation"][patient["language"]]
        complexity = "simple" if patient["age"] > 65 else "detailed"
        
        message = template[complexity].format(
            date=datetime.now().strftime("%d-%m-%Y"),
            time=time_str
        )
        
        # A/B Testing variation
        if patient.get('ab_group') == 'B':
            greeting = self.ab_variants["greeting"][patient["language"]].format(patient["name"])
            message = f"{greeting} {message}"

        if channel == "IVR":
            return f"[{patient['language']} Voice-TTS]: 🔊 [LARGER-FONT] {message.split('.')[0]}"
        if patient["age"] > 65 and channel != "IVR":
            return f"🔊[LARGER-FONT] {message}"
        return message

    def send_message(self, patient, channel, time_str):
        message = self.format_message(patient, channel, time_str)
        confirmed = random.random() < patient["effectiveness"]

        print(f"📩 {patient['name']} ({patient['language']}) - {channel} Channel")
        print(f"   Message: {message}")
        print(f"   Confirmation Status: {'Confirmed' if confirmed else 'Not Confirmed'}\n")

        return confirmed

    def conduct_survey(self):
        for patient in self.patients:
            response = {
                'patient_id': patient['id'],
                'language': patient['language'],
                'ratings': {
                    'language_clarity': max(1, min(5, int(patient['effectiveness'] * 5)) + random.randint(-1, 1)),
                    'message_ease': max(1, min(5, int(patient['effectiveness'] * 5)) + random.randint(-1, 1))
                },
                'channel_preference': patient['preferred_channels'][0]
            }
            self.survey_data['responses'].append(response)

    def analyze_survey(self):
        analysis = {
            'language_clarity': {},
            'message_ease': {},
            'channel_preferences': {},
        }

        lang_ratings = {}
        for resp in self.survey_data['responses']:
            lang = resp['language']
            lang_ratings.setdefault(lang, {'clarity': [], 'ease': []})
            lang_ratings[lang]['clarity'].append(resp['ratings']['language_clarity'])
            lang_ratings[lang]['ease'].append(resp['ratings']['message_ease'])

        for lang, ratings in lang_ratings.items():
            analysis['language_clarity'][lang] = round(sum(ratings['clarity'])/len(ratings['clarity']), 1)
            analysis['message_ease'][lang] = round(sum(ratings['ease'])/len(ratings['ease']), 1)

        channel_counts = {}
        for resp in self.survey_data['responses']:
            channel = resp['channel_preference']
            channel_counts[channel] = channel_counts.get(channel, 0) + 1
        analysis['channel_preferences'] = channel_counts

        return analysis

    def generate_report(self, results):
        print(f"✅ Overall Confirmation Rate: {(sum(results['confirmed']))/len(results['confirmed'])*100:.2f}%")
        print("\n🔍 Performance Metrics:")
        print("Channel Performance:", results['channels'])
        print("Language Performance:", results['languages'])
        print("Age Group Performance:", results['age_groups'])

        self.conduct_survey()
        survey_results = self.analyze_survey()

        print("\n📊 Patient Satisfaction Survey Analysis:")
        print("Language Clarity Ratings:", survey_results['language_clarity'])
        print("Message Ease Ratings:", survey_results['message_ease'])
        print("Channel Preferences:", survey_results['channel_preferences'])

        results['satisfaction_survey'] = {
            'overall_language_clarity': survey_results['language_clarity'],
            'overall_message_ease': survey_results['message_ease'],
            'channel_preferences': survey_results['channel_preferences']
        }

        print("\n🔀 A/B Test Results:")
        a_total = results['ab_groups']['A']['total']
        b_total = results['ab_groups']['B']['total']
        a_confirmed = results['ab_groups']['A']['confirmed']
        b_confirmed = results['ab_groups']['B']['confirmed']

        a_rate = (a_confirmed / a_total) * 100 if a_total > 0 else 0.0
        b_rate = (b_confirmed / b_total) * 100 if b_total > 0 else 0.0
        
        print(f"Group A ({a_total} patients): {a_rate:.1f}% confirmation rate")
        print(f"Group B ({b_total} patients): {b_rate:.1f}% confirmation rate")

        results['ab_testing'] = {
            'group_A': {'total': a_total, 'confirmed': a_confirmed, 'rate': a_rate},
            'group_B': {'total': b_total, 'confirmed': b_confirmed, 'rate': b_rate}
        }

        results['total_patients'] = len(self.patients)
        results['confirmed_patients'] = sum(results['confirmed'])

        with open('report.json', 'w') as f:
            json.dump(results, f, indent=4)

        return results

    def run_simulation(self):
        results = {
            'confirmed': [],
            'channels': {},
            'languages': {},
            'age_groups': {'elderly': {'total': 0, 'confirmed': 0},
                          'adult': {'total': 0, 'confirmed': 0}},
            'ab_groups': {'A': {'total': 0, 'confirmed': 0},
                          'B': {'total': 0, 'confirmed': 0}}
        }

        slot_counts = {"morning": 0, "afternoon": 0, "evening": 0}

        for patient in self.patients:
            channel = self.select_channel(patient)
            preferred_slot = patient["preferred_slot"]
            
            # Calculate staggered appointment time
            base_time = datetime.strptime(self.time_slots[preferred_slot], "%I:%M %p")
            appointment_time = base_time + timedelta(minutes=30 * slot_counts[preferred_slot])
            time_str = appointment_time.strftime("%I:%M %p")
            slot_counts[preferred_slot] += 1

            # Assign A/B test group
            patient['ab_group'] = random.choice(['A', 'B'])
            
            # Send message once with A/B variation
            confirmed = self.send_message(patient, channel, time_str)

            # Track results
            results['confirmed'].append(confirmed)
            results['channels'][channel] = results['channels'].get(channel, 0) + confirmed
            results['languages'][patient['language']] = results['languages'].get(patient['language'], 0) + confirmed

            age_group = 'elderly' if patient['age'] > 65 else 'adult'
            results['age_groups'][age_group]['total'] += 1
            if confirmed:
                results['age_groups'][age_group]['confirmed'] += 1

            # Track A/B test results
            results['ab_groups'][patient['ab_group']]['total'] += 1
            if confirmed:
                results['ab_groups'][patient['ab_group']]['confirmed'] += 1

        return self.generate_report(results)

# Execute the system
if __name__ == "__main__":
    system = AIClinicCommunicationSystem()
    results = system.run_simulation()
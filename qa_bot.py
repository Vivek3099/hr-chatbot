import difflib

# Absolute path to your HR policy file
file_path = r"D:\NLP\hr_policy_chatbot PDF TEXT BASED\data\HR_policy.txt"

# Load the text file content
with open(file_path, "r", encoding="utf-8") as f:
    policy_text = f.read()

# Parse into a dictionary (each section should be separated by 1 blank line)
hr_policy = {}
sections = policy_text.split("\n\n")
for section in sections:
    lines = section.strip().split("\n")
    if lines:
        key = lines[0].strip().lower()   # First line is the key
        value = "\n".join(lines[1:]).strip()  # Rest is the value
        hr_policy[key] = value

# Define the Q&A function
def ask_question(query):
    query_lower = query.lower()
    keys = hr_policy.keys()

    best_match = difflib.get_close_matches(query_lower, keys, n=1, cutoff=0.4)

    if best_match:
        return hr_policy[best_match[0]]
    else:
        return "❌ Sorry, I couldn’t find a relevant HR policy section."

"""
"Resume & Cover Letter Customizer – Smart Text Personalization Engine"

🧠 **Project Idea:
Build a smart CLI-based tool that takes a master resume and cover letter 
template as input and auto-customizes them** for different job roles, companies, 
and formats. This project simulates a real-world content personalization tool 
used in job applications and marketing.

"""

import os
from datetime import datetime

def load_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def save_output(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def format_content(template, replacements):
    for key, value in replacements.items():
        template = template.replace(f"<|{key}|>", value)
    return template

def clean_text(text):
    return " ".join(text.split())

def smart_case(text):
    return text.strip().capitalize()

def user_inputs():
    name = input("Enter your name: ").strip()
    role = input("Enter role you’re applying for: ").strip()
    skills = input("Enter key skills (comma-separated): ").strip()
    company = input("Enter company name: ").strip()
    today = datetime.today().strftime("%B %d, %Y")

    return {
        "Name": smart_case(name),
        "Role": smart_case(role),
        "Skills": skills.lower(),
        "Company": smart_case(company),
        "Date": today
    }

def main():
    print("\n📝 Resume & Cover Letter Customizer\n")

    base_path = "templates"
    output_path = "output"
    os.makedirs(output_path, exist_ok=True)

    resume_template = load_template(os.path.join(base_path, "resume_template.txt"))
    cover_letter_template = load_template(os.path.join(base_path, "cover_letter_template.txt"))

    inputs = user_inputs()

    customized_resume = format_content(resume_template, inputs)
    customized_letter = format_content(cover_letter_template, inputs)

    # Clean and format
    customized_resume = clean_text(customized_resume)
    customized_letter = clean_text(customized_letter)

    # Save outputs
    save_output(customized_resume, os.path.join(output_path, "resume_final.txt"))
    save_output(customized_letter, os.path.join(output_path, "cover_letter_final.txt"))

    print("\n✅ Customized documents generated in the 'output/' folder!")

if __name__ == "__main__":
    main()

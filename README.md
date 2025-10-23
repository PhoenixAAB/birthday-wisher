# 🎉 Birthday Wisher

A Python script that automatically sends personalized birthday emails using data from a CSV file.  
Originally inspired by a **100 Days of Python challenge project**, but adapted as an independent tool.

---

## 📂 Project Structure

Birthday-Wisher/
│
├── main.py # Main script to run
├── birthdays.csv # CSV file containing birthdays
├── .env # Environment variables (email & app password) - NOT uploaded to GitHub
├── .gitignore
└── letter_templates/ # Folder containing birthday letter templates
├── letter_1.txt
├── letter_2.txt
└── letter_3.txt


---

## 📝 CSV Format

The `birthdays.csv` file should contain the following columns:

| name | email             | year | month | day |
|------|-----------------|------|-------|-----|
| Ali  | ali@example.com   | 1995 | 10    | 23  |
| Sara | sara@example.com  | 1992 | 10    | 23  |

> Month and day are used to check if today matches a birthday.

---

## ✏️ Letter Templates

- Place your `.txt` templates in the `letter_templates` folder.
- Use `[NAME]` as a placeholder for the recipient’s name.  
Example template:

Happy Birthday [NAME]!

Wishing you a fantastic day filled with joy and surprises.


---

## 🔐 Environment Variables

To keep your email credentials safe, store them in a `.env` file (do **not** commit it to GitHub).

Example `.env`:

MY_EMAIL=youremail@gmail.com

MY_PASSWORD=your_app_password


**Important:** Use a **Gmail App Password** instead of your main Gmail password.

---

## 🚀 How to Run

1. Install dependencies:

`bash
pip install pandas python-dotenv

2. Ensure your .env file is set up correctly.

3. Run the script:

python main.py


The script will check if today matches any birthdays in birthdays.csv.

If yes, it will pick a random template from letter_templates/ and send a personalized email.

⚡ Tips

Use emojis in templates or subject lines for a fun touch.

You can add more templates in letter_templates/ — the script will choose randomly.

Make sure the birthdays.csv is up-to-date.

📌 Notes

The script only sends emails to recipients whose birthday matches today.

Sending multiple emails at once (for multiple birthdays on the same day) can be added easily.

Keep your .env file secure to protect your credentials.


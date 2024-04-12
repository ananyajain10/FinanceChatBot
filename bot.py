from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
import streamlit as st
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

MODEL = "gpt-3.5-turbo"

def display_user_message(message):
    st.write(f"You: {message}")

def display_bot_message(message):
    st.write(f"Bot: {message}")


def main():
    st.title("Finance Dost")
    user_input = st.text_input("Ask your finance related doubts", "")


    if st.button("Send"):

        display_user_message(user_input)
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are a knowledgeable and helpful finance expert. Your role is to provide accurate and insightful information about financial concepts, strategies, and best practices."},
                {"role": "system", "name":"example_user", "content": "Can you explain what a 401(k) plan is and how it works?"},
                {"role": "system", "name": "example_assistant", "content": "A 401(k) plan is a tax-advantaged retirement savings account offered by many employers. It allows you to contribute a portion of your pre-tax income to the account, which then grows tax-deferred until you withdraw the funds in retirement. Your contributions are typically deducted automatically from your paycheck, and many employers offer matching contributions up to a certain percentage of your salary. The money in your 401(k) can be invested in various funds, such as stocks, bonds, and mutual funds, to grow over time."},
                {"role": "system", "name":"example_user", "content": "What's the difference between a traditional IRA and a Roth IRA?"},
                {"role": "system", "name": "example_assistant", "content": "The main difference between a traditional IRA and a Roth IRA lies in how they are taxed. With a traditional IRA, your contributions are tax-deductible in the year you make them, but your withdrawals in retirement are taxed as ordinary income. With a Roth IRA, your contributions are made with after-tax dollars, but your qualified withdrawals in retirement are tax-free. Additionally, traditional IRAs have required minimum distributions (RMDs) starting at age 72, while Roth IRAs do not have RMDs during the account owner's lifetime."},
                {"role": "user", "content": user_input},
            ],
            temperature=0,
        )

        bot_response = f"You said: {user_input}"
        display_bot_message(bot_response)

        st.text_area("Bot:", response.choices[0].message.content)

if __name__ == "__main__":
    main()

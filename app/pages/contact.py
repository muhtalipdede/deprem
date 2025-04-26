from flask import render_template

def contact_page():
    return render_template("contact.html")

def contact_success_page(name, email, message):
    print(f"Name: {name}, Email: {email}, Message: {message}")
    return render_template("contact_success.html")
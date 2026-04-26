import smtplib

my_email = "my-email@gmail.com"
my_password = "my-app-password"
with connection = smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="recipient@gmail.com",
        msg="Subject:Hello\n\nThist is the body of the email."
    )
# connection.close() needed if not used "with connection..." block

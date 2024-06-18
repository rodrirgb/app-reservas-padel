import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st


def enviar(email, nombre, fecha, hora, pista):

    ##credenciales
    user = st.secrets["emails"]["smtp_user"]
    password = st.secrets["emails"]["smtp_password"]
    # Configuracion del servidor
    msg = MIMEMultipart()

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "Club de pádel Sevilla"

    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Reserva pista"

    message = f"""
    Hola {nombre},
    Su reserva ha sido realizada con éxito.
    Fecha: {fecha}
    Hora: {hora}
    Pista: {pista}

    Gracias por confiar en nosotros.
    Un saludo
    """

    msg.attach(MIMEText(message, 'plain'))

    #Conexion al servidor
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(user, password)
    server.sendmail(sender_email, email, msg.as_string())
    server.quit()
  


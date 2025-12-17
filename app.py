from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

EMAIL_RECEPTOR = "photoclases4@gmail.com"
EMAIL_EMISOR = "nikole.margarita.carrasquel@gmail.com"
PASSWORD = "fops epin ecef nyfp"

@app.route("/enviar" , methods=["POST"])

def enviar_correo():
    data = request.json

    msg = EmailMessage()
    msg["Subject"] = "Nuevo mensaje desde la wed"
    msg["From"] = EMAIL_EMISOR
    msg["To"] = EMAIL_RECEPTOR
    msg.set_content(f""" 
        Nombre: {data['nombre']}
        Correo: {data['correo']}
        Mensaje: {data['mensaje']}
""")
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_EMISOR, PASSWORD)
            smtp.send_message(msg)

        return jsonify({"mensaje": "Correo enviado correctamente ✅"})
    except Exception as e:
        print(e)
        return jsonify({"mensaje": "Error al enviar el correo ❌"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

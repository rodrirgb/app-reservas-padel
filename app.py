import streamlit as st
from streamlit_option_menu import option_menu
from enviaremail import enviar
from google_sheets import GoogleSheets
import re
import uuid  # Asegúrate de importar uuid
from google_calendar import GoogleCalendar
import numpy as np
import datetime
## Variables
page_title = "Club de padel"
page_icon = "🎾"
layout = "centered"
horas = ["9:00", "10:30", "12:00", "13:30", "15:00", "16:30", "18:00", "19:30", "21:00"]
pistas = ["Pista 1", "Pista 2"]
document = "gestion-club-padel"
sheet = "reservas"
credentials = st.secrets["sheets"]["credentials_sheet"]
idcalendar = "rodridev10@gmail.com"
idcalendar2 = "a243ffbb98aa7c1dce3e534c89220b355a209217ebc5e164c26f486c64933e03@group.calendar.google.com"
time_zone = 'Europe/Madrid'
## Funciones

def add_hour_half(time):
    parsed_time = datetime.datetime.strptime(time, "%H:%M").time() 
    new_time = (datetime.datetime.combine(datetime.date.today(), parsed_time) + datetime.timedelta(hours=1, minutes=30)).time()
    return new_time.strftime("%H:%M")

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

def generate_uid():
    return str(uuid.uuid4())

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

st.image("assets/padel.jpg")
st.title("Club de padel")
st.text("Calle San Francisco Javier, nº4")

selected = option_menu(
    menu_title=None,
    options=["Reservar", "Pistas", "Detalles", "Sobre nosotros"],
    icons=["calendar-date", "building-add", "clipboard-minus", "book"],
    orientation="horizontal"
)



if selected == "Detalles":

    st.subheader("Ubicación")
    st.markdown(
        """<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d6340.840295443493!2d-5.976691922636908!3d37.37989507208741!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd126ea2f6be790d%3A0x5efb1cd3f8d7cde!2sAv.%20San%20Francisco%20Javier%2C%20Sevilla!5e0!3m2!1ses!2ses!4v1716224344705!5m2!1ses!2ses" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>""",
        unsafe_allow_html=True
    )
    
    st.subheader("Horarios")
    st.write(
        """
        | Día        | Horario       |
        |------------|---------------|
        | Lunes      | 9:00 - 21:00 |
        | Martes     | 9:00 - 21:00 |
        | Miércoles  | 9:00 - 21:00 |
        | Jueves     | 9:00 - 21:00 |
        | Viernes    | 9:00 - 21:00 |
        | Sábado     | 9:00 - 21:00 |
        | Domingo    | 9:00 - 21:00 |
        """
    )

    st.subheader("Contacto")
    st.text("📞 661542442")
    st.subheader("Instagram")
    st.markdown("Síguenos [aquí](https://www.instagram.com/padelclub_/)")
    
if selected == "Sobre nosotros":
    st.subheader("Nuestra historia")
    st.write(
        """
        En el año **2014**, en un tranquilo barrio de la ciudad,
        cuatro amigos apasionados por el pádel decidieron dar vida a su sueño compartido. 
        **Juan García**, **María López**, **Carlos Martínez** y **Elena Fernández**
        se reunieron con la determinación de crear un espacio donde la comunidad
        pudiera disfrutar del pádel en un ambiente acogedor y amigable.
        El impulso detrás de la creación del club fue la falta de instalaciones adecuadas para el pádel en la zona. 
        Con visión y entusiasmo, el grupo de amigos trabajó arduamente para convertir su visión en realidad. 
        Después de meses de planificación y preparación, el **15 de septiembre de 2014**, el Club Padelero abrió oficialmente sus puertas.
        Desde entonces, el club ha crecido y prosperado, atrayendo a jugadores de todas las edades y niveles de habilidad.
        """
    )
    st.subheader("Nuestra Misión")
    st.write(
        """
        En el Club Padelero, nuestra misión es fomentar la pasión por el pádel, promover un estilo de vida saludable y 
        crear una comunidad unida por el deporte. Nos esforzamos por ofrecer instalaciones 
        de primera clase y un ambiente inclusivo donde jugadores de todas las edades y niveles
        puedan mejorar sus habilidades y disfrutar del juego.
        """
    ) 
    st.subheader("Nuestras instalaciones")
    st.write(
        """
        Contamos con modernas instalaciones diseñadas para ofrecer la mejor experiencia a nuestros miembros:
        - **Canchas de pádel**: Cuatro pistas de última generación con iluminación LED.
        - **Zona de Relax**: Área de descanso y cafetería para relajarse después de los partidos.
        - **Vestuarios**: Espacios amplios y limpios con duchas y taquillas.
        """
    ) 
    st.subheader("Nuestro equipo")
    st.write(
        """
        Nuestro equipo está formado por profesionales apasionados y dedicados al deporte del pádel:
        - **Juan García**: Fundador y entrenador principal, con más de 15 años de experiencia en el pádel.
        - **María López**: Co-fundadora y coordinadora de eventos, conocida por su entusiasmo y habilidades organizativas.
        - **Carlos Martínez**: Entrenador y preparador físico, especializado en mejorar el rendimiento de nuestros jugadores.
        - **Elena Fernández**: Administradora del club, encargada de la gestión diaria y atención a los miembros.
        """
    )
    
    desired_width = 160
    
    Juan, María, Carlos, Elena = st.columns(4)
    with Juan:
        st.text("")
        st.image("assets/JuanGarcía.jpg", width=desired_width)
        st.text("Juan García")
    with María:
        st.text("")
        st.image("assets/Maria_Lopez.jpg", width=desired_width)
        st.text("María Lopez")    
    with Carlos:
        st.text("")
        st.image("assets/CarlosMartinez.png", width=desired_width)
        st.text("Carlos Martinez")
    with Elena:
        st.text("")
        st.image("assets/Elena Fernandez.jpeg", width=desired_width)
        st.text("Elena Fernandez") 

if selected == "Pistas":
    st.subheader("Nuestras pistas")
    st.image("assets/Pistasdescubiertas.jpg", caption="Estas son nuestras pistas descubiertas")
    st.write("**-Pista 1**")
    st.write("**-Pista 2**")

if selected == "Reservar":
    st.subheader("Reservar")

    c1, c2 = st.columns(2) 

    nombre = c1.text_input("Tu nombre*")
    email = c2.text_input("Tu email*")
    fecha = c1.date_input("Fecha")
    pista = c1.selectbox("Pistas", pistas)
    if fecha:
        if pista == "Pista 1":      
            id = idcalendar
        elif pista == "Pista 2":
            id = idcalendar2  
        calendar = GoogleCalendar(credentials,id)
        hours_blocked = calendar.get_events_start_time(str(fecha))
        results_hours = np.setdiff1d(horas, hours_blocked)
    hora = c2.selectbox("Hora", results_hours)  
    notas = c2.text_area("Notas")

    enviar_reserva = st.button("Reservar")

    ## BACKEND

    if enviar_reserva:
        
        with st.spinner("Cargando..."):

            if nombre == "":
                st.warning("El nombre es obligatorio")
            elif email == "":
                st.warning("El email es obligatorio")    
            elif not validate_email(email):
                st.warning("El email no es válido")
            else:
                #Crar evento en google calendar
                parsed_time = datetime.datetime.strptime(hora, "%H:%M").time()
                hours1 = parsed_time.hour
                minutes1 = parsed_time.minute
                end_hours = add_hour_half(hora)
                parsed_time2 = datetime.datetime.strptime(end_hours, "%H:%M").time()
                hours2 = parsed_time2.hour
                minutes2 = parsed_time2.minute
                start_time = datetime.datetime(fecha.year,fecha.month,fecha.day, hours1+2, minutes1).astimezone(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
                end_time = datetime.datetime(fecha.year,fecha.month,fecha.day, hours2+2, minutes2).astimezone(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
                calendar = GoogleCalendar(credentials,id)
                calendar.create_event(nombre,start_time,end_time,time_zone)
                #Crear hoja de calculo
                uid = generate_uid()  # Llamar a la función para generar el UID
                data = [[nombre, email, pista, str(fecha), hora, notas, uid]]

                # Verifica que no haya funciones en data
                for item in data[0]:
                    if callable(item):
                        st.error(f"El valor {item} es una función y no puede ser serializado a JSON")
                        raise TypeError(f"El valor {item} es una función y no puede ser serializado a JSON")

                gs = GoogleSheets(credentials, document, sheet)
                range_ = gs.get_last_row_range()
                gs.write_data(range_, data)
                enviar(email, nombre, fecha, hora, pista)
            
                st.success("Su pista ha sido reservada")

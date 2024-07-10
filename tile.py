import mysql.connector
from mysql.connector import Error
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Función para conectar a la base de datos MySQL
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='imm_db_dev',
            user='root',
            password='sAntamonicab78@'
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)

# Función para generar un reporte de citas completadas en formato PDF
def generate_completed_appointments_report_pdf():
    try:
        conn = connect_to_mysql()
        if conn:
            cursor = conn.cursor(dictionary=True)

            # Consulta SQL para obtener los datos desde la vista CompletedAppointments
            query = """
                SELECT * FROM CompletedAppointments;
            """
            cursor.execute(query)
            appointments = cursor.fetchall()

            # Crear un documento PDF
            pdf_filename = "completed_appointments_report.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            # Crear una lista para contener los datos de las citas completadas
            data = [["Appointment Date", "Appointment Hour", "Doctor", "Patient", "Document Number", "Comment"]]

            # Iterar sobre los resultados y agregar filas a la lista de datos
            for appointment in appointments:
                data.append([
                    appointment['appointmentDate'],
                    appointment['appointmentHour'],
                    f"{appointment['doctorName']} {appointment['doctorLastName']}",
                    f"{appointment['patientName']} {appointment['patientLastName']}",
                    appointment['patientDocument'],
                    appointment['comment']
                ])

            # Crear una tabla para los datos en el PDF
            table = Table(data)
            style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])

            table.setStyle(style)

            # Crear el documento PDF con la tabla
            elements = [table]
            doc.build(elements)

            print(f"PDF report '{pdf_filename}' generated successfully.")

            cursor.close()
            conn.close()

    except Error as e:
        print(e)

# Llamar a la función para generar el reporte de citas completadas en PDF
generate_completed_appointments_report_pdf()

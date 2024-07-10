import mysql.connector
from mysql.connector import Error
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='imm_db_dev',
            user='',
            password=''
        )
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)

def generate_appointment_detail_report_pdf():
    try:
        conn = connect_to_mysql()
        if conn:
            cursor = conn.cursor(dictionary=True)

            # Consulta SQL para obtener todas las citas con información completa
            query = """
                SELECT * FROM AppointmentDetails;
            """
            cursor.execute(query)
            appointments = cursor.fetchall()

            # Crear un documento PDF en orientación horizontal
            pdf_filename = "appointment_report_horizontal.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=landscape(letter))

            # Crear una lista para contener los datos de las citas
            data = [["Appointment ID", "Date", "Time", "Status", "Procedure Type", "Comment", "Doctor", "Patient"]]

            # Iterar sobre los resultados y agregar filas a la lista de datos
            for appointment in appointments:
                data.append([
                    appointment['appointmentId'],
                    appointment['appointmentDate'],
                    appointment['appointmentHour'],
                    appointment['status'],
                    appointment['procedureType'],
                    appointment['comment'],
                    f"{appointment['doctorName']} {appointment['doctorLastName']}",
                    f"{appointment['patientName']} {appointment['patientLastName']} (DNI: {appointment['patientDocument']})"
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

            # Ajustar ancho de columna para que se ajuste horizontalmente
            table._argW[0] = 1.5 * inch  # Ajusta el ancho de la primera columna

            # Crear el documento PDF con la tabla
            elements = [table]
            doc.build(elements)

            print(f"PDF report '{pdf_filename}' generated successfully.")

            cursor.close()
            conn.close()

    except Error as e:
        print(e)

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

def generate_pending_appointments_report_pdf():
    try:
        conn = connect_to_mysql()
        if conn:
            cursor = conn.cursor(dictionary=True)

            # Consulta SQL para obtener los datos desde la vista PendingAppointments
            query = """
                SELECT * FROM PendingAppointments;
            """
            cursor.execute(query)
            appointments = cursor.fetchall()

            # Crear un documento PDF
            pdf_filename = "pending_appointments_report.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            # Crear una lista para contener los datos de las citas pendientes
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

def generate_in_progress_appointments_report_pdf():
    try:
        conn = connect_to_mysql()
        if conn:
            cursor = conn.cursor(dictionary=True)

            # Consulta SQL para obtener los datos desde la vista InProgressAppointments
            query = """
                SELECT * FROM InProgressAppointments;
            """
            cursor.execute(query)
            appointments = cursor.fetchall()

            # Crear un documento PDF
            pdf_filename = "in_progress_appointments_report.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            # Crear una lista para contener los datos de las citas en progreso
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

def generate_colposcopy_exams_on_date_report_pdf():
    try:
        conn = connect_to_mysql()
        if conn:
            cursor = conn.cursor(dictionary=True)

            # Consulta SQL para obtener los datos desde la vista ColposcopyExamsOnDate
            query = """
                SELECT * FROM ColposcopyExamsOnDate;
            """
            cursor.execute(query)
            exams = cursor.fetchall()

            # Crear un documento PDF
            pdf_filename = "colposcopy_exams_report.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            # Crear una lista para contener los datos de los exámenes de colposcopía
            data = [["Exam Date", "Exam Hour", "Doctor", "Patient", "Document Number", "Indications", "Vulva", "Vagina", "Perineo", "Tincion", "Union Escamocolumnar", "Zona Transformacion", "Otros Hallazgos", "Exam Adecuado", "Diagnostico Vulva", "Diagnostico Cervix", "Diagnostico Vagina"]]

            # Iterar sobre los resultados y agregar filas a la lista de datos
            for exam in exams:
                data.append([
                    exam['appointmentDate'],
                    exam['appointmentHour'],
                    f"{exam['doctorName']} {exam['doctorLastName']}",
                    f"{exam['patientName']} {exam['patientLastName']}",
                    exam['patientDocumentNumber'],
                    exam['colposcopyIndications'],
                    exam['colposcopyVulva'],
                    exam['colposcopyVagina'],
                    exam['colposcopyPerineo'],
                    exam['colposcopyTincion'],
                    exam['colposcopyUnionEscamocolumnar'],
                    exam['colposcopyZonaTransformacion'],
                    exam['colposcopyOtrosHallazgos'],
                    exam['colposcopyExamAdecuado'],
                    exam['colposcopyDiagnosticoVulva'],
                    exam['colposcopyDiagnosticoCervix'],
                    exam['colposcopyDiagnosticoVagina']
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
        
def generate_doctor_info_report_pdf():
    try:
        conn = connect_to_mysql()
        if conn:
            cursor = conn.cursor(dictionary=True)

            # Consulta SQL para obtener los datos desde la vista DoctorInfo
            query = """
                SELECT * FROM DoctorInfo;
            """
            cursor.execute(query)
            doctors = cursor.fetchall()

            # Crear un documento PDF
            pdf_filename = "doctor_info_report.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            # Crear una lista para contener los datos de los doctores
            data = [["ID", "Name", "Last Name"]]

            # Iterar sobre los resultados y agregar filas a la lista de datos
            for doctor in doctors:
                data.append([
                    doctor['id'],
                    doctor['name'],
                    doctor['lastName']
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

def generate_patient_info_report_pdf():
    try:
        conn = connect_to_mysql()
        if conn:
            cursor = conn.cursor(dictionary=True)

            # Consulta SQL para obtener los datos desde la vista PatientInfo
            query = """
                SELECT * FROM PatientInfo;
            """
            cursor.execute(query)
            patients = cursor.fetchall()

            # Crear un documento PDF
            pdf_filename = "patient_info_report.pdf"
            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            # Crear una lista para contener los datos de los pacientes
            data = [["ID", "Name", "Last Name", "Birth Date", "Document Type", "Document Number"]]

            # Iterar sobre los resultados y agregar filas a la lista de datos
            for patient in patients:
                data.append([
                    patient['id'],
                    patient['name'],
                    patient['lastName'],
                    patient['birthDate'].strftime('%Y-%m-%d'),  # Formato de fecha deseado
                    patient['documentType'],
                    patient['documentNumber']
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

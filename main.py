from flask import Flask, send_file, jsonify
from reports import (
    generate_appointment_detail_report_pdf,
    generate_completed_appointments_report_pdf,
    generate_colposcopy_exams_on_date_report_pdf,
    generate_in_progress_appointments_report_pdf,
    generate_pending_appointments_report_pdf,
    generate_doctor_info_report_pdf,
    generate_patient_info_report_pdf
)

app = Flask(__name__)

# Function to generate reports
def generate_reports():
    generate_appointment_detail_report_pdf()
    generate_completed_appointments_report_pdf()
    generate_colposcopy_exams_on_date_report_pdf()
    generate_in_progress_appointments_report_pdf()
    generate_pending_appointments_report_pdf()
    generate_doctor_info_report_pdf()
    generate_patient_info_report_pdf()

# Route to generate and download Appointment Detail Report
@app.route('/api/reports/appointment-detail', methods=['GET'])
def get_appointment_detail_report():
    generate_appointment_detail_report_pdf()
    return send_file('appointment_detail_report.pdf', as_attachment=True)

# Route to generate and download Completed Appointments Report
@app.route('/api/reports/completed-appointments', methods=['GET'])
def get_completed_appointments_report():
    generate_completed_appointments_report_pdf()
    return send_file('completed_appointments_report.pdf', as_attachment=True)

# Route to generate and download Colposcopy Exams on Date Report
@app.route('/api/reports/colposcopy-exams-on-date', methods=['GET'])
def get_colposcopy_exams_on_date_report():
    generate_colposcopy_exams_on_date_report_pdf()
    return send_file('colposcopy_exams_on_date_report.pdf', as_attachment=True)

# Route to generate and download In Progress Appointments Report
@app.route('/api/reports/in-progress-appointments', methods=['GET'])
def get_in_progress_appointments_report():
    generate_in_progress_appointments_report_pdf()
    return send_file('in_progress_appointments_report.pdf', as_attachment=True)

# Route to generate and download Pending Appointments Report
@app.route('/api/reports/pending-appointments', methods=['GET'])
def get_pending_appointments_report():
    generate_pending_appointments_report_pdf()
    return send_file('pending_appointments_report.pdf', as_attachment=True)

# Route to generate and download Doctor Info Report
@app.route('/api/reports/doctor-info', methods=['GET'])
def get_doctor_info_report():
    generate_doctor_info_report_pdf()
    return send_file('doctor_info_report.pdf', as_attachment=True)

# Route to generate and download Patient Info Report
@app.route('/api/reports/patient-info', methods=['GET'])
def get_patient_info_report():
    generate_patient_info_report_pdf()
    return send_file('patient_info_report.pdf', as_attachment=True)

# Route to trigger generation of all reports
@app.route('/api/reports/generate-all', methods=['GET'])
def generate_all_reports():
    generate_reports()
    return jsonify({'message': 'Reports generated successfully'})

if __name__ == '__main__':
    app.run(debug=True)

from io import BytesIO

from flask import Flask, send_file
from openpyxl import Workbook

app = Flask(__name__)


def get_tdd_excel_workbook():
    wb = Workbook()
    ws = wb.active
    ws.append(['TDD', 'is', 'AWESOME!'])
    ws.append(['Except', 'when', 'it', 'is', 'particularly', 'hard'])
    ws.append(['But', 'we', 'can', 'handle', 'it'])
    return wb


@app.route('/excel/download')
def download_excel():
    wb = get_tdd_excel_workbook()

    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    return send_file(file_stream, attachment_filename="tdd-excel.xlsx", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

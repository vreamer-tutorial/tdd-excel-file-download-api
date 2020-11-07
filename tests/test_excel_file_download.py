import unittest
from io import BytesIO

from openpyxl import load_workbook

from app import app


class TestExcelFileDownload(unittest.TestCase):
    def test_download_excel_file(self):
        # Setup / Arrange
        client = app.test_client()

        # Execute / Act
        response = client.get('/excel/download')

        # Assert
        # Assert file name is correct
        self.assertEqual(200, response.status_code)
        self.assertEqual('attachment; filename=tdd-excel.xlsx', response.headers['Content-Disposition'])

        # Assert file content is correct
        expected_file_content = [
            ['TDD', 'is', 'AWESOME!'],
            ['Except', 'when', 'it', 'is', 'particularly', 'hard'],
            ['But', 'we', 'can', 'handle', 'it'],
        ]
        wb = load_workbook(filename=BytesIO(response.data))
        ws = wb.worksheets[0]
        actual_file_content = [[cell.value for cell in row if cell.value is not None] for row in ws.rows]
        self.assertEqual(expected_file_content, actual_file_content)

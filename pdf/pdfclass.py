import pdfkit as pdf


class Option(object):
    def __init__(self, inputs, path):
        self.inputs = inputs
        self.path = path

    def url(self):
        pdf.from_url(self.inputs, self.path + ".pdf")

    def files(self):
        pdf.from_file(self.inputs, self.path + ".pdf")

    def string(self):
        pdf.from_string(self.inputs, self.path + ".pdf")

    def others(self, options):
        self.options = options
        pdf.from_url(self.inputs, self.path + ".pdf", options=self.options )

    def mult(self, many):
        self.many = pdf.from_url([
            'google.com',
            'yandex.ru',
            'engadget.com'
                ], self.many + ".pdf")

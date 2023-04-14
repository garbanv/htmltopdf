import pdfkit
import jinja2


user = 'Alexei Garbán'

context ={'user':user}

template_loader = jinja2.FileSystemLoader('./pages/api/python/')
template_env=jinja2.Environment(loader=template_loader)

template=template_env.get_template("template.html")
output_text=template.render(context)

config= pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
pdfkit.from_string(output_text,'mynewpdf.pdf',configuration=config)





print("saved")








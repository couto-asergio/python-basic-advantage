from datetime import datetime
from string import Template

with open('template.html', 'r') as html:
    template = Template(html.read())
    current_date = datetime.now().strftime('%d/%m/%Y')
    msg_body = template.safe_substitute(name='Luiz Otávio', date=current_date)

print(msg_body)

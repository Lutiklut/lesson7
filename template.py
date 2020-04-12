import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def get_context(company, model, character):
    return {
        'company': company,
        'model': model,
        'character':character}


def from_template(company, model, character, template):
        template = DocxTemplate(template)
        context = get_context(company, model, character)
        template.render(context)
        template.save(company +'_template.docx')



def generate_report(company, model, character):
              template = 'template.docx'
              document = from_template(company, model, character, template)




with open('data') as f:
    for line in f:
        newlist = line.split(',')

print(get_context(newlist[0],newlist[1],newlist[2]))
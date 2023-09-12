# importing openai module into your openai environment
import Keys
import openai

# assigning API KEY to initialize openai environment
openai.api_key = Keys.openai_api_key

titles = [
    ['Administrador de redes y seguridad informática',
    'Licencia en tecnología e informática',
    'Analista de Sistemas Informáticos (Software Test).',
    'Ingeniero/a en Sistemas o Informática con Experiencia en Desarrollo Full Stack',
    'Analista de Sistemas Informáticos (Software Test).',
    'Tecnico de soporte',
    'Analista de Sistemas Informáticos (Software Test).',
    'Administrador base de datos TI MS SQL',
    'Analista de Seguridad Informatica',
    'Analista de seguridad informática (Medellín)',
    'Oficial de seguridad informática',
    'Administrador de seguridad Informática',
    'Docente de informática para Apartadó',
    'Coordinador/a de campo para Urabá',
    'Coordinador/a de empacadora para Urabá',
    'Analista de bases de Datos Microsoft Dynamics',
    'Analista de TI / Tecnólogo',
    'profesional administrativo',
    'Cientifico de datos',
    'Coordinador de inteligencia de negocios'],
    ['Analista de infraestructura',
    'Desarrollador Front',
    'Analista en gestión del riesgo Medellin',
    'Auxiliar de TIC',
    'Analista Funcional SAP',
    'tecnólogo en sistemas',
    'Auxiliar de Infraestructura',
    'Dermoconsultora',
    'Auxiliar contable',
    'Sales Operations Coordinator',
    '¡¡Gran Convocatoria!! Asesor comercial con exp en ventas en calle, consumo masivo, financiero, sector agroinsumos o similares',
    'Asistente Administrativo/a',
    'Ingeniero de Detalles (Estructural)',
    'Operador de medios tecnológicos 3849',
    'Administrador de punto',
    'Desarrollador/a Python',
    'Desarrollador middle',
    'Profesional de Maquinaria y Equipos – Sector Construcción',
    'Auxiliar de sistemas',
    'Asistente de afiliación y registro'],
    ['Desarrollador Front',
    'Analista de Sistemas',
    'Regente de farmacia',
    'Agente de mesa ayuda SAP',
    'Analista de Bases de Datos SQL',
    'Supervisor logistico de alimentos',
    'arquitecto/a Software',
    'Auxiliar de soporte técnico',
    'Coordinador/a de campo para Urabà',
    'Coordinador(a) de empacadora para Apartadó',
    'Contador/a revisor/a fiscal',
    'Ingeniero Especializado Medellín',
    'Ingeniero de sistemas certificado como auditor de sistemas de información',
    'Analista',
    'Ingeniero de sistemas',
    'supervisor/a de producción',
    'Analista de Soporte de Sistemas',
    'Representante de Visual Merchandising y entrenamiento',
    'Analista de Infraestructura – Soporte nivel 1',
    'Especialista de Tecnologías de información'],
    ['Técnico de soporte insite',
    'Trabajo Desde Casa Analista de Negocios / Ref. 0031S',
    'Trabajo Desde Casa Analista de Negocios / Ref. 0031S',
    'Trabajo Desde Casa Analista de Negocios / Ref. 0031S',
    'Trabajo Desde Casa Analista de Negocios / Ref. 0031S',
    'Trabajo Desde Casa Analista de Negocios / Ref. 0031S',
    'Trabajo Desde Casa Analista de Negocios / Ref. 0031S',
    'Analista de sistemas',
    'Desarrollador AWS',
    'Consultor ERP',
    'Técnico de servicio',
    'Analista de bienestar y desarrollo',
    'community manager',
    'community manager',
    'Asistente Comercial',
    '3573',
    'Auxiliar de seguridad logistico',
    'Desarrollador Microsoft Project Server 2013',
    'Analista de desarrollo y soporte',
    'Técnico o tecnologo mecanico, electrico, electronico, electromecanicos']
]

categorias = """
Developer, full-stack
Developer, back-end
Developer, front-end
Developer, desktop or enterprise applications
Developer, mobile
Engineering manager
Student
Developer, embedded applications or devices
Data scientist or machine learning specialist
DevOps specialist
Academic researcher
Research & Development role
Senior Executive (C-Suite, VP, etc.)
Engineer, data
Cloud infrastructure engineer
Developer, game or graphics
Data or business analyst
System administrator
Project manager
Developer, QA or test
Security professional
Product manager
Engineer, site reliability
Educator
Scientist
Developer Experience
Blockchain
Hardware Engineer
Designer
Database administrator
Developer Advocate
Marketing or sales professional
"""
category="""
Software Engineer/Developer
Frontend Developer
Backend Developer
Full-Stack Developer
Quality Assurance (QA) Analyst
DevOps Engineer
Data Scientist
Cloud Engineer
Mobile App Developer
Cybersecurity Engineer
other
"""

# function that takes in string argument as parameter
def comp(PROMPT, MaxToken=50, outputs=1):
	# using OpenAI's Completion module that helps execute
	# any tasks involving text
	response = openai.Completion.create(
		# model name used here is text-davinci-003
		# there are many other models available under the
		# umbrella of GPT-3
		model="text-davinci-003",
		# passing the user input
		prompt=PROMPT,
		# generated output can have "max_tokens" number of tokens
		max_tokens=MaxToken,
		# number of outputs generated in one call
		n=outputs
	)
	# creating a list to store all the outputs
	output = list()
	for k in response['choices']:
		output.append(k['text'].strip())
		
	return print(output)

PROMPT = """
Te daré unas categorías, de las cuales tu rol sera devolverme un json con clave (la categoría) y el valor será el número del cual tu identificaras cuantos títulos de trabajo que te pasare se relacionan de alguna manera con esas categorías estas son las categorías {categorias} y acá te proporciono los títulos {titles} recuerda que son 80 títulos, solo responde con el JSON, NADA MAS.
"""
# comp(PROMPT, MaxToken=3000, outputs=1)


response = openai.ChatCompletion.create(
  model="gpt-4-0613",
  messages=[
        {"role": "system", "content": "Hello"},
        {"role": "user", "content": f"""
        te dare unas categorias, de las cuales tu rol sera devolverme un json con clave (la categoria) y el valor dera el numero del cual tu identificaras cuantos titulos de trabajo que te pasare se relacionan con esas categorias estos son las categorias {category} y aca te proporciono los titulos {titles} recuerda que son 80 titulos; solo responde con el JSON, NADA MAS."""}
    ]
)

print(response['choices'][0]['message']['content'])
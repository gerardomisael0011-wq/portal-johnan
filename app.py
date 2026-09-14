import os
from flask import Flask, render_template

app = Flask(__name__)


# ==========================================================
# INFORMACIÓN DE LAS ÁREAS
# ==========================================================

areas = {

    "Control de Producción IT": {
        "descripcion": "Área encargada del soporte y control de los sistemas tecnológicos relacionados con la operación y producción.",
        "objetivo": "Mantener disponibles y funcionando correctamente los recursos tecnológicos necesarios para la operación.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Soporte de sistemas",
                "descripcion": "Atención y seguimiento de incidencias relacionadas con sistemas y aplicaciones."
            },
            {
                "nombre": "Infraestructura IT",
                "descripcion": "Administración y soporte de equipos, redes y recursos tecnológicos."
            },
            {
                "nombre": "Monitoreo",
                "descripcion": "Supervisión del funcionamiento de los servicios y recursos tecnológicos."
            }
        ],

        "personal": []
    },


    "Calidad": {
        "descripcion": "Área responsable de establecer y mantener los estándares de calidad dentro de los procesos de la organización.",
        "objetivo": "Garantizar el cumplimiento de los estándares y requisitos establecidos para los procesos y productos.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Control de calidad",
                "descripcion": "Supervisión y seguimiento de los estándares establecidos."
            },
            {
                "nombre": "Auditorías",
                "descripcion": "Seguimiento de auditorías y cumplimiento de requisitos."
            },
            {
                "nombre": "Mejora continua",
                "descripcion": "Identificación de oportunidades para mejorar los procesos."
            }
        ],

        "personal": [
            {
                "nombre": "Colaborador de ejemplo",
                "puesto": "Responsable de Calidad",
                "descripcion": "Información del colaborador.",
                "foto": "persona1.jpg"
            },
            {
                "nombre": "Colaborador de ejemplo 2",
                "puesto": "Especialista de Calidad",
                "descripcion": "Información del colaborador.",
                "foto": "persona2.jpg"
            },
            {
                "nombre": "Colaborador de ejemplo 3",
                "puesto": "Analista de Calidad",
                "descripcion": "Información del colaborador.",
                "foto": "persona3.jpg"
            }
            ]
    },


    "Contabilidad": {
        "descripcion": "Área encargada de administrar y controlar la información financiera y contable de la organización.",
        "objetivo": "Mantener un adecuado control de las operaciones financieras y contables.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Contabilidad general",
                "descripcion": "Registro y control de las operaciones contables."
            },
            {
                "nombre": "Facturación",
                "descripcion": "Gestión y seguimiento de procesos de facturación."
            },
            {
                "nombre": "Reportes financieros",
                "descripcion": "Generación y análisis de información financiera."
            }
        ],

        "personal": []
    },


    "Recursos Humanos": {
        "descripcion": "Área responsable de la gestión del personal y de los procesos relacionados con los colaboradores.",
        "objetivo": "Administrar de manera eficiente los procesos relacionados con el talento humano.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Reclutamiento",
                "descripcion": "Gestión de procesos de selección e incorporación de personal."
            },
            {
                "nombre": "Capacitación",
                "descripcion": "Coordinación de actividades de formación y desarrollo."
            },
            {
                "nombre": "Administración de personal",
                "descripcion": "Gestión de información y procesos administrativos del personal."
            }
        ],

        "personal": []
    },


    "Compras": {
        "descripcion": "Área encargada de gestionar la adquisición de materiales, productos y servicios necesarios para la operación.",
        "objetivo": "Garantizar el abastecimiento oportuno de los recursos requeridos por la organización.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Proveedores",
                "descripcion": "Gestión y seguimiento de proveedores."
            },
            {
                "nombre": "Cotizaciones",
                "descripcion": "Solicitud y comparación de propuestas comerciales."
            },
            {
                "nombre": "Órdenes de compra",
                "descripcion": "Gestión y seguimiento de órdenes de compra."
            }
        ],

        "personal": []
    },


    "Ventas": {
        "descripcion": "Área encargada de gestionar las actividades comerciales y la relación con clientes.",
        "objetivo": "Impulsar las actividades comerciales y mantener una adecuada atención a los clientes.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Clientes",
                "descripcion": "Gestión y seguimiento de las relaciones con clientes."
            },
            {
                "nombre": "Ventas",
                "descripcion": "Seguimiento de oportunidades y actividades comerciales."
            },
            {
                "nombre": "Atención comercial",
                "descripcion": "Apoyo y atención a las necesidades comerciales."
            }
        ],

        "personal": []
    },


    "Nuevos Proyectos": {
        "descripcion": "Área enfocada en la planeación y desarrollo de nuevos proyectos dentro de la organización.",
        "objetivo": "Coordinar y dar seguimiento a iniciativas destinadas al crecimiento y mejora de la organización.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Planeación",
                "descripcion": "Definición y organización de nuevos proyectos."
            },
            {
                "nombre": "Desarrollo",
                "descripcion": "Seguimiento de las diferentes etapas de los proyectos."
            },
            {
                "nombre": "Implementación",
                "descripcion": "Coordinación de la puesta en marcha de nuevos proyectos."
            }
        ],

        "personal": []
    },


    "Producción": {
        "descripcion": "Área responsable de las actividades relacionadas con la fabricación y operación productiva.",
        "objetivo": "Mantener una operación productiva eficiente, segura y orientada al cumplimiento de los objetivos establecidos.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Operación",
                "descripcion": "Actividades relacionadas con la operación de producción."
            },
            {
                "nombre": "Procesos",
                "descripcion": "Seguimiento y control de los procesos productivos."
            },
            {
                "nombre": "Supervisión",
                "descripcion": "Coordinación y seguimiento de las actividades de producción."
            }
        ],

        "personal": []
    },


    "Embarques": {
        "descripcion": "Área encargada de coordinar y controlar las actividades relacionadas con los embarques y movimientos de producto.",
        "objetivo": "Garantizar que los productos sean preparados y enviados de manera correcta y oportuna.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Preparación",
                "descripcion": "Preparación de productos para su envío."
            },
            {
                "nombre": "Logística",
                "descripcion": "Coordinación de actividades relacionadas con los embarques."
            },
            {
                "nombre": "Control de envíos",
                "descripcion": "Seguimiento y control de los productos enviados."
            }
        ],

        "personal": []
    },


    "Mantenimiento": {
        "descripcion": "Área responsable de conservar en condiciones adecuadas los equipos, instalaciones y recursos necesarios para la operación.",
        "objetivo": "Prevenir fallas y mantener la disponibilidad de los recursos utilizados en la organización.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Mantenimiento preventivo",
                "descripcion": "Actividades programadas para prevenir fallas."
            },
            {
                "nombre": "Mantenimiento correctivo",
                "descripcion": "Atención de fallas y problemas detectados."
            },
            {
                "nombre": "Infraestructura",
                "descripcion": "Mantenimiento de instalaciones y recursos físicos."
            }
        ],

        "personal": []
    },


    "Dirección": {
        "descripcion": "Área encargada de la dirección estratégica y coordinación general de la organización.",
        "objetivo": "Establecer objetivos estratégicos y coordinar las acciones necesarias para alcanzarlos.",
        "ubicacion": "Por definir",
        "contacto": "Por definir",

        "subcategorias": [
            {
                "nombre": "Dirección general",
                "descripcion": "Coordinación y supervisión general de la organización."
            },
            {
                "nombre": "Planeación estratégica",
                "descripcion": "Definición y seguimiento de objetivos estratégicos."
            },
            {
                "nombre": "Toma de decisiones",
                "descripcion": "Evaluación de información para la toma de decisiones."
            }
        ],

        "personal": []
    }
}


# ==========================================================
# PÁGINA PRINCIPAL
# ==========================================================

@app.route("/")
def inicio():
    return render_template("index.html")


# ==========================================================
# PÁGINA DINÁMICA DE CADA ÁREA
# ==========================================================

@app.route("/area/")
def area(nombre_area):

    if nombre_area not in areas:
        return "Área no encontrada", 404

    datos_area = areas[nombre_area]

    return render_template(
        "area.html",
        nombre_area=nombre_area,
        area=datos_area
    )


# ==========================================================
# INICIAR SERVIDOR
# ==========================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
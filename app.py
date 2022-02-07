import yaml


class DBTDocParser:
    def __init__(self, ymlfile):
        self.yaml_file = ymlfile
        self.template = None
        self.data = None

    def load_yaml(self):
        """
        Función para cargar un yaml como diccionario
        :return: dict
        """
        with open(self.yaml_file) as file:
            self.data = yaml.load(file, Loader=yaml.FullLoader)
            print("Yaml cargado...")
            return self.data

    def parser(self):
        """
        Iterador que pasa por cada una de las propiedades del yml y las inyecta en un template de HTML
        :return: :type str
        """
        dict_ = self.data
        template_base = """
        <html>
            <head>
              <meta name="viewport" content="width=device-width, initial-scale=1">
              <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            </head>
            <div class="container">
                <div class="row">
                    {}
                </div>
            </div>    
        </html>
        """
        table_ = ""
        table_colums_ = ""
        for model in dict_['models']:
            table_ = f"<h2> Tabla: {model['name']} </h2> \n"
            table_ = table_ + f"<small> Descripcion: {model['description']} </small> <br>"
            table_ = table_ + """
            <table class="table table-striped table-condensed" style="width: 1450px;table-layout: fixed;overflow-wrap: break-word;">
            <thead>
                <tr>
                    <th>Column</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                {}
            </tbody>
            </table>
            """

            for column in model['columns']:
                table_colums_ = table_colums_ + f"""
                    <tr>
                        <td>{column['name']}</td>
                        <td>{column['description']}</td>
                    </tr>
                """

        self.template = template_base.format(table_.format(table_colums_))
        print("Template cargado...")
        return self.template

    def generate_html(self):
        """
        Funcion para generar HTML con el template generado
        """
        html_template_name = "template.html"
        with open(html_template_name, 'w') as fd:
            fd.write(self.template)

        print(f"HTML[{html_template_name}] creado ...")

    def run(self):
        self.load_yaml()
        self.parser()
        self.generate_html()
        print(f"Fin de la ejecucion.")


if __name__ == '__main__':
    DBTDocParser(ymlfile="schema.yaml").run()

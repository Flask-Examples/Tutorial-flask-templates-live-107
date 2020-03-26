"""routes.py"""

from flask import  Flask, render_template, request, flash


def load(app: Flask) -> Flask:
    @app.route("/testing")
    def testing():
        return render_template('testing.html')

    @app.route("/about")
    def about():
        return render_template('about.html')


    @app.route("/")
    def home():

        pharse = """
        Bulma is a free, open source CSS framework based on Flexbox and used by more than 200,000 developers.
        Bulma is a free, open source CSS framework based on Flexbox and used by more than 200,000 developers.
        """
        name = "Home Page"
        languages = ['Python', 'Javascript', 'C#', 'Go']

        return render_template('home.html', name=name, pharse=pharse, languages=languages)

    @app.route("/login", methods=['GET', 'POST'])
    def login():

        contact = ''

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            contact = f'<Name {name}> {email}'
            flash('Logado com sucesso!', 'success')

        return render_template('login.html', contact=contact)

    return app

import fabric # importing the base package
from fabric import Application
from fabric.widgets.label import Label # gets the Label class
from fabric.widgets.window import Window # grabs the Window class from Fabric
from fabric.widgets.circularprogressbar import CircularProgressBar # imports the CircularProgressBar class
from fabric.utils import get_relative_path # imports the get_relative_path function


"""Widget for displaying the volume levels."""
class VolumeWidget(Label):









if __name__ == "__main__":
    app = Application(

    )

    app.set_stylesheet_from_file(get_relative_path("main.css"))

    app.run()

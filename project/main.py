import pyfiglet

from .configuration.config import setConfig
from .view.interface import gui


def main():
    try:
        path = setConfig().path
        platform = setConfig().platform
        #Capturar los datos relevantes del proceso 
        (pwd, project, projectFrontendType, backendSevice, frontendService) = gui()

        ascii_banner = pyfiglet.figlet_format(
            "Custom Project \n Frontend - Backend \n Angular - Ionic \n TypeScript!")
        print(ascii_banner)
        print("Version: 1.0.0", f'System: {platform}' )
        print("Your path:", path)

        #Verificar el tipo de servicio seleccionado
        if(frontendService.lower() == 'yes'):
            print('Service Backend selected')
            #Generar el servicio frontend dependiendo del framework seleccionado
        if(backendSevice.lower() == 'yes'):
            print('Service Backend selected')
            #Generar el servio backend en typescrip
    except Exception as err:
        print("Error:", err)
        return



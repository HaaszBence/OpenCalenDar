import uvicorn
import os
from dotenv import load_dotenv
from api.main import app

class Backend:
    def __init__(self, host: str = "127.0.0.1", port: int = 8000):
        self.host: str = host # uvicorn serving host
        self.port: int = port # uvicorn serving port
        self.dev: bool = False
        self.prod: bool = False
        
    def run(self):
        print("Starting OpenCalenDar backend...\n")
        
        self.load_config()
        
        uvicorn.run(app, host=self.host, port=self.port)
        
        
        
    def load_config(self) -> None:
        env = input("Production or Development environment? (P/D): ")
        
        match env.upper():
            case "D":
                print("Loading development environment variables...")
                load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../SECRETS/DEV.env"))
                self.dev = True
            case "P":
                print("Loading production environment variables...")
                load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../SECRETS/PROD.env"))
                self.prod = True
            case _:
                print("Invalid environment choice. Exiting.")
                exit(1)
                
    def load_environment_variables(self) -> None:
        if self.dev:
            print("Development environment variables loaded successfully.")
        elif self.prod:
            print("Production environment variables loaded successfully.")
        else:
            print("No environment selected. Exiting.")
            exit(1)
    
        
        
if __name__ == "__main__":
    backend = Backend()
    backend.run()
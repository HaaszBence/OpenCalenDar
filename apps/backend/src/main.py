import argparse
import os
import uvicorn
from fastapi import FastAPI


parser = argparse.ArgumentParser()
parser.add_argument("--env", choices=["dev", "prod"], default="dev", help="Set the environment for the application")
args = parser.parse_args()

BASE_DIR = os.path.dirname(__file__)
for _ in range(3):
    BASE_DIR = os.path.dirname(BASE_DIR)
# NOTE: This is a workaround to reach project root for imports. Consider restructuring the project to avoid this.

env_file = os.path.join(BASE_DIR, "SECRETS", f"{args.env.upper()}.env")

from settings import Settings

settings = Settings(_env_file=env_file)
app = FastAPI()

class Main:
    def __init__(self, settings: Settings):
        self.settings = settings
        
    @app.get("/")
    async def health_check():
        return {"status": "healthy"}
    
    def run(self):
        print("Launching OpenCalenDar API...\n")
        
        uvicorn.run(app, host=self.settings.uvi_host, port=self.settings.uvi_port)       
        
if __name__ == "__main__":
    main = Main(settings=settings)
    main.run()
    
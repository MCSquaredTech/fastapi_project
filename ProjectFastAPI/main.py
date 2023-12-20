import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ProjectFastAPI.database import database
from ProjectFastAPI.routers.post import router as post_router


# Get the Logger and set it's value 
logger = logging.getLogger("myApiProject")
logger.setLevel(logging.Debug)

# Create Handlers 
console_handler = logging.StreamHandler()
file_handler = logging.StreamHandler("myApiProject.log") 

# Create the Formatter 
logger_formatter = logging.Formatter(
    "%asctime)s %(levelname)s %(name)s: %(lineno)d %(message)s"
)

# Add formatter to the handlers 
console_handler.setFormatter(logger_formatter)
file_handler.setFormatter(logger_formatter) 

# Add the handlers to the logger 
logger.addHandler(console_handler)
logger.addHandler(file_handler) 
 
@asynccontextmanager 
async def lifespan(app: FastAPI): 
    await database.connect()
    print("start database.commenction")
    yield 
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(post_router)
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['USER']
pwd = os.environ['PASSWORD']
database = os.environ['DATABASE']
host = os.environ['HOST']
server = os.environ['SERVER']

DATABASE_CONNECTION=f'{server}://{user}:{pwd}@{host}/{database}'
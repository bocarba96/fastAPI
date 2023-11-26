from fastapi import FastAPI, HTTPException
from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from model import User, Gender, Role

app = FastAPI()


# contenu supprime
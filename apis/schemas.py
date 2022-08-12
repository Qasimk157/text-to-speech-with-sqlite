from pydantic import BaseModel


class TTSRequestPayload(BaseModel):
    enterText: str
    
    
class TTSResponsePayload(BaseModel) :
    
    enterText: str
    text_id: int   

class Responses(BaseModel):
    
    status: bool
    message: str
    
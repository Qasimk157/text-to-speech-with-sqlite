from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from apis import models, schemas
from apis.database import SessionLocal, engine
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
app=FastAPI()

models.Base.metadata.create_all(engine)
def get_db():

    db=SessionLocal()

    try:

        yield db

    finally:
        db.close()
        

@app.post('/text-to-speech/', tags=['text-to-speech'], status_code=status.HTTP_201_CREATED, response_model=schemas.TTSResponsePayload,
                           responses={
                           status.HTTP_400_BAD_REQUEST: {"model":  schemas.Responses},
                           status.HTTP_422_UNPROCESSABLE_ENTITY: {"model":  schemas.Responses},
                           status.HTTP_500_INTERNAL_SERVER_ERROR: {"model":  schemas.Responses}})
def create(request:schemas.TTSRequestPayload,db:Session=Depends(get_db)):
    new_text=models.TTSPayload(enterText=request.enterText)
    try:
        db.add(new_text)
        db.commit()
        db.refresh(new_text)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content =jsonable_encoder(new_text))
    except Exception:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content =jsonable_encoder(schemas.Responses))

@app.post('/tts/', tags=['text-to-speech'], status_code=status.HTTP_201_CREATED, response_model=schemas.TTSResponsePayload,
                           responses={
                           status.HTTP_400_BAD_REQUEST: {"model":  schemas.Responses},
                           status.HTTP_422_UNPROCESSABLE_ENTITY: {"model":  schemas.Responses},
                           status.HTTP_500_INTERNAL_SERVER_ERROR: {"model":  schemas.Responses}})
def create(request:schemas.TTSRequestPayload,db:Session=Depends(get_db)):
    new_text=models.TTSPayload(enterText=request.enterText)
    try:
        db.add(new_text)
        db.commit()
        db.refresh(new_text)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content =jsonable_encoder(new_text))
    except Exception:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content =jsonable_encoder(schemas.Responses))

@app.post('/pyttsx3/', tags=['text-to-speech'], status_code=status.HTTP_201_CREATED, response_model=schemas.TTSResponsePayload,
                           responses={
                           status.HTTP_400_BAD_REQUEST: {"model":  schemas.Responses},
                           status.HTTP_422_UNPROCESSABLE_ENTITY: {"model":  schemas.Responses},
                           status.HTTP_500_INTERNAL_SERVER_ERROR: {"model":  schemas.Responses}})
def create(request:schemas.TTSRequestPayload,db:Session=Depends(get_db)):
    new_text=models.TTSPayload(enterText=request.enterText)
    try:
        db.add(new_text)
        db.commit()
        db.refresh(new_text)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content =jsonable_encoder(new_text))
    except Exception:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content =jsonable_encoder(schemas.Responses))

@app.post('/gtts/', tags=['text-to-speech'], status_code=status.HTTP_201_CREATED, response_model=schemas.TTSResponsePayload,
                           responses={
                           status.HTTP_400_BAD_REQUEST: {"model":  schemas.Responses},
                           status.HTTP_422_UNPROCESSABLE_ENTITY: {"model":  schemas.Responses},
                           status.HTTP_500_INTERNAL_SERVER_ERROR: {"model":  schemas.Responses}})
def create(request:schemas.TTSRequestPayload,db:Session=Depends(get_db)):
    new_text=models.TTSPayload(enterText=request.enterText)
    try:
        db.add(new_text)
        db.commit()
        db.refresh(new_text)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content =jsonable_encoder(new_text))
    except Exception:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content =jsonable_encoder(schemas.Responses))

@app.post('/ruth-tts/', tags=['text-to-speech'], status_code=status.HTTP_201_CREATED, response_model=schemas.TTSResponsePayload,
                           responses={
                           status.HTTP_400_BAD_REQUEST: {"model":  schemas.Responses},
                           status.HTTP_422_UNPROCESSABLE_ENTITY: {"model":  schemas.Responses},
                           status.HTTP_500_INTERNAL_SERVER_ERROR: {"model":  schemas.Responses}})
def create(request:schemas.TTSRequestPayload,db:Session=Depends(get_db)):
    new_text=models.TTSPayload(enterText=request.enterText)
    try:
        db.add(new_text)
        db.commit()
        db.refresh(new_text)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content =jsonable_encoder(new_text))
    except Exception:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content =jsonable_encoder(schemas.Responses))


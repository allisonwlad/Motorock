from fastapi import APIRouter, UploadFile, File, HTTPException
from util.fileProcess import load_sales_table, read_transform_csv, conn
import os

router = APIRouter(prefix='/v1/fileProcess')
path_files = "files/"

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        try:
            with open(path_files+file.filename, 'wb') as f:
                f.write(contents)

            df = read_transform_csv(path_files+file.filename)
            try:
                load_sales_table(conn, df, 'vendas.tb_vendas')

                os.remove(path_files+file.filename)
                return {"message": "Record Sucessful"}
            except Exception:
                raise HTTPException(status_code=500, detail="Error Database")
        except Exception:
            raise HTTPException(status_code=500, detail=f"Error recording file {file.filename}")
    except Exception:
        raise HTTPException(status_code=500, detail=f"Error uploading file {file.filename}")
    finally:
        file.file.close()

    
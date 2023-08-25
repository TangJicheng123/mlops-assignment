from fastapi import FastAPI
from pydantic import BaseModel
import base64
import io

app = FastAPI()

class InputData(BaseModel):
    request_id: int
    text: str
    input_image_base64: str
    random_seed: int
    temperature: float

class OutputData(BaseModel):
    request_id: int
    output_image_base64: str

def fake_process_image(prompt: str, image_base64: str, seed: int) -> str:
    # Based on the input, you need to generate the output image 
    # and encode it to base64. 
    # Here, we are just demonstrating the process and not actually generating the image.
    with open("./output.png", "rb") as image_file:
        image_data = image_file.read()
    output_base64_str = base64.b64encode(image_data).decode('utf-8')
    return output_base64_str

@app.post("/generation")
def generation_image(input_data: InputData) -> OutputData:
    processed_image = fake_process_image(input_data.text, input_data.input_image_base64, input_data.random_seed)
    output_data = OutputData(request_id=input_data.request_id, output_image_base64=processed_image)
    return output_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

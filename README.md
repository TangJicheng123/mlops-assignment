# MLOps Assignment

Please implement a service that generates images using ControlNet and provides an API on port 8000.

You should first fork this repository, and then send us the code or the url of your forked repository via email.

Please do not submit any pull requests to this repository.

## Input/Output
```
curl -X 'POST' \
  'http://0.0.0.0:8000/generation/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "request_id": 1234,
  "text": "Here is the prompt, like: a muscle man",
  "input_image_base64": "Here is the input image base64 string",
  "random_seed": 5678
}'
```

Should return:

```
{
   "request_id": 1234,
   "output_image_base64": "Here is the output image base64 string"
}
```

I gave an example of server.py in the example/ for your reference,  
you need implement a server with the same api.   

## Delivery
- Dockerfile: To generate an application image
- app/ : Your server code

## Evaluation
#### 1. Service availability     
We will use the following command to deploy your code based on the Dockerfile you provided.   
```
docker build -t mlops:v1 .
docekr run -d -p 8000:8000 mlops:v1
python example/client.py
```

#### 2. Performance   
We measure the performance of your code by request latency.    
We care more about the performance of your code on the GPU, please make sure your code can take advantage of CUDA

## Reference
https://huggingface.co/blog/controlnet     
https://github.com/lllyasviel/ControlNet    

## FAQ
#### 1. Controlnet has a lot of parameters, should I need to add input parameters in the server ?  
No need to add new parameters, you can set the default value directly in the server.

#### 2. There are many models in ControlNet, and there are also many base models for stable diffusion. Which one should I use ?
You can choose any of the available models. For reference, the ControlNet model, cannay-type models can be used. The base model can use the model of sd v1.5

#### 3. Can I implement it in other languages like C/C++/CUDA/Go?  
Yes. Just make sure the api is available and optimize performance as much as possible  

#### 4. Can I use 3rd party library to speed up the library? For example TensorRT/Onnxruntime and so on.   
Yes. You can use any legal code to optimize performance. It should be noted that if you have converted the model format, you need to provide a script for converting the model.

#### 5. Is the image format jpeg/jpg or png?
Both are OK.


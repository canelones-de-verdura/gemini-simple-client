Chat **muy** simple usando la API de Gemini.  

[Grabación de pantalla desde 2024-10-22 14-20-52.webm](https://github.com/user-attachments/assets/e375eccf-c489-4af6-87f0-610dedee79f4)

### Como usar  

Antes que nada hay que levantar un venv e instalar la SDK:

```
$ python -m venv .
$ ./bin/pip install google-generativeai
```  

Además, el programa espera una clave para la API en ```secret/apikey.py``` de la siguiente forma:  
```python
API_KEY = <tu clave>
```  

Por último, para ejecutar el programa:  
```
$ ./bin/python main.py
```  

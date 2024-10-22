Chat **muy** simple usando la API de Gemini.  

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

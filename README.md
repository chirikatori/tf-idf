# tf-idf

## Run Locally  

Clone the project  

~~~bash  
  git clone https://github.com/chirikatori/tf-idf.git
~~~

Go to the project directory  

~~~bash  
  cd tf-idf
~~~

Crawl_data  

~~~bash  
python crawl.py
~~~

Install requirements

~~~bash  
pip install -r requirements.txt && python tools/nltk_downloader.py
~~~

Create term-document.csv  

~~~bash  
python term-document.py
~~~

Create tf-idf.csv  

~~~bash  
python tf-idf.py
~~~


## License  

[MIT](https://choosealicense.com/licenses/mit/)

FROM jupyter/base-notebook:python-3.12

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/ml-latest-small && chmod -R 755 /app/ml-latest-small

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]

FROM python:3

WORKDIR /code

RUN mkdir ./inventario

COPY DeLab/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "appDeLab.py" ]
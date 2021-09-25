FROM python:3

WORKDIR /usr/src/msappflask

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./appservice.py", "0.0.0.0:5000"]

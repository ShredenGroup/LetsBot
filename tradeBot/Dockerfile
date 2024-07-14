FROM python:3.12.4
WORKDIR /app/tradeBot

COPY requirements.txt .

RUN pip install  -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

# Add your CMD or ENTRYPOINT here if needed
# CMD ["python", "your_script.py"]
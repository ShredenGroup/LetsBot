FROM --platform=$BUILDPLATFORM python:3.8 as builder

WORKDIR /install


COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

FROM python:3.8
WORKDIR /app

COPY --from=builder /install /usr/local
COPY . /app/tradeBot

CMD ["python", "-m", "tradeBot"]

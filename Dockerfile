FROM python
RUN pip install flask
COPY main.py .
CMD python main.py
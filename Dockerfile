FROM python:3
RUN pip install djangorestframework
CMD ["python", "app.py"]

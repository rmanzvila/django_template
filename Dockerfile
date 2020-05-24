FROM python:3.7-slim-buster as image_base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONDEBUG 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext bash \
  # Geospatial deependencies
  && apt-get install -y binutils libproj-dev gdal-bin \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


COPY ./requirements /requirements
RUN pip install -r /requirements/common.txt


EXPOSE 8000
WORKDIR /app

#
#  P R O D U C T I O N
#
FROM image_base as development

RUN pip install -r /requirements/develop.txt
RUN pip install -r /requirements/production.txt


COPY compose/start-prod /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

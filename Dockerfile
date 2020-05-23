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
#  D E V E L O P M E N T
#
FROM image_base as development

RUN pip install -r /requirements/develop.txt

COPY compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


COPY compose/start-dev /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start


ENTRYPOINT ["/entrypoint"]

#
#  C I / C D
#
FROM development as ci_cd

RUN pip install docker-compose awscli

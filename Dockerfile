# Extend the official Rasa SDK image
FROM rasa/rasa:3.5.2
USER root
# To install packages from PyPI
RUN pip3 install --no-cache-dir pytz==2019.3
USER 1001

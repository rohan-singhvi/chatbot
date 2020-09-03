import os
import ssl
import nltk
if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context


nltk.download()

# go to models and download punkt
# go to corpora and download the required file.
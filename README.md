# Streamlit Sample Application :baseball:

[Streamlit](https://www.streamlit.io/)をサクッと使うためのサンプルアプリケーションです.

![](img/sampleapp.jpg)

## install

### local

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Usage

### local

```bash
(venv) $ stremlit run sample_app.py
```

### Docker

```bash
docker-compose -f docker-compose-local.yml up
```

### Cloud Run(for GCP)

```bash
sh gcp_deploy.sh ${your project name}
```

# Maintainer

[@shinyorke(Shinichi-Nakagawa)](https://github.com/Shinichi-Nakagawa)
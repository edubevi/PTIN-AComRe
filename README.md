# PTIN-AComRe
## Getting Started
Projecte per l'assignatura PTIN curs 2017-18, EPSEVG-UPC

El projecte de l'equip 3 està principalment escrit en Python. Per desenvolupar instal·lar els requeriments:
```python
pip install -r requirements.txt
```

## Usage
Per compilar el contenidor
```
docker build peremontpeo/virtualdevices:latest .
```

Per descarregar el contenidor ja compilat de Docker Hub
```
docker pull peremontpeo/virtualdevices:latest
```

Per executar el contenidor
```
docker run peremontpeo/virtualdevices:latest -t 1
```
Paràmetre `-t` indica el tipus de dispositiu:
 - 1: doctor
 - 2: pacient
 - 3: ambulància
 - 4: detector de fum
 - 5: estació meteorològica
 - 6: qualitat de l'aire

Paràmetre `-i` seguit d'un integer (segons) indica l'interval amb que el dispositiu envia informació a la base de dades.

### Orquestrador
La orquestració de l'entorn virtual es fa amb l'aplicació `orchestrer_tool`. Per executar l'eina CLI
```python
python3 orchestrer_tool.py
```

### Built with
- [Docker](https://docs.docker.com/)
- [tkinter](https://wiki.python.org/moin/TkInter): Python's de-facto standard GUI
- [Faker](http://faker.readthedocs.io/en/master/):  a Python package that generates fake data

# Autors
- Adrià Pedraza
- Eduard Berenguer
- Joan Sanchez
- Pere Montpeó
- Pol Pericàs

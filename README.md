# Analiza danych zawierających informacje na temat zróżnicowania wysokości terenu i grupowanie danych ze względu na wzrost wysokości mierzony na podstawie conajmniej 10 punktów

# The purpose of project
The main purpose of our project is to compare performance between single local station and clusters during big data processing. 

### Parameters of local machine
To benchmark our program, we use: Asus ZenBook UX410UA
- Intel i5 - 7200U (2 cores, 4 threads, 2.50-210 GHz 3MB cache)
- 8 GB RAM
- Intel HD Graphics 620 ( :( )
- Disk 512 SSD M.2

### Configurations of EMR's
- some
- of 
- them ($$$)


## Prerequisites
- Python version > 2.7
- Java JDK version > 7
```bash
python
pip3 install -r requirements.txt
```

## Java installation on local machine - Linux
PySpark also requires Java to execute scripts. If user gets

```bash
$JAVA_HOME not set
``` 
error while running, then general installation is necessary.

```bash
sudo apt install default-jre
sudo apt install default-jdk
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
```

## AWS service setup
- S3 resources Tiles Terrain
- EMR Cluster (smaller than default one - m5.large)
- Pyspark included


### autorzy:
- Julia Okuniewska
- Marek Mikulski

\
aseid-2018-MikulskiM created by GitHub Classroom

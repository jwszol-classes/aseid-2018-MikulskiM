# [PL] Analiza danych zawierających informacje na temat zróżnicowania wysokości terenu (Ameryka Północna + Ameryka Południowa) i grupowanie danych (wyznaczyć 6 grup) ze względu na wzrost wysokości mierzony na podstawie conajmniej 10 punktów.
# [ENG] Data analysis of data containing information about differentiation of the altitude of the terrain (North + South America) and data grouping (designate 6 groups) based on increase in altitude measured on the basis of at least 10 points.

# The purpose of project
The main purpose of our project is to compare performance between single local station and clusters during big data processing. 

## Parameters of local machines:
To benchmark our program, we use:
#### Asus ZenBook UX410UA
- Intel i5 - 7200U (2 cores, 4 threads, 2.50-210 GHz 3MB cache)
- 8 GB RAM
- Intel HD Graphics 620 ( :( )
- Disk 512 SSD M.2
#### Samsung NP550P7C-S04PL
- Intel i5 - 3210M (2 cores, 4 threads, 2.50 - 3.10 GHz 3MB cache)
- 8 GB RAM
- Intel HD Graphics 4000
- NVIDIA GeForce GT 650M
- Disk 256 GB SSD SATA II
- Disk 1 TB HDD SATA II
- Ubuntu 20.04 virtual machine 

## Configurations of EMR's
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


## PODPAC - data collection
PODPAC is an open-source Python library built to make analysis of heterogenous geospatial datasets simple, reproducible and cloud-compatible.
On the https://registry.opendata.aws/terrain-tiles/ at the Usage Examples section there is PODPAC being mentioned as the Python library supporting Terrain Tiles for analysis made by Creare. The setup and data collection with podpac is very easy to do.
![image](https://user-images.githubusercontent.com/28922780/93671513-f24d8000-faa3-11ea-8c11-0fc4438941f7.png)
<p align="center">
  Picture 1. Data collected with PODPAC (result of getting_and_printing_data.py)
</p>

## Algorithm used to group data based on increase in altitude

![image](https://user-images.githubusercontent.com/28922780/93671856-c2ec4280-faa6-11ea-85ca-39598a4a0e85.png)
<p align="center">
  Picture 2. Grouping data (6 groups) based on increase in altitude
</p>
<br/><br/>

<br/><br/>
<br/><br/>
### authors:
- Julia Okuniewska
- Marek Mikulski

\
aseid-2018-MikulskiM created by GitHub Classroom

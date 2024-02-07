# Mapir Survey 3 Raw to Tiff Converter

This is a downstream version of the original code found at [mapircamera/camera-scripts](https://github.com/mapircamera/camera-scripts) adapted to work on Linux systems with the help of Wine.

### Configuration

Before using this code it is recommended that you create a python virtual environment to install the python packages inside. [Anaconda](https://docs.conda.io/en/latest/miniconda.html) is a good option for that.

After creating a virtual enviroment install the dependencies with:

```bash
pip install -r requirements.txt
```

If you are on a **Linux** based system you will also need to install [wine](https://wiki.winehq.org/Wine_Installation_and_Configuration) to run the `exiftool.exe` script used during the convertion.
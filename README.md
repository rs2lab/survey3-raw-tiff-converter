# Mapir Survey 3 Raw to Tiff Converter

This is a downstream version of the original code found at [mapircamera/camera-scripts](https://github.com/mapircamera/camera-scripts) adapted to work on Linux systems with the help of Wine.

### Configuration

Before using this code, you should create a Python virtual environment to install the Python packages inside. [Anaconda](https://docs.conda.io/en/latest/miniconda.html) is a good option for that.

After creating a virtual environment install the dependencies with the following:

```bash
pip install -r requirements.txt
```

If you are on a **Linux** based system you will also need to install [wine](https://wiki.winehq.org/Wine_Installation_and_Configuration) to run the `exiftool.exe` script used during the conversion.

More info about the configuration is on the [official website (setup)](https://mapir.gitbook.io/mapir-scripts/setup-do-this-first).

### How to use?

First, create two new directories to manage the processing of the files named `inFolder` and `outFolder`. Inside the `inFolder` you should set the images taken with the Mapir Survey 3 camera to be converted to the TIFF format. Then, make sure you run the following command inside the environment created in the configuration section,

On GNU/Linux Systems:

```bash
python Convert_Survey3_RAW_to_Tiff.py "$(pwd)/inFolder" "$(pwd)/outFolder"
```

On Windows:

```powershell
py "Convert_Survey3_RAW_to_Tiff.py" "%~dp0\inFolder" "%~dp0\outFolder"
```
More info on the [official website (convert raw to tiff)](https://mapir.gitbook.io/mapir-scripts/survey3-cameras/convert-raw+jpg-to-tiff).

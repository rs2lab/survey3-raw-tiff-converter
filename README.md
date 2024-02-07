# Mapir Survey 3 Raw to Tiff Converter

This is a downstream version of the original code found at [mapircamera/camera-scripts](https://github.com/mapircamera/camera-scripts) adapted to work on Linux systems with the help of Wine.

### Configuration

Before using this code, you should create a Python virtual environment to install the Python packages inside. [Anaconda](https://docs.conda.io/en/latest/miniconda.html) is a good option for that.

After creating a virtual environment install the dependencies with the following:

```bash
pip install -r requirements.txt
```

If you are on a **Linux** based system you will also need to install [wine](https://wiki.winehq.org/Wine_Installation_and_Configuration) to run the `exiftool.exe` script used during the conversion.

More info about the configuration is on the [official website](https://mapir.gitbook.io/mapir-scripts/setup-do-this-first).

### How to use?

First, create two new directories to manage the processing of the files named `inFolder` and `outFolder`. After that, make sure you run the following command inside the environment created in the configuration section:

```bash
python Convert_Survey3_RAW_to_Tiff.py $(pwd)/inFolder $(pwd)/outFolder
```

The command above was meant to be executed on a GNU/Linux based systems, for the respective commands when running on Windows see more info on the [official website](https://mapir.gitbook.io/mapir-scripts/survey3-cameras/convert-raw+jpg-to-tiff).

# image-batch-compressor
Utility to batch processing of image compression. Support with folder custom destination and dynamic size (widht, height) images.

# Feature
- Able to compress batch image from default directory input
- Able to compress batch image drom custom directory input
- Able to compress images with spesific size width and height target

# Environtment
- Python 3.6+ (https://www.python.org/downloads/)
- Pillow images packages (https://pypi.org/project/Pillow/)

# Help
Get help command and parameter usage for this repository
```bash
    python batch-compressor.py -h
```

# How to run (from default directory input)
You can use predefined directory in this repository. Only move your files into directory "input", then run code below. Batch compress result will be saved at "output" directory
```bash
    python batch-compressor.py
```


https://user-images.githubusercontent.com/19168382/203016066-70db9a8d-de67-4d1f-93c9-b4828be99d08.mov


# How to run (from custom directory input)
You can use custom directory and target for images sizing. Please follow this docs to demonstrate feature batch image compression using custom parameters
```bash
    python batch-compressor.py -i input_custom -o output_custom -ww 640 -hh 640
```


https://user-images.githubusercontent.com/19168382/203016264-007b74de-69ec-4d0a-aed8-f56746e16d90.mov


# Parameters Descriptions
- -i = assign parameter input directory
- -o = assign parameter output directory
- -ww = assign parameter custom width target for image output
- -hh - assign parameter custom height target for image output


# INSTALL
#### Credits: [JazzCore](https://github.com/JazzCore)

## Linux
#### Debian/Ubuntu
```bash
pip3 install -r requirements.txt && apt-get install wkhtmltopdf
```

#### Fedora
```bash
pip3 install -r reqiurements.txt && yum install wkhtmltopdf
```


## Windows
```bash
pip3 install -r requirements.txt
```
Download the installer from the [wkhtmltopdf downloads list](http://wkhtmltopdf.org/downloads.html) and add folder with wkhtmltopdf binary to PATH.


## Mac
Download the disk image from [wkhtmltopdf downloads list](http://wkhtmltopdf.org/downloads.html) and copy the file to a directory where PDFKit can find it. Homebrew is also available, run brew install Caskroom/cask/wkhtmltopdf
```bash
brew install Caskroom/cask/wkhtmltopdf
```

## Usage
```bash
cd 2-PDF
python3 2pdf.py
```
ENJOY!!!

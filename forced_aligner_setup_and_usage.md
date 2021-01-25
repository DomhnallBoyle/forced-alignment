## Installation and Setup of the Penn Phonetics Lab Forced Aligner

Note: Installation was completed on a Ubuntu 64-bit architecture

### Installing the Hidden Markov Model Toolkit (HTK) 3.4:
This toolkit is required to install the Forced Aligner

* Go to http://htk.eng.cam.ac.uk/download.shtml and select "HTK Software (all versions)", you will need to register for an account before proceeding
* Go to http://htk.eng.cam.ac.uk/ftp/software/, login and download the file HTK-3.4 software depending on the type of platform you're using
* Extract the contents of the software (```tar -xvf [path]```)
* Run ```./configure --prefix=/usr/local```
* Ensure ```gcc-multilib```, ```libx11-dev``` and ```libx11-dev:i386``` is installed using ```sudo apt-get install```
* The HLMTools Makefile contains an issue with spaces on line 77, replace this with a tab instead
* Run ```make all```
* Run ```make install``` (this may need to be done using sudo)
* To test the installation, download the HTK samples at http://htk.eng.cam.ac.uk/ftp/software/HTK-samples-3.4.1.tar.gz and extract
* cd HTKDemo and run ./runDemo configs/monPlainM1S1.dcf. Make sure that the recognition results match those of the HTK README. You may be required to add the directories accs, hmms/hmm.0, hmms/hmm.1, hmms/hmm.2, hmms/hmm.3, hmms/temp, proto and test before running the demo. COMMAND: ```mkdir accs hmms/hmm.0 hmms/hmm.1 hmms/hmm.2 hmms/hmm.3 hmms/temp proto test```
* HTK is installed correctly if the training and test results match those from the README 
	
### Installing the Forced Aligner:
* Download the Penn Phonetics Lab Forced Aligner at https://babel.ling.upenn.edu/phonetics/old_website_2015/p2fa/p2fa_1.003.tgz
* To run the forced aligner, it requires <b>Python 2</b>. Run ```python align.py [audio file] [transcript file] [output file]```
    * The audio file should be in ```.wav``` format
    * The transcript file should be in ```.txt``` format
    * The output file should be in ```.TextGrid``` format

### Testing the Forced Aligner and HTK 3.4 Toolkit: 
* To test, run ```python align.py ./test/BREY00538.wav ./test/BREY00538.txt ./test/BREY00538.TextGrid```
* The output file should contain the words from the text with their associated start and end times from the audio file 
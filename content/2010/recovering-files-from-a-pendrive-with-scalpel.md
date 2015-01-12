Title: Recovering files from a pendrive with scalpel
Date: 2010-4-14
Category: TODO
Tags: linux, life

I have no idea how it happened but I had to give today a housework in the university and it wasn't in the pendrive. At the moment I have
recovered 1 of 2 files with [scalpel](http://www.digitalforensicssolutions.com/Scalpel/) (I just love the name of foresnic tools :D). From
the website:

> Scalpel is a fast file carver that reads a database of header and footer definitions and extracts matching files from a set of image files
> or raw device files. Scalpel is filesystem-independent and will carve files from FATx, NTFS, ext2/3, or raw partitions. It is useful for
> both digital forensics investigation and file recovery. Scalpel resulted from a complete rewrite of [foremost
> 0.69](http://foremost.sourceforge.net/), a popular open source file carver, to enhance performance and decrease memory usage.

Steps: Create an iso image from your pendrive: sudo dd if=/dev/sdc of=pendrive.iso Have a look to the example configuration file (required)
or copy it to \$PWD: cp /etc/scalpel/scalpel.conf .As I had to recover a C file I added to the end of the config file this line: echo "c    
y       11000     /\*\*" \>\> scalpel.conf Which means "find files with 'c' extension, but not 'C' (case sensitive) and read 11000 bytes
from the header. I played with a bit of advantage as I knew for sure the file started with comments as the professor gave us a skeleton
file. The length field is not so important but I knew that I had not written 10K of code. Run scalpel: scalpel -c scalpel.conf -o recovered
pendrive.iso After that, in the *recovered* folder I had a log file named "audit.txt" and a folder named "c-0-0". Inside the folder there
were a lot of ".c" files, all with length 11000 and that started with "/\*\*" and manually I have found the one that I searched and removed
the trailing 11000-true\_bytes bytes. Appart from this manual usage I did, it has preconfigured headers for a lot of filetypes like jpg,
avi, doc, pdf, pgp, zip... so that you only need to uncomment the line in scalpel.conf of the files that you are searching. My pendrive was
formatted with FAT32 but it's filesystem-independent. Kudos to Scalpel!

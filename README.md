# thebigrenaming
Renaming large amounts of photo files.

Given problem: I have some 20,000 photo files on my harddisk, sorted in directories with the name scheme yyyymmdd, so there is a directory for every day I took at least one photograph. My Canon EOS 350D gives the photographs file names in the scheme IMG_nnnn.JPG. But I wanted them to have the file name scheme yyyymmdd-hhmmss.jpg.

With that they cannot only be sorted easier together when mixed to a photo series with photos from more than one camera (i.e. the camera in my smartphone), but in a copying process to some media the original file date would get lost (of course usually they can also be found in the EXIF data of each file, but that cannot be seen in a file manager).

Solution: Search the given path for all directories; in all directories look at all files and get their timestamp; build the new filename with that timestamp and rename each file.

ToDo:
- Read more file name schemes from different cameras.
- Correct timestamps in files from a camera with a known difference to the real time before renaming.
- Read other directory name schemes.
- Perhaps: Check if the file is really the file type given in the extension.

Use:
Change the variable „filepath“ to your path, then save and start the script.
Or change the source name scheme to your needs. :-)

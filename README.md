# file_integrity_monitor
A program that continuously monitors a directory and each of its subdirectories
for files that have been added, deleted, or modified since the start of the scan.

Program uses sha256 hashing to verify integrity of files. When any file change
is discovered, the program logs the object file, what happened to it, and the 
date/time of the change.

Example log:
--------------------------------------------------------------------------------
2023-08-19 14:15:03.061802 - MONITORING IN PROGRESS: /home/ccandau/Desktop/
--------------------------------------------------------------------------------
2023-08-19 14:15:18.429821	File created:	/home/ccandau/Desktop/file1.txt
2023-08-19 14:15:21.476268	File created:	/home/ccandau/Desktop/.file1.txt.swp
2023-08-19 14:15:22.913671	File modified:	/home/ccandau/Desktop/.file1.txt.swp
2023-08-19 14:15:27.282116	File created:	/home/ccandau/Desktop/file1.txt~
2023-08-19 14:15:27.282581	File modified:	/home/ccandau/Desktop/file1.txt
2023-08-19 14:15:27.287706	File modified:	/home/ccandau/Desktop/.file1.txt.swp
2023-08-19 14:15:27.288023	File deleted:	/home/ccandau/Desktop/file1.txt~
2023-08-19 14:15:27.289466	File deleted:	/home/ccandau/Desktop/.file1.txt.swp
2023-08-19 14:15:29.706692	File created:	/home/ccandau/Desktop/.file1.txt.swp
2023-08-19 14:15:30.615629	File modified:	/home/ccandau/Desktop/.file1.txt.swp
2023-08-19 14:15:36.311214	File modified:	/home/ccandau/Desktop/file1.txt
2023-08-19 14:15:36.311667	File created:	/home/ccandau/Desktop/file1.txt~
2023-08-19 14:15:36.316913	File modified:	/home/ccandau/Desktop/.file1.txt.swp
2023-08-19 14:15:36.317679	File deleted:	/home/ccandau/Desktop/file1.txt~
2023-08-19 14:15:36.318437	File deleted:	/home/ccandau/Desktop/.file1.txt.swp
2023-08-19 14:16:01.074624	File created:	/home/ccandau/Desktop/test/file2.txt
2023-08-19 14:16:02.869520	File created:	/home/ccandau/Desktop/test/.file2.txt.swp
2023-08-19 14:16:05.902523	File modified:	/home/ccandau/Desktop/test/.file2.txt.swp
2023-08-19 14:16:08.329200	File created:	/home/ccandau/Desktop/test/file2.txt~
2023-08-19 14:16:08.329993	File modified:	/home/ccandau/Desktop/test/file2.txt
2023-08-19 14:16:08.334794	File modified:	/home/ccandau/Desktop/test/.file2.txt.swp
2023-08-19 14:16:08.335141	File deleted:	/home/ccandau/Desktop/test/file2.txt~
2023-08-19 14:16:08.336297	File deleted:	/home/ccandau/Desktop/test/.file2.txt.swp
2023-08-19 14:16:24.568099	File deleted:	/home/ccandau/Desktop/file1.txt
2023-08-19 14:16:30.083342	File deleted:	/home/ccandau/Desktop/test/file2.txt

# SpeedTest-Chart
This a Docker container Flask application to display the results of speedtests in a 
chart. I use Ookala's (https://www.speedtest.net/) CLI to perform the tests on a regular 
basis. The output is saved into JSON files and later these files are added to a SQLite3
database which Flask uses to display the chart.

I know it is not the prettiest and most probably using some CSS magic it can be made to
look reasonable. But for my purpose it does the trick. If you feel compeled to make it
better by all means go ahead and have fun with it.

Extract the tar.bz2 file in the directory of your choice and the build the docker image.
It is based of python:3.8.9-alpine3.13 but if you want to use something else, knock
yourself out the alpine version is small enough and it works.

After you build the image run it using the following

	docker run -d \
    	--name speedtest \
    	-p WHATEVER_PORT_YOU_WANT_TO_USE:8080 \
    	-e TZ="America/New York" \
    	-v WHERE_IS_YOUR_DBFILE:/app/db \
    	--restart=unless-stopped \
    	speedtest

As you can see the default port of the container is 8080 but you can port forward any
port you want to it or you can just change the source code before building the image and
use a different port.

The database that the application uses is a simple SQLite3 database and in my case I keep
it in /data/speedtest/db and then I link that folder to the /app/data folder in the
container.

I am not a python developer (I did this to teach myself some python and flask) so the
code is not perfect, and I know that there are much better/prettier/efficient/etc.
ways to do things, but it works and it is easy to follow and understand.

# Populate the database
Here are the steps to populate the DB. I do all of this on a linux box so commands given will be linux, if you use Windows or Mac you need to figure it out on oyur own, but the steps should be similar.

	1. Download the speedtest CLI for your OS from (https://www.speedtest.net/apps/cli)
	2. Extract the files and put somewhere where you can run it (somewhere in your path)
	3. I created a script that I run via cron
		#!/bin/bash
		fn="/data/speedtest/"$(hostname)"-"$(date +"%s")".json"
		/usr/local/bin/speedtest -f json > $fn
	4. I created a python script that grabs the JSON file and adds the data to the 
	   database. Eventually I will put the script here (it needs a lot of cleaning), 
	   but feel free to create your own and use that.
	5. I created 2 cron jobs that run every 4 hours that run each of the scripts
		10 */4 * * * /usr/bin/dospeedtest 2>&1       <- This is the file created on #3
		20 */4 * * * /usr/bin/json2db 2>&!           <- This is the script on #4

If you have any questions let me know and I'll do my best to help. 

# License
ISC License (ISC)
Copyright 2021 L0rddarkF0rce

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

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
    	-p 8080:8080 \
    	-e TZ="America/New York" \
    	-v /data/speedtest/db:/app/data \
    	--restart=unless-stopped \
    	l0rddarkf0rce/speedtest

As you can see the default port of the container is 8080 but you can port forward any
port you want to it or you can just change the source code before building the image and
use a different port.

The database that the application uses is a simple SQLite3 database and in my case I keep
it in /data/speedtest/db and then I link that folder to the /app/data folder in the
container.

I am not a python developer (I did this to teach myself some python and flask) so the
code is not perfect, and I know that there are much better/prettier/efficient/etc.
ways to do things, but it works and it is easy to follow and understand.

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

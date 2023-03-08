all:
	gcc -Wl,-z,lazy,-z,relro main.c -o chall -fno-stack-protector -no-pie
	cp main.c ../distfiles/
	mv chall ../distfiles/

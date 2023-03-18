all:
	gcc -Wl,-z,now,-z,relro main.c -o chall -fstack-protector -pie
	cp main.c ../distfiles/
	mv chall ../distfiles/

#
# Makefile for thei True64 UNIX PAWZAgent 
#
CFLAGS=	 -g -c  -DTRACE_KAT_MCT -DINTERMEDIATE_VALUE_KAT
#
OBJS=rijndael-alg-fst.o  rijndael-api-fst.o  rijndael-test-fst.o	
SRCS=rijndael-alg-fst.c  rijndael-api-fst.c  rijndael-test-fst.c	
#
#
CC=   /usr/bin/cc
.c.o:
	${CC} ${CFLAGS} ${*}.c

all:	rijndael-alg-fst

rijndael-alg-fst:	${OBJS}  
	/usr/bin/cc -g  -o rijndael-alg-fst ${OBJS}  ${LIBS}

clean:
	rm -f rijndael-alg-fst ${OBJS}

depend:
	/usr/bin/X11/makedepend -I. -I../include ${SRCS}

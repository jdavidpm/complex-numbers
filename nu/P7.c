#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <dirent.h>
#include <limits.h>
#include <pthread.h>
#include <sys/stat.h>
#include <sys/types.h>

#define BUFFERSIZE 1024
#define COPYMORE 0644

int dostat(char *filename)
{
	struct stat fileInfo;

	if (stat(filename, &fileInfo) >= 0)
		if (S_ISREG(fileInfo.st_mode))
			return 1;
	else
		return 0;
}

void showError(char *str1, char *str2)
{
	fprintf(stderr, "Error: %s ", str1);
	perror(str2);
	exit(1);
}


void createDir(const char *dir)
{
        char tmp[256];
        char *p = NULL;
        size_t len;

        snprintf(tmp, sizeof(tmp),"%s",dir);
        len = strlen(tmp);
        if(tmp[len - 1] == '/')
                tmp[len - 1] = 0;
        for(p = tmp + 1; *p; p++)
                if(*p == '/') {
                        *p = 0;
                        mkdir(tmp, S_IRWXU);
                        *p = '/';
                }
        mkdir(tmp, S_IRWXU);
}

int copyFiles(char *source, char *destination)
{
	int in_fd, out_fd, n_chars;
	char buf[BUFFERSIZE];

	if ((in_fd= open(source, O_RDONLY)) == -1)
		showError("No se pudo abrir", source);
	if ((out_fd = creat(destination,  COPYMORE)) == -1)
		showError("No se puedo crear directorio: ", destination);

	while ((n_chars = read(in_fd, buf, BUFFERSIZE)) > 0)
	{
		if (write(out_fd, buf, n_chars) != n_chars)
			showError("Error al escribir: ", destination);
		if (n_chars == -1)
			showError("Error al leer de: ", source);
	}
	if (close(in_fd) == -1 || close(out_fd) == -1)
		showError("Error al cerrar archivos", "");
	return 1;
}

int copyDir(char *source, char *destination)
{
	DIR *dir_ptr = NULL;
	struct dirent *direntp;
	char tempDest[strlen(destination) + 1];
	char tempSrc[strlen(source) + 1];
	strcat(destination, "/");
	strcat(source, "/");
	strcpy(tempDest, destination);
	strcpy(tempSrc, source);

	struct stat fileinfo;
	if ((dir_ptr = opendir(source)) == NULL)
	{
		fprintf(stderr, "cp1: cannot open %s for copying\n", source);
		return 0;
	}
	else
	{
		while ((direntp = readdir(dir_ptr)))
		{
			if (dostat(direntp->d_name))
			{
				strcat(tempDest, direntp->d_name);
				strcat(tempSrc, direntp->d_name);
				copyFiles(tempSrc, tempDest);
				strcpy(tempDest, destination);
				strcpy(tempSrc, source);
			}
		}
		closedir(dir_ptr);
		return 1;
	}
}

int main(int argc, char *argv[])
{
	int i = 0;
	char *src = argv[1];
	char dest[PATH_MAX + 1];

	if (argc != 3)
	{
		fprintf(stderr, "usage: %s source destination\n", *argv);
		exit(1);
	}
	strcpy(dest, argv[2]);

	if (src[0] != '/' && dest[0] != '/')
		copyFiles(src, dest);
	else if (src[0] != '/' && dest[0] == '/')
	{
		for (i = 0; i < strlen(dest); i++)
			dest[i] = dest[i + 1];
		strcat(dest, "/");
		strcat(dest, src);
		copyFiles(src, dest);
	}
	else if (src[0] == '/' && dest[0] == '/')
	{
		for (i = 0; i < strlen(dest); i++)
			dest[i] = dest[i + 1];
		createDir(dest);

		for(i = 0; i < strlen(src); i++)
			src[i] = src[i + 1];
		copyDir(src, dest);
	}
	else
	{
		fprintf(stderr, "usage: cp1 source destination\n");
		exit(1);
	}
	return 0;
}
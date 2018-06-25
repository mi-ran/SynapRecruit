#!/usr/bin/python
import sys

# fontMap
# key = char, value = matrix
fontMap = {}
fontMapFile = 'bitmap.txt'

def readFile():
    f = open(fontMapFile)
    # number of matrix
    f.readline()

    # read matrix
    key = 65
    while True:
        line = f.readline()
        if not line:
            break
        if line is '\n':
            key = key+1
            continue

        if key not in fontMap:
            fontMap[key] = [list(line)]
        else:
            fontMap[key].extend([list(line)])
    f.close()

    # space도 맵에 넣어주기
    fontMap[32] = [['0','0','0','0','0','0','\n'], ['0','0','0','0','0','0','\n'], ['0','0','0','0','0','0','\n'], ['0','0','0','0','0','0','\n'], ['0','0','0','0','0','0','\n'], ['0','0','0','0','0','0','\n'], ['0','0','0','0','0','0','\n']]


def str2Matrix(input_str):
    textMatrix = fontMap[ord(input_str[0])]
    for i in range(1, len(input_str)):
        for j in range(len(textMatrix)):
            textMatrix[j] = textMatrix[j] + fontMap[ord(input_str[i])][j]
    return textMatrix


def printChar(char, width):
    for i in range(width):
        if char is '0':
            print(" ", end='')
        elif char is '1':
            print("@", end='')
        elif char is '\n':
            print(" ", end='')
            return


def printRow(row, width, height):
    for i in range(height):
        for j in range(len(row)):
            printChar(row[j], width)
        if i < height-1:
            print()


def rotate90(textMatrix):
    rotated = textMatrix[::-1]
    return [[row[cIdx] for row in rotated] for cIdx in range(len(rotated[0]))]


def printText(textMatrix, rotateAncle, width, height):
    for i in range(rotateAncle//90):
        textMatrix = rotate90(textMatrix)

    for r in range(len(textMatrix)):
        if (rotateAncle//90)%2 is 1:
            printRow(textMatrix[r], height, width)
        else:
            printRow(textMatrix[r], width, height)
        print()
    print()


if __name__ == '__main__':
    rotateAncle = 0
    # read font map file
    readFile()
    # get input text
    input_text = " ".join(sys.argv[1:])
    # string을 편집하기 쉬운 모양의 행렬로 바꿈
    textMatrix = str2Matrix(input_text)
    # print
    printText(textMatrix, rotateAncle, 2, 1);
    # lotate
    rotateAncle = 90
    #print
    printText(textMatrix, rotateAncle, 1, 2);

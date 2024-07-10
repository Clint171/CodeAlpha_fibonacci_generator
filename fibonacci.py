def getSequence(first , second , stopIndex):
    sequence = [first, second]
    for i in range(2, stopIndex):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def __main__():
    first = int(input("Enter the first number in the sequence: "))
    second = int(input("Enter the second number in the sequence: "))
    stopIndex = int(input("Enter the number of elements in the sequence: "))
    print(getSequence(first, second, stopIndex))

if __name__ == "__main__":
    __main__()
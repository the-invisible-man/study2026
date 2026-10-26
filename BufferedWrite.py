class File:
    def write(self, data: bytes) -> None:
        """Writes all provided bytes to the file."""

class BufferedFileWriter:
    def __init__(self, file: File, capacity: int):
        self.file = file
        self.capacity = capacity
        self.buffer = bytearray()

    def write(self, data: bytes) -> None:
        remainingCapacity = self.capacity - len(self.buffer)
        remainingWriteSize = len(bytes)

        while remainingWriteSize > 0:
            if remainingWriteSize > remainingCapacity:
                chunk = data[:remainingCapacity]
                self.file.write(chunk)
                data = data[remainingCapacity-1:]
            else:
                self.buffer.extend(data)

            remainingWriteSize

    def flush(self) -> None:
        pass